# Stormwater Design Standards — Kentucky

## Revision Log

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| 0 | 2026-07-30 | Claude / JEDS | Initial reference — [VERIFY] all data against current regulatory editions |

---

## 1. Regulatory Framework

### 1.1 Governing Agencies

| Agency | Authority | Jurisdiction |
|--------|-----------|-------------|
| KDOW (Kentucky Division of Water) | KPDES permits, water quality, floodplain | Statewide |
| KDEP (Kentucky Dept. for Environmental Protection) | Parent agency of KDOW | Statewide |
| EPA Region 4 | NPDES program oversight, CWA enforcement | Federal |
| Army Corps of Engineers (Louisville District) | Section 404 (wetlands), Section 10, floodway | Federal — navigable waters |
| Local MS4 Jurisdictions | Local stormwater ordinances, post-construction BMPs | Municipal / county |
| FEMA | National Flood Insurance Program, floodplain mapping | Federal |

### 1.2 Key Permits

| Permit | Trigger | Authority |
|--------|---------|-----------|
| KYG2 (KPDES General Permit for Stormwater) | Land disturbance >= 1 acre (or < 1 acre if part of larger common plan of development) | KDOW |
| Section 404 (CWA) | Discharge of dredged or fill material into waters of the U.S. | Army Corps |
| Floodplain Development Permit | Development within SFHA (100-year floodplain) | Local floodplain administrator |
| Local Stormwater Permit | Per local ordinance | Municipal / county |
| Dam Safety Permit | Dams per KRS 151.250 criteria | KDOW Dam Safety |

### 1.3 KYG2 Permit — KPDES Stormwater General Permit

**Applicability:** Required for construction activities disturbing 1 acre or more of land, or less than 1 acre if part of a larger common plan of development that will ultimately disturb 1 acre or more.

**Key Requirements:**

| Requirement | Detail |
|-------------|--------|
| Notice of Intent (NOI) | Filed with KDOW at least 48 hours before construction [VERIFY current timing] |
| Stormwater Pollution Prevention Plan (SWPPP) | Required before construction begins; maintained on-site |
| BMP Installation | Erosion and sediment controls installed before land disturbance |
| Inspections | Every 7 calendar days and within 24 hours of 0.5-inch rainfall event [VERIFY] |
| Corrective Actions | Deficiencies corrected within 7 calendar days of discovery [VERIFY] |
| Notice of Termination (NOT) | Filed when final stabilization is achieved |
| Final Stabilization | 70% perennial vegetation established on all disturbed areas [VERIFY] |

**NOI Submission:**
- Filed electronically through KDOW ePermit system [VERIFY current system]
- Requires: project location, owner/operator, acreage disturbed, receiving water body, SWPPP certification
- Fee: [VERIFY current fee — typically $100-$500 range]

### 1.4 MS4 Requirements

Municipal Separate Storm Sewer System (MS4) communities in Kentucky must comply with post-construction stormwater management requirements per their KPDES MS4 permit.

**Kentucky MS4 Communities Relevant to JEDS:**

| Community | MS4 Phase | Post-Construction Requirements |
|-----------|-----------|-------------------------------|
| Lexington-Fayette (LFUCG) | Phase I | Water quality volume, channel protection, flood control [VERIFY] |
| Louisville-Jefferson County (MSD) | Phase I | MSD design manual, water quality, detention [VERIFY] |
| Elizabethtown | Phase II [VERIFY] | [VERIFY local stormwater ordinance] |
| Bardstown | [VERIFY MS4 status] | [VERIFY local requirements] |
| Lebanon | [VERIFY MS4 status] | [VERIFY local requirements] |

---

## 2. Hydrologic Methods

### 2.1 Rational Method

**Applicability:** Drainage areas less than 200 acres. Single design storm event. Assumes uniform rainfall intensity over the drainage area.

**Formula:**
```
Q = C * i * A
```

Where:
- Q = Peak runoff rate (cfs)
- C = Runoff coefficient (dimensionless)
- i = Rainfall intensity (in/hr) for the design storm and time of concentration
- A = Drainage area (acres)

