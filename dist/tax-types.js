"use strict";

// Auto-generated from tax_types.json.

const TAX_TYPES = {
  SIMPLIFIED_5: "SIMPLIFIED_5",
  SIMPLE: "SIMPLE",
  SIMPLIFIED_7: "SIMPLIFIED_7",
  SIMPLE_15: "SIMPLE_15",
  COMMON: "COMMON",
  AUTOMATED_8: "AUTOMATED_8",
  AUTOMATED_20: "AUTOMATED_20",
  PATENT: "PATENT"
};

const TAX_TYPES_OPTIONS = [
  { value: TAX_TYPES.SIMPLIFIED_5, title: "УСН 5%" },
  { value: TAX_TYPES.SIMPLE, title: "УСН 6%" },
  { value: TAX_TYPES.SIMPLIFIED_7, title: "УСН 7%" },
  { value: TAX_TYPES.SIMPLE_15, title: "УСН 15%" },
  { value: TAX_TYPES.COMMON, title: "Общая" },
  { value: TAX_TYPES.AUTOMATED_8, title: "АУСН 8%" },
  { value: TAX_TYPES.AUTOMATED_20, title: "АУСН 20%" },
  { value: TAX_TYPES.PATENT, title: "ПСН" },
];

const TAX_TYPES_TITLE = {
  [TAX_TYPES.SIMPLIFIED_5]: "УСН 5%",
  [TAX_TYPES.SIMPLE]: "УСН 6%",
  [TAX_TYPES.SIMPLIFIED_7]: "УСН 7%",
  [TAX_TYPES.SIMPLE_15]: "УСН 15%",
  [TAX_TYPES.COMMON]: "Общая",
  [TAX_TYPES.AUTOMATED_8]: "АУСН 8%",
  [TAX_TYPES.AUTOMATED_20]: "АУСН 20%",
  [TAX_TYPES.PATENT]: "ПСН",
};

module.exports = {
  TAX_TYPES,
  TAX_TYPES_OPTIONS,
  TAX_TYPES_TITLE,
};
