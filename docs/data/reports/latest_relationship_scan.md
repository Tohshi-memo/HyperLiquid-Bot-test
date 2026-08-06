# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T23:37:30.293843+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11765`

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

- `market_context_high->unknown_24h` score `34.521` n `109` status `ready` deltaP `3.7571` edge `2.856` maxDD `-0.0104`
- `market_context_high->commodity_4h` score `1.1598` n `120` status `ready` deltaP `13.1071` edge `0.0939` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.904` n `109` status `ready` deltaP `3.7004` edge `0.1675` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5441` n `109` status `ready` deltaP `21.4854` edge `0.0471` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4799` n `120` status `ready` deltaP `7.7994` edge `0.0296` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0194` n `120` status `ready` deltaP `5.5539` edge `-0.0045` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.417` n `120` status `ready` deltaP `5.0754` edge `-0.0013` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5537` n `120` status `ready` deltaP `-2.2255` edge `-0.0067` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7638` n `120` status `ready` deltaP `-2.8443` edge `-0.0079` maxDD `-3.0178`
- `market_context_high->index_1h` score `-1.0851` n `120` status `ready` deltaP `-3.2734` edge `-0.0152` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-1.3128` n `120` status `ready` deltaP `1.2406` edge `0.0058` maxDD `-3.211`
- `market_context_high->index_24h` score `-1.3179` n `109` status `ready` deltaP `-3.7172` edge `0.0753` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.3927` n `120` status `ready` deltaP `3.1986` edge `-0.0434` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.6923` n `120` status `ready` deltaP `-7.862` edge `-0.0391` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.895` n `120` status `ready` deltaP `1.9004` edge `-0.0316` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.6022` n `120` status `ready` deltaP `-6.4521` edge `-0.0365` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.0044` n `109` status `ready` deltaP `-5.9793` edge `-0.0662` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-6.1223` n `120` status `ready` deltaP `-0.1245` edge `-0.2552` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.2869` n `109` status `ready` deltaP `9.8099` edge `0.0051` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.3024` n `120` status `ready` deltaP `-6.6063` edge `-0.1433` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
