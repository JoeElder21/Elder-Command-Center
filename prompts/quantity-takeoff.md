# Quantity Takeoff

## Purpose

Perform accurate quantity takeoffs from construction documents for civil engineering and landscape architecture projects in Kentucky. Takeoffs support cost estimating, bid preparation, material ordering, and pay application verification using methods consistent with KYTC measurement standards and industry practice.

## When to Use

- Preparing engineer's or landscape architect's opinion of probable construction cost
- Verifying contractor bid quantities against plan quantities on public bid projects
- Supporting progress pay application reviews during construction administration
- Performing quantity comparisons for value engineering or change order review
- Generating material quantity summaries for procurement on design-build projects

## Required Inputs

1. **Construction plan set** (grading, utility, paving, landscape, erosion control, structural, detail sheets)
2. **Construction specifications** (for unit definitions, measurement methods, and pay item descriptions)
3. **Cross-sections** (for earthwork, roadway, and channel quantities)
4. **Geotechnical report** (for rock excavation estimates, undercut quantities, soil classification)
5. **KYTC Standard Specifications** (current edition, for measurement and payment definitions on state projects)
6. **Bid item list or schedule of values** and **digital terrain model files** (DTM/TIN if available)

## Procedure

1. **Organize by pay item.** Mirror the bid form or schedule of values. For KYTC projects, use Standard Pay Item codes (e.g., 02082 -- Excavation, 02436 -- 15" Pipe, Class III). For private projects, organize by CSI division.
2. **Earthwork takeoff.** Use the average end area method for roadway/channel earthwork; apply the prismoidal correction for volumes exceeding 5,000 CY with significant section variation. For site grading, use the grid method (25-ft or 50-ft grid) or DTM surface comparison. Separate common excavation from rock excavation per the geotechnical rock line profile -- in Kentucky limestone geology, assume rock at the reported auger refusal depth. Apply shrink/swell factors (typical Kentucky: 1.15 shrink for compacted clay fill, 0.75 swell for blasted limestone). Calculate topsoil strip/replacement separately (6-inch depth per KYTC Section 211).
3. **Linear utility takeoff.** Measure pipe lengths manhole-center to manhole-center; do not deduct for barrel width. Categorize by diameter, material, and depth range if the bid structure separates by depth. Count manholes, inlets, and endwalls by type (reference KYTC standard drawing numbers, e.g., Type A inlet per RDM 010). Calculate trench rock as the volume below rock line within a trench width of pipe OD plus 24 inches.
4. **Paving and surfacing takeoff.** Calculate pavement areas by surface type (HMA, PCC, gravel), deducting for inlets and manholes. Convert HMA to tons at 110 lb/SY/inch or mix design unit weight (KYTC Section 401). Measure curb and gutter in LF by type (e.g., Type 1 CG per RDM 035). Calculate sidewalk/ADA ramp areas separately; count detectable warning panels per ramp.
5. **Landscape and erosion control takeoff.** Count plant materials by species, size, and type from the planting plan; verify against the plant schedule. Calculate seeding/mulching areas by mix type (KYTC Mixture E temporary, Mixture A permanent per Section 212). Measure silt fence and EP&SC BMPs in LF or each per the EP&SC plan. Calculate mulch at 2 tons/acre (straw) or 4 tons/acre (wood cellulose fiber).
6. **Structural takeoff.** Calculate concrete volumes by element (footing, wall, slab) in CY. Calculate reinforcing steel weight in pounds with a 5% waste/lap factor. Count structural steel by member size, length, and connection type.
7. **Compile and cross-check.** Sum by pay item. Cross-check: excavation vs. fill volumes (with shrink/swell), pipe trench excavation vs. pipe length, paving area vs. subgrade area. Round per KYTC conventions: earthwork to nearest 10 CY, pipe to nearest LF, HMA to nearest ton, seeding to nearest 0.1 acre.

## Output Format

- Quantity summary table: Pay Item Number, Description, Unit, Calculated Quantity, Drawing Reference, Notes/Assumptions
- Detailed backup worksheets showing individual calculations for each quantity
- Earthwork summary with line items for common excavation, rock excavation, embankment, topsoil, waste/borrow
- Landscape quantity schedule matching the plant schedule format; digital spreadsheet (XLSX) with formulas intact

## Quality Checks

- [ ] Earthwork cut and fill volumes balance within 10% or borrow/waste quantities are explicitly identified
- [ ] Pipe quantities match between plan view measurement and profile stationing
- [ ] Pavement areas from plan match within 3% of areas from typical sections
- [ ] Plant material counts match the plant schedule on the landscape plan
- [ ] All quantities use the correct unit of measure per the specification (LF, SY, CY, TON, EACH, LS)
- [ ] Rock excavation quantities are supported by geotechnical boring data
- [ ] No pay items in the bid form are left without a calculated quantity
- [ ] Shrink/swell factors are documented and sourced from the geotechnical report
- [ ] KYTC pay item codes are current and match the active Standard Specifications edition

## Template Reference

- KYTC Standard Specifications for Road and Bridge Construction (measurement and payment clauses)
- KYTC Estimating Guide and Standard Pay Item List
- KYTC Standard Drawings (RDM, RPM, RDR series for structure and detail dimensions)
- Kentucky Erosion Prevention and Sediment Control Field Guide (BMP sizing and measurement)
- CSI UniFormat / MasterFormat for private project pay item organization