**Runoff Coefficients (C) — Typical Values:**

| Surface / Land Use | C Value |
|-------------------|---------|
| Rooftops | 0.90-0.95 |
| Asphalt / Concrete Pavement | 0.85-0.95 |
| Gravel Surface | 0.50-0.70 |
| Bare Soil (compacted) | 0.60-0.80 |
| Lawn — Sandy Soil, Flat (< 2%) | 0.05-0.10 |
| Lawn — Sandy Soil, Moderate (2-7%) | 0.10-0.15 |
| Lawn — Sandy Soil, Steep (> 7%) | 0.15-0.20 |
| Lawn — Clay Soil, Flat (< 2%) | 0.13-0.17 |
| Lawn — Clay Soil, Moderate (2-7%) | 0.18-0.22 |
| Lawn — Clay Soil, Steep (> 7%) | 0.25-0.35 |
| Woodland — Sandy Soil | 0.10-0.20 |
| Woodland — Clay Soil | 0.20-0.30 |
| Pasture — Sandy Soil | 0.10-0.20 |
| Pasture — Clay Soil | 0.20-0.35 |
| Single-Family Residential (1/4 acre lots) | 0.40-0.50 |
| Single-Family Residential (1 acre lots) | 0.25-0.35 |
| Multi-Family Residential | 0.60-0.75 |
| Commercial / Industrial | 0.70-0.90 |
| Shopping Centers | 0.70-0.85 |

**Composite Runoff Coefficient:**
```
C_composite = (C1*A1 + C2*A2 + ... + Cn*An) / A_total
```

### 2.2 Time of Concentration (Tc)

**Methods for Estimating Tc:**

**Sheet Flow (first 300 ft maximum):**
```
Tt = [0.007 * (n * L)^0.8] / [(P2)^0.5 * S^0.4]
```
Where:
- Tt = Travel time (hr)
- n = Manning's roughness coefficient
- L = Flow length (ft) — maximum 300 ft
- P2 = 2-year, 24-hour rainfall depth (inches)
- S = Slope (ft/ft)

**Sheet Flow Manning's n Values:**

| Surface | n |
|---------|---|
| Smooth surface (concrete, asphalt) | 0.011 |
| Fallow / bare soil | 0.05 |
| Short grass / lawn | 0.15 |
| Dense grass / turf | 0.24 |
| Bermuda grass | 0.41 |
| Light woods / brush | 0.40 |
| Dense woods | 0.80 |

**Shallow Concentrated Flow:**
```
V = k * S^0.5 (ft/s)
```
Where k = 16.1 for paved surfaces, k = 20.3 for unpaved surfaces [VERIFY].
```
Tt = L / (3600 * V)
```

**Channel Flow:**
```
V = (1.49/n) * R^(2/3) * S^(1/2) (Manning's equation)
Tt = L / (3600 * V)
```

**Minimum Tc:** 5 minutes (some jurisdictions specify 10 minutes) [VERIFY local requirements].

### 2.3 SCS/NRCS TR-55 Method

**Applicability:** Drainage areas up to 2,000 acres (larger areas require TR-20 or HEC-HMS). Provides peak discharge and hydrograph.

**SCS Curve Number (CN):**

| Land Use / Cover | Hydrologic Soil Group A | B | C | D |
|-----------------|------------------------|---|---|---|
| Impervious (pavement, roofs) | 98 | 98 | 98 | 98 |
| Open space — good condition (> 75% grass) | 39 | 61 | 74 | 80 |
| Open space — fair condition (50-75% grass) | 49 | 69 | 79 | 84 |
| Open space — poor condition (< 50% grass) | 68 | 79 | 86 | 89 |
| Residential — 1/8 acre lots (65% imp.) | 77 | 85 | 90 | 92 |
| Residential — 1/4 acre lots (38% imp.) | 61 | 75 | 83 | 87 |
| Residential — 1/2 acre lots (25% imp.) | 54 | 70 | 80 | 85 |
| Residential — 1 acre lots (20% imp.) | 51 | 68 | 79 | 84 |
| Commercial (85% imp.) | 89 | 92 | 94 | 95 |
| Industrial (72% imp.) | 81 | 88 | 91 | 93 |
| Row crops — straight row, good condition | 67 | 78 | 85 | 89 |
| Pasture — good condition | 39 | 61 | 74 | 80 |
| Woods — good condition | 30 | 55 | 70 | 77 |
| Woods — fair condition | 36 | 60 | 73 | 79 |
| Woods — poor condition | 45 | 66 | 77 | 83 |
| Farmstead | 59 | 74 | 82 | 86 |

