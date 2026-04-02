from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PYTHON_PACKAGE = ROOT / "src" / "supplies_contracts"
DIST_DIR = ROOT / "dist"
NPM_INDEX_JS_OUTPUT = DIST_DIR / "index.js"
NPM_INDEX_D_TS_OUTPUT = DIST_DIR / "index.d.ts"
PYTHON_INIT_OUTPUT = PYTHON_PACKAGE / "__init__.py"


@dataclass(frozen=True)
class ContractItem:
    code: str
    title: str


@dataclass(frozen=True)
class Contract:
    source_path: Path
    name: str
    items: tuple[ContractItem, ...]

    @property
    def class_name(self) -> str:
        return "".join(part.capitalize() for part in self.name.split("_"))

    @property
    def ts_type_name(self) -> str:
        class_name = self.class_name
        if class_name.endswith("Types"):
            return f"{class_name[:-1]}"
        if class_name.endswith("s") and len(class_name) > 1:
            return class_name[:-1]
        return class_name

    @property
    def constant_name(self) -> str:
        return self.name.upper()

    @property
    def js_file_stem(self) -> str:
        return self.name.replace("_", "-")

    @property
    def python_output(self) -> Path:
        return PYTHON_PACKAGE / f"{self.name}.py"

    @property
    def npm_js_output(self) -> Path:
        return DIST_DIR / f"{self.js_file_stem}.js"

    @property
    def npm_d_ts_output(self) -> Path:
        return DIST_DIR / f"{self.js_file_stem}.d.ts"


class InvalidContractError(ValueError):
    pass


def _iter_contract_json_files() -> list[Path]:
    return sorted(path for path in ROOT.glob("*.json") if path.is_file())


def _parse_contract(path: Path) -> Contract | None:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        return None

    name = payload.get("name")
    raw_items = payload.get("items")
    if not isinstance(name, str) or not isinstance(raw_items, list):
        return None

    items: list[ContractItem] = []
    for raw_item in raw_items:
        if not isinstance(raw_item, dict):
            raise InvalidContractError(f"{path.name}: each item must be object")
        code = raw_item.get("code")
        title = raw_item.get("title")
        if not isinstance(code, str) or not isinstance(title, str):
            raise InvalidContractError(
                f"{path.name}: each item must contain string code/title"
            )
        items.append(ContractItem(code=code, title=title))

    if not items:
        raise InvalidContractError(f"{path.name}: items must not be empty")

    return Contract(source_path=path, name=name, items=tuple(items))


def _load_contracts() -> list[Contract]:
    contracts: list[Contract] = []
    for path in _iter_contract_json_files():
        contract = _parse_contract(path)
        if contract is None:
            continue
        contracts.append(contract)

    if not contracts:
        raise InvalidContractError("No contract JSON files found")

    names = [contract.name for contract in contracts]
    if len(names) != len(set(names)):
        raise InvalidContractError("Contract names must be unique")

    return sorted(contracts, key=lambda contract: contract.name)


def _render_python(contract: Contract) -> str:
    lines = [
        f'"""Auto-generated from {contract.source_path.name}."""',
        "",
        "from supplies_contracts._choices import TextChoices",
        "",
        "",
        f"class {contract.class_name}(TextChoices):",
        "    __slots__ = ()",
        "",
    ]
    for item in contract.items:
        lines.append(f'    {item.code} = "{item.code}", "{item.title}"')
    lines.append("")

    return "\n".join(lines)


def _render_npm_js(contract: Contract) -> str:
    constant_name = contract.constant_name
    options_name = f"{constant_name}_OPTIONS"
    title_name = f"{constant_name}_TITLE"

    lines = [
        '"use strict";',
        "",
        f"// Auto-generated from {contract.source_path.name}.",
        "",
        f"const {constant_name} = {{",
    ]
    for index, item in enumerate(contract.items):
        suffix = "," if index < len(contract.items) - 1 else ""
        lines.append(f'  {item.code}: "{item.code}"{suffix}')
    lines.extend(["};", "", f"const {options_name} = ["])
    for item in contract.items:
        lines.append(f'  {{ value: {constant_name}.{item.code}, title: "{item.title}" }},')
    lines.extend(["];", "", f"const {title_name} = {{"])
    for item in contract.items:
        lines.append(f'  [{constant_name}.{item.code}]: "{item.title}",')
    lines.extend(
        [
            "};",
            "",
            "module.exports = {",
            f"  {constant_name},",
            f"  {options_name},",
            f"  {title_name},",
            "};",
            "",
        ]
    )

    return "\n".join(lines)


def _render_npm_d_ts(contract: Contract) -> str:
    constant_name = contract.constant_name
    options_name = f"{constant_name}_OPTIONS"
    title_name = f"{constant_name}_TITLE"
    ts_type_name = contract.ts_type_name

    lines = [f"export declare const {constant_name}: {{"]
    for item in contract.items:
        lines.append(f'  readonly {item.code}: "{item.code}";')
    lines.extend(
        [
            "};",
            "",
            f"export type {ts_type_name} = (typeof {constant_name})[keyof typeof {constant_name}];",
            "",
            f"export declare const {options_name}: readonly {{",
            f"  readonly value: {ts_type_name};",
            "  readonly title: string;",
            "}[];",
            "",
            f"export declare const {title_name}: Record<{ts_type_name}, string>;",
            "",
        ]
    )

    return "\n".join(lines)


def _render_npm_index_js(contracts: list[Contract]) -> str:
    lines = ['"use strict";', ""]

    for contract in contracts:
        lines.append(
            f'const {contract.name} = require("./{contract.js_file_stem}.js");'
        )

    lines.extend(["", "module.exports = {"])
    for contract in contracts:
        lines.append(f"  ...{contract.name},")
    lines.extend(["};", ""])

    return "\n".join(lines)


def _render_npm_index_d_ts(contracts: list[Contract]) -> str:
    lines = [f'export * from "./{contract.js_file_stem}";' for contract in contracts]
    lines.append("")
    return "\n".join(lines)


def _render_python_init(contracts: list[Contract]) -> str:
    lines: list[str] = []

    for contract in contracts:
        lines.append(
            f"from supplies_contracts.{contract.name} import {contract.class_name}"
        )

    lines.extend(["", "__all__ = ["])
    for contract in contracts:
        lines.append(f'    "{contract.class_name}",')
    lines.extend(["]", ""])

    return "\n".join(lines)


def main() -> None:
    contracts = _load_contracts()

    PYTHON_PACKAGE.mkdir(parents=True, exist_ok=True)
    DIST_DIR.mkdir(parents=True, exist_ok=True)

    for contract in contracts:
        contract.python_output.write_text(_render_python(contract), encoding="utf-8")
        contract.npm_js_output.write_text(_render_npm_js(contract), encoding="utf-8")
        contract.npm_d_ts_output.write_text(_render_npm_d_ts(contract), encoding="utf-8")

    NPM_INDEX_JS_OUTPUT.write_text(_render_npm_index_js(contracts), encoding="utf-8")
    NPM_INDEX_D_TS_OUTPUT.write_text(_render_npm_index_d_ts(contracts), encoding="utf-8")
    PYTHON_INIT_OUTPUT.write_text(_render_python_init(contracts), encoding="utf-8")


if __name__ == "__main__":
    main()
