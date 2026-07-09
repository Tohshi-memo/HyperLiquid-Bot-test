# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T22:27:37.687938+00:00`
- Price records: `672`
- Market context records: `6223`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11110`

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

- `news_risk_high->crypto_alt_24h` score `13.2998` n `32` status `ready` deltaP `42.2194` edge `0.8416` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.4406` n `32` status `ready` deltaP `55.4422` edge `0.1671` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1513` n `32` status `ready` deltaP `43.5213` edge `0.0604` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `2.5756` n `32` status `ready` deltaP `15.625` edge `0.304` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.3332` n `32` status `ready` deltaP `28.1437` edge `0.0207` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.0875` n `192` status `ready` deltaP `2.4108` edge `0.2587` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3782` n `32` status `ready` deltaP `14.128` edge `0.1292` maxDD `-2.0691`
- `news_risk_high->commodity_24h` score `1.3747` n `32` status `ready` deltaP `21.4498` edge `-0.0079` maxDD `-0.3101`
- `market_context_high->unknown_4h` score `0.7983` n `192` status `ready` deltaP `-1.5371` edge `0.33` maxDD `-11.925`
- `news_risk_high->crypto_alt_1h` score `0.76` n `32` status `ready` deltaP `10.1235` edge `0.0761` maxDD `-1.6923`
- `market_context_high->metal_24h` score `-0.0478` n `192` status `ready` deltaP `19.8023` edge `0.1187` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2151` n `32` status `ready` deltaP `8.801` edge `0.0009` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3003` n `192` status `ready` deltaP `1.0604` edge `-0.001` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.5691` n `192` status `ready` deltaP `-0.7485` edge `0.0022` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.6244` n `192` status `ready` deltaP `3.8237` edge `0.0132` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.815` n `32` status `ready` deltaP `-4.0419` edge `-0.0278` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.9037` n `192` status `ready` deltaP `4.3943` edge `0.0301` maxDD `-9.3536`
- `market_context_high->metal_1h` score `-0.9131` n `192` status `ready` deltaP `1.1664` edge `-0.004` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.9215` n `192` status `ready` deltaP `4.2322` edge `0.0304` maxDD `-9.807`
- `market_context_high->equity_4h` score `-0.9934` n `192` status `ready` deltaP `1.2957` edge `0.0003` maxDD `-2.671`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