Source: NRCS TR-55, Table 2-2a [VERIFY].

**Hydrologic Soil Groups in Kentucky:**

| Group | Infiltration Rate | Description | Common Kentucky Soils |
|-------|-------------------|-------------|----------------------|
| A | > 0.30 in/hr | Deep, well-drained sand/gravel | Uncommon in central KY |
| B | 0.15-0.30 in/hr | Moderate depth, moderate drainage | Shelbyville, Elk silt loams |
| C | 0.05-0.15 in/hr | Slow infiltration, fine texture | Lowell, Faywood silt loams |
| D | < 0.05 in/hr | Very slow infiltration, clay, shallow bedrock | Eden, Cynthiana, Brassfield |

[VERIFY] specific soil HSG classifications using NRCS Web Soil Survey for each project site.

**SCS Runoff Equation:**
```
Q = (P - 0.2*S)^2 / (P + 0.8*S)    when P > 0.2*S
Q = 0                                when P <= 0.2*S

S = (1000 / CN) - 10
Ia = 0.2 * S
```
Where:
- Q = Runoff depth (inches)
- P = Rainfall depth (inches)
- S = Maximum potential retention (inches)
- Ia = Initial abstraction (inches)
- CN = Curve Number

**SCS Peak Discharge (Graphical Method):**
```
qp = qu * Am * Q * Fp
```
Where:
- qp = Peak discharge (cfs)
- qu = Unit peak discharge (csm/in) — from TR-55 Exhibit 4
- Am = Drainage area (mi^2)
- Q = Runoff depth (inches)
- Fp = Pond and swamp adjustment factor

### 2.4 HEC-HMS / HEC-RAS

**When Required:**
- Complex watersheds with multiple subbasins
- Floodplain analysis
- Dam breach analysis
- Reservoir routing
- Drainage areas > 2,000 acres
- When required by reviewing agency

**Software:**

| Program | Developer | Application |
|---------|-----------|-------------|
| HEC-HMS | USACE | Hydrologic modeling, runoff, routing |
| HEC-RAS | USACE | Hydraulic modeling, water surface profiles, floodplain |
| SWMM | EPA | Urban stormwater, combined sewer, water quality |
| HydroCAD | HydroCAD Software Solutions | Detention design, hydrograph routing |
| PondPack / CivilStorm | Bentley | Pond design, storm sewer design |

---

## 3. Kentucky Rainfall Data

### 3.1 NOAA Atlas 14 — Precipitation Frequency Estimates

NOAA Atlas 14 (Volume 2, Version 3.0) provides precipitation frequency estimates for Kentucky. Values are point-specific and should be obtained from the NOAA Precipitation Frequency Data Server (PFDS) for the exact project location.

**Access:** https://hdsc.nws.noaa.gov/pfds/ [VERIFY URL is current]

**Representative Rainfall Depths (inches) — Central Kentucky:**

The following are approximate values for the Elizabethtown/Bardstown corridor. **Always obtain site-specific values from NOAA Atlas 14 for design calculations.**

