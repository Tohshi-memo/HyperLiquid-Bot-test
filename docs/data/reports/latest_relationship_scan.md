# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T04:22:30.271974+00:00`
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

- `market_context_high->unknown_1h` score `10112.6165` n `126` status `ready` deltaP `1.0146` edge `842.7311` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6145.8513` n `126` status `ready` deltaP `-0.3145` edge `512.1869` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `2.9412` n `108` status `ready` deltaP `26.794` edge `1.0052` maxDD `-57.8734`
- `market_context_high->metal_1h` score `-0.1898` n `126` status `ready` deltaP `3.9516` edge `0.0158` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2788` n `126` status `ready` deltaP `3.1579` edge `0.0044` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5953` n `126` status `ready` deltaP `10.4239` edge `0.0348` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4322` n `126` status `ready` deltaP `-9.2553` edge `-0.0017` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.7867` n `126` status `ready` deltaP `5.6886` edge `0.0191` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.9713` n `126` status `ready` deltaP `-7.6413` edge `-0.0002` maxDD `-1.794`
- `market_context_high->crypto_alt_24h` score `-2.1475` n `108` status `ready` deltaP `13.8311` edge `0.7189` maxDD `-72.5383`
- `market_context_high->commodity_1h` score `-2.1937` n `126` status `ready` deltaP `-7.1738` edge `-0.0218` maxDD `-4.3877`
- `market_context_high->crypto_major_1h` score `-2.3479` n `126` status `ready` deltaP `2.7088` edge `0.0181` maxDD `-13.8788`
- `market_context_high->index_4h` score `-2.4457` n `126` status `ready` deltaP `-3.9465` edge `-0.0142` maxDD `-7.0639`
- `market_context_high->crypto_alt_1h` score `-3.0515` n `126` status `ready` deltaP `-3.7449` edge `-0.0016` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.5738` n `126` status `ready` deltaP `-1.1082` edge `0.1139` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.7681` n `108` status `ready` deltaP `12.7894` edge `0.1234` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.6434` n `108` status `ready` deltaP `-17.4769` edge `-0.0098` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.9638` n `126` status `ready` deltaP `-19.7299` edge `-0.0795` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.6513` n `126` status `ready` deltaP `-0.6509` edge `0.048` maxDD `-46.5016`
- `market_context_high->index_24h` score `-12.7608` n `108` status `ready` deltaP `-26.3888` edge `-0.1245` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
