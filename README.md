# Fictitious Labs — Document Control

A pretend EDMS for a fictional company: **Fictitious Labs Inc.**, a small
US-based biologics company making a monoclonal antibody drug substance
(FL-101). The register behaves like a real electronic document management
system — document numbers, versions, effective dates, superseded versions
that stay findable, change notes — because that is what it is for.

## What's inside

44 controlled documents: 36 SOPs (Good Documentation Practices, Document
Control, Change Control, Deviations, CAPA, Batch Record Review and Product
Release, Computerized Systems & Data Integrity, and the rest of a small
quality system's backbone), a Validation Master Plan, the A280 test method
for FL-101 in two versions (v3.0 effective, v2.0 superseded — check the
acceptance criteria before you trust an old result), the assay
worksheet form, and the master batch record for FL-101 in two versions
(v2.0 effective, v1.0 superseded).

## How it was made

Most of these documents were drafted by
[The Procedure Machine](https://procedure-machine.streamlit.app/), a
multi-agent pipeline that builds procedures from public regulations and
guidance (ICH Q10, 21 CFR Parts 210/211, and friends), then adopted into
the fictional company: placeholders resolved against a consistency ledger,
citations verified against the source packet, one action per step.
A few were written directly, to the same standards, to close gaps a
library review found — procedures the rest of the library referenced but
nobody had written. The library is maintained as one system: when a
review finds a reference pointing at nothing, the missing document
gets written.

## Why it exists

It began as the reference world for a QA document-review training
simulator: reviewers check completed records against these governing
documents, in this system, the way the job actually works. That
simulator is now live alongside it, as the
[QA Review Simulator](https://fictitious-labs-review-sim.streamlit.app/).

It has become a thing in its own right: an open-source starter quality
system for a small biologics company. Most small companies build
effectively the same quality system, starting from a blank page or a
consultant's template library. This one is public, and MIT licensed.
Take it as a framework to iterate from, not as drop-in controlled
documents — every company has to make these its own before use.

Fictitious Labs Inc. does not exist. Any resemblance to a real company's
quality system is the point — and still a coincidence.