| Duration | 2-Year | 5-Year | 10-Year | 25-Year | 50-Year | 100-Year |
|----------|--------|--------|---------|---------|---------|----------|
| 5-min | 0.48 | 0.57 | 0.64 | 0.73 | 0.80 | 0.87 |
| 15-min | 0.92 | 1.10 | 1.24 | 1.42 | 1.56 | 1.70 |
| 30-min | 1.24 | 1.49 | 1.69 | 1.94 | 2.14 | 2.34 |
| 60-min | 1.52 | 1.84 | 2.10 | 2.43 | 2.69 | 2.96 |
| 2-hr | 1.82 | 2.22 | 2.55 | 2.97 | 3.31 | 3.66 |
| 3-hr | 2.01 | 2.46 | 2.83 | 3.31 | 3.70 | 4.10 |
| 6-hr | 2.39 | 2.93 | 3.38 | 3.98 | 4.47 | 4.97 |
| 12-hr | 2.78 | 3.42 | 3.97 | 4.70 | 5.30 | 5.92 |
| 24-hr | 3.18 | 3.92 | 4.56 | 5.42 | 6.14 | 6.88 |

[VERIFY] all values for the specific project location using NOAA Atlas 14 PFDS. These are approximations for reference only.

**2-Year, 24-Hour Rainfall (P2):**
- Elizabethtown area: approximately 3.1-3.3 inches [VERIFY]
- Bardstown area: approximately 3.1-3.3 inches [VERIFY]
- Lexington area: approximately 3.0-3.2 inches [VERIFY]
- Louisville area: approximately 3.1-3.3 inches [VERIFY]

### 3.2 SCS Rainfall Distributions

Kentucky uses **SCS Type II** rainfall distribution for design storm hydrographs.

Type II is the standard distribution for the eastern United States east of the Appalachian Divide, which includes all of Kentucky.

### 3.3 Rainfall Intensity (IDF) Relationships

Rainfall intensity for the Rational Method is derived from IDF curves using:
```
i = a / (Tc + b)^c
```

Where a, b, c are regression coefficients specific to the location and return period.

For Kentucky, IDF values should be obtained from NOAA Atlas 14 for the specific project location. Do not use generic IDF curves from textbooks.

---

## 4. Detention Design

### 4.1 General Criteria

**Objective:** Limit post-development peak discharge to pre-development levels for required design storms.

**Typical Design Storm Requirements:**

| Storm Event | Requirement | Typical Application |
|-------------|-------------|---------------------|
| 2-year | Post <= Pre peak discharge | Channel protection |
| 10-year | Post <= Pre peak discharge | Minor system design |
| 25-year | Post <= Pre peak discharge | Intermediate standard |
| 100-year | Post <= Pre peak discharge, safe overflow | Major system / emergency |

[VERIFY] specific detention requirements with the local jurisdiction for each project. Requirements vary significantly between municipalities.

### 4.2 Detention Pond Design Parameters

| Parameter | Typical Requirement |
|-----------|---------------------|
| Side Slopes | 3:1 maximum (4:1 preferred for maintenance) |
| Bottom Width | 4 ft minimum |
| Depth | 5 ft maximum (without dam safety classification) |
| Freeboard | 1.0 ft above 100-year HWL |
| Emergency Spillway | Sized for 100-year storm assuming outlet is blocked |
| Outlet Structure | Multi-stage for multiple design storms |
| Low-Flow Orifice | Sized for 2-year or water quality event |
| Maintenance Access | 15-ft all-weather access road to outlet structure |
| Safety Bench | 10-ft flat bench at normal pool for wet ponds |
| Anti-Seep Collar | Required on outlet pipes through embankments |
| Sediment Forebay | Recommended; 15-25% of total volume |

### 4.3 Stage-Storage-Discharge Methodology

1. **Stage-Storage Curve:** Calculate storage volume at each stage (elevation) using average-end-area or conic method
2. **Stage-Discharge Curve:** Calculate outflow at each stage based on outlet structure hydraulics (orifice, weir, pipe flow)
3. **Hydrograph Routing:** Route the inflow hydrograph through the storage volume using Modified Puls (level pool) method
4. **Verify:** Post-development peak discharge <= pre-development peak discharge for each design storm

**Outlet Structure Hydraulics:**

