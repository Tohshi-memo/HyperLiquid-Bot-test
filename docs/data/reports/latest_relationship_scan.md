# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T08:52:32.595369+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11540`

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

- `market_context_high->unknown_24h` score `228.9434` n `88` status `ready` deltaP `6.0318` edge `19.0525` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `87.5742` n `88` status `ready` deltaP `7.2201` edge `7.2945` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `30.0659` n `52` status `ready` deltaP `23.9486` edge `2.407` maxDD `-3.2263`
- `market_context_high->equity_24h` score `14.8341` n `88` status `ready` deltaP `16.5185` edge `1.3652` maxDD `-16.7984`
- `news_risk_high->crypto_major_24h` score `12.3274` n `52` status `ready` deltaP `37.9491` edge `1.524` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.5666` n `53` status `ready` deltaP `35.1731` edge `0.8416` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.8771` n `52` status `ready` deltaP `40.1384` edge `0.3055` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.1204` n `88` status `ready` deltaP `34.9638` edge `0.9328` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.8921` n `88` status `ready` deltaP `35.0071` edge `0.2296` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.3755` n `53` status `ready` deltaP `42.1279` edge `0.1214` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.175` n `53` status `ready` deltaP `22.4201` edge `0.3472` maxDD `-9.2335`
- `news_risk_high->index_24h` score `4.0093` n `52` status `ready` deltaP `21.0074` edge `0.2201` maxDD `-0.4168`
- `news_risk_high->equity_1h` score `3.5586` n `53` status `ready` deltaP `18.3143` edge `0.2457` maxDD `-3.6997`
- `market_context_high->index_24h` score `2.8774` n `88` status `ready` deltaP `16.9864` edge `0.1728` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.7676` n `53` status `ready` deltaP `24.8821` edge `0.0901` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.3202` n `53` status `ready` deltaP `26.1936` edge `0.2867` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.2909` n `53` status `ready` deltaP `21.9656` edge `0.0881` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.0971` n `53` status `ready` deltaP `24.9915` edge `0.0336` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3568` n `53` status `ready` deltaP `17.7748` edge `0.0247` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7967` n `53` status `ready` deltaP `18.0431` edge `0.0798` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
