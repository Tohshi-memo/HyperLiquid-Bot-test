# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T01:52:34.699513+00:00`
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

- `market_context_high->unknown_1h` score `10118.2961` n `126` status `ready` deltaP `1.4638` edge `843.2014` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6148.4001` n `126` status `ready` deltaP `-0.3145` edge `512.3993` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `3.0059` n `108` status `ready` deltaP `26.794` edge `1.0135` maxDD `-57.8734`
- `market_context_high->metal_1h` score `-0.221` n `126` status `ready` deltaP `3.5025` edge `0.0148` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2835` n `126` status `ready` deltaP `3.1579` edge `0.0038` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.6024` n `126` status `ready` deltaP `10.4239` edge `0.0339` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4454` n `126` status `ready` deltaP `-9.405` edge `-0.0018` maxDD `-0.4757`
- `market_context_high->crypto_alt_24h` score `-1.6963` n `108` status `ready` deltaP `13.8311` edge `0.7565` maxDD `-72.5383`
- `market_context_high->equity_1h` score `-1.9102` n `126` status `ready` deltaP `5.2395` edge `0.0118` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.988` n `126` status `ready` deltaP `-7.9462` edge `-0.0003` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.1577` n `126` status `ready` deltaP `-6.7247` edge `-0.0218` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.4273` n `126` status `ready` deltaP `-3.6416` edge `-0.0147` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.4991` n `126` status `ready` deltaP `2.7088` edge `0.0055` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.1848` n `126` status `ready` deltaP `-3.4455` edge `-0.0147` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.6986` n `126` status `ready` deltaP `-1.1082` edge `0.0979` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.675` n `108` status `ready` deltaP `12.963` edge `0.13` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.7979` n `108` status `ready` deltaP `-19.213` edge `-0.0111` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.9638` n `126` status `ready` deltaP `-19.7299` edge `-0.0795` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.9023` n `126` status `ready` deltaP `-0.8034` edge `0.0281` maxDD `-46.5016`
- `market_context_high->index_24h` score `-12.8604` n `108` status `ready` deltaP `-26.3888` edge `-0.1328` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
