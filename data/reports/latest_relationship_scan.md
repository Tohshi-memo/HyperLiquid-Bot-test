# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T15:52:36.411715+00:00`
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

- `market_context_high->unknown_24h` score `31.7084` n `52` status `ready` deltaP `22.2088` edge `2.4986` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.1861` n `89` status `ready` deltaP `-0.1319` edge `0.5326` maxDD `-3.6303`
- `market_context_high->crypto_alt_24h` score `5.1836` n `52` status `ready` deltaP `28.6992` edge `0.282` maxDD `-1.3088`
- `market_context_high->commodity_24h` score `4.8213` n `52` status `ready` deltaP `29.5406` edge `0.308` maxDD `-6.2527`
- `market_context_high->commodity_4h` score `1.0871` n `89` status `ready` deltaP `14.4628` edge `0.0788` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.2229` n `89` status `ready` deltaP `15.8965` edge `0.0086` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.1992` n `89` status `ready` deltaP `5.3556` edge `0.0225` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1865` n `89` status `ready` deltaP `8.0536` edge `-0.0033` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.5025` n `89` status `ready` deltaP `1.016` edge `-0.0178` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5504` n `89` status `ready` deltaP `-1.682` edge `-0.0099` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6414` n `89` status `ready` deltaP `3.9669` edge `0.0148` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8147` n `89` status `ready` deltaP `4.7907` edge `0.0026` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.0799` n `89` status `ready` deltaP `-1.9848` edge `-0.0057` maxDD `-3.0178`
- `market_context_high->fx_24h` score `-1.301` n `52` status `ready` deltaP `-1.0417` edge `0.0191` maxDD `-4.3126`
- `market_context_high->equity_1h` score `-1.7185` n `89` status `ready` deltaP `4.3884` edge `-0.096` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.8914` n `89` status `ready` deltaP `-10.431` edge `-0.0475` maxDD `-4.7021`
- `market_context_high->metal_24h` score `-2.2184` n `52` status `ready` deltaP `-19.5112` edge `-0.0375` maxDD `-2.6802`
- `market_context_high->unknown_1h` score `-3.4194` n `89` status `ready` deltaP `2.661` edge `-0.258` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5025` n `89` status `ready` deltaP `-12.5463` edge `-0.0709` maxDD `-7.6533`
- `market_context_high->index_24h` score `-4.5601` n `52` status `ready` deltaP `-23.6913` edge `-0.2072` maxDD `-7.8922`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
