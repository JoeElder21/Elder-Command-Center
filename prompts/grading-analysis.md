# Grading Analysis

## Purpose
Perform a cut/fill analysis and evaluate grading strategies for a development site. This analysis balances earthwork on site, identifies haul-off or import needs, addresses erosion control, and ensures compliance with local grading standards and ADA accessibility requirements.

## When to Use
- During preliminary design to evaluate site feasibility and earthwork costs
- When comparing alternative site layouts to minimize grading expense
- Preparing a grading plan for a land disturbance permit (KYR10 or local equivalent)
- Reviewing a contractor's proposed grading approach for constructability

## Required Inputs
1. **Topographic survey** with 1-foot or 2-foot contour intervals and spot elevations
2. **Proposed site plan** with building pad elevations, road profiles, and parking grades
3. **Geotechnical report** with soil classifications, rock depth, and fill suitability
4. **Stormwater design constraints** (detention basin footprints, BMP locations, outfall elevations)
5. **Utility invert elevations** for gravity sewer, storm sewer, and water main cover requirements
6. **Local grading ordinance requirements** (maximum disturbed slope, retaining wall triggers)

## Procedure
1. **Existing Conditions Modeling** -- Build an existing surface model from the topographic survey using Civil 3D, OpenRoads, or equivalent software. Verify survey data against LiDAR (KyFromAbove) for areas outside the surveyed limits. Identify existing drainage patterns, concentration points, and off-site drainage entering the parcel.
2. **Proposed Surface Development** -- Design the finished grade surface incorporating: building pad elevations (minimum 1-foot above the 100-year flood elevation or adjacent ground), parking lot grades (1.5% minimum, 5% maximum), ADA-accessible routes (2% maximum cross-slope, 5% maximum running slope per ADA/ANSI A117.1), and roadway profiles per KYTC or local public works design standards.
3. **Cut/Fill Volume Calculation** -- Generate a cut/fill map (heat map) and compute earthwork volumes using the average end area or prismoidal method. Separate rock excavation quantities if the geotechnical report indicates rock within the grading limits. Present results as: total cut (CY), total fill (CY), net earthwork (CY), and shrink/swell-adjusted balance (apply 15-25% shrinkage factor for common earth depending on soil type).
4. **Earthwork Balance Optimization** -- If the site is significantly out of balance, evaluate adjustments: raise or lower building pad elevations, adjust parking lot grades, steepen or flatten slopes, add retaining walls to reduce earthwork, or incorporate excess cut into landscape berms or detention basin embankments. Document each scenario with revised volumes.
5. **Slope Stability and Retaining Walls** -- Identify all proposed slopes exceeding 3:1 (H:V). Slopes steeper than 2:1 typically require geotechnical analysis and engineered stabilization. Flag any fills exceeding 10 feet in depth that require controlled compaction specifications. Note retaining walls exceeding 4 feet in exposed height that trigger structural engineering and building permit requirements.
6. **Erosion and Sediment Control** -- Overlay the grading limits on a phasing plan. Identify areas of concentrated flow, steep slopes, and stockpile locations. Specify BMP placement per the Kentucky Erosion Prevention and Sediment Control Field Guide: silt fence, sediment basins (required for disturbed areas draining more than 10 acres to a common point), inlet protection, construction entrances, and temporary seeding schedules.
7. **Drainage Integration** -- Verify that the proposed grades direct runoff to the designed stormwater system. Check that building finished floor elevations provide positive drainage away from structures (minimum 6 inches of fall in the first 10 feet). Confirm detention basin bottom grades, overflow spillway elevations, and outfall pipe inverts are consistent with the grading plan.

## Output Format
- Cut/fill summary table (area, cut volume, fill volume, net, adjusted net)
- Cut/fill heat map exhibit (color-coded plan view)
- Grading scenario comparison matrix (if multiple layouts evaluated)
- Slope analysis exhibit (slopes categorized: 0-5%, 5-15%, 15-25%, 25%+)
- Earthwork cost estimate using current unit rates (common excavation, rock excavation, fill placement, topsoil stripping and replacement)
- Recommendations narrative (1-2 pages)

## Quality Checks
- Surface model verified against survey control points (maximum 0.1-foot tolerance)
- Cut/fill volumes computed from the same datum and coordinate system
- Shrinkage/swell factor documented and appropriate for the soil types on site
- All proposed slopes within the jurisdiction's allowable maximums
- ADA routes verified for slope compliance at every segment
- Earthwork balance accounts for topsoil stripping, unsuitable material removal, and infrastructure trench backfill
- Erosion control plan references the current KYR10 permit requirements

## Template Reference
- KYTC Highway Design Manual (slope and roadway grade standards)
- Kentucky Erosion Prevention and Sediment Control Field Guide (BMP selection)
- KPDES KYR10 General Permit for stormwater discharge from construction activities
- ADA Standards for Accessible Design and ANSI A117.1
- Local grading ordinance (Louisville Metro, LFUCG, or applicable jurisdiction)
