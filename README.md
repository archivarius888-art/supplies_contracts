# Shared Contracts

Один источник правды для справочников, которые используются и на Python-беке, и на JS/TS-фронте.

## Структура

- `tax_types.json` — исходные данные
- `generate.py` — генератор артефактов
- `pyproject.toml` — Python package
- `package.json` — npm package
- `src/supplies_contracts/` — Python-модуль
- `dist/` — npm-артефакты

## Генерация

```bash
python3 generate.py
```

Или:

```bash
npm run generate
```

## Использование в Python

```python
from supplies_contracts import TaxTypes
```

## Использование в JS/TS

```ts
import { TAX_TYPES, TAX_TYPES_TITLE, TAX_TYPE_OPTIONS } from "@spro/supplies-contracts";
```

## Локальная установка

Python:

```bash
pip install git+ssh://git@<your-host>/<group>/shared_contracts.git
```

npm:

```bash
npm install git+ssh://git@<your-host>/<group>/shared_contracts.git
```
