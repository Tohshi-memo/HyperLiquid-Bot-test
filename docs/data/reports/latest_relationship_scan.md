# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T07:07:40.170705+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2700`

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

- `market_context_high->unknown_1h` score `10069.3853` n `126` status `ready` deltaP `1.1643` edge `839.1275` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6143.7933` n `126` status `ready` deltaP `-0.3145` edge `512.0154` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `3.6073` n `108` status `ready` deltaP `26.794` edge `1.0906` maxDD `-57.8734`
- `market_context_high->metal_1h` score `-0.1953` n `126` status `ready` deltaP `3.9516` edge `0.0151` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3061` n `126` status `ready` deltaP `2.7088` edge `0.0039` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5022` n `126` status `ready` deltaP `11.7958` edge `0.0376` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.3663` n `126` status `ready` deltaP `-8.5068` edge `-0.0012` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.7868` n `126` status `ready` deltaP `6.1377` edge `0.0161` maxDD `-13.1399`
- `market_context_high->crypto_alt_24h` score `-1.8667` n `108` status `ready` deltaP `13.8311` edge `0.7423` maxDD `-72.5383`
- `market_context_high->fx_4h` score `-1.931` n `126` status `ready` deltaP `-7.0315` edge `0.0009` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.2308` n `126` status `ready` deltaP `-7.6229` edge `-0.0219` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.3325` n `126` status `ready` deltaP `-2.727` edge `-0.0129` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.4044` n `126` status `ready` deltaP `3.1579` edge `0.0104` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.1199` n `126` status `ready` deltaP `-3.5952` edge `-0.0083` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.0902` n `126` status `ready` deltaP `-0.1936` edge `0.1698` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.8523` n `108` status `ready` deltaP `12.4422` edge `0.1187` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.4607` n `108` status `ready` deltaP `-15.5671` edge `-0.0073` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.8188` n `126` status `ready` deltaP `-18.0531` edge `-0.0786` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.2181` n `126` status `ready` deltaP `-0.6509` edge `0.0841` maxDD `-46.5016`
- `market_context_high->index_24h` score `-12.6468` n `108` status `ready` deltaP `-26.3888` edge `-0.115` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
