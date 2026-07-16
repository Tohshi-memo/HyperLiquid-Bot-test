# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T14:07:28.828714+00:00`
- Price records: `672`
- Market context records: `6925`
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

- `market_context_high->fx_1h` score `-0.195` n `224` status `ready` deltaP `3.1357` edge `0.0026` maxDD `-0.5468`
- `market_context_high->unknown_24h` score `-0.3899` n `206` status `ready` deltaP `-5.2868` edge `0.3869` maxDD `-14.4643`
- `market_context_high->crypto_alt_1h` score `-0.4115` n `224` status `ready` deltaP `2.9593` edge `0.0224` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4795` n `224` status `ready` deltaP `4.4456` edge `0.0208` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6331` n `224` status `ready` deltaP `-0.7485` edge `-0.0077` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.702` n `224` status `ready` deltaP `0.1684` edge `0.0` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7451` n `224` status `ready` deltaP `-2.6465` edge `-0.0011` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.7726` n `224` status `ready` deltaP `14.6124` edge `0.0099` maxDD `-2.1765`
- `market_context_high->unknown_1h` score `-1.5115` n `224` status `ready` deltaP `-2.0637` edge `-0.0221` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.5453` n `224` status `ready` deltaP `-3.5606` edge `-0.0254` maxDD `-5.5853`
- `market_context_high->equity_1h` score `-1.5611` n `224` status `ready` deltaP `4.0312` edge `-0.009` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.7168` n `224` status `ready` deltaP `7.6002` edge `-0.0128` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-1.9734` n `224` status `ready` deltaP `4.7583` edge `0.0136` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.7092` n `224` status `ready` deltaP `2.0579` edge `-0.0027` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.7548` n `224` status `ready` deltaP `0.0653` edge `-0.0209` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-2.9331` n `224` status `ready` deltaP `-7.3606` edge `0.0412` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.0312` n `206` status `ready` deltaP `-2.7865` edge `-0.0472` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.0396` n `206` status `ready` deltaP `-4.0054` edge `-0.0063` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.7085` n `224` status `ready` deltaP `4.9978` edge `-0.0989` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.4654` n `206` status `ready` deltaP `-11.9475` edge `-0.113` maxDD `-31.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