| Flow Condition | Equation |
|---------------|----------|
| Orifice Flow | Q = Cd * A * (2*g*h)^0.5 |
| Weir Flow (sharp-crested) | Q = Cd * L * h^1.5 |
| Weir Flow (broad-crested) | Q = Cd * L * h^1.5 |
| Pipe Flow (inlet control) | Per FHWA HDS-5 / KYTC nomographs |
| Pipe Flow (outlet control) | Per FHWA HDS-5 / Manning's equation |

Typical orifice coefficient Cd = 0.60. Typical sharp-crested weir coefficient Cd = 3.33 (US customary).

### 4.4 Dam Safety Considerations

Per KRS 151.250 and 401 KAR 4:030 [VERIFY], dams meeting the following criteria require a Dam Safety permit:

| Criteria | Threshold |
|----------|-----------|
| Height | >= 25 ft (from natural streambed to top of dam) |
| Storage | >= 50 acre-feet at top of dam |
| Combined | Height >= 6 ft AND storage >= 15 acre-feet |

[VERIFY] current dam safety thresholds with KDOW Dam Safety Section. Design detention facilities below dam safety thresholds whenever possible to avoid additional permitting requirements.

---

## 5. Water Quality

### 5.1 Water Quality Volume (WQv)

The water quality volume (WQv) is the storage needed to capture and treat the runoff from small, frequent storms. Methodology varies by jurisdiction.

**Common WQv Calculation:**
```
WQv = P * Rv * A / 12
```
Where:
- WQv = Water quality volume (acre-feet)
- P = Rainfall depth — typically 0.75 to 1.0 inches (the "first flush") [VERIFY local requirement]
- Rv = Volumetric runoff coefficient = 0.05 + 0.009 * I
- I = Percent imperviousness of contributing drainage area
- A = Contributing drainage area (acres)

### 5.2 Water Quality BMP Performance

| BMP Type | TSS Removal | TP Removal | TN Removal |
|----------|-------------|------------|------------|
| Bioretention / Rain Garden | 80-95% | 50-80% | 40-60% |
| Constructed Wetland | 80-90% | 50-70% | 30-50% |
| Wet Pond (Retention) | 70-90% | 50-70% | 30-40% |
| Dry Extended Detention | 50-70% | 20-40% | 15-25% |
| Sand Filter | 80-95% | 50-80% | 30-50% |
| Permeable Pavement | 70-90% | 50-70% | 40-60% |
| Vegetated Swale | 60-80% | 20-40% | 20-40% |
| Filter Strip | 50-80% | 20-50% | 20-40% |
| Underground Detention | 20-40% | 10-20% | < 10% |

[VERIFY] removal rates against current regulatory guidance. Performance varies with design, maintenance, and site conditions.

---

## 6. BMP Design Criteria

### 6.1 Bioretention / Rain Garden

| Parameter | Criteria |
|-----------|---------|
| Contributing Drainage Area | 0.25 - 5 acres (typical) |
| Bottom Area | 3-8% of contributing impervious area |
| Ponding Depth | 6-12 inches maximum |
| Media Depth | 24-48 inches |
| Media Composition | 50-60% sand, 20-30% topsoil, 10-20% comite/leaf compost [VERIFY] |
| Media Infiltration Rate | 1-4 in/hr (target 2 in/hr) |
| Underdrain | 4-6 inch perforated PVC or HDPE in 8-12 inch gravel bed |
| Underdrain Gravel | AASHTO #57 stone, 12 inches minimum |
| Overflow | Non-erosive overflow for storms exceeding WQv |
| Setback from Structures | 10 ft minimum from building foundations |
| Setback from Property Line | 5 ft minimum [VERIFY local requirements] |
| Drawdown Time | 24-48 hours for WQv |
| Native Plantings | Recommended; select species tolerant of wet/dry cycles |
| Mulch | 2-3 inches shredded hardwood; no dyed mulch |

### 6.2 Wet Pond (Retention Pond)

