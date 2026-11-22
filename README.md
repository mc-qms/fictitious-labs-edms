# Fictitious Labs — Document Control

A pretend EDMS for a fictional company: **Fictitious Labs Inc.**, a small
US-based biologics company making a monoclonal antibody drug substance
(FL-101). The register behaves like a real electronic document management
system — document numbers, versions, effective dates, superseded versions
that stay findable, change notes — because that is what it is for.

## What's inside

40 controlled documents: 34 SOPs (Good Documentation Practices, Document
Control, Change Control, Deviations, CAPA, Batch Record Review and Product
Release, Computerized Systems & Data Integrity, and the rest of a small
quality system's backbone), a Validation Master Plan, the A280 test method
for FL-101 in two versions (v3.0 effective, v2.0 superseded — check the
acceptance criteria before you trust an old result), and the assay
worksheet form.

## How it was made

Every SOP in this library but one was drafted by
[The Procedure Machine](https://procedure-machine.streamlit.app/), a
multi-agent pipeline that builds procedures from public regulations and
guidance (ICH Q10, 21 CFR Parts 210/211, and friends), then adopted into
the fictional company: placeholders resolved against a consistency ledger,
citations verified against the source packet, one action per step.
The exceptions are SOP-QA-027, Batch Record Content and Control,
SOP-QA-028, Specification Management, and SOP-QA-029, Contamination
Control Strategy, written directly to the same standards to close gaps
a library review found: batch records were referenced by nine
procedures but defined by none, specifications were applied everywhere
but governed nowhere, and the contamination control strategy was
overseen but never written down. The FL-101 specification and the
FL-101 packaging and labeling work instruction were likewise authored
directly, against the company's consistency ledger.

## Why it exists

The library is the reference world for a QA document-review training
simulator: reviewers check completed records against these governing
documents, in this system, the way the job actually works. The simulator
is a separate app, coming later.

Fictitious Labs Inc. does not exist. Any resemblance to a real company's
quality system is the point — and still a coincidence.
