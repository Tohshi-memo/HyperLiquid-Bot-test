# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T06:22:26.480979+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2704`

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

- `market_context_high->unknown_1h` score `10084.1333` n `126` status `ready` deltaP `1.1643` edge `840.3565` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6140.1729` n `126` status `ready` deltaP `-0.3145` edge `511.7137` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `3.4903` n `108` status `ready` deltaP `26.794` edge `1.0756` maxDD `-57.8734`
- `market_context_high->metal_1h` score `-0.1914` n `126` status `ready` deltaP `3.9516` edge `0.0156` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.296` n `126` status `ready` deltaP `2.8585` edge `0.0042` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5124` n `126` status `ready` deltaP `11.6434` edge `0.0373` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.3951` n `126` status `ready` deltaP `-8.8062` edge `-0.0016` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.7496` n `126` status `ready` deltaP `6.1377` edge `0.0192` maxDD `-13.1399`
- `market_context_high->crypto_alt_24h` score `-1.8847` n `108` status `ready` deltaP `13.8311` edge `0.7408` maxDD `-72.5383`
- `market_context_high->fx_4h` score `-1.9349` n `126` status `ready` deltaP `-7.0315` edge `0.0004` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.244` n `126` status `ready` deltaP `-7.7726` edge `-0.022` maxDD `-4.3877`
- `market_context_high->crypto_major_1h` score `-2.2736` n `126` status `ready` deltaP `3.1579` edge `0.0213` maxDD `-13.8788`
- `market_context_high->index_4h` score `-2.3447` n `126` status `ready` deltaP `-2.8794` edge `-0.0129` maxDD `-7.0639`
- `market_context_high->crypto_alt_1h` score `-3.0084` n `126` status `ready` deltaP `-3.4455` edge `0.0` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.134` n `126` status `ready` deltaP `-0.3461` edge `0.1652` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.8403` n `108` status `ready` deltaP `12.4422` edge `0.1197` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.5143` n `108` status `ready` deltaP `-16.088` edge `-0.0083` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.8578` n `126` status `ready` deltaP `-18.5104` edge `-0.0788` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.2469` n `126` status `ready` deltaP `-0.6509` edge `0.0817` maxDD `-46.5016`
- `market_context_high->index_24h` score `-12.6744` n `108` status `ready` deltaP `-26.3888` edge `-0.1173` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