| Parameter | Criteria |
|-----------|---------|
| Contributing Drainage Area | 10 - 50+ acres (minimum 10 acres for reliable base flow) |
| Permanent Pool Volume | Equal to WQv (minimum) |
| Length-to-Width Ratio | 2:1 minimum (3:1 preferred) |
| Average Depth | 3-6 ft |
| Maximum Depth | 8-10 ft |
| Safety Bench | 10 ft wide at 0-1% slope around permanent pool perimeter |
| Aquatic Bench | 10-15 ft wide at 0-12 inches below normal pool |
| Sediment Forebay | 15-25% of total permanent pool volume |
| Side Slopes (above NWL) | 3:1 maximum (4:1 preferred) |
| Side Slopes (below NWL) | 3:1 to aquatic bench |
| Freeboard | 1.0 ft above 100-year HWL |
| Outlet Structure | Multi-stage riser with trash rack |
| Emergency Spillway | Sized for 100-year with primary blocked |
| Maintenance Access | 15-ft paved or gravel to outlet and forebay |
| Landscaping | Riparian buffer planting around perimeter |

### 6.3 Dry Extended Detention

| Parameter | Criteria |
|-----------|---------|
| Contributing Drainage Area | 2 - 50+ acres |
| Extended Detention Volume | WQv released over 24-48 hours |
| Length-to-Width Ratio | 2:1 minimum |
| Bottom Grade | 1-2% minimum to prevent standing water |
| Side Slopes | 3:1 maximum (4:1 preferred) |
| Maximum Depth | 5 ft (without dam safety implications) |
| Low-Flow Channel | Concrete or riprap pilot channel, 2 ft minimum width |
| Low-Flow Orifice | Sized for 24-48 hour drawdown; minimum 3-inch diameter to avoid clogging |
| Trash Rack | Required on all orifices and outlet pipes |
| Freeboard | 1.0 ft above 100-year HWL |
| Maintenance Access | 15-ft all-weather to outlet and basin floor |
| Vegetation | Turf grass bottom (mowed) or native meadow |

### 6.4 Permeable Pavement

| Parameter | Criteria |
|-----------|---------|
| Contributing Drainage Area | Site pavement only (max 3:1 impervious-to-pervious ratio) |
| Pavement Types | Pervious concrete, porous asphalt, permeable interlocking concrete pavers (PICP) |
| Surface Infiltration Rate | > 100 in/hr when new; design for 10 in/hr (clogged condition) |
| Base Course | AASHTO #57 stone, 6-12 inches (reservoir layer) |
| Sub-Base | AASHTO #2 stone, 6-24 inches (storage and structural) |
| Geotextile | Non-woven on bottom and sides of reservoir layer |
| Underdrain | Required if native soil infiltration rate < 0.5 in/hr |
| Soil Investigation | Required — infiltration testing at subgrade elevation |
| Slope | 0-2% maximum surface slope |
| Setback from Wells | 100 ft [VERIFY] |
| Setback from Foundations | 10 ft uphill / 100 ft downhill [VERIFY] |
| Maintenance | Vacuum sweeping 2-4 times annually |
| Load Rating | Design for traffic loading (no heavy trucks without structural analysis) |

### 6.5 Vegetated Swale

| Parameter | Criteria |
|-----------|---------|
| Contributing Drainage Area | 5 acres maximum |
| Bottom Width | 2-8 ft |
| Side Slopes | 3:1 or flatter |
| Longitudinal Slope | 1-4% (check dams for slopes > 4%) |
| Maximum Flow Depth | 12 inches for WQv event |
| Maximum Velocity | 1 fps for WQv, 4 fps for 10-year |
| Manning's n | 0.15 for water quality, 0.03-0.05 for flood control |
| Residence Time | 9-10 minutes minimum for WQv |
| Length | Determined by residence time and velocity requirements |
| Vegetation | Dense turf grass, minimum 3-inch height |
| Check Dams | 6-12 inches high where needed; wood, stone, or concrete |
| Freeboard | 6 inches above 10-year flow depth |

---

## 7. Erosion and Sediment Control

### 7.1 SWPPP Requirements

