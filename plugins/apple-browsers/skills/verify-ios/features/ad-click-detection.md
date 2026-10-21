# Ad-click privacy classification

Source-mapped coverage at `89c18e4893ab5f5f51f3c82ba8c852d367799dd1`; no scenario in this file was executed by this source-only pass.

## Sub-features

- `01_yjs_heuristic_no_ad_domain_param_u3_param_included` — `.maestro/ad_click_detection_flow_tests/01_yjs_heuristic_no_ad_domain_param_u3_param_included.yaml`.
- `02_mjs_heuristic_no_ad_domain_param_dsl_param_included` — `.maestro/ad_click_detection_flow_tests/02_mjs_heuristic_no_ad_domain_param_dsl_param_included.yaml`.
- `03_yjs_heuristic_no_ad_domain_param_but_missing_u3_param` — `.maestro/ad_click_detection_flow_tests/03_yjs_heuristic_no_ad_domain_param_but_missing_u3_param.yaml`.
- `04_mjs_heuristic_no_ad_domain_param_but_missing_dsl_param` — `.maestro/ad_click_detection_flow_tests/04_mjs_heuristic_no_ad_domain_param_but_missing_dsl_param.yaml`.
- `05_yjs_heuristic_ad_domain_provided_but_empty_u3_not_needed` — `.maestro/ad_click_detection_flow_tests/05_yjs_heuristic_ad_domain_provided_but_empty_u3_not_needed.yaml`.
- `06_mjs_heuristic_ad_domain_provided_but_empty_dsl_not_needed` — `.maestro/ad_click_detection_flow_tests/06_mjs_heuristic_ad_domain_provided_but_empty_dsl_not_needed.yaml`.
- `07_yjs_bing-provided_ad_domain_provided_u3_not_needed` — `.maestro/ad_click_detection_flow_tests/07_yjs_bing-provided_ad_domain_provided_u3_not_needed.yaml`.
- `08_mjs_bing-provided_ad_domain_provided_dsl_not_needed` — `.maestro/ad_click_detection_flow_tests/08_mjs_bing-provided_ad_domain_provided_dsl_not_needed.yaml`.
- `09_yjs_bing-provided_ad_domain_provided_but_incorrect_u3_not_needed` — `.maestro/ad_click_detection_flow_tests/09_yjs_bing-provided_ad_domain_provided_but_incorrect_u3_not_needed.yaml`.
- `10_mjs_bing-provided_ad_domain_provided_but_incorrect_dsl_not_needed` — `.maestro/ad_click_detection_flow_tests/10_mjs_bing-provided_ad_domain_provided_but_incorrect_dsl_not_needed.yaml`.
- `11_yjs_bing-provided_ad_domain_provided_but_its_not_a_domain_u3_not_needed` — `.maestro/ad_click_detection_flow_tests/11_yjs_bing-provided_ad_domain_provided_but_its_not_a_domain_u3_not_needed.yaml`.
- `12_mjs_bing-provided_ad_domain_provided_but_its_not_a_domain_dsl_not_needed` — `.maestro/ad_click_detection_flow_tests/12_mjs_bing-provided_ad_domain_provided_but_its_not_a_domain_dsl_not_needed.yaml`.
- `13_yjs_bing-provided_ad_domain_provided_but_its_a_subdomain_of_advertiser_u3_not_needed` — `.maestro/ad_click_detection_flow_tests/13_yjs_bing-provided_ad_domain_provided_but_its_a_subdomain_of_advertiser_u3_not_needed.yaml`.
- `14_mjs_bing-provided_ad_domain_provided_but_its_a_subdomain_of_advertiser_dsl_not_needed` — `.maestro/ad_click_detection_flow_tests/14_mjs_bing-provided_ad_domain_provided_but_its_a_subdomain_of_advertiser_dsl_not_needed.yaml`.

## How to get to it (user POV)

Load the exact www.search-company.site fixture fragment in the scenario, choose its named SERP ad, then use privacy-icon-shield.button → View Tracker Companies / View Non-Tracker Companies.

## Driving it with MobileBuildMCP

