"use strict";

const beneficiaries_info_mode = require("./beneficiaries-info-mode.js");
const tax_types = require("./tax-types.js");

module.exports = {
  ...beneficiaries_info_mode,
  ...tax_types,
};