A Stormwater Pollution Prevention Plan must include:

| Component | Description |
|-----------|-------------|
| Site Description | Location, acreage, receiving waters, soil types |
| Existing Conditions Map | Topography, drainage, vegetation, waters of state |
| Construction Sequence | Phasing of grading and BMP installation |
| ESC Plan | Map showing all temporary BMPs |
| Permanent Stormwater Plan | Post-construction BMPs |
| Maintenance Plan | BMP inspection and maintenance schedule |
| Pollution Prevention | Concrete washout, fuel storage, material staging |
| SWPPP Amendment Log | Record of changes during construction |
| Inspection Records | Inspection forms per KYG2 requirements |

### 7.2 Temporary BMP Sizing

**Sediment Basin:**

| Parameter | Criteria |
|-----------|---------|
| When Required | Drainage area >= 10 acres to a common discharge point [VERIFY] |
| Storage Volume | 3,600 cf per acre of disturbed drainage area |
| Dewatering Device | Perforated riser or skimmer |
| Drawdown Time | 48-72 hours |
| Emergency Spillway | Required for 25-year, 24-hour storm |
| Side Slopes | 2:1 interior, 3:1 exterior of embankment |

**Sediment Trap:**

| Parameter | Criteria |
|-----------|---------|
| When Required | Drainage area < 10 acres where sediment basin is not feasible |
| Storage Volume | 3,600 cf per acre of disturbed drainage area |
| Maximum Drainage Area | 5 acres per trap [VERIFY] |
| Outlet | Stone weir section |

**Silt Fence:**

| Parameter | Criteria |
|-----------|---------|
| When Required | Perimeter of disturbed area, downslope |
| Maximum Slope Length | 100 ft (contributing area above fence) |
| Maximum Drainage Area | 0.25 acres per 100 ft of fence [VERIFY] |
| Post Spacing | 6 ft maximum (3 ft on slopes > 2:1) |
| Post Embedment | 12-18 inches minimum |
| Fabric Height | 24-36 inches above ground |
| Toe-In | 6-8 inches buried trench with backfill |

**Construction Entrance:**

| Parameter | Criteria |
|-----------|---------|
| Stone Size | KYTC #2 or #1 coarse aggregate |
| Depth | 6 inches minimum |
| Width | 20 ft minimum (full road width at public road) |
| Length | 50 ft minimum (100 ft on steep slopes) |
| Geotextile | Non-woven separation fabric beneath stone |
| Wash Rack | Required if tracking onto public roads |

### 7.3 Temporary Seeding

| Season | Seed Mixture | Application Rate |
|--------|-------------|-----------------|
| Spring/Summer (Mar 15 - Aug 15) | German millet or Sudan grass | 40 lbs/acre |
| Fall (Aug 15 - Oct 15) | Annual ryegrass + cereal rye | 120 lbs/acre combined |
| Late Fall/Winter (Oct 15 - Mar 15) | Cereal rye or wheat | 120 lbs/acre |

[VERIFY] against current KDOW / KYTC temporary seeding specifications. Local jurisdictions may have different requirements.

---

## 8. Floodplain Management

### 8.1 NFIP Requirements

| Requirement | Standard |
|-------------|----------|
| Regulatory Floodplain | FEMA Special Flood Hazard Area (SFHA) — Zone A, AE, AH, AO, V, VE |
| Base Flood Elevation (BFE) | 1% annual chance (100-year) flood elevation |
| Lowest Floor Elevation | At or above BFE (many communities require BFE + 1 ft or BFE + 2 ft) [VERIFY local freeboard] |
| Floodway | Area that must remain unobstructed for flood conveyance; no rise in BFE allowed |
| Flood Fringe | Area between floodway and SFHA boundary; development permitted if no adverse impact |
| No-Rise Certification | Required for any work within the floodway |
| CLOMR / LOMR | Required for projects that change flood boundaries or BFEs |

### 8.2 Kentucky-Specific Floodplain Requirements

