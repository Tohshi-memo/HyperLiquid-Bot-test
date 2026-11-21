# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T01:22:25.785370+00:00`
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

- `market_context_high->unknown_1h` score `10118.3225` n `126` status `ready` deltaP `1.4638` edge `843.2036` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6157.0989` n `126` status `ready` deltaP `-0.3145` edge `513.1242` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `3.0715` n `108` status `ready` deltaP `26.794` edge `1.0219` maxDD `-57.8734`
- `market_context_high->metal_1h` score `-0.2295` n `126` status `ready` deltaP `3.3528` edge `0.0147` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.275` n `126` status `ready` deltaP `3.3076` edge `0.0039` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5834` n `126` status `ready` deltaP `10.7288` edge `0.0343` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4214` n `126` status `ready` deltaP `-9.1056` edge `-0.0018` maxDD `-0.4757`
- `market_context_high->crypto_alt_24h` score `-1.5583` n `108` status `ready` deltaP `13.8311` edge `0.768` maxDD `-72.5383`
- `market_context_high->equity_1h` score `-1.9222` n `126` status `ready` deltaP `5.0898` edge `0.0118` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.9887` n `126` status `ready` deltaP `-7.9462` edge `-0.0004` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.1841` n `126` status `ready` deltaP `-7.0241` edge `-0.022` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.3981` n `126` status `ready` deltaP `-3.3367` edge `-0.0143` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.5003` n `126` status `ready` deltaP `2.7088` edge `0.0054` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.192` n `126` status `ready` deltaP `-3.4455` edge `-0.0153` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.6376` n `126` status `ready` deltaP `-0.9558` edge `0.1047` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.6654` n `108` status `ready` deltaP `12.963` edge `0.1308` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.7979` n `108` status `ready` deltaP `-19.213` edge `-0.0111` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.965` n `126` status `ready` deltaP `-19.7299` edge `-0.0796` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.8385` n `126` status `ready` deltaP `-0.6509` edge `0.0324` maxDD `-46.5016`
- `market_context_high->index_24h` score `-12.8784` n `108` status `ready` deltaP `-26.3888` edge `-0.1343` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
