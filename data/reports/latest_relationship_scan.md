# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T13:07:36.229474+00:00`
- Price records: `672`
- Market context records: `6285`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11100`

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

- `news_risk_high->crypto_alt_24h` score `15.2346` n `32` status `ready` deltaP `43.2292` edge `0.9961` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9593` n `32` status `ready` deltaP `50.5208` edge `0.1598` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1865` n `32` status `ready` deltaP `43.8262` edge `0.0613` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.1243` n `32` status `ready` deltaP `16.6667` edge `0.4956` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.7164` n `32` status `ready` deltaP `26.0417` edge `0.0733` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3596` n `32` status `ready` deltaP `28.4431` edge `0.0209` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.52` n `206` status `ready` deltaP `0.5814` edge `0.2236` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.379` n `32` status `ready` deltaP `13.9783` edge `0.1303` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8582` n `32` status `ready` deltaP `11.3211` edge `0.0807` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.5717` n `194` status `ready` deltaP `-2.3588` edge `0.3166` maxDD `-11.925`
- `market_context_high->equity_4h` score `0.2928` n `194` status `ready` deltaP `6.4983` edge `0.0728` maxDD `-2.671`
- `market_context_high->metal_4h` score `-0.2096` n `194` status `ready` deltaP `5.6779` edge `0.0316` maxDD `-2.7056`
- `market_context_high->metal_24h` score `-0.286` n `183` status `ready` deltaP `18.3259` edge `0.098` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2983` n `32` status `ready` deltaP `7.2917` edge `0.0003` maxDD `-2.3058`
- `market_context_high->commodity_1h` score `-0.486` n `206` status `ready` deltaP `0.4084` edge `0.0028` maxDD `-0.682`
- `market_context_high->fx_1h` score `-0.5457` n `206` status `ready` deltaP `0.045` edge `-0.0012` maxDD `-0.5659`
- `news_risk_high->metal_1h` score `-0.7052` n `32` status `ready` deltaP `-2.5449` edge `-0.0237` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7168` n `206` status `ready` deltaP `2.7949` edge `-0.0006` maxDD `-1.8877`
- `market_context_high->commodity_4h` score `-0.7598` n `194` status `ready` deltaP `-2.4972` edge `0.0093` maxDD `-1.2054`
- `market_context_high->crypto_alt_1h` score `-0.8283` n `206` status `ready` deltaP `5.8296` edge `0.0302` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