| Requirement | Standard |
|-------------|----------|
| State Freeboard | [VERIFY — Kentucky may require additional freeboard beyond FEMA minimum] |
| Compensatory Storage | Required in many Kentucky communities — cut-and-fill balance within SFHA |
| Substantial Improvement | > 50% of market value — triggers full compliance |
| Local Floodplain Ordinance | Must meet or exceed NFIP minimum [VERIFY for each jurisdiction] |

---

## 9. Pipe Design — Hydraulic Calculations

### 9.1 Manning's Equation (Open Channel and Full Pipe Flow)

```
Q = (1.49/n) * A * R^(2/3) * S^(1/2)
V = (1.49/n) * R^(2/3) * S^(1/2)
```

Where:
- Q = Flow rate (cfs)
- n = Manning's roughness coefficient
- A = Cross-sectional area of flow (sf)
- R = Hydraulic radius = A / Wetted Perimeter (ft)
- S = Slope (ft/ft)
- V = Velocity (ft/s)

### 9.2 Manning's n Values for Pipe

| Material | Manning's n |
|----------|-------------|
| RCP (Reinforced Concrete Pipe) | 0.012-0.013 |
| HDPE (Smooth Interior) | 0.012 |
| HDPE (Corrugated Interior) | 0.018-0.025 |
| PVC (Smooth) | 0.009-0.011 |
| CMP (Corrugated Metal) | 0.022-0.027 |
| Concrete Box Culvert | 0.012-0.015 |

### 9.3 Minimum Pipe Velocity and Slope

| Pipe Diameter (in) | Minimum Velocity (fps) | Minimum Slope (%) — n=0.013 |
|--------------------|----------------------|------------------------------|
| 12 | 2.5 | 0.43 |
| 15 | 2.5 | 0.33 |
| 18 | 2.5 | 0.26 |
| 24 | 2.5 | 0.18 |
| 30 | 2.5 | 0.14 |
| 36 | 2.5 | 0.11 |
| 42 | 2.5 | 0.09 |
| 48 | 2.5 | 0.07 |

**Maximum Velocity:** 15 fps for RCP, 10 fps for HDPE and CMP [VERIFY].

---

## References

1. NRCS, *Technical Release 55 (TR-55): Urban Hydrology for Small Watersheds*, June 1986
2. NRCS, *Technical Release 20 (TR-20): Computer Program for Project Formulation Hydrology*
3. NOAA, *Atlas 14: Precipitation-Frequency Atlas of the United States*, Volume 2, Version 3.0
4. USACE, *HEC-HMS Technical Reference Manual*
5. USACE, *HEC-RAS Hydraulic Reference Manual*
6. FHWA, *HDS-5: Hydraulic Design of Highway Culverts*
7. KDOW, *KYG2 — KPDES General Permit for Stormwater Discharges Associated with Construction Activities* [VERIFY current edition]
8. KDOW, *Kentucky Best Management Practices for Construction Activities*
9. FEMA, *NFIP Regulations — 44 CFR Parts 59-78*
10. KRS Chapter 151 — Water Resources
11. KRS Chapter 224 — Environmental Protection
12. 401 KAR 4:060 — Floodplain Management
13. 401 KAR 5:029 — KPDES General Permit (KYG2)

---

## Verification Notes

- All rainfall data must be obtained from NOAA Atlas 14 for the specific project location. The values in this reference are approximations only.
- Runoff coefficients, curve numbers, and Manning's n values are professional judgment parameters. Verify appropriateness for each project.
- Local MS4 jurisdictions may have stormwater design requirements that exceed state and federal minimums. Always check local ordinances.
- BMP removal efficiencies are estimates based on published literature. Actual performance varies with design, maintenance, and site conditions.
- Detention design criteria vary significantly between jurisdictions. Always verify the required design storms and performance standards with the local reviewing authority.
- Dam safety thresholds are per Kentucky law (KRS 151.250). Design detention facilities below these thresholds whenever possible.
- This reference does not replace project-specific engineering analysis. All designs must be prepared by or under the supervision of a licensed professional engineer.
