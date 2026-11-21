# SOP-QA-018 — Computer System Validation and Data Integrity

**Fictitious Labs Inc.** · Version 1.0 · Effective 2026-03-02 · Owner: Quality Assurance

## 1. Purpose

Establish how computerized systems used in regulated activities are validated and controlled, and how the integrity of the data they create and hold is assured throughout their lifecycle.

## 2. Scope

Applies to computerized systems that create, process, or store regulated records at Fictitious Labs Inc., a US-based biologics organization manufacturing monoclonal antibody drug substance in the United States, in the following functions: Quality Assurance, Quality Control laboratory, Engineering and maintenance.

Does not cover business systems with no regulated records, or the validation of individual spreadsheets used outside regulated records.

## 3. Responsibilities

- **System Owner**
  - Maintain system availability and maintenance.
  - Protect the security of data residing on the system.
  - Ensure the system's regulated use and applicable responsibilities are defined.
  - Own the system's entry in the system inventory, its risk assessment, its validation deliverables, its operation and periodic evaluation, and any request for its retirement.

- **System Administrator**
  - Administer system access and settings. Keep system-administration rights separate from responsibility for record content.
  - Document authorized access privileges and changes to access authorizations.
  - Process access requests approved by the System Owner.
  - Review access authorizations with the System Owner at least annually.
  - Operate the system's backup, recovery, and configuration controls.

- **Quality Assurance**
  - Review audit trails associated with regulated records as part of the review of those records.
  - Production and control records, including audit trails, are reviewed and approved by Quality Assurance.
  - Approve each system's criticality category, risk assessment, user requirements, supplier assessment, validation plan and report, and periodic evaluation.
  - Authorize release of a system for regulated use before use; release of a GMP-critical system also requires QA Manager approval.

- Personnel assigned duties involving computerized systems must have appropriate qualifications, access, and defined responsibilities. Qualifications and training follow SOP-QA-005, Training and Qualification; responsibility assignments are recorded in the system inventory.

## 4. Procedure

### 4.1 Inventory and risk assessment

1. Identify computerized systems that create, process, or store regulated records.
2. Record their regulated functions in an inventory.
3. Keep the inventory current. The system of record is the system inventory in FL-EDMS, maintained by Document Control.
4. When adding or updating an entry, users complete the system name and ID, System Owner, System Administrator, regulated functions, criticality category, Part 11 applicability and closed/open determination, validation status, and periodic evaluation due date.
5. Assess each system's risks throughout its lifecycle, considering patient safety, data integrity, and product quality.
6. Document the basis for the extent of validation and data-integrity controls.
7. Scale validation effort to the system's impact on product quality and data integrity, based on its intended use, not its size.
8. Before identifying a system as critical, use the following selection rule: systems are categorized as GMP-critical (direct impact on product quality or on the integrity of data used for release decisions), GMP-supporting (indirect impact), or non-GMP.
9. The System Owner proposes the category from a risk assessment under SOP-QA-009, Quality Risk Management.
10. Quality Assurance approves the category.
11. For systems identified as critical, maintain a current system description covering physical and logical arrangements, data flows and interfaces, hardware and software prerequisites, and security measures.

### 4.2 Requirements and supplier assessment

1. Document the system's required functions in a User Requirements Specification based on its intended use, regulated impact, and documented risk assessment.
2. Keep requirements traceable throughout the system lifecycle.
3. Assess supplier competence and reliability when selecting a system or service provider. Base the need for a supplier audit on risk.
4. Review supplier documentation for commercial off-the-shelf systems to determine whether it supports the documented user requirements.
5. For third-party services involving system provision, installation, configuration, integration, validation, maintenance, modification, retention, or data processing, establish a formal agreement that clearly defines responsibilities. Apply this requirement to internal IT departments providing such services.
6. User requirements, supplier assessments, and agreements are approved by the System Owner and Quality Assurance before use; supplier assessment and audit follow SOP-QA-015, Supplier Quality, proportionate to risk.

### 4.3 Validation and release

