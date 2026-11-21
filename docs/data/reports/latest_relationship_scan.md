# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T03:07:29.138495+00:00`
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

- `market_context_high->unknown_1h` score `10115.9165` n `126` status `ready` deltaP `1.4638` edge `843.0031` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6148.7325` n `126` status `ready` deltaP `-0.3145` edge `512.427` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `2.7337` n `108` status `ready` deltaP `26.794` edge `0.9786` maxDD `-57.8734`
- `market_context_high->metal_1h` score `-0.2054` n `126` status `ready` deltaP `3.8019` edge `0.0148` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2835` n `126` status `ready` deltaP `3.1579` edge `0.0038` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.6293` n `126` status `ready` deltaP `9.9666` edge `0.0335` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4334` n `126` status `ready` deltaP `-9.2553` edge `-0.0018` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.8815` n `126` status `ready` deltaP `5.5389` edge `0.0122` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.9872` n `126` status `ready` deltaP `-7.9462` edge `-0.0002` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.1961` n `126` status `ready` deltaP `-7.1738` edge `-0.022` maxDD `-4.3877`
- `market_context_high->crypto_alt_24h` score `-2.2099` n `108` status `ready` deltaP `13.8311` edge `0.7137` maxDD `-72.5383`
- `market_context_high->index_4h` score `-2.4809` n `126` status `ready` deltaP `-4.2513` edge `-0.0151` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.5291` n `126` status `ready` deltaP `2.7088` edge `0.003` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.2699` n `126` status `ready` deltaP `-3.8946` edge `-0.0188` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.7626` n `126` status `ready` deltaP `-1.1082` edge `0.0897` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.7417` n `108` status `ready` deltaP `12.7894` edge `0.1256` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.7225` n `108` status `ready` deltaP `-18.3449` edge `-0.0106` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.9662` n `126` status `ready` deltaP `-19.7299` edge `-0.0797` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.9479` n `126` status `ready` deltaP `-0.8034` edge `0.0243` maxDD `-46.5016`
- `market_context_high->index_24h` score `-12.8184` n `108` status `ready` deltaP `-26.3888` edge `-0.1293` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
