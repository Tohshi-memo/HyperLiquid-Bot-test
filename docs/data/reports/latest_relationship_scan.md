# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T08:54:57.610671+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2566`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->unknown_1h` score `11496.7338` n `112` status `ready` deltaP `1.1175` edge `958.0735` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `7309.9278` n `109` status `ready` deltaP `0.1301` edge `609.1882` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `12.4287` n `98` status `ready` deltaP `39.594` edge `1.6565` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `10.5283` n `98` status `ready` deltaP `22.3569` edge `1.4131` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.235` n `112` status `ready` deltaP `3.4431` edge `0.0134` maxDD `-2.6517`
- `market_context_high->metal_4h` score `-0.2814` n `109` status `ready` deltaP `13.5685` edge `0.0171` maxDD `-6.1475`
- `market_context_high->metal_24h` score `-0.2857` n `98` status `ready` deltaP `15.3557` edge `0.1963` maxDD `-15.7982`
- `market_context_high->crypto_major_4h` score `-0.3874` n `109` status `ready` deltaP `0.7468` edge `0.3036` maxDD `-22.3259`
- `market_context_high->crypto_alt_4h` score `-0.6465` n `109` status `ready` deltaP `1.2041` edge `0.1901` maxDD `-17.1476`
- `market_context_high->crypto_major_1h` score `-0.8077` n `112` status `ready` deltaP `2.8443` edge `0.0642` maxDD `-10.2705`
- `market_context_high->index_1h` score `-0.8307` n `112` status `ready` deltaP `-1.62` edge `0.003` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.0603` n `112` status `ready` deltaP `-1.9247` edge `0.0272` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3806` n `112` status `ready` deltaP `-8.9019` edge `-0.0008` maxDD `-0.392`
- `market_context_high->index_4h` score `-2.0738` n `109` status `ready` deltaP `-5.0514` edge `-0.0048` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.5043` n `112` status `ready` deltaP `-11.142` edge `-0.0266` maxDD `-3.9584`
- `market_context_high->equity_1h` score `-2.7576` n `112` status `ready` deltaP `1.358` edge `-0.0211` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-3.8479` n `109` status `ready` deltaP `-16.704` edge `-0.005` maxDD `-2.0104`
- `market_context_high->fx_24h` score `-6.6612` n `98` status `ready` deltaP `-18.1194` edge `-0.0034` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.3021` n `109` status `ready` deltaP `-22.8015` edge `-0.0971` maxDD `-14.7522`
- `market_context_high->index_24h` score `-9.1551` n `98` status `ready` deltaP `-16.7694` edge `-0.1089` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