Use only the selected provider MobileBuildMCP. Call `snapshot_ui`, match the exact identifiers or labels below, then use current `elementRef` values with `tap` and `type_text(elementRef, text)`. Refresh after each navigation. Use `wait_for_ui` exists/gone/textContains for the expected state, inspect a resulting snapshot, and save both action/result records and a screenshot to external evidence. The following ordered recipes transcribe source intent; Maestro is never executed. Parent recipes reference helper behavior explicitly; read those helpers before driving. Literal regex text is a source oracle, so match actual returned text rather than passing the regex as an exact label.

### 01_yjs_heuristic_no_ad_domain_param_u3_param_included

Source: `.maestro/ad_click_detection_flow_tests/01_yjs_heuristic_no_ad_domain_param_u3_param_included.yaml`. Tags: `["iphone", "adClick"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://www.search-company.site/#ad-id-1"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible text `"[Ad 1] SERP Ad (heuristic)"`.
7. Tap text `"[Ad 1] SERP Ad (heuristic)"`.
8. Require visible text `"Publisher site"`.
9. Tap identifier `"privacy-icon-shield.button"`.
10. Require visible text `"View Tracker Companies"`.
11. Tap text `"View Tracker Companies"`.
12. Require visible text `"The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`.
13. Require visible text `"About our Web Tracking Protections"`.
14. Require visible text `".*Ad Company"`.
15. Require visible text `"convert.ad-company.site"`.
16. Require visible text `"ad-company.site"`.
17. Tap label/text `"Back"`.
18. Require visible text `"View Non-Tracker Companies"`.
19. Tap text `"View Non-Tracker Companies"`.
20. Require visible text `"We did not identify any requests from third-party domains."`.
21. Require visible text `"About our Web Tracking Protections"`.

### 02_mjs_heuristic_no_ad_domain_param_dsl_param_included

Source: `.maestro/ad_click_detection_flow_tests/02_mjs_heuristic_no_ad_domain_param_dsl_param_included.yaml`. Tags: `["iphone", "adClick"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://www.search-company.site/#ad-id-2"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible text `"[Ad 2] Shopping Tab Ad (heuristic)"`.
7. Tap text `"[Ad 2] Shopping Tab Ad (heuristic)"`.
8. Require visible text `"Publisher site"`.
9. Tap identifier `"privacy-icon-shield.button"`.
10. Require visible text `"View Tracker Companies"`.
11. Tap text `"View Tracker Companies"`.
12. Require visible text `"The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`.
13. Require visible text `"About our Web Tracking Protections"`.
14. Require visible text `".*Ad Company"`.
15. Require visible text `"convert.ad-company.site"`.
16. Require visible text `"ad-company.site"`.
17. Tap label/text `"Back"`.
18. Require visible text `"View Non-Tracker Companies"`.
19. Tap text `"View Non-Tracker Companies"`.
20. Require visible text `"We did not identify any requests from third-party domains."`.
21. Require visible text `"About our Web Tracking Protections"`.

### 03_yjs_heuristic_no_ad_domain_param_but_missing_u3_param

Source: `.maestro/ad_click_detection_flow_tests/03_yjs_heuristic_no_ad_domain_param_but_missing_u3_param.yaml`. Tags: `["iphone", "adClick"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://www.search-company.site/#ad-id-3"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible text `"[Ad 3] SERP Ad (heuristic)"`.
7. Tap text `"[Ad 3] SERP Ad (heuristic)"`.
8. Require visible text `"Publisher site"`.
9. Tap identifier `"privacy-icon-shield.button"`.
10. Require visible text `"View Tracker Companies"`.
11. Tap text `"View Tracker Companies"`.
12. Require visible text `"The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`.
13. Require visible text `"About our Web Tracking Protections"`.
14. Require visible text `".*Ad Company"`.
15. Require visible text `"convert.ad-company.site"`.
16. Require visible text `"ad-company.site"`.
17. Tap label/text `"Back"`.
18. Require visible text `"View Non-Tracker Companies"`.
19. Tap text `"View Non-Tracker Companies"`.
20. Require visible text `"We did not identify any requests from third-party domains."`.
21. Require visible text `"About our Web Tracking Protections"`.

