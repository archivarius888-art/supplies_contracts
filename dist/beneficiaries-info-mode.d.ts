export declare const BENEFICIARIES_INFO_MODE: {
  readonly REQUIRED: "REQUIRED";
  readonly NO_INFO: "NO_INFO";
  readonly REFUSAL: "REFUSAL";
  readonly SAME_AS_FOUNDERS: "SAME_AS_FOUNDERS";
};

export type BeneficiariesInfoMode = (typeof BENEFICIARIES_INFO_MODE)[keyof typeof BENEFICIARIES_INFO_MODE];

export declare const BENEFICIARIES_INFO_MODE_OPTIONS: readonly {
  readonly value: BeneficiariesInfoMode;
  readonly title: string;
}[];

export declare const BENEFICIARIES_INFO_MODE_TITLE: Record<BeneficiariesInfoMode, string>;
