# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T13:07:32.626653+00:00`
- Price records: `672`
- Market context records: `6921`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

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

- `market_context_high->fx_1h` score `-0.1701` n `224` status `ready` deltaP `3.5848` edge `0.0028` maxDD `-0.5468`
- `market_context_high->unknown_24h` score `-0.2539` n `203` status `ready` deltaP `-4.757` edge `0.4008` maxDD `-14.4643`
- `market_context_high->crypto_alt_1h` score `-0.3539` n `224` status `ready` deltaP `3.2587` edge `0.0252` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4195` n `224` status `ready` deltaP `4.8947` edge `0.0228` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6315` n `224` status `ready` deltaP `-0.8982` edge `-0.0065` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.7043` n `224` status `ready` deltaP `0.1684` edge `-0.0003` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.7465` n `224` status `ready` deltaP `15.0697` edge `0.0102` maxDD `-2.1765`
- `market_context_high->metal_1h` score `-0.7661` n `224` status `ready` deltaP `-2.9459` edge `-0.0018` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.459` n `224` status `ready` deltaP `-2.9508` edge `-0.0184` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5223` n `224` status `ready` deltaP `-2.2134` edge `-0.022` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.6173` n `224` status `ready` deltaP `3.5821` edge `-0.0132` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.7634` n `224` status `ready` deltaP `6.9905` edge `-0.0147` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.034` n `224` status `ready` deltaP `4.1485` edge `0.0099` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.6447` n `224` status `ready` deltaP `2.6677` edge `0.0015` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.7312` n `224` status `ready` deltaP `0.3702` edge `-0.0199` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-2.9051` n `224` status `ready` deltaP `-7.0558` edge `0.0415` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-2.9352` n `203` status `ready` deltaP `-2.6671` edge `-0.04` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.0477` n `203` status `ready` deltaP `-4.1372` edge `-0.0061` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.8245` n `224` status `ready` deltaP `4.3881` edge `-0.1097` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.2779` n `203` status `ready` deltaP `-11.6545` edge `-0.1107` maxDD `-29.4965`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