### 04_mjs_heuristic_no_ad_domain_param_but_missing_dsl_param

Source: `.maestro/ad_click_detection_flow_tests/04_mjs_heuristic_no_ad_domain_param_but_missing_dsl_param.yaml`. Tags: `["iphone", "adClick"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://www.search-company.site/#ad-id-4"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible text `"[Ad 4] Shopping Tab Ad (heuristic)"`.
7. Tap text `"[Ad 4] Shopping Tab Ad (heuristic)"`.
8. Require visible text `"Publisher site"`.
9. Tap identifier `"privacy-icon-shield.button"`.
10. Require visible text `"View Tracker Companies"`.
11. Tap text `"View Tracker Companies"`.
12. Require visible text `"The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`.
13. Require visible text `"About our Web Tracking Protections"`.
14. Require visible text `".*Ad Company"`.
15. Require visible text `"convert.ad-company.site"`.
16. Require visible text `"ad-company.site"`.
17. Tap label/text `"Back"`.
18. Require visible text `"View Non-Tracker Companies"`.
19. Tap text `"View Non-Tracker Companies"`.
20. Require visible text `"We did not identify any requests from third-party domains."`.
21. Require visible text `"About our Web Tracking Protections"`.

### 05_yjs_heuristic_ad_domain_provided_but_empty_u3_not_needed

Source: `.maestro/ad_click_detection_flow_tests/05_yjs_heuristic_ad_domain_provided_but_empty_u3_not_needed.yaml`. Tags: `["iphone", "adClick"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://www.search-company.site/#ad-id-5"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible text `"[Ad 5] SERP Ad (heuristic)"`.
7. Tap text `"[Ad 5] SERP Ad (heuristic)"`.
8. Require visible text `"Publisher site"`.
9. Tap identifier `"privacy-icon-shield.button"`.
10. Require visible text `"View Tracker Companies"`.
11. Tap text `"View Tracker Companies"`.
12. Require visible text `"The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`.
13. Require visible text `"About our Web Tracking Protections"`.
14. Require visible text `".*Ad Company"`.
15. Require visible text `"ad-company.site"`.
16. Tap label/text `"Back"`.
17. Require visible text `"View Non-Tracker Companies"`.
18. Tap text `"View Non-Tracker Companies"`.
19. Require visible text `"The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`.
20. Require visible text `"About our Web Tracking Protections"`.
21. Require visible text `"The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`.
22. Require visible text `"How our search ads impact our protections"`.
23. Require visible text `".*Ad Company"`.
24. Require visible text `"convert.ad-company.site"`.

### 06_mjs_heuristic_ad_domain_provided_but_empty_dsl_not_needed

Source: `.maestro/ad_click_detection_flow_tests/06_mjs_heuristic_ad_domain_provided_but_empty_dsl_not_needed.yaml`. Tags: `["iphone", "adClick"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://www.search-company.site/#ad-id-6"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible text `"[Ad 6] Shopping Tab Ad (heuristic)"`.
7. Tap text `"[Ad 6] Shopping Tab Ad (heuristic)"`.
8. Require visible text `"Publisher site"`.
9. Tap identifier `"privacy-icon-shield.button"`.
10. Require visible text `"View Tracker Companies"`.
11. Tap text `"View Tracker Companies"`.
12. Require visible text `"The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`.
13. Require visible text `"About our Web Tracking Protections"`.
14. Require visible text `".*Ad Company"`.
15. Require visible text `"ad-company.site"`.
16. Tap label/text `"Back"`.
17. Require visible text `"View Non-Tracker Companies"`.
18. Tap text `"View Non-Tracker Companies"`.
19. Require visible text `"The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`.
20. Require visible text `"About our Web Tracking Protections"`.
21. Require visible text `"The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`.
22. Require visible text `"How our search ads impact our protections"`.
23. Require visible text `".*Ad Company"`.
24. Require visible text `"convert.ad-company.site"`.

### 07_yjs_bing-provided_ad_domain_provided_u3_not_needed

