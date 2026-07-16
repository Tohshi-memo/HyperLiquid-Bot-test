# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T13:37:32.257303+00:00`
- Price records: `672`
- Market context records: `6923`
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

- `market_context_high->fx_1h` score `-0.1786` n `224` status `ready` deltaP `3.4351` edge `0.0027` maxDD `-0.5468`
- `market_context_high->unknown_24h` score `-0.2923` n `204` status `ready` deltaP `-4.8204` edge `0.3963` maxDD `-14.4643`
- `market_context_high->crypto_alt_1h` score `-0.3827` n `224` status `ready` deltaP `3.109` edge `0.0238` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4567` n `224` status `ready` deltaP `4.5953` edge `0.0217` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6268` n `224` status `ready` deltaP `-0.7485` edge `-0.0069` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.7035` n `224` status `ready` deltaP `0.1684` edge `-0.0002` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7475` n `224` status `ready` deltaP `-2.6465` edge `-0.0014` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.7552` n `224` status `ready` deltaP `14.9173` edge `0.0101` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.5037` n `224` status `ready` deltaP `-3.2557` edge `-0.0221` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5115` n `224` status `ready` deltaP `-2.0637` edge `-0.0221` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.6032` n `224` status `ready` deltaP `3.7318` edge `-0.0124` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.7389` n `224` status `ready` deltaP `7.2953` edge `-0.0136` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.0033` n `224` status `ready` deltaP `4.4534` edge `0.0118` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.6738` n `224` status `ready` deltaP `2.3628` edge `-0.0002` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.7327` n `224` status `ready` deltaP `0.3702` edge `-0.0201` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-2.9027` n `224` status `ready` deltaP `-7.0558` edge `0.0417` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-2.9871` n `204` status `ready` deltaP `-2.8206` edge `-0.0433` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.0544` n `204` status `ready` deltaP `-4.2061` edge `-0.0062` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.7657` n `224` status `ready` deltaP `4.693` edge `-0.1042` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.3265` n `204` status `ready` deltaP `-11.6382` edge `-0.1107` maxDD `-30.0039`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
