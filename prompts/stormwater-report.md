# Stormwater Management Report Prompt

## Purpose

Develop a stormwater management analysis for a development site in Kentucky, including pre- and post-development hydrology, water quality treatment strategy, and Best Management Practice (BMP) selection. This report supports KPDES permit applications, MSD/LFUCG stormwater plan approvals, and compliance with 401 KAR Chapter 5 and local stormwater ordinances.

## When to Use

- Preparing a stormwater management plan for a land disturbance permit application
- Developing the drainage study component of a subdivision or development plan
- Responding to Louisville MSD, LFUCG, or county stormwater review comments
- Designing BMPs for a site subject to post-construction water quality requirements
- Preparing a Stormwater Pollution Prevention Plan (SWPPP) for KPDES KYR10 permit coverage

## Required Inputs

1. **Topographic survey** with 1-foot contours minimum (2-foot for sites over 10 acres)
2. **USDA soils data** -- hydrologic soil groups (A, B, C, D) mapped across the site
3. **Proposed site plan** with impervious area calculations (rooftops, pavement, sidewalks)
4. **Offsite contributing drainage areas** delineated from USGS topo or LiDAR
5. **Downstream conveyance information** -- pipe sizes, ditch capacities, receiving stream
6. **Local stormwater design criteria** -- Louisville MSD Design Manual, LFUCG Stormwater Manual, or county equivalent
7. **Project disturbed area** in acres (triggers KPDES KYR10 if 1 acre or more)

## Procedure

1. **Watershed Delineation**: Delineate pre-development drainage sub-basins on the topographic survey. Identify all discharge points leaving the site. Delineate offsite contributing areas that flow onto or through the site. Use the KYTC Drainage Manual or Louisville MSD methodology for delineation standards.
2. **Pre-Development Hydrology**: Calculate pre-development peak runoff rates using the Rational Method (sites under 100 acres) or SCS/NRCS TR-55 methodology (sites over 100 acres or where detention is required). Document the following for each sub-basin: drainage area, time of concentration (Tc), runoff coefficient (C) or curve number (CN), and peak flow for the 2-year, 10-year, 25-year, and 100-year storm events. Use Kentucky-specific rainfall data from NOAA Atlas 14, Volume 2 (Ohio River Basin).
3. **Post-Development Hydrology**: Recalculate all hydrologic parameters for the developed condition. Account for increased impervious surface, grading changes that alter drainage boundaries, and concentrated flow from roof drains and pavement. Document the change in peak discharge at each discharge point.
4. **Detention/Retention Sizing**: Size detention facilities to meet local release rate requirements. Louisville MSD requires post-development peak discharge not to exceed pre-development rates for the 2-year through 25-year storms and safe passage of the 100-year storm. LFUCG requires similar control. Use the Modified Rational Method or reservoir routing (Modified Puls) to size detention basins. Provide stage-storage-discharge tables for each facility.
5. **Water Quality Volume (WQv) Calculation**: Calculate the water quality volume per the local standard. Louisville MSD requires treatment of the first 0.6 inches of rainfall from the post-development impervious area (WQv = 0.6 in x impervious area / 12). LFUCG uses a similar standard. Document the WQv for each drainage area requiring treatment.
6. **BMP Selection and Design**: Select BMPs appropriate to the site conditions, soils, and local approval:
   - **Bioretention/Rain Gardens**: Suitable for HSG A and B soils; size for WQv with 48-hour drawdown; provide underdrain in HSG C and D soils
   - **Permeable Pavement**: Viable for parking areas with low truck traffic; requires HSG A or B subgrade or underdrain system
   - **Constructed Wetlands**: Appropriate for large sites with sustained base flow; minimum 1% of contributing impervious area
   - **Detention Basins (Dry/Wet)**: Standard practice for peak rate control; must include sediment forebay sized for 0.1 inches per impervious acre
   - **Level Spreaders/Vegetated Filter Strips**: Appropriate for sheet flow from small impervious areas; maximum 75-foot flow length per MSD standards
   - **Underground Detention**: Permitted by MSD when surface detention is infeasible; must provide maintenance access
7. **Conveyance Design**: Size storm sewers using the Rational Method and Manning's equation. Minimum pipe diameter 12 inches for Louisville MSD, 15 inches for LFUCG. Design open channels using Manning's equation with appropriate roughness coefficients. Verify outlet protection per KDOW erosion prevention standards.
8. **Floodplain and Stream Buffer Compliance**: If the site is adjacent to a blue-line stream or within a mapped floodplain, document compliance with 401 KAR 4:060 (floodplain management), any local stream buffer ordinance (Louisville MSD requires 50-foot stream buffers), and any required USACE Section 404 permits for stream or wetland impacts.
9. **Erosion Prevention and Sediment Control (EPSC)**: Outline the EPSC plan components required for KPDES KYR10 coverage: construction phasing, perimeter sediment controls, inlet protection, temporary seeding schedule, concrete washout provisions, and inspection frequency (every 7 days and within 24 hours of 0.5-inch rainfall).

## Output Format

- Executive Summary (site area, impervious change, BMP approach, permit requirements)
- Pre-Development Hydrology Tables (sub-basin data, Tc calculations, peak flows)
- Post-Development Hydrology Tables (revised parameters, peak flows, volume comparison)
- Detention Facility Design (stage-storage-discharge, routing summary, emergency spillway)
- Water Quality Volume Calculations and BMP Sizing Sheets
- Storm Sewer Design Tables (pipe schedule with size, slope, capacity, velocity)
- EPSC Narrative and Phasing Plan
- Appendices: NOAA Atlas 14 rainfall data, soil reports, downstream analysis

## Quality Checks

- Rainfall intensities must be from NOAA Atlas 14 for the correct Kentucky county, not outdated IDF curves
- Time of concentration calculations must use segmented Tc (sheet flow limited to 100 feet per TR-55)
- Curve numbers must reflect actual soil survey HSG, not assumed values
- Detention routing must show the full inflow/outflow hydrograph, not just peak-in/peak-out
- BMP sizing must demonstrate WQv capture with drawdown time meeting local standards
- All pipe velocities must be between 2.5 fps (minimum self-cleaning) and 15 fps (maximum)
- KPDES KYR10 NOI filing requirement must be flagged for any site disturbing 1 acre or more

## Template Reference

- Louisville MSD Stormwater Design Manual (current edition)
- LFUCG Stormwater Manual and Best Management Practices Manual
- KYTC Drainage Manual (hydraulic methodology)
- NOAA Atlas 14, Volume 2 -- Precipitation-Frequency Atlas
- KDOW KPDES KYR10 General Permit for Stormwater Discharge Associated with Construction
- 401 KAR Chapter 4 (floodplain management regulations)
- 401 KAR Chapter 5 (water quality standards)
- USDA TR-55, Urban Hydrology for Small Watersheds