Source: `.maestro/ad_click_detection_flow_tests/07_yjs_bing-provided_ad_domain_provided_u3_not_needed.yaml`. Tags: `["iphone", "adClick"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://www.search-company.site/#ad-id-7"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible text `"[Ad 7] SERP Ad (SERP-provided)"`.
7. Tap text `"[Ad 7] SERP Ad (SERP-provided)"`.
8. Require visible text `"Publisher site"`.
9. Tap identifier `"privacy-icon-shield.button"`.
10. Require visible text `"View Tracker Companies"`.
11. Tap text `"View Tracker Companies"`.
12. Require visible text `"The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`.
13. Require visible text `"About our Web Tracking Protections"`.
14. Require visible text `".*Ad Company"`.
15. Require visible text `"ad-company.site"`.
16. Tap label/text `"Back"`.
17. Require visible text `"View Non-Tracker Companies"`.
18. Tap text `"View Non-Tracker Companies"`.
19. Require visible text `"The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`.
20. Require visible text `"About our Web Tracking Protections"`.
21. Require visible text `"The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`.
22. Require visible text `"How our search ads impact our protections"`.
23. Require visible text `".*Ad Company"`.
24. Require visible text `"convert.ad-company.site"`.

### 08_mjs_bing-provided_ad_domain_provided_dsl_not_needed

Source: `.maestro/ad_click_detection_flow_tests/08_mjs_bing-provided_ad_domain_provided_dsl_not_needed.yaml`. Tags: `["iphone", "adClick"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://www.search-company.site/#ad-id-8"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible text `"[Ad 8] Shopping Tab Ad (SERP-provided)"`.
7. Tap text `"[Ad 8] Shopping Tab Ad (SERP-provided)"`.
8. Require visible text `"Publisher site"`.
9. Tap identifier `"privacy-icon-shield.button"`.
10. Require visible text `"View Tracker Companies"`.
11. Tap text `"View Tracker Companies"`.
12. Require visible text `"The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`.
13. Require visible text `"About our Web Tracking Protections"`.
14. Require visible text `".*Ad Company"`.
15. Require visible text `"ad-company.site"`.
16. Tap label/text `"Back"`.
17. Require visible text `"View Non-Tracker Companies"`.
18. Tap text `"View Non-Tracker Companies"`.
19. Require visible text `"The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`.
20. Require visible text `"About our Web Tracking Protections"`.
21. Require visible text `"The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`.
22. Require visible text `"How our search ads impact our protections"`.
23. Require visible text `".*Ad Company"`.
24. Require visible text `"convert.ad-company.site"`.

### 09_yjs_bing-provided_ad_domain_provided_but_incorrect_u3_not_needed

Source: `.maestro/ad_click_detection_flow_tests/09_yjs_bing-provided_ad_domain_provided_but_incorrect_u3_not_needed.yaml`. Tags: `["iphone", "adClick"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://www.search-company.site/#ad-id-9"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible text `"[Ad 9] SERP Ad (SERP-provided)"`.
7. Tap text `"[Ad 9] SERP Ad (SERP-provided)"`.
8. Require visible text `"Publisher site"`.
9. Tap identifier `"privacy-icon-shield.button"`.
10. Require visible text `"View Tracker Companies"`.
11. Tap text `"View Tracker Companies"`.
12. Require visible text `"The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`.
13. Require visible text `"About our Web Tracking Protections"`.
14. Require visible text `".*Ad Company"`.
15. Require visible text `"convert.ad-company.site"`.
16. Require visible text `"ad-company.site"`.
17. Tap label/text `"Back"`.
18. Require visible text `"View Non-Tracker Companies"`.
19. Tap text `"View Non-Tracker Companies"`.
20. Require visible text `"We did not identify any requests from third-party domains."`.
21. Require visible text `"About our Web Tracking Protections"`.

### 10_mjs_bing-provided_ad_domain_provided_but_incorrect_dsl_not_needed

