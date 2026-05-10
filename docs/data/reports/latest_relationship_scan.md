# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T07:22:17.189815+00:00`
- Price records: `672`
- Market context records: `952`
- Flow alert records: `2667`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `14.7613` n `163` status `ready` deltaP `32.1756` edge `1.049` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `8.3282` n `163` status `ready` deltaP `8.5069` edge `0.6373` maxDD `0.0`
- `market_context_high->equity_24h` score `1.0182` n `163` status `ready` deltaP `2.9141` edge `0.3259` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.2597` n `163` status `ready` deltaP `1.5827` edge `0.2106` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.2316` n `204` status `ready` deltaP `3.402` edge `0.0388` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.3919` n `204` status `ready` deltaP `1.0098` edge `0.0011` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.6108` n `204` status `ready` deltaP `1.4794` edge `0.0161` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.657` n `193` status `ready` deltaP `1.9659` edge `0.0023` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.7231` n `204` status `ready` deltaP `2.8942` edge `0.0058` maxDD `-2.8282`
- `market_context_high->equity_4h` score `-1.2128` n `193` status `ready` deltaP `2.781` edge `0.0956` maxDD `-10.5498`
- `market_context_high->unknown_1h` score `-1.3569` n `204` status `ready` deltaP `-2.9412` edge `-0.0163` maxDD `-3.5069`
- `market_context_high->commodity_4h` score `-1.3974` n `193` status `ready` deltaP `-0.9881` edge `0.0817` maxDD `-13.0076`
- `market_context_high->index_4h` score `-1.4637` n `193` status `ready` deltaP `0.4344` edge `0.0274` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.6594` n `204` status `ready` deltaP `5.7473` edge `-0.0043` maxDD `-11.4508`
- `market_context_high->metal_1h` score `-1.8144` n `204` status `ready` deltaP `-1.1535` edge `-0.029` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-1.934` n `204` status `ready` deltaP `1.2299` edge `-0.0254` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.4197` n `193` status `ready` deltaP `9.1882` edge `0.1077` maxDD `-22.648`
- `market_context_high->crypto_alt_4h` score `-3.3571` n `193` status `ready` deltaP `-2.0623` edge `0.0118` maxDD `-15.2248`
- `market_context_high->unknown_4h` score `-3.3751` n `193` status `ready` deltaP `6.3543` edge `-0.1358` maxDD `-8.3588`
- `market_context_high->unknown_24h` score `-4.5277` n `163` status `ready` deltaP `4.8462` edge `-0.0622` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
