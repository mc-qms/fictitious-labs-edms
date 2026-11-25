# SOP-QA-039 — Batch and Lot Numbering and Expiration Dating

**Fictitious Labs Inc.** · Version 1.0 · Effective 2026-03-02 · Owner: Quality Assurance

## 1. Purpose

This procedure states the lot number syntax for FL-101 drug substance and the rules for assigning retest dates and expiration dates.
It also states how sub-lots, pooled lots, and raw materials are numbered and dated.

## 2. Scope

Applies to batch and lot numbering and expiration dating for FL-101 drug substance and its raw materials at Fictitious Labs Inc., a US-based biologics organization manufacturing monoclonal antibody drug substance in the United States, in the following functions: Quality Assurance, Quality Control laboratory, Manufacturing, Warehouse, Document Control.

Does not cover batch number assignment or batch record issuance. Batch number assignment and batch record issuance are governed by SOP-QA-027, Batch Record Content and Control (§4.3); this procedure states the numbering syntax and dating rules that SOP does not state, and does not duplicate assignment.

## 3. Responsibilities

**Document Control**

- Assign the sequence portion of each lot number.
- Maintain lot number assignments in FL-EDMS.
- Confirm that a lot number has not been used before it is issued.

**Quality Assurance**

- Own this procedure.
- Review lot numbering and dating entries during batch record review under SOP-QA-006, Batch Record Review and Product Release.
- Handle numbering errors under SOP-QA-010, Handling of Deviations.

**Quality Control**

- Assign raw-material retest dates.
- Assign the FL-101 retest date under SOP-QC-002, Stability Testing.
- Assign QC sample IDs.
- Retest material that is past its retest date under SOP-QC-008, Raw Material Sampling, Testing, and TSE/BSE Control.

**Manufacturing Supervisor**

- Record the start of manufacture for each batch.
- Record the date of manufacture for each lot.
- Apply the assigned lot number in the batch record.

**Warehouse Supervisor**

- Confirm material lot identity on receipt.
- Segregate material that is past its retest date.
- Apply assigned lot numbers and dates to warehouse records and labels.

## 4. Procedure

### 4.1 Apply the lot number syntax

1. Confirm that the batch number has been assigned at issuance in FL-EDMS under SOP-QA-027, Batch Record Content and Control (§4.3).
2. Obtain the lot number from Document Control.
3. Use the format FL101-<YYMM>-<NNN> for each FL-101 lot number.
4. Enter FL101 as the product code.
5. Enter <YYMM> as the year and month of the start of manufacture.
6. Obtain <NNN> as the sequence assigned by Document Control.
7. Check the completed number against the example format FL101-2611-004.
8. Record the lot number in FL-EDMS.
9. Record the lot number in the batch record executed from FRM-MF-101, Master Batch Record, FL-101 Drug Substance.
10. Verify that the lot number on the record matches the lot number in FL-EDMS.
11. Report any mismatch to Quality Assurance.
12. Handle a numbering error discovered on a record or label under SOP-QA-010, Handling of Deviations.

### 4.2 Number sub-lots and pooled lots

1. Identify when one batch is split into sub-lots.
2. Keep the base lot number for the split batch.
3. Add a letter suffix to identify each sub-lot.
4. Assign -A to the first sub-lot.
5. Assign -B to the second sub-lot.
6. Continue the letter sequence for any additional sub-lots.
7. Record each sub-lot number in FL-EDMS.
8. Record each sub-lot number in the batch record.
9. Identify when harvests are pooled.
10. Record each source lot number in FL-EDMS.
11. Keep the source lots traceable in FL-EDMS after pooling.
12. Number the pooled lot as a new lot.
13. Apply the syntax in Section 4.1 to the pooled lot number.
14. Record the pooled lot number in the batch record.
15. Verify that the pooled lot record lists all source lots.

### 4.3 Assign retest and expiration dating

1. Record the date of manufacture for FL-101 drug substance.
2. Use the date the drug substance is filled into its final containers after sterile filtration as the date of manufacture.
3. Assign a retest date to FL-101.
4. Assign the retest date under SOP-QC-002, Stability Testing.
5. Base the retest date on stability data.
6. Do not take a fixed retest period from SPEC-101, FL-101 Drug Substance Specification.
7. Note that the specification deliberately does not fix the retest period.
8. Record the retest date in FL-EDMS.
9. Record the retest date on the lot record.
10. Determine whether an expiration date is required for the lot.
11. Calculate the expiration date from the date of manufacture where an expiration date is required.
12. Calculate the expiration date consistent with 21 CFR 610.50.
13. Record the expiration date in FL-EDMS.
14. Record the expiration date on the lot record.
15. Verify that the dating on the label matches the dating in FL-EDMS.
16. Report any dating mismatch to Quality Assurance.
17. Handle a dating error discovered on a record or label under SOP-QA-010, Handling of Deviations.

### 4.4 Control raw-material dating

1. Confirm material lot identity on receipt.
2. Follow SOP-QA-023, Warehouse and Distribution Control for material lot identity on receipt.
3. Follow SOP-QC-008, Raw Material Sampling, Testing, and TSE/BSE Control for material lot identity on receipt.
4. Record the supplier lot number in the receipt record.
5. Assign a QC sample ID to each sample taken.
6. Use the format QC-<YYYY>-<NNNN> for each QC sample ID.
7. Enter <YYYY> as the calendar year.
8. Enter <NNNN> as the sample sequence for that year.
9. Record the QC sample ID on the sample label.
10. Record the QC sample ID in the laboratory record.
11. Assign a raw-material retest date for each material lot.
12. Have Quality Control assign the raw-material retest date.
13. Base the raw-material retest date on the supplier's dating.
14. Base the raw-material retest date on the material specification.
15. Record the raw-material retest date in FL-EDMS.
16. Record the raw-material retest date on the material record.
17. Check the retest date before a material is issued for use.
18. Do not use material past its retest date.
19. Retest material past its retest date under SOP-QC-008, Raw Material Sampling, Testing, and TSE/BSE Control.
20. Release the material for use only after retesting is complete.

## 5. Records

Lot number assignments, sub-lot and pooled lot records, retest date assignments, expiration date calculations, QC sample ID records, and raw-material receipt and retest records are completed in FL-EDMS and in the associated batch and laboratory records. Records are completed in accordance with SOP-QA-001, Good Documentation Practices. Completed records for each lot are reviewed as part of batch record review under SOP-QA-006, Batch Record Review and Product Release. All records generated under this procedure are retained under the retention requirements of SOP-QA-001, Good Documentation Practices.

## 6. References

- 21 CFR 211.130, Packaging and labeling operations.
- 21 CFR 211.137, Expiration dating.
- 21 CFR 211.188, Batch production and control records.
- 21 CFR 610.50, Date of manufacture.
- SOP-QA-001, Good Documentation Practices.
- SOP-QA-006, Batch Record Review and Product Release.
- SOP-QA-010, Handling of Deviations.
- SOP-QA-023, Warehouse and Distribution Control.
- SOP-QA-027, Batch Record Content and Control.
- SOP-QC-002, Stability Testing.
- SOP-QC-008, Raw Material Sampling, Testing, and TSE/BSE Control.
- SPEC-101, FL-101 Drug Substance Specification.
- FRM-MF-101, Master Batch Record, FL-101 Drug Substance.
