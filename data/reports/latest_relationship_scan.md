# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T16:37:27.790147+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->unknown_24h` score `75.9927` n `159` status `ready` deltaP `-24.4399` edge `6.7869` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.6431` n `32` status `ready` deltaP `-42.1875` edge `4.6695` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.6431` n `32` status `ready` deltaP `-42.1875` edge `4.6695` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.3418` n `36` status `ready` deltaP `10.0694` edge `0.7493` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.4255` n `36` status `ready` deltaP `35.2134` edge `0.3007` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.0756` n `32` status `ready` deltaP `28.8194` edge `0.1475` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.0756` n `32` status `ready` deltaP `28.8194` edge `0.1475` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.6892` n `32` status `ready` deltaP `19.1311` edge `0.1148` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.6892` n `32` status `ready` deltaP `19.1311` edge `0.1148` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.54` n `36` status `ready` deltaP `15.625` edge `0.1075` maxDD `0.0`
- `market_context_high->commodity_24h` score `2.105` n `159` status `ready` deltaP `18.7565` edge `0.1307` maxDD `-2.4263`
- `risk_on_high->fx_24h` score `1.8999` n `32` status `ready` deltaP `21.3542` edge `0.0344` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.8999` n `32` status `ready` deltaP `21.3542` edge `0.0344` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.6397` n `36` status `ready` deltaP `19.3089` edge `0.0211` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.4881` n `159` status `ready` deltaP `16.4778` edge `0.078` maxDD `-2.1077`
- `news_risk_high->equity_1h` score `1.4024` n `36` status `ready` deltaP `7.0859` edge `0.1015` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2012` n `32` status `ready` deltaP `13.0614` edge `0.0363` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2012` n `32` status `ready` deltaP `13.0614` edge `0.0363` maxDD `-0.1957`
- `risk_on_high->crypto_major_24h` score `1.1524` n `32` status `ready` deltaP `11.6319` edge `0.1858` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.1524` n `32` status `ready` deltaP `11.6319` edge `0.1858` maxDD `-6.2481`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
