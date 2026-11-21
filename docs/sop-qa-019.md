# SOP-QA-019 — AI Use

**Fictitious Labs Inc.** · Version 1.0 · Effective 2026-03-02 · Owner: Quality Assurance

## 1. Purpose

Establish the requirements for the selection, assessment, approval, use, and monitoring of artificial intelligence tools in regulated activities.

## 2. Scope

Applies to all personnel at Fictitious Labs Inc., a US-based biologics organization manufacturing monoclonal antibody drug substance in the United States, who use, evaluate, approve, or oversee artificial intelligence tools that draft, check, summarize, or analyze content used in regulated records, submissions, or quality decisions, in the following functions: Quality Assurance, Quality Control laboratory.

Does not cover artificial intelligence embedded in validated manufacturing or laboratory equipment under change control, or software features that do not touch regulated records or decisions.

## 3. Responsibilities

- **Requester**
  - Request an AI tool for a defined intended use.
  - Use approved tools only within their approved intended use.
  - Report out-of-scope use or tool errors to Quality Assurance.

- **System Owner**
  - Own the tool's risk assessment, configuration, user support, and monitoring for each approved tool.
  - Maintain its entry in the AI tool register.

- **Quality Assurance**
  - Oversee AI tool use under this procedure.
  - Approve each tool for its intended use before use.
  - Accept residual risk.
  - Review monitoring outcomes.
  - Decide escalations.

## 4. Procedure

### 4.1 Selection

1. Select an AI tool for a defined regulated use. Selection considers: fit for the defined task; data handling — no GMP or confidential data is sent to a service not approved for it; sufficient transparency about the model and its limitations for the risk involved; and whether the tool's output can be verified by a qualified reviewer.
2. The Requester submits the proposed tool and intended use to Quality Assurance.
3. Before use, identify the intended use and the regulated records, submissions, or quality decisions the tool may affect.
4. The intended use and the permitted use are documented in the tool's entry in the AI tool register in FL-EDMS, which is how users determine what a tool is approved for.

### 4.2 Assessment

1. Assess risks to product quality and patient protection using the quality risk management process of SOP-QA-009, Quality Risk Management, which identifies hazards, analyzes and evaluates associated risks, and considers risk controls. Base the assessment on scientific knowledge and available evidence. Make the level of effort, formality, and documentation proportionate to the risk, uncertainty, importance, and complexity of the decision.
2. Address the AI-specific assessment factors: the tool's autonomy (what it does without human direction); the sensitivity of the data it receives or produces; the criticality of the output to a record or decision; and how detectable the tool's failure modes are by a qualified reviewer. Consider the strength and limitations of the information used in the assessment.
3. Record relevant assumptions and uncertainty in the assessment record in FL-EDMS.
4. Evaluate proposed controls to determine whether they reduce risk to an acceptable level. Consider whether a control could introduce new risks or increase existing risks.
5. Reassess the risk when controls may change it.
6. Quality Assurance evaluates and accepts the residual risk against the acceptance criteria of SOP-QA-009; a residual risk rated high also requires QA Manager acceptance.

### 4.3 Approval

1. Do not use an AI tool for regulated work until it has been approved for its intended use.
2. Quality Assurance approves the tool for the assessed intended use when the assessment shows the residual risk is acceptable and the controls of section 4.4 can be met.
3. The approval, the tool and its version, the System Owner, and the permitted use are recorded in the AI tool register.
4. A change to the tool, its version, or its intended use is made through SOP-QA-004, Change Control, and may require reassessment.

### 4.4 Use

1. Use an approved AI tool only within its approved intended use, as recorded in the AI tool register.
2. A user who identifies a need outside the approved use stops.
3. A user who identifies a need outside the approved use reports the out-of-scope use or need to Quality Assurance the same business day.
4. If an AI-assisted output has already entered a record outside the approved use, the record is handled under SOP-QA-010, Handling of Deviations.
5. An AI tool never makes a GMP decision autonomously. Before AI-assisted output contributes to a record or decision, a person whose qualification to review AI-assisted output has been established reviews the output. The reviewer must be qualified on the underlying task under SOP-QA-005, Training and Qualification — competent to catch the tool's failure modes for that task — and that qualification is documented in the training record. The reviewer remains accountable for every record or decision the output contributes to.
6. Ensure every AI-assisted record is traceable to the sources used to produce it. The record identifies the tool and its version.
7. The sources used to produce the output are retained and linked to the record in FL-EDMS or the record's own system, under the retention requirements of SOP-QA-001, Good Documentation Practices.

### 4.5 Monitoring

1. The System Owner monitors the tool's performance and errors in routine use.
2. Quality Assurance reviews each approved tool at least annually — more often where the assessed risk is higher — and on a trigger: a model or version change, an error trend, an incident involving AI-assisted output, or a proposed new use.
3. Monitoring outcomes, including any reassessment and its conclusions, are documented in the tool's register entry.
4. Monitoring outcomes, including any reassessment and its conclusions, are communicated to the tool's users.
5. Issues are escalated to Quality Assurance, and significant issues are inputs to management review under SOP-QA-008.

## 5. Records

AI use records, including the AI tool register, intended-use requests, risk assessments and residual-risk acceptances, approvals, reviewer qualification records, and monitoring and review records, retained in FL-EDMS under the retention requirements of SOP-QA-001, Good Documentation Practices.

## 6. References

- SOP-QA-001, Good Documentation Practices.
- SOP-QA-004, Change Control.
- SOP-QA-005, Training and Qualification.
- SOP-QA-008, Management Review.
- SOP-QA-009, Quality Risk Management.
- SOP-QA-010, Handling of Deviations.
- SOP-QA-018, Computer System Validation and Data Integrity.
