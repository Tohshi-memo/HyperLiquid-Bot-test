# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T17:37:34.121656+00:00`
- Price records: `672`
- Market context records: `6109`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `8.5514` n `30` status `ready` deltaP `35.6944` edge `0.4894` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `8.0466` n `30` status `ready` deltaP `71.5278` edge `0.1937` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1849` n `32` status `ready` deltaP `43.5213` edge `0.0632` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2925` n `32` status `ready` deltaP `27.5449` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.283` n `32` status `ready` deltaP `13.9783` edge `0.118` maxDD `-2.0691`
- `market_context_high->equity_4h` score `1.0566` n `195` status `ready` deltaP `7.2561` edge `0.1314` maxDD `-2.671`
- `news_risk_high->crypto_alt_1h` score `0.6681` n `32` status `ready` deltaP `9.0756` edge `0.0713` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0555` n `30` status `ready` deltaP `9.2361` edge `0.0327` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.34` n `195` status `ready` deltaP `0.2372` edge `-0.0006` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.34` n `30` status `ready` deltaP `14.7917` edge `-0.1064` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6099` n `195` status `ready` deltaP `3.847` edge `0.0149` maxDD `-3.4996`
- `market_context_high->equity_1h` score `-0.6567` n `195` status `ready` deltaP `0.9381` edge `0.0211` maxDD `-4.2573`
- `market_context_high->commodity_1h` score `-0.6888` n `195` status `ready` deltaP `-1.3903` edge `-0.0035` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7255` n `32` status `ready` deltaP `-2.2455` edge `-0.0283` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7505` n `195` status `ready` deltaP `3.1391` edge `-0.0036` maxDD `-2.0564`
- `market_context_high->index_4h` score `-0.8577` n `195` status `ready` deltaP `2.156` edge `0.0221` maxDD `-1.381`
- `market_context_high->crypto_alt_1h` score `-0.9078` n `195` status `ready` deltaP `4.0596` edge `0.0318` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9149` n `195` status `ready` deltaP `4.7636` edge `0.0277` maxDD `-9.807`
- `news_risk_high->index_1h` score `-1.1093` n `32` status `ready` deltaP `-9.8241` edge `-0.0204` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.2335` n `195` status `ready` deltaP `-2.7568` edge `0.0025` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