1. Plan validation across the relevant lifecycle stages.
2. Document the standards, protocols, acceptance criteria, procedures, and records.
3. Justify them based on risk.
4. For bespoke or customized systems, formally assess quality and performance measures across the lifecycle stages.
5. For bespoke or customized systems, formally report quality and performance measures across the lifecycle stages.
6. Demonstrate appropriate test methods and scenarios.
7. Include system and process parameter limits, data limits, and error handling where relevant.
8. The System Owner, with Quality Assurance, determines in the validation plan when these limits and error-handling scenarios are relevant.
9. The decision is documented in the protocol.
10. Assess the adequacy of automated testing tools and test environments.
11. Document the assessment.
12. Record validation deviations and applicable change-control records in the validation documentation.
13. For data migration or transfer to another format or system, verify that data values and meaning are not altered.
14. For systems within the scope of 21 CFR Part 11, validate the system to ensure accuracy, reliability, consistent intended performance, and the ability to discern invalid or altered records.
15. Before regulated use, complete the required validation deliverables. The required deliverables are the validation plan, user requirements specification, risk assessment, test protocols and results, traceability record, and validation report.
16. Assess results against the acceptance criteria. Validation deviations are dispositioned under SOP-QA-010, Handling of Deviations.
17. Quality Assurance approves the validation report.
18. Quality Assurance authorizes release for regulated use; release of a GMP-critical system also requires QA Manager approval. No system is used for regulated work before that authorization.

### 4.4 Operation and data integrity

1. Maintain records that are attributable, legible, contemporaneous, original, and accurate (ALCOA) from creation to retirement, in whatever system holds them.
2. Design and operate systems so required data are captured when the activity is performed. Do not use temporary records that are discarded after transcription.
3. Ensure changes to required data are recorded.
4. For critical data entered manually, provide an additional accuracy check by a second operator or validated electronic means.
5. Address the criticality and potential consequences of incorrect entry through risk management.
6. For systems that exchange data electronically, use appropriate built-in checks for correct and secure data entry and processing.
7. Protect data against physical and electronic damage.
8. Check stored data for accessibility, readability, and accuracy.
9. Ensure access throughout the applicable retention period.
10. Generate accurate and complete copies of electronic records in human-readable and electronic form, suitable for review, inspection, and copying.
11. For records supporting batch release, ensure printouts can indicate whether data changed after original entry.
12. For systems within the scope of 21 CFR Part 11, determine whether each system is a closed system or an open system before regulated use. The QA Manager, with the System Owner, makes the classification and determines which Part 11 controls apply.
   - For closed systems, apply the applicable controls in 21 CFR Part 11 § 11.10, including the controls listed below.
   - For open systems, apply the applicable controls in § 11.10 and additional measures as needed to protect record authenticity, integrity, and, as appropriate, confidentiality from creation to receipt. Additional measures may include document encryption and appropriate digital signature standards.
   - Protect records so they can be accurately and readily retrieved throughout their retention period.
   - Use operational checks to enforce permitted sequencing of steps and events, and authority checks to ensure that only authorized individuals can perform system actions, as appropriate.
   - Use secure, computer-generated, time-stamped audit trails to record operator actions that create, modify, or delete records. Do not obscure previously recorded information. Retain audit-trail documentation at least as long as the related records.
13. The determination is recorded in the system inventory.
14. Review audit trails associated with regulated records as part of the review of those records. Where regulations specify a review frequency, apply that frequency to the audit trail.
15. Otherwise, the QA Manager sets the frequency in the system inventory using process knowledge and a risk assessment that considers data criticality, controls, and product-quality impact.
16. Laboratory record audit trails are reviewed together with the record by the record reviewer.
17. Standalone system audit trails are reviewed by the System Owner.
18. Each review is documented in FL-EDMS.
19. Record the identity of operators who enter, change, confirm, or delete data, including the date and time.
20. Record the creation, change, and cancellation of access authorizations.
21. Restrict system access to authorized individuals. Do not use shared login credentials for actions that must be attributable to an individual.
22. Document authorized personnel's access privileges.
23. Where possible, use technical controls to restrict changes to specifications, process parameters, data, or manufacturing and testing methods.
24. For electronic signatures used under 21 CFR Part 11:
    - Ensure each signature is unique to one individual, is not reused or reassigned, and is linked to its record. Include the signer's name, the date and time, and the meaning of the signature with the signed record.
    - Verify an individual's identity before establishing, assigning, certifying, or otherwise authorizing that individual's electronic signature.
    - For signatures not based on biometrics, require at least two distinct identification components, such as an identification code and password. For a series of signings during one continuous period of controlled system access, require all components for the first signing and at least one component for subsequent signings. For signings outside that period, require all components for each signing.
    - Ensure non-biometric signature components are used only by their genuine owners, and that attempts by anyone else to use them require collaboration by two or more individuals. Design biometric signatures so they cannot be used by anyone other than their genuine owners.
    - For identification codes and passwords, maintain unique combinations; periodically check, recall, or revise issuances; deauthorize potentially compromised tokens, cards, or other devices and issue replacements using suitable controls; use safeguards to prevent unauthorized use and to detect and report attempted unauthorized use promptly; and initially and periodically test devices that bear or generate identification-code or password information.
    - For signatures used in place of handwritten signatures, certify to FDA, before or at the time of use, that the signatures are intended to be the legally binding equivalent of handwritten signatures. This certification applies to the electronic signatures used in FL-EDMS and is made before first use.