Source: `.maestro/ad_click_detection_flow_tests/10_mjs_bing-provided_ad_domain_provided_but_incorrect_dsl_not_needed.yaml`. Tags: `["iphone", "adClick"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://www.search-company.site/#ad-id-10"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible text `"[Ad 10] Shopping Tab Ad (SERP-provided)"`.
7. Tap text `"[Ad 10] Shopping Tab Ad (SERP-provided)"`.
8. Require visible text `"Publisher site"`.
9. Tap identifier `"privacy-icon-shield.button"`.
10. Require visible text `"View Tracker Companies"`.
11. Tap text `"View Tracker Companies"`.
12. Require visible text `"The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`.
13. Require visible text `"About our Web Tracking Protections"`.
14. Require visible text `".*Ad Company"`.
15. Require visible text `"convert.ad-company.site"`.
16. Require visible text `"ad-company.site"`.
17. Tap label/text `"Back"`.
18. Require visible text `"View Non-Tracker Companies"`.
19. Tap text `"View Non-Tracker Companies"`.
20. Require visible text `"We did not identify any requests from third-party domains."`.
21. Require visible text `"About our Web Tracking Protections"`.

### 11_yjs_bing-provided_ad_domain_provided_but_its_not_a_domain_u3_not_needed

Source: `.maestro/ad_click_detection_flow_tests/11_yjs_bing-provided_ad_domain_provided_but_its_not_a_domain_u3_not_needed.yaml`. Tags: `["iphone", "adClick"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://www.search-company.site/#ad-id-11"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible text `"[Ad 11] SERP Ad (heuristic)"`.
7. Tap text `"[Ad 11] SERP Ad (heuristic)"`.
8. Require visible text `"Publisher site"`.
9. Tap identifier `"privacy-icon-shield.button"`.
10. Require visible text `"View Tracker Companies"`.
11. Tap text `"View Tracker Companies"`.
12. Require visible text `"The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`.
13. Require visible text `"About our Web Tracking Protections"`.
14. Require visible text `".*Ad Company"`.
15. Require visible text `"ad-company.site"`.
16. Tap label/text `"Back"`.
17. Require visible text `"View Non-Tracker Companies"`.
18. Tap text `"View Non-Tracker Companies"`.
19. Require visible text `"The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`.
20. Require visible text `"About our Web Tracking Protections"`.
21. Require visible text `"The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`.
22. Require visible text `"How our search ads impact our protections"`.
23. Require visible text `".*Ad Company"`.
24. Require visible text `"convert.ad-company.site"`.

### 12_mjs_bing-provided_ad_domain_provided_but_its_not_a_domain_dsl_not_needed

Source: `.maestro/ad_click_detection_flow_tests/12_mjs_bing-provided_ad_domain_provided_but_its_not_a_domain_dsl_not_needed.yaml`. Tags: `["iphone", "adClick"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://www.search-company.site/#ad-id-12"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible text `"[Ad 12] Shopping Tab Ad (heuristic)"`.
7. Tap text `"[Ad 12] Shopping Tab Ad (heuristic)"`.
8. Require visible text `"Publisher site"`.
9. Tap identifier `"privacy-icon-shield.button"`.
10. Require visible text `"View Tracker Companies"`.
11. Tap text `"View Tracker Companies"`.
12. Require visible text `"The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`.
13. Require visible text `"About our Web Tracking Protections"`.
14. Require visible text `".*Ad Company"`.
15. Require visible text `"ad-company.site"`.
16. Tap label/text `"Back"`.
17. Require visible text `"View Non-Tracker Companies"`.
18. Tap text `"View Non-Tracker Companies"`.
19. Require visible text `"The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`.
20. Require visible text `"About our Web Tracking Protections"`.
21. Require visible text `"The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`.
22. Require visible text `"How our search ads impact our protections"`.
23. Require visible text `".*Ad Company"`.
24. Require visible text `"convert.ad-company.site"`.

### 13_yjs_bing-provided_ad_domain_provided_but_its_a_subdomain_of_advertiser_u3_not_needed

