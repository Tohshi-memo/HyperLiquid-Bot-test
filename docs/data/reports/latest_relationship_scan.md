# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T15:23:00.196684+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9839`

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

- `market_context_high->unknown_24h` score `33.1885` n `50` status `ready` deltaP `22.3056` edge `2.6213` maxDD `-0.0103`
- `market_context_high->commodity_24h` score `6.0589` n `50` status `ready` deltaP `32.3472` edge `0.3564` maxDD `-4.038`
- `market_context_high->crypto_alt_24h` score `5.9412` n `50` status `ready` deltaP `32.0069` edge `0.3088` maxDD `-0.8333`
- `market_context_high->unknown_4h` score `5.1885` n `89` status `ready` deltaP `-0.1319` edge `0.5328` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.0643` n `89` status `ready` deltaP `14.4628` edge `0.0769` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.2229` n `89` status `ready` deltaP `15.8965` edge `0.0086` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2016` n `89` status `ready` deltaP `5.3556` edge `0.0227` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1865` n `89` status `ready` deltaP `8.0536` edge `-0.0033` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.5002` n `89` status `ready` deltaP `1.016` edge `-0.0175` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5511` n `89` status `ready` deltaP `-1.682` edge `-0.01` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6177` n `89` status `ready` deltaP `4.2718` edge `0.0158` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8124` n `89` status `ready` deltaP `4.7907` edge `0.0029` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.0763` n `89` status `ready` deltaP `-1.9848` edge `-0.0054` maxDD `-3.0178`
- `market_context_high->fx_24h` score `-1.5768` n `50` status `ready` deltaP `-3.6944` edge `0.0138` maxDD `-4.3126`
- `market_context_high->equity_1h` score `-1.6966` n `89` status `ready` deltaP `4.5381` edge `-0.0942` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.8669` n `89` status `ready` deltaP `-10.1261` edge `-0.0464` maxDD `-4.7021`
- `market_context_high->metal_24h` score `-2.6028` n `50` status `ready` deltaP `-21.5486` edge `-0.0732` maxDD `-2.6802`
- `market_context_high->unknown_1h` score `-3.4134` n `89` status `ready` deltaP `2.661` edge `-0.2575` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5013` n `89` status `ready` deltaP `-12.5463` edge `-0.0708` maxDD `-7.6533`
- `market_context_high->index_24h` score `-4.9009` n `50` status `ready` deltaP `-25.8056` edge `-0.2368` maxDD `-7.8922`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