25. Access to each system is approved by the System Owner (with Quality Assurance concurrence for GMP-critical systems) on a documented request recorded in FL-EDMS.
26. The System Administrator and the System Owner review access authorizations at least annually; record, data, and audit-trail reviews are performed by the roles assigned in this section.
27. Completion of each review is documented in FL-EDMS.

### 4.5 Backup, recovery, and continuity

1. Back up relevant data regularly.
2. During validation, check backup integrity and accuracy.
3. During validation, demonstrate that data can be restored.
4. Monitor these controls periodically.
5. For systems supporting critical processes, document continuity arrangements, such as a manual or alternative system.
6. For systems supporting critical processes, test continuity arrangements, such as a manual or alternative system.
7. Set the time to bring alternative arrangements into use based on risk and the supported process.
8. Backup frequency is set in the system inventory by the System Owner with Quality Assurance — no less than weekly for GMP-critical systems.
9. The System Administrator monitors backup completion.
10. Restoration is tested at validation and at least annually.
11. Continuity arrangements for GMP-critical systems are decided by the System Owner with Quality Assurance.

### 4.6 Changes, incidents, and periodic evaluation

1. Do not make a system or configuration change unless it follows SOP-QA-004, Change Control, which is the governing procedure for computerized-system changes as for all other controlled changes.
2. Report every incident, including system failures and data errors, as a deviation under SOP-QA-010, Handling of Deviations; there is no separate system-incident route.
3. Assess every incident, including system failures and data errors, as a deviation under SOP-QA-010, Handling of Deviations.
4. Where the assessment requires corrective or preventive action, it is handled under SOP-QA-011, Corrective and Preventive Action (CAPA).
5. The assessment and follow-up are documented in the deviation and CAPA records.
6. For critical incidents, identify the root cause.
7. For critical incidents, use the root cause as the basis for corrective and preventive actions.
8. Evaluate systems periodically to confirm that they remain in a valid state and comply with applicable GMP requirements. As appropriate, include current functionality, deviations, incidents, problems, upgrade history, performance, reliability, security, and validation status.
9. The System Owner performs the periodic evaluation at least every 2 years for GMP-critical systems and every 3 years for GMP-supporting systems, and on trigger (a major change or an incident trend).
10. Quality Assurance approves the evaluation.
11. The evaluation record is held in FL-EDMS.

### 4.7 Archiving and retirement

1. Check archived data for accessibility, readability, and integrity.
2. When a system change could affect archived data retrieval, test the ability to retrieve the data.
3. On retirement, the System Owner proposes the retirement.
4. On retirement, Quality Assurance approves the retirement.
5. Data are archived or migrated to the successor system with verification that values and meaning are not altered; archive responsibilities rest with the System Owner and Document Control, and archived records are retained under SOP-QA-001, Good Documentation Practices.

## 5. Records

Computerized-system records, including the system inventory, risk assessments, user requirements specifications, supplier assessments and agreements, validation plans, protocols, results, traceability records and reports, release authorizations, access requests and reviews, audit-trail reviews, backup and restoration records, periodic evaluations, and retirement records, retained in FL-EDMS under the retention requirements of SOP-QA-001, Good Documentation Practices.

## 6. References

- 21 CFR Part 11, Electronic Records; Electronic Signatures.
- FDA guidance: Data Integrity and Compliance With Drug CGMP: Questions and Answers (December 2018).
- SOP-QA-001, Good Documentation Practices.
- SOP-QA-004, Change Control.
- SOP-QA-005, Training and Qualification.
- SOP-QA-009, Quality Risk Management.
- SOP-QA-010, Handling of Deviations.
- SOP-QA-011, Corrective and Preventive Action (CAPA).
- SOP-QA-015, Supplier Quality.
