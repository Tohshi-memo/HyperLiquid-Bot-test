# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T09:07:31.188743+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9968`

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

- `market_context_high->unknown_1h` score `65.997` n `47` status `ready` deltaP `10.4154` edge `5.4374` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `41.0719` n `46` status `ready` deltaP `28.4647` edge `3.2485` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `26.3442` n `46` status `ready` deltaP `23.4375` edge `2.0391` maxDD `0.0`
- `market_context_high->equity_24h` score `23.8505` n `46` status `ready` deltaP `25.8605` edge `1.8252` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.8838` n `46` status `ready` deltaP `34.8883` edge `0.4331` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `7.3308` n `103` status `ready` deltaP `0.7737` edge `1.51` maxDD `-63.6743`
- `news_risk_high->crypto_major_4h` score `4.212` n `106` status `ready` deltaP `16.9553` edge `0.2957` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `4.1091` n `106` status `ready` deltaP `12.0485` edge `0.3619` maxDD `-5.9838`
- `news_risk_high->crypto_alt_24h` score `4.0821` n `103` status `ready` deltaP `-1.8052` edge `1.0535` maxDD `-49.7699`
- `market_context_high->metal_24h` score `3.1302` n `46` status `ready` deltaP `28.8648` edge `0.0918` maxDD `-0.2042`
- `market_context_high->index_4h` score `2.8733` n `47` status `ready` deltaP `33.1117` edge `0.0341` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.4262` n `114` status `ready` deltaP `13.2472` edge `0.1629` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.2423` n `47` status `ready` deltaP `15.925` edge `0.1225` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.0589` n `114` status `ready` deltaP `15.343` edge `0.1128` maxDD `-1.8141`
- `news_risk_high->commodity_24h` score `1.6715` n `103` status `ready` deltaP `19.4073` edge `0.1278` maxDD `-2.431`
- `news_risk_high->fx_4h` score `1.6449` n `106` status `ready` deltaP `23.9358` edge `0.0411` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2817` n `103` status `ready` deltaP `30.1847` edge `0.1262` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.9331` n `47` status `ready` deltaP `14.3107` edge `0.0102` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8828` n `47` status `ready` deltaP `10.7179` edge `0.0424` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.7014` n `103` status `ready` deltaP `20.739` edge `0.0965` maxDD `-7.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
