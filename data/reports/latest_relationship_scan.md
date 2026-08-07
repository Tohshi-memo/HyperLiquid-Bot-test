# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T18:52:32.137097+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->metal_24h` score `3.3556` n `94` status `ready` deltaP `15.4391` edge `0.2343` maxDD `-2.2743`
- `market_context_high->equity_24h` score `2.7182` n `94` status `ready` deltaP `-2.8551` edge `0.5682` maxDD `-21.1456`
- `market_context_high->fx_24h` score `1.6717` n `94` status `ready` deltaP `26.8121` edge `0.0589` maxDD `-2.5339`
- `market_context_high->commodity_4h` score `1.5491` n `109` status `ready` deltaP `15.5977` edge `0.0924` maxDD `-2.7169`
- `market_context_high->index_24h` score `0.8315` n `94` status `ready` deltaP `8.9398` edge `0.161` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `0.4414` n `117` status `ready` deltaP `10.4279` edge `0.0263` maxDD `-1.1388`
- `market_context_high->fx_4h` score `0.1358` n `109` status `ready` deltaP `9.3113` edge `0.0079` maxDD `-1.6928`
- `market_context_high->fx_1h` score `-0.1742` n `117` status `ready` deltaP `5.7053` edge `-0.003` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.4676` n `109` status `ready` deltaP `0.6252` edge `-0.0036` maxDD `-1.1743`
- `market_context_high->index_1h` score `-0.7064` n `117` status `ready` deltaP `-1.4995` edge `-0.0096` maxDD `-1.1418`
- `market_context_high->metal_1h` score `-0.872` n `117` status `ready` deltaP `-2.953` edge `-0.0034` maxDD `-0.9664`
- `market_context_high->equity_1h` score `-0.9037` n `117` status `ready` deltaP `4.097` edge `-0.0205` maxDD `-7.8142`
- `market_context_high->metal_4h` score `-0.9334` n `109` status `ready` deltaP `2.9397` edge `0.0035` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.3643` n `109` status `ready` deltaP `7.8205` edge `-0.0321` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.4787` n `117` status `ready` deltaP `-5.9855` edge `-0.0204` maxDD `-2.3669`
- `market_context_high->crypto_alt_4h` score `-2.6161` n `109` status `ready` deltaP `-2.4376` edge `-0.0461` maxDD `-5.7857`
- `market_context_high->crypto_major_24h` score `-2.995` n `94` status `ready` deltaP `1.7021` edge `-0.1459` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-3.0227` n `117` status `ready` deltaP `-7.6706` edge `-0.0628` maxDD `-7.7029`
- `market_context_high->crypto_alt_24h` score `-4.5391` n `94` status `ready` deltaP `-16.0575` edge `-0.1269` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-6.7653` n `109` status `ready` deltaP `-7.6485` edge `-0.1899` maxDD `-19.164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