Source: `.maestro/ad_click_detection_flow_tests/13_yjs_bing-provided_ad_domain_provided_but_its_a_subdomain_of_advertiser_u3_not_needed.yaml`. Tags: `["iphone", "adClick"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://www.search-company.site/#ad-id-13"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible text `"[Ad 13] SERP Ad (SERP-provided)"`.
7. Tap text `"[Ad 13] SERP Ad (SERP-provided)"`.
8. Require visible text `"Publisher site"`.
9. Tap identifier `"privacy-icon-shield.button"`.
10. Require visible text `"View Tracker Companies"`.
11. Tap text `"View Tracker Companies"`.
12. Require visible text `"The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`.
13. Require visible text `"About our Web Tracking Protections"`.
14. Require visible text `".*Ad Company"`.
15. Require visible text `"ad-company.site"`.
16. Tap label/text `"Back"`.
17. Require visible text `"View Non-Tracker Companies"`.
18. Tap text `"View Non-Tracker Companies"`.
19. Require visible text `"The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`.
20. Require visible text `"About our Web Tracking Protections"`.
21. Require visible text `"The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`.
22. Require visible text `"How our search ads impact our protections"`.
23. Require visible text `".*Ad Company"`.
24. Require visible text `"convert.ad-company.site"`.

### 14_mjs_bing-provided_ad_domain_provided_but_its_a_subdomain_of_advertiser_dsl_not_needed

Source: `.maestro/ad_click_detection_flow_tests/14_mjs_bing-provided_ad_domain_provided_but_its_a_subdomain_of_advertiser_dsl_not_needed.yaml`. Tags: `["iphone", "adClick"]`.

Dependencies: `.maestro/shared/setup.yaml`.

1. Follow visible behavior from `.maestro/shared/setup.yaml`.
2. Require visible identifier `"searchEntry"`.
3. Tap identifier `"searchEntry"`.
4. Enter `"https://www.search-company.site/#ad-id-14"` into the currently focused field using its refreshed elementRef.
5. Use the exposed provider key action for `"Enter"`; inspect its schema first.
6. Require visible text `"[Ad 14] Shopping Tab Ad (SERP-provided)"`.
7. Tap text `"[Ad 14] Shopping Tab Ad (SERP-provided)"`.
8. Require visible text `"Publisher site"`.
9. Tap identifier `"privacy-icon-shield.button"`.
10. Require visible text `"View Tracker Companies"`.
11. Tap text `"View Tracker Companies"`.
12. Require visible text `"The following third-party domains’ requests were blocked from loading because they were identified as tracking requests. If a company's requests are loaded, it can allow them to profile you."`.
13. Require visible text `"About our Web Tracking Protections"`.
14. Require visible text `".*Ad Company"`.
15. Require visible text `"ad-company.site"`.
16. Tap label/text `"Back"`.
17. Require visible text `"View Non-Tracker Companies"`.
18. Tap text `"View Non-Tracker Companies"`.
19. Require visible text `"The following third-party domains’ requests were loaded. If a company's requests are loaded, it can allow them to profile you, though our other web tracking protections still apply."`.
20. Require visible text `"About our Web Tracking Protections"`.
21. Require visible text `"The following domain’s requests were loaded because a publisher-company.site ad on DuckDuckGo was recently clicked. These requests help evaluate ad effectiveness. All ads on DuckDuckGo are non-profiling."`.
22. Require visible text `"How our search ads impact our protections"`.
23. Require visible text `".*Ad Company"`.
24. Require visible text `"convert.ad-company.site"`.

## Gotchas

The 14 fixture cases distinguish yjs and mjs, missing/empty/invalid domains, advertiser domains and subdomains, u3 and dsl. Preserve URL and ad number exactly. Remote fixture availability is a dependency. Dashboard company/request classification is the visible oracle; do not claim network request evidence without obtaining it.

Read `.maestro/AGENTS.md`: deciding feature flags must be pinned as quoted strings, internalOnly flags also need internal-user mode, and every navigation needs a destination-specific wait. Do not inherit live privacy-config defaults silently. Preserve source launch intent but use only supported provider operations on an explicitly designated disposable simulator. Environment placeholders (`${...}`), seeded snapshots, passcodes, clipboard/recovery codes, live account state and web availability are dependencies to resolve; none are established by this map.
