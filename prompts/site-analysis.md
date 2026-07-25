# Site Analysis Prompt

## Purpose

Evaluate a parcel's development potential by systematically assessing physical, regulatory, and environmental constraints. This analysis supports due diligence for clients considering land acquisition or development in Kentucky and produces a constraints-and-opportunities summary suitable for inclusion in feasibility reports.

## When to Use

- Pre-acquisition due diligence for a client considering purchase of a parcel
- Early-phase feasibility study before schematic design begins
- Responding to an RFP or RFQ that requires a site constraints narrative
- Evaluating an existing site for redevelopment or change of use

## Required Inputs

1. **Parcel ID / PVA number** and county (for KY PVA and KYTC records lookup)
2. **Street address or GPS coordinates** of the site
3. **Proposed use** (residential, commercial, institutional, mixed-use, etc.)
4. **Available survey data** -- boundary survey, ALTA, or topographic survey if on hand
5. **Client goals** -- target density, square footage, timeline, budget constraints

## Procedure

1. **Boundary and Legal Review**: Confirm parcel boundaries via the county PVA GIS portal. Note deed restrictions, easements (utility, access, conservation), and right-of-way dedications recorded in the county clerk's office. For Louisville Metro, use LOJIC; for Lexington-Fayette, use LFUCG GIS.
2. **Topographic Assessment**: Obtain or generate a topographic survey. Identify slopes exceeding 20% (KRS 100.111 steep-slope provisions), ridgelines, saddles, and drainage divides. Calculate the overall relief across the parcel. Note any karst features -- sinkholes, swallets, or springs -- referencing the KGS sinkhole inventory.
3. **Soils and Geotechnical**: Pull USDA Web Soil Survey data for the parcel. Flag hydric soils (potential wetland indicators), soils with severe limitations for building foundations or septic systems (if unsewered), and shrink-swell potential. Recommend a Phase I geotechnical investigation if karst or fill soils are suspected.
4. **Utilities**: Contact each provider to verify service availability and capacity: sanitary sewer (Louisville MSD, Lexington LFUCG Sanitary Sewer, or regional utility), water (Louisville Water Company, Kentucky American Water, or local water district), electric (LG&E, KU, or local cooperative), gas, and telecom. Document distance to nearest tap or connection point and any required main extensions.
5. **Access and Transportation**: Identify existing curb cuts, driveways, or road frontage. Determine roadway classification (KYTC functional classification system). Note if an encroachment permit from KYTC or the local public works department is needed. Assess sight distance at potential access points per AASHTO and KYTC standards.
6. **Environmental Screening**: Check the USFWS IPaC system for threatened and endangered species. Query the Kentucky Division of Water (KDOW) 303(d) list for impaired waters on or adjacent to the site. Identify wetlands using the National Wetlands Inventory and confirm with a field delineation if NWI features are present. Review FEMA FIRM panels for floodplain boundaries (Zone A, AE, or X). Screen for Phase I ESA triggers -- historical aerial photography, Sanborn maps, EDR database.
7. **Zoning and Land Use**: Identify the current zoning classification and overlay districts. Determine if the proposed use is permitted by right, conditional, or requires a zone change. Note setbacks, height limits, FAR, lot coverage, and parking ratios. Reference the local comprehensive plan for consistency.

## Output Format

Produce a narrative report with the following sections:
- Executive Summary (1 paragraph stating go/no-go recommendation with key constraints)
- Site Description (location, acreage, current condition)
- Topography and Soils (slopes, karst, hydric soils, geotechnical concerns)
- Utilities (availability, capacity, extension requirements)
- Access and Circulation (frontage, sight distance, required permits)
- Environmental Constraints (wetlands, floodplain, T&E species, contamination risk)
- Zoning and Regulatory (current zoning, permitted uses, required approvals)
- Opportunities and Constraints Map (annotated exhibit listing)
- Recommendations and Next Steps

## Quality Checks

- Every constraint cited must reference the specific data source (FEMA panel number, soil map unit, KGS sinkhole ID, zoning article number)
- Slope percentages must be calculated from survey data or LiDAR, not estimated
- Utility availability must reflect direct provider confirmation, not assumptions
- Floodplain boundaries must reference the effective FIRM date and community panel number
- Environmental screening must document negative findings as well as positive findings
- Karst assessment is mandatory for any site in the Inner Bluegrass, Pennyroyal, or Western Kentucky karst regions

## Template Reference

- ASCE site assessment standards
- KRS Chapter 100 (planning and zoning enabling legislation)
- 401 KAR Chapter 4 (floodplain management)
- KYTC Drainage Manual for watershed delineation methods
- Louisville Metro Land Development Code or LFUCG Zoning Ordinance as applicable
