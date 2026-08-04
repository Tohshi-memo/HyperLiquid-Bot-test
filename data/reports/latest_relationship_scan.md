# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T21:22:35.595865+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9856`

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

- `market_context_high->unknown_24h` score `20.1824` n `74` status `ready` deltaP `19.1347` edge `1.5586` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.3809` n `90` status `ready` deltaP `1.7479` edge `0.5363` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5171` n `90` status `ready` deltaP `16.9276` edge `0.0982` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.5943` n `74` status `ready` deltaP `-3.1766` edge `0.2142` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5581` n `74` status `ready` deltaP `18.3042` edge `0.0701` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.2438` n `90` status `ready` deltaP `5.4923` edge `0.0253` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.1369` n `90` status `ready` deltaP `14.3767` edge `0.0077` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.1362` n `90` status `ready` deltaP `7.4551` edge `-0.0035` maxDD `-0.7878`
- `market_context_high->crypto_alt_24h` score `-0.0612` n `74` status `ready` deltaP `6.4705` edge `0.0894` maxDD `-4.2311`
- `market_context_high->metal_1h` score `-0.5239` n `90` status `ready` deltaP `-1.3074` edge `-0.009` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5363` n `90` status `ready` deltaP `0.4425` edge `-0.0183` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.7149` n `90` status `ready` deltaP `-2.159` edge `-0.0062` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.7353` n `90` status `ready` deltaP `2.8794` edge `0.01` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8704` n `90` status `ready` deltaP `4.0955` edge `0.0001` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.6152` n `90` status `ready` deltaP `5.2495` edge `-0.0885` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0028` n `90` status `ready` deltaP `-11.6734` edge `-0.0535` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.1978` n `74` status `ready` deltaP `-9.0418` edge `-0.002` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.3816` n `90` status `ready` deltaP `-11.4105` edge `-0.0684` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4324` n `90` status `ready` deltaP `2.0492` edge `-0.255` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-3.7786` n `74` status `ready` deltaP `9.9193` edge `-0.0346` maxDD `-31.9443`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
