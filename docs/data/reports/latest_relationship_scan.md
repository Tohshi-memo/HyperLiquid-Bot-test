# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T20:52:27.881591+00:00`
- Price records: `672`
- Market context records: `6853`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11809`

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

- `market_context_high->unknown_24h` score `1.1136` n `176` status `ready` deltaP `-1.5467` edge `0.5283` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2359` n `223` status `ready` deltaP `2.4684` edge `0.0018` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.4703` n `176` status `ready` deltaP `6.7551` edge `0.1026` maxDD `-5.2791`
- `market_context_high->crypto_alt_1h` score `-0.6` n `223` status `ready` deltaP `1.7125` edge `0.015` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.607` n `223` status `ready` deltaP `3.8056` edge `0.0142` maxDD `-4.2122`
- `market_context_high->commodity_1h` score `-0.6914` n `223` status `ready` deltaP `-2.171` edge `-0.0057` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.8888` n `223` status `ready` deltaP `-2.9148` edge `-0.0034` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.9557` n `223` status `ready` deltaP `-5.602` edge `-0.0084` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-1.0111` n `216` status `ready` deltaP `10.5974` edge `0.0061` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.469` n `216` status `ready` deltaP `-3.9521` edge `-0.013` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6166` n `223` status `ready` deltaP `-2.6121` edge `-0.0272` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.9924` n `223` status `ready` deltaP `-0.527` edge `-0.0339` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.0853` n `216` status `ready` deltaP `2.5237` edge `-0.0262` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.4941` n `216` status `ready` deltaP `-1.0106` edge `-0.0147` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.0424` n `216` status `ready` deltaP `-0.6944` edge `-0.0527` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.1648` n `216` status `ready` deltaP `-9.1915` edge `0.0341` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-3.1795` n `216` status `ready` deltaP `-0.717` edge `-0.0445` maxDD `-20.6678`
- `market_context_high->fx_24h` score `-4.502` n `176` status `ready` deltaP `-9.7853` edge `-0.0063` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.6751` n `216` status `ready` deltaP `-0.4347` edge `-0.1866` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-9.0804` n `176` status `ready` deltaP `-18.8447` edge `-0.19` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
