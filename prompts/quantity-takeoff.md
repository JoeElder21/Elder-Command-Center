# Quantity Takeoff

## Purpose

Perform accurate quantity takeoffs from construction documents for civil engineering and landscape architecture projects in Kentucky. Takeoffs support cost estimating, bid preparation, material ordering, and pay application verification. All quantities must be calculated using methods consistent with KYTC measurement standards and industry practice.

## When to Use

- Preparing engineer's or landscape architect's opinion of probable construction cost
- Verifying contractor bid quantities against plan quantities on public bid projects
- Supporting progress pay application reviews during construction administration
- Performing quantity comparisons for value engineering analysis
- Generating material quantity summaries for procurement on design-build projects
- Reviewing change order quantity documentation for reasonableness

## Required Inputs

1. **Construction plan set** (grading plans, utility plans, paving plans, landscape plans, erosion control plans, structural plans, detail sheets)
2. **Construction specifications** (for unit definitions, measurement methods, and pay item descriptions)
3. **Cross-sections** (for earthwork, roadway, and channel quantities)
4. **Geotechnical report** (for rock excavation estimates, undercut quantities, soil classification)
5. **KYTC Standard Specifications** (current edition, for measurement and payment definitions on state projects)
6. **Bid item list or schedule of values** (defines the pay item structure and units)
7. **Digital terrain model files** (DTM/TIN surfaces for earthwork volume computation, if available)

## Procedure

1. **Organize the takeoff by specification division and pay item.** Create a worksheet structure that mirrors the bid form or schedule of values. For KYTC projects, use the KYTC Standard Pay Item codes (e.g., 02082 -- Excavation, 02436 -- 15" Pipe, Class III). For private projects, organize by CSI division.

2. **Perform earthwork takeoff.**
   - Use the average end area method for roadway and channel earthwork when cross-sections are provided. Apply the prismoidal correction for volumes exceeding 5,000 CY where section shapes vary significantly.
   - For site grading, use the grid method (typically 25-ft or 50-ft grid) or compute from DTM surface comparison (existing ground vs. proposed grade).
   - Separate common excavation from rock excavation based on the geotechnical report's rock line profile. In Kentucky limestone geology, assume rock begins at the reported auger refusal depth unless borings indicate otherwise.
   - Apply shrink and swell factors: typical values for Kentucky soils are 1.15 shrink factor for compacted clay fill, 0.75 swell factor for blasted limestone rock. Confirm factors with the geotechnical engineer.
   - Calculate topsoil strip and replacement volumes separately (typically 6-inch depth per KYTC Standard Specification Section 211).

3. **Perform linear utility takeoff.**
   - Measure pipe lengths from manhole center to manhole center along the plan alignment. Do not deduct for manhole barrel width.
   - Count each pipe segment by diameter, material, and depth range (e.g., 8" PVC SDR 26 sanitary sewer, 0-6 ft depth; 8" PVC SDR 26 sanitary sewer, 6-10 ft depth) if the bid structure separates by depth.
   - Count manholes, junction boxes, inlets, and endwalls by type. For KYTC projects, reference the standard drawing type number (e.g., Type A inlet per KYTC RDM 010).
   - Measure trench rock separately if the geotechnical report indicates rock within the trench prism. Calculate trench rock as the volume below the rock line within a trench width of pipe OD plus 24 inches (or per specification).

4. **Perform paving and surfacing takeoff.**
   - Calculate pavement areas by surface type (HMA, PCC, gravel). Measure from plan dimensions, deducting areas for inlets, manholes, and other penetrations.
   - Calculate pavement quantities in tons for HMA (use 110 lb/SY/inch or the mix design unit weight) and in CY for PCC. Reference KYTC Standard Specification Section 401 for HMA and Section 501 for PCC.
   - Measure curb and gutter in linear feet by type (e.g., KYTC Type 1 CG per RDM 035).
   - Calculate sidewalk and ADA ramp areas separately. Count detectable warning panels per ADA ramp.

5. **Perform landscape and erosion control takeoff.**
   - Count plant materials by species, size, and type (shade tree, ornamental tree, shrub, groundcover) from the planting plan. Verify against the plant schedule.
   - Calculate seeding and mulching areas by seed mix type. For KYTC projects, reference the seed mixture designation (e.g., Mixture E for temporary, Mixture A for permanent).
   - Measure silt fence, construction entrance, and other EP&SC BMPs in linear feet or each, per the EP&SC plan. Calculate sediment basin volumes from the grading shown on the EP&SC detail.
   - Calculate mulch quantities in tons (typically 2 tons per acre for straw mulch, 4 tons per acre for wood cellulose fiber).

6. **Perform structural takeoff** (if applicable).
   - Calculate concrete volumes by structural element (footing, wall, slab, beam) in CY.
   - Calculate reinforcing steel weight in pounds, applying a 5% waste/lap factor unless the specification states otherwise.
   - Count structural steel by member size, length, and connection type.

7. **Compile and cross-check quantities.**
   - Sum all quantities by pay item.
   - Cross-check related quantities for consistency: excavation volume vs. fill volume (account for shrink/swell), pipe trench excavation vs. pipe length, paving area vs. subgrade area.
   - Round quantities per KYTC conventions: earthwork to nearest 10 CY, pipe to nearest LF, HMA to nearest ton, seeding to nearest 0.1 acre.

## Output Format

- Quantity summary table: Pay Item Number, Description, Unit, Calculated Quantity, Drawing Reference (sheet and grid location), Notes/Assumptions
- Detailed backup worksheets showing individual calculations for each quantity
- Earthwork summary with separate line items for common excavation, rock excavation, embankment, topsoil, and waste/borrow
- Landscape quantity schedule matching the plant schedule format on the plans
- Digital spreadsheet (XLSX) with formulas intact for audit trail

## Quality Checks

- [ ] Earthwork cut and fill volumes balance within 10% or borrow/waste quantities are explicitly identified
- [ ] Pipe quantities match between the plan view measurement and the profile stationing
- [ ] Pavement areas computed from the plan match within 3% of areas computed from typical sections
- [ ] Plant material counts match the plant schedule on the landscape plan
- [ ] All quantities use the correct unit of measure per the specification (LF, SY, CY, TON, EACH, LS)
- [ ] Rock excavation quantities are supported by geotechnical boring data
- [ ] No pay items in the bid form are left without a calculated quantity (zero quantities must be confirmed intentional)
- [ ] Shrink and swell factors are documented and sourced from the geotechnical report
- [ ] KYTC pay item codes are current and match the active Standard Specifications edition
- [ ] Quantity rounding follows agency or contract conventions

## Template Reference

- KYTC Standard Specifications for Road and Bridge Construction (measurement and payment clauses)
- KYTC Estimating Guide and Standard Pay Item List
- KYTC Standard Drawings (RDM, RPM, RDR series for structure and detail dimensions)
- AASHTO Guide for Design in Pavement Structures (pavement layer unit weights)
- Kentucky Erosion Prevention and Sediment Control Field Guide (BMP sizing and measurement)
- CSI UniFormat / MasterFormat for private project pay item organization
- ASCE Standard Guidelines for the Collection and Depiction of Existing Subsurface Utility Data (CI/ASCE 38-02)
