# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T12:52:27.544337+00:00`
- Price records: `672`
- Market context records: `8516`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5882`

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

- `news_risk_high->unknown_24h` score `6277.6869` n `52` status `ready` deltaP `44.7383` edge `522.8844` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.5578` n `64` status `ready` deltaP `21.1128` edge `0.3821` maxDD `-3.4427`
- `market_context_high->equity_4h` score `3.525` n `32` status `ready` deltaP `30.4878` edge `0.1203` maxDD `-1.3839`
- `news_risk_high->index_4h` score `1.9867` n `64` status `ready` deltaP `16.5015` edge `0.0746` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7721` n `64` status `ready` deltaP `16.1022` edge `0.088` maxDD `-2.4803`
- `market_context_high->crypto_major_4h` score `1.0524` n `32` status `ready` deltaP `7.3933` edge `0.159` maxDD `-2.8692`
- `market_context_high->crypto_alt_4h` score `1.0139` n `32` status `ready` deltaP `11.2043` edge `0.1301` maxDD `-3.9846`
- `news_risk_high->crypto_major_4h` score `0.8565` n `64` status `ready` deltaP `5.8308` edge `0.1485` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.7897` n `64` status `ready` deltaP `14.3293` edge `0.1449` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.5622` n `64` status `ready` deltaP `9.3095` edge `0.0627` maxDD `-1.8813`
- `market_context_high->metal_4h` score `0.3447` n `32` status `ready` deltaP `15.7774` edge `-0.0083` maxDD `-1.2157`
- `news_risk_high->crypto_major_1h` score `0.3275` n `64` status `ready` deltaP `6.6149` edge `0.0491` maxDD `-2.0972`
- `market_context_high->index_4h` score `0.3173` n `32` status `ready` deltaP `8.689` edge `0.0118` maxDD `-0.3238`
- `market_context_high->commodity_1h` score `0.095` n `44` status `ready` deltaP `8.914` edge `0.0153` maxDD `-2.0038`
- `news_risk_high->fx_1h` score `0.0846` n `64` status `ready` deltaP `5.2863` edge `0.0037` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0659` n `64` status `ready` deltaP `4.6688` edge `0.009` maxDD `-0.5338`
- `market_context_high->fx_4h` score `0.0647` n `32` status `ready` deltaP `6.4787` edge `0.0146` maxDD `-0.2932`
- `news_risk_high->fx_4h` score `-0.0062` n `64` status `ready` deltaP `11.1662` edge `0.0208` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `-0.0248` n `64` status `ready` deltaP `1.7149` edge `0.033` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.1287` n `64` status `ready` deltaP `3.256` edge `0.0079` maxDD `-0.5599`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
