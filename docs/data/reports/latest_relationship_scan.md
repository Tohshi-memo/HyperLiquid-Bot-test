# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T07:52:26.009178+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8506`

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

- `market_context_high->equity_24h` score `9.3332` n `32` status `ready` deltaP `16.4931` edge `0.9051` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.4377` n `32` status `ready` deltaP `7.8125` edge `0.2098` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.3654` n `32` status `ready` deltaP `16.6667` edge `0.1102` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.8025` n `32` status `ready` deltaP `11.8056` edge `-0.003` maxDD `-0.0397`
- `market_context_high->metal_4h` score `0.2756` n `75` status `ready` deltaP `7.1057` edge `0.0476` maxDD `-1.7712`
- `market_context_high->commodity_4h` score `0.0038` n `75` status `ready` deltaP `1.2744` edge `0.0505` maxDD `-2.0276`
- `market_context_high->metal_1h` score `-0.1295` n `87` status `ready` deltaP `5.4718` edge `0.0152` maxDD `-1.3312`
- `market_context_high->index_4h` score `-0.3434` n `75` status `ready` deltaP `7.2947` edge `0.0156` maxDD `-2.4279`
- `market_context_high->commodity_1h` score `-0.3853` n `87` status `ready` deltaP `1.9805` edge `0.0045` maxDD `-1.7019`
- `market_context_high->index_1h` score `-0.7706` n `87` status `ready` deltaP `-4.627` edge `0.0101` maxDD `-0.9102`
- `market_context_high->equity_1h` score `-1.0244` n `87` status `ready` deltaP `-4.7767` edge `0.074` maxDD `-7.5459`
- `market_context_high->fx_1h` score `-1.3421` n `87` status `ready` deltaP `-14.6139` edge `-0.0062` maxDD `-0.8088`
- `market_context_high->crypto_alt_1h` score `-1.5485` n `87` status `ready` deltaP `2.6653` edge `-0.0252` maxDD `-10.2873`
- `market_context_high->metal_24h` score `-1.784` n `32` status `ready` deltaP `-1.5625` edge `-0.163` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.4888` n `75` status `ready` deltaP `-14.2683` edge `-0.0151` maxDD `-2.3754`
- `market_context_high->crypto_major_1h` score `-2.9371` n `87` status `ready` deltaP `-3.7288` edge `-0.0949` maxDD `-15.5433`
- `market_context_high->equity_4h` score `-4.0795` n `75` status `ready` deltaP `4.7439` edge `0.0064` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-4.3978` n `32` status `ready` deltaP `-4.8611` edge `0.0302` maxDD `-23.1423`
- `market_context_high->crypto_alt_4h` score `-8.2258` n `75` status `ready` deltaP `1.3943` edge `-0.2279` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-9.1906` n `32` status `ready` deltaP `-18.75` edge `-0.183` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
