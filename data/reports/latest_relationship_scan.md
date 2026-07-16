# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T15:07:39.552170+00:00`
- Price records: `672`
- Market context records: `6929`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11706`

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

- `market_context_high->fx_1h` score `-0.2019` n `227` status `ready` deltaP `3.0474` edge `0.0023` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4144` n `227` status `ready` deltaP `2.9531` edge `0.0222` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.501` n `227` status `ready` deltaP `4.2662` edge `0.0202` maxDD `-4.2314`
- `market_context_high->unknown_24h` score `-0.5967` n `210` status `ready` deltaP `-6.1929` edge `0.368` maxDD `-14.5906`
- `market_context_high->index_1h` score `-0.7141` n `227` status `ready` deltaP `-0.0191` edge `-0.0003` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7526` n `227` status `ready` deltaP `-2.7606` edge `-0.0013` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.8051` n `224` status `ready` deltaP `14.0027` edge `0.0098` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.0592` n `227` status `ready` deltaP `-1.4093` edge `-0.0104` maxDD `-2.1443`
- `market_context_high->unknown_1h` score `-1.5314` n `227` status `ready` deltaP `-2.0721` edge `-0.0237` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.5916` n `224` status `ready` deltaP `-3.8655` edge `-0.0293` maxDD `-5.5853`
- `market_context_high->equity_1h` score `-1.6373` n `227` status `ready` deltaP `3.3468` edge `-0.0142` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.6773` n `224` status `ready` deltaP `8.21` edge `-0.0118` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-1.9332` n `224` status `ready` deltaP `5.2156` edge `0.0157` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.7461` n `224` status `ready` deltaP `1.753` edge `-0.0054` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.7706` n `224` status `ready` deltaP `-0.0871` edge `-0.0219` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-2.9889` n `224` status `ready` deltaP `-7.818` edge `0.0396` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.1163` n `210` status `ready` deltaP `-2.7399` edge `-0.0546` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.0971` n `210` status `ready` deltaP `-4.5441` edge `-0.0075` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.6051` n `224` status `ready` deltaP `5.6076` edge `-0.0897` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.7004` n `210` status `ready` deltaP `-12.5485` edge `-0.1169` maxDD `-32.8574`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
