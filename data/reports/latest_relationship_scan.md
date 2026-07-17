# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T10:37:28.410894+00:00`
- Price records: `672`
- Market context records: `7019`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11529`

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

- `market_context_high->fx_1h` score `-0.2608` n `224` status `ready` deltaP `2.0958` edge `0.0011` maxDD `-0.5468`
- `market_context_high->unknown_24h` score `-0.579` n `211` status `ready` deltaP `-6.2434` edge `0.4224` maxDD `-18.7342`
- `market_context_high->crypto_alt_1h` score `-0.6501` n `224` status `ready` deltaP `0.8795` edge `0.0264` maxDD `-4.5815`
- `market_context_high->metal_1h` score `-0.6883` n `224` status `ready` deltaP `-1.7483` edge `0.0002` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.7153` n `224` status `ready` deltaP `-0.1176` edge `0.0002` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.7489` n `224` status `ready` deltaP `2.5235` edge `0.0224` maxDD `-7.1523`
- `market_context_high->fx_4h` score `-0.9643` n `224` status `ready` deltaP `10.1589` edge `0.006` maxDD `-2.1216`
- `market_context_high->commodity_1h` score `-1.2953` n `224` status `ready` deltaP `-2.8336` edge `-0.0169` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.3104` n `224` status `ready` deltaP `-2.5048` edge `-0.0024` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.7094` n `224` status `ready` deltaP `-4.7365` edge `-0.0406` maxDD `-5.4249`
- `market_context_high->index_4h` score `-1.8088` n `224` status `ready` deltaP `7.4259` edge `-0.0115` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-1.9155` n `224` status `ready` deltaP `6.3371` edge `0.0105` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.3673` n `224` status `ready` deltaP `-5.9125` edge `0.0733` maxDD `-9.826`
- `market_context_high->crypto_alt_4h` score `-2.7746` n `224` status `ready` deltaP `0.8275` edge `0.0173` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-2.8602` n `211` status `ready` deltaP `-4.0605` edge `-0.0804` maxDD `-4.4704`
- `market_context_high->equity_1h` score `-2.9818` n `224` status `ready` deltaP `3.0047` edge `-0.0131` maxDD `-15.7664`
- `market_context_high->crypto_major_4h` score `-3.1651` n `224` status `ready` deltaP `1.8402` edge `0.0104` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-4.0848` n `211` status `ready` deltaP `-5.0092` edge `-0.0149` maxDD `-4.7019`
- `market_context_high->equity_4h` score `-11.5904` n `224` status `ready` deltaP `4.0723` edge `-0.0713` maxDD `-66.7371`
- `market_context_high->metal_24h` score `-13.4483` n `211` status `ready` deltaP `-10.2982` edge `-0.0551` maxDD `-39.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
