# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T08:37:27.137192+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4522`

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

- `market_context_high->unknown_1h` score `11661.748` n `109` status `ready` deltaP `0.5177` edge `971.8287` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7257.0214` n `109` status `ready` deltaP `-1.8572` edge `604.7947` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.234` n `109` status `ready` deltaP `3.8826` edge `0.0106` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3473` n `109` status `ready` deltaP `2.5737` edge `0.0026` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.2024` n `109` status `ready` deltaP `-8.3434` edge `-0.0016` maxDD `-0.4384`
- `market_context_high->crypto_major_1h` score `-1.4258` n `109` status `ready` deltaP `4.1092` edge `0.0008` maxDD `-13.8788`
- `market_context_high->fx_4h` score `-1.5793` n `109` status `ready` deltaP `-1.102` edge `0.0031` maxDD `-1.5246`
- `market_context_high->equity_1h` score `-1.7265` n `109` status `ready` deltaP `7.5908` edge `0.0031` maxDD `-13.1399`
- `market_context_high->metal_4h` score `-1.8928` n `109` status `ready` deltaP `3.1774` edge `0.0017` maxDD `-10.1161`
- `market_context_high->crypto_alt_1h` score `-2.1449` n `109` status `ready` deltaP `-3.9787` edge `-0.0374` maxDD `-13.8848`
- `market_context_high->commodity_1h` score `-2.4723` n `109` status `ready` deltaP `-10.2895` edge `-0.0257` maxDD `-4.2715`
- `market_context_high->index_4h` score `-3.2467` n `109` status `ready` deltaP `-11.7839` edge `-0.0287` maxDD `-7.0639`
- `market_context_high->fx_24h` score `-5.0319` n `109` status `ready` deltaP `-7.8905` edge `-0.0027` maxDD `-6.1216`
- `market_context_high->commodity_4h` score `-6.7597` n `109` status `ready` deltaP `-17.3081` edge `-0.0875` maxDD `-14.834`
- `market_context_high->metal_24h` score `-9.8882` n `109` status `ready` deltaP `-6.8727` edge `0.0314` maxDD `-52.1012`
- `market_context_high->crypto_major_4h` score `-10.3777` n `109` status `ready` deltaP `-7.2024` edge `-0.1239` maxDD `-47.4317`
- `market_context_high->crypto_alt_4h` score `-10.7766` n `109` status `ready` deltaP `-7.8121` edge `-0.1647` maxDD `-46.5016`
- `market_context_high->commodity_24h` score `-12.8167` n `109` status `ready` deltaP `-27.4847` edge `-0.3484` maxDD `-63.2559`
- `market_context_high->crypto_major_24h` score `-15.0936` n `109` status `ready` deltaP `8.4193` edge `0.0688` maxDD `-152.134`
- `market_context_high->index_24h` score `-15.8416` n `109` status `ready` deltaP `-31.3248` edge `-0.1717` maxDD `-39.8349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
