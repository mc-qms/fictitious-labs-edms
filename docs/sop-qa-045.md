# SOP-QA-045 — User Access Administration, Audit Trail Review, and Backup/Restore Verification

**Fictitious Labs Inc.** · Version 1.0 · Effective 2026-03-02 · Owner: Quality Assurance

## 1. Purpose

This procedure is the operational companion to the policy in SOP-QA-018, Computer System Validation and Data Integrity. It describes how user access is administered, how standalone audit trails are reviewed, and how backup and restoration are verified in practice.

## 2. Scope

Applies to computerized systems recorded in the system inventory in FL-EDMS at Fictitious Labs Inc., a US-based biologics organization manufacturing monoclonal antibody drug substance in the United States, in the following functions: Quality Assurance, Document Control. It also applies in the functions that own systems, where the System Owner for each system carries out the steps assigned to that role in this procedure.

Does not cover system validation, criticality categorization, or the policy requirements themselves, which are governed by SOP-QA-018, Computer System Validation and Data Integrity; this procedure sets the operating cadence and mechanics only. Downtime working is governed by SOP-QA-047, Electronic System Downtime and Paper Backup.

## 3. Responsibilities

**System Administrator**

- Administer access and configuration for computerized systems.
- Remain independent of responsibility for record content.
- Provision access only as described in Section 4.1.
- Remove access within 2 business days of a role change or departure.
- Monitor backups as described in Section 4.4.
- Record completed reviews and tests in FL-EDMS as assigned in this procedure.

**System Owner**

- Approve documented requests for access to systems under their ownership.
- Review access authorizations with the System Administrator as described in Section 4.2.
- Review standalone system audit trails at the frequency set in the system inventory.
- Set the backup frequency in the system inventory with Quality Assurance.
- Set the scope of each scheduled restore test with Quality Assurance.

**Quality Assurance**

- Provide concurrence for access to GMP-critical systems.
- Approve criticality categories — GMP-critical, GMP-supporting, and non-GMP — under SOP-QA-018, Computer System Validation and Data Integrity.
- Agree the backup frequency in the system inventory with the System Owner.
- Agree the scope of each scheduled restore test with the System Owner.

**QA Manager**

- Set the standalone audit trail review frequency in the system inventory.
- Review the frequency when a system or its use changes.

**Document Control**

- Maintain the system inventory in FL-EDMS.
- Maintain this procedure in FL-EDMS.

## 4. Procedure

### 4.1 Provision and remove user access

1. Confirm the system is recorded in the system inventory in FL-EDMS.
2. Receive a documented request for access.
3. Confirm the System Owner has approved the request.
4. Confirm Quality Assurance concurrence is documented for a GMP-critical system.
5. Confirm the requester has completed the training required for the role under SOP-QA-005, Training and Qualification.
6. Provision the access exactly as approved.
7. Record the provisioned access in FL-EDMS.
8. Notify the user that access has been provisioned.
9. Receive notice of a role change or departure.
10. Remove the access within 2 business days of the role change or departure.
11. Record the removal in FL-EDMS.
12. Raise any access discrepancy found during provisioning or removal under SOP-QA-010, Handling of Deviations.

### 4.2 Review access authorizations

1. Schedule the review of access authorizations at least annually.
2. List the current access authorizations for the system.
3. Compare each authorization against the documented approved requests.
4. Confirm each authorization still matches the user's current role.
5. Identify any authorization that is no longer required.
6. Remove any authorization that is no longer required.
7. Correct any authorization that does not match its approved request.
8. Record the completed review in FL-EDMS.
9. Raise any finding from the review under SOP-QA-010, Handling of Deviations.

### 4.3 Review standalone audit trails

1. Confirm the audit trail is for a system recorded in FL-EDMS, a closed system.
2. Obtain the standalone system audit trail for the review period.
3. Review the audit trail at the frequency the QA Manager has set in the system inventory.
4. Check the audit trail for changes to access and configuration.
5. Check the audit trail for deletions or alterations of records.
6. Check the audit trail for activity outside normal use of the system.
7. Record the outcome of the review in FL-EDMS.
8. Handle any finding from the review under SOP-QA-010, Handling of Deviations.
9. Raise a corrective or preventive action where required under SOP-QA-011, Corrective and Preventive Action (CAPA).
10. Note that laboratory record audit trails are reviewed together with the record and are not reviewed under this procedure.

### 4.4 Verify backups and test restoration

1. Confirm the backup frequency is set in the system inventory by the System Owner with Quality Assurance.
2. Confirm the frequency is no less than weekly for GMP-critical systems.
3. Take backups at the frequency set in the system inventory.
4. Monitor each backup for successful completion.
5. Record the backup outcome in FL-EDMS.
6. Handle a failed backup under SOP-QA-010, Handling of Deviations.
7. Test restoration at validation.
8. Schedule a restore test at least annually after validation.
9. Set the scope of the scheduled restore test with Quality Assurance.
10. Restore the backed-up data in the test environment specified in the test scope.
11. Compare the restored data against the scope set for the test.
12. Record the result of the restore test in FL-EDMS.
13. Handle a failed restore test under SOP-QA-010, Handling of Deviations.
14. Raise a corrective or preventive action where required under SOP-QA-011, Corrective and Preventive Action (CAPA).
15. Process any change arising from a backup or restore test under SOP-QA-004, Change Control.

## 5. Records

Records created under this procedure include documented access requests and approvals, records of access provisioned and removed, access authorization reviews, standalone audit trail reviews, backup monitoring records, and restore test results. Each record is recorded in FL-EDMS, the company EDMS, at the time the activity is completed. Incomplete or corrected records are handled in FL-EDMS in the manner described in this procedure. All records created under this procedure are retained under the retention requirements of SOP-QA-001, Good Documentation Practices.

## 6. References

- 21 CFR Part 11, Electronic Records; Electronic Signatures.
- EU GMP Annex 11, Computerised Systems, as relied on by SOP-QA-018, Computer System Validation and Data Integrity.
- SOP-QA-001, Good Documentation Practices.
- SOP-QA-004, Change Control.
- SOP-QA-005, Training and Qualification.
- SOP-QA-010, Handling of Deviations.
- SOP-QA-011, Corrective and Preventive Action (CAPA).
- SOP-QA-018, Computer System Validation and Data Integrity.
- SOP-QA-047, Electronic System Downtime and Paper Backup.
