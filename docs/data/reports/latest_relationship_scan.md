# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T22:52:26.556990+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2736`

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

- `market_context_high->unknown_1h` score `10128.7157` n `126` status `ready` deltaP `1.4638` edge `844.0697` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6179.7657` n `126` status `ready` deltaP `-0.3145` edge `515.0131` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `3.4841` n `108` status `ready` deltaP `26.794` edge `1.0748` maxDD `-57.8734`
- `market_context_high->metal_1h` score `-0.2116` n `126` status `ready` deltaP `3.6522` edge `0.015` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2571` n `126` status `ready` deltaP `3.607` edge `0.0042` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5005` n `126` status `ready` deltaP `11.9483` edge `0.0368` maxDD `-10.1161`
- `market_context_high->crypto_alt_24h` score `-0.7147` n `108` status `ready` deltaP `13.8311` edge `0.8383` maxDD `-72.5383`
- `market_context_high->fx_1h` score `-1.3843` n `126` status `ready` deltaP `-8.6565` edge `-0.0017` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.8407` n `126` status `ready` deltaP `5.5389` edge `0.0156` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.9887` n `126` status `ready` deltaP `-7.9462` edge `-0.0004` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.2607` n `126` status `ready` deltaP `-7.9223` edge `-0.0224` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.262` n `126` status `ready` deltaP `-1.9648` edge `-0.0121` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.5195` n `126` status `ready` deltaP `2.5591` edge `0.0048` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.2291` n `126` status `ready` deltaP `-3.5952` edge `-0.0174` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.2487` n `126` status `ready` deltaP `0.5686` edge `0.1444` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.6906` n `108` status `ready` deltaP `12.963` edge `0.1287` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.8746` n `108` status `ready` deltaP `-20.081` edge `-0.0117` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.0078` n `126` status `ready` deltaP `-20.3397` edge `-0.0791` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.3122` n `126` status `ready` deltaP `0.8735` edge `0.0661` maxDD `-46.5016`
- `market_context_high->index_24h` score `-12.9732` n `108` status `ready` deltaP `-26.3888` edge `-0.1422` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
