# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T00:07:27.911622+00:00`
- Price records: `672`
- Market context records: `7615`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14551`

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

- `market_context_high->equity_24h` score `0.9595` n `145` status `ready` deltaP `16.9771` edge `0.5004` maxDD `-34.5784`
- `market_context_high->unknown_24h` score `0.671` n `146` status `ready` deltaP `11.7057` edge `0.0959` maxDD `-4.775`
- `market_context_high->commodity_24h` score `0.2288` n `145` status `ready` deltaP `14.8072` edge `0.0787` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.114` n `146` status `ready` deltaP `7.5631` edge `0.0121` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1471` n `146` status `ready` deltaP `8.0059` edge `0.0238` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.189` n `146` status `ready` deltaP `2.5039` edge `0.0223` maxDD `-2.7243`
- `market_context_high->commodity_1h` score `-0.2554` n `146` status `ready` deltaP `3.7804` edge `-0.0009` maxDD `-1.5641`
- `market_context_high->commodity_4h` score `-0.2652` n `146` status `ready` deltaP `5.5821` edge `0.0152` maxDD `-2.2943`
- `market_context_high->fx_24h` score `-0.3443` n `145` status `ready` deltaP `9.2803` edge `0.0182` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.4159` n `146` status `ready` deltaP `6.4277` edge `0.0552` maxDD `-7.7764`
- `market_context_high->index_4h` score `-0.5717` n `146` status `ready` deltaP `9.9807` edge `0.0303` maxDD `-3.2774`
- `market_context_high->metal_1h` score `-0.6037` n `146` status `ready` deltaP `1.8374` edge `0.0149` maxDD `-1.0307`
- `market_context_high->fx_1h` score `-0.6906` n `146` status `ready` deltaP `-0.8721` edge `-0.0018` maxDD `-0.6615`
- `market_context_high->crypto_alt_4h` score `-0.925` n `146` status `ready` deltaP `3.5019` edge `0.057` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.1249` n `146` status `ready` deltaP `8.8268` edge `0.0647` maxDD `-14.4206`
- `market_context_high->equity_4h` score `-1.4299` n `146` status `ready` deltaP `2.8256` edge `0.2122` maxDD `-20.4824`
- `market_context_high->unknown_1h` score `-1.4319` n `146` status `ready` deltaP `-0.2358` edge `-0.0554` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.6062` n `146` status `ready` deltaP `-0.9084` edge `0.0458` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-1.8883` n `146` status `ready` deltaP `-2.5828` edge `0.1008` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.5776` n `146` status `ready` deltaP `-6.3529` edge `-0.004` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
