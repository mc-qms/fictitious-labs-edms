# SOP-QA-002 — Reporting Numerical Values

**Fictitious Labs Inc.** · Version 1.0 · Effective 2026-03-02 · Owner: Quality Assurance

## 1. Purpose

Establish one convention for rounding and reporting numerical results so
that a reported value means the same thing regardless of who produced it.

## 2. Scope

All QC test results, in-process values, and calculated values recorded on
Fictitious Labs forms, worksheets, and reports.

## 3. Rules

3.1 **Round once, at the end.** Intermediate values are carried unrounded.
Only the final reported value is rounded.

3.2 **Round half up.** A final digit of exactly 5 rounds the preceding digit
up. (0.125 → 0.13 at two decimal places; 2.5 → 3 at zero decimal places.)

3.3 **Report to the method's precision.** Each test method states the
reporting precision for its results. Report exactly that many decimal
places — no more, no fewer. Trailing zeros are significant and are written
(e.g., a protein concentration reported to one decimal place is written
10.0, not 10).

3.4 **Never report more precision than the measurement supports.** A value
read from an instrument display is transcribed exactly as displayed;
digits are never added.

3.5 **Transcription is exact.** A reported value must match the value on
the raw data record digit for digit after the rounding in 3.1–3.3 is
applied. Any difference between the raw record and the report is a
documentation error, not a rounding difference.

3.6 **Averages.** Where a method calls for replicate readings, the reported
result is the average of the replicates, rounded per 3.1–3.3 after
averaging.

## 4. References

- SOP-QA-001, Good Documentation Practices
- Individual test methods (reporting precision for each result)
