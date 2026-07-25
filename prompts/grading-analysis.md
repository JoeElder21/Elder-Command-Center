# Grading Analysis Prompt

## Purpose

Evaluate a proposed grading strategy for a development site in Kentucky, including cut/fill volume analysis, slope stability assessment, and compliance with local grading ordinances and EPSC requirements. This analysis supports cost estimation, earthwork bid evaluation, and identification of geotechnical risks before construction begins.

## When to Use

- Developing a preliminary grading plan during schematic or design development phases
- Evaluating cut/fill balance to minimize hauling costs during construction budgeting
- Reviewing a contractor's proposed grading approach against design intent
- Assessing slope stability for sites in karst terrain or with fill-over-natural-ground conditions
- Preparing the grading component of a land disturbance permit application

## Required Inputs

1. **Existing topographic survey** with 1-foot contours (2-foot acceptable for sites over 20 acres)
2. **Proposed grading plan** with finished grade contours and spot elevations
3. **Geotechnical investigation report** including boring logs, soil classifications (USCS), and compaction recommendations
4. **Building finished floor elevations (FFE)** and minimum freeboard above 100-year flood or stormwater ponding
5. **Utility invert elevations** -- sanitary sewer, storm sewer, water main -- to verify gravity service and cover requirements
6. **Local grading ordinance** -- Louisville MSD, LFUCG, or county requirements for maximum slopes, retaining walls, and land disturbance permits

## Procedure

1. **Existing Conditions Analysis**: Generate an existing conditions surface model from the topographic survey. Identify the overall relief (highest to lowest elevation), predominant slope direction, and natural drainage patterns. Flag areas of steep slopes (greater than 3:1), existing retaining walls or embankments, and any karst features (sinkholes, springs, exposed bedrock). For sites in Kentucky karst regions (Inner Bluegrass, Pennyroyal Plateau, Western Coalfield), overlay the KGS sinkhole database on the existing topo.
2. **Design Grade Establishment**: Confirm finished floor elevations provide minimum freeboard: 1 foot above the 100-year flood elevation for structures in or near floodplains (per 401 KAR 4:060), and a minimum of 6 inches above adjacent grade for slab-on-grade construction. Verify that building pad grades allow gravity flow to the sanitary sewer connection with minimum 1% slope on the building lateral. Confirm that the FFE allows a minimum of 3 feet of cover over the water service line.
3. **Cut/Fill Volume Calculation**: Generate a cut/fill map using the existing and proposed surface models. Use the average-end-area method or grid method to compute earthwork volumes. Report gross cut volume, gross fill volume, net cut or fill, and the resulting balance or surplus/deficit. Apply a shrinkage factor of 15-25% for general fill and a swell factor of 20-30% for rock excavation, calibrated to the geotechnical report's soil classifications. Separate topsoil stripping volumes (typically 6 inches) and report them independently for reuse calculations.
4. **Slope Analysis**:
   - Verify all proposed fill slopes do not exceed 3:1 (horizontal to vertical) unless a retaining wall or engineered slope is provided
   - Verify all cut slopes in soil do not exceed 2:1 unless supported by geotechnical analysis
   - For any slopes steeper than 3:1 that will receive turf, specify erosion control blanket and confirm species selection for slope stabilization (Kentucky 31 fescue or equivalent per KYTC Standard Specifications Section 212)
   - Verify that building pads have positive drainage away from foundations at minimum 2% slope for the first 10 feet
5. **Retaining Wall Assessment**: Identify locations where retaining walls are needed to transition between grade differentials. Classify walls by exposed height: walls 4 feet or less may use segmental retaining wall (SRW) units per manufacturer's gravity wall tables; walls exceeding 4 feet require a geogrid-reinforced design or cast-in-place concrete with PE-sealed structural design. Note that any retaining wall exceeding 4 feet in exposed height requires a building permit and structural engineering per the Kentucky Building Code (KBC).
6. **Karst and Sinkhole Mitigation**: For sites with identified karst features, specify sinkhole repair procedures per KGS and local requirements. Louisville MSD requires sinkhole investigation and engineered repair for any sinkhole within 100 feet of proposed construction. Document the proposed treatment: throat excavation, geotechnical fabric and graded stone backfill, clay cap, and positive drainage rerouting. Flag any sinkholes that require KDOW notification or coordination.
7. **Erosion Prevention and Sediment Control (EPSC) Coordination**: Verify that the proposed grading plan supports the EPSC phasing plan. Confirm that sediment basins are sized for the contributing drainage area (3,600 cubic feet per acre of disturbed land per KDOW requirements). Identify temporary sediment basin locations and confirm that they can be constructed before mass grading begins. Verify that permanent stormwater facilities are not used as temporary sediment basins unless specifically designed for dual use.
8. **Earthwork Cost Estimate**: Develop a rough-order-of-magnitude earthwork cost estimate using current unit prices: on-site cut and fill ($3-8/CY for common excavation in central KY), rock excavation ($15-35/CY depending on method), import fill ($12-25/CY delivered and compacted), export of surplus ($10-20/CY loaded and hauled). Adjust for haul distances exceeding 1,000 feet on site.

## Output Format

- Grading Summary (site area, overall relief, cut/fill balance, net earthwork)
- Existing and Proposed Surface Comparison Exhibit
- Cut/Fill Color Map with volume annotations by area
- Earthwork Volume Table (sub-area breakdown with cut, fill, net, and adjusted volumes)
- Slope Analysis Map (color-coded by slope range: 0-5%, 5-10%, 10-15%, 15-20%, 20%+)
- Retaining Wall Schedule (location, exposed height, wall type, design responsibility)
- Karst Feature Inventory and Mitigation Plan (if applicable)
- Earthwork Cost Estimate Summary
- Recommendations for Design Refinement

## Quality Checks

- Cut/fill volumes must account for topsoil stripping separately from mass earthwork
- Shrinkage and swell factors must be derived from the geotechnical report, not generic assumptions
- All slopes adjacent to public rights-of-way must be 4:1 or flatter for mowing safety
- FFE must be verified against both the flood elevation and the sanitary sewer invert
- Retaining walls exceeding 4 feet must be flagged for structural engineering and building permit
- Karst features must be documented even if they are outside the proposed disturbance area
- EPSC sediment basin sizing must use the actual disturbed area, not the total parcel area
- Cost estimates must state the pricing date and geographic basis

## Template Reference

- KYTC Standard Specifications for Road and Bridge Construction (earthwork and erosion control)
- 401 KAR 4:060 (floodplain management -- minimum FFE requirements)
- Kentucky Building Code (retaining wall structural requirements)
- KGS Sinkhole Database and karst remediation guidance
- Louisville MSD Design Manual (grading, sinkhole repair, and EPSC requirements)
- LFUCG Stormwater Manual (grading standards and EPSC phasing)
- KDOW Land Disturbance Permit requirements (BMP sizing criteria)
