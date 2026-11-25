# SOP-QA-035 — Cold Chain Management and Temperature Excursion Evaluation

**Fictitious Labs Inc.** · Version 1.0 · Effective 2026-03-02 · Owner: Quality Assurance

## 1. Purpose

This procedure describes how product shipments are prepared, monitored, and closed at Fictitious Labs Inc.
It also describes how a temperature excursion in transit is evaluated against the shipment's stability budget.

## 2. Scope

Applies to the transport and distribution of FL-101 drug substance at Fictitious Labs Inc., a US-based biologics organization manufacturing monoclonal antibody drug substance in the United States, in the following functions: Quality Assurance, Warehouse, Quality Control laboratory.

Does not cover storage of product at Fictitious Labs Inc. sites or storage-condition excursions.
Storage and storage-condition excursions are governed by SOP-QA-023, Warehouse and Distribution Control.
This procedure covers transport and distribution only.

## 3. Responsibilities

**Warehouse Operator**

- Prepare each shipment in the qualified shipping configuration for the lane.
- Place the calibrated temperature data logger in each shipment.
- Complete the shipment preparation entries in the distribution record.

**Warehouse Supervisor**

- Verify the dispatch checks for each shipment before dispatch.
- Confirm only Released product is presented for dispatch.
- Escalate a reported transit problem to Quality Assurance.

**Quality Assurance**

- Review the logger record for each shipment.
- Evaluate each temperature excursion in transit against the shipment's stability budget.
- Decide whether product affected by an excursion remains acceptable.
- Notify the consignee before product affected by an excursion beyond the stability budget is used.
- Close each shipment in FL-EDMS after review.

**QA Manager**

- Approve the disposition of product affected by an excursion beyond the stability budget.
- Review excursion evaluations for completeness before shipment closure.

**Stability Coordinator**

- Provide the stability budget for a lot on request from Quality Assurance.
- Identify the stability data under SOP-QC-002, Stability Testing, that support the budget.

## 4. Procedure

### 4.1 Qualify and prepare a shipment

1. Confirm the shipping lane is qualified under SOP-QA-026, Equipment, Facilities, Utilities, and Systems Qualification.
2. Confirm the shipper configuration is qualified under SOP-QA-026, Equipment, Facilities, Utilities, and Systems Qualification.
3. Select the qualified shipping configuration for the lane.
4. Verify the product lot status is Released under SOP-QA-006, Batch Record Review and Product Release.
5. Pick the quantity of FL-101 drug substance stated on the distribution order.
6. Inspect each container for damage before packing.
7. Pack the containers in the qualified shipping configuration.
8. Condition the shipper components as specified for the configuration.
9. Verify the logger calibration status is current under SOP-QA-020, Calibration and Preventive Maintenance.
10. Place a calibrated temperature data logger in the shipment.
11. Record the logger identifier in the distribution record.
12. Start the temperature data logger before sealing the shipper.
13. Seal the shipper.
14. Label the shipper with the consignee address.
15. Record the consignee in the distribution record.
16. Record the lot number in the distribution record.
17. Record the quantity in the distribution record.
18. Record the dispatch date in the distribution record.
19. Complete the dispatch check for the shipment.
20. Release the shipment to the carrier.

### 4.2 Monitor the shipment in transit

1. Track the shipment against the planned transit time for the lane.
2. Record a carrier delay in the distribution record.
3. Report a carrier delay to the Warehouse Supervisor.
4. Report a damaged shipper on arrival to Quality Assurance.
5. Retrieve the temperature data logger at receipt.
6. Download the logger record.
7. Attach the logger record to the distribution record in FL-EDMS.
8. Forward the distribution record to Quality Assurance for review.

### 4.3 Evaluate a temperature excursion

1. Compare the logger record against the distribution condition of −20 °C ± 5 °C.
2. Identify each period outside the distribution condition.
3. Calculate the cumulative time out of condition for the shipment.
4. Request the stability budget for the lot from the Stability Coordinator.
5. Compare the cumulative time out of condition against the stability budget.
6. Record the comparison in the distribution record.
7. Decide whether the product remains acceptable when the time out of condition is within the stability budget.
8. Document the evaluation in the distribution record.
9. Raise a deviation under SOP-QA-010, Handling of Deviations, when the time out of condition exceeds the stability budget.
10. Notify the consignee before the product is used when the time out of condition exceeds the stability budget.
11. Record the consignee notification in the distribution record.
12. Obtain QA Manager approval of the disposition for an excursion beyond the stability budget.
13. Record the disposition in the distribution record.

### 4.4 Close the shipment

1. Confirm the logger record is attached to the distribution record.
2. Confirm the excursion evaluation is documented in the distribution record.
3. Confirm the distribution record states the consignee.
4. Confirm the distribution record states the lot number.
5. Confirm the distribution record states the quantity.
6. Confirm the distribution record states the dispatch date.
7. Sign the review entry in the distribution record.
8. Close the shipment in FL-EDMS.

## 5. Records

Distribution records are held under SOP-QA-023, Warehouse and Distribution Control.
Each distribution record states the consignee, lot, quantity, and date for the shipment.
The logger record for each shipment is filed with the distribution record.
The excursion evaluation for a shipment is documented in the distribution record.
Records generated under this procedure are retained under the retention requirements of SOP-QA-001, Good Documentation Practices.

## 6. References

- World Health Organization. WHO Technical Report Series 961, Annex 9: Model guidance for the storage and transport of time- and temperature-sensitive pharmaceutical products. 2011.
- 21 CFR 211.150, Distribution procedures, as applicable.
- 21 CFR 211.204, Returned drug products, as applicable.
- SOP-QA-001, Good Documentation Practices.
- SOP-QA-006, Batch Record Review and Product Release.
- SOP-QA-010, Handling of Deviations.
- SOP-QA-020, Calibration and Preventive Maintenance.
- SOP-QA-023, Warehouse and Distribution Control.
- SOP-QA-026, Equipment, Facilities, Utilities, and Systems Qualification.
- SOP-QC-002, Stability Testing.
