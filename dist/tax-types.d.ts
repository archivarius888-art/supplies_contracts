export declare const TAX_TYPES: {
  readonly SIMPLIFIED_5: "SIMPLIFIED_5";
  readonly SIMPLE: "SIMPLE";
  readonly SIMPLIFIED_7: "SIMPLIFIED_7";
  readonly SIMPLE_15: "SIMPLE_15";
  readonly COMMON: "COMMON";
  readonly AUTOMATED_8: "AUTOMATED_8";
  readonly AUTOMATED_20: "AUTOMATED_20";
  readonly PATENT: "PATENT";
};

export type TaxType = (typeof TAX_TYPES)[keyof typeof TAX_TYPES];

export declare const TAX_TYPES_OPTIONS: readonly {
  readonly value: TaxType;
  readonly title: string;
}[];

export declare const TAX_TYPES_TITLE: Record<TaxType, string>;
