# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T22:07:28.693638+00:00`
- Price records: `672`
- Market context records: `6752`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11724`

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

- `market_context_high->unknown_24h` score `1.1211` n `176` status `ready` deltaP `1.0574` edge `0.5119` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `-0.0099` n `176` status `ready` deltaP `7.6518` edge `0.0337` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.0788` n `176` status `ready` deltaP `5.7975` edge `0.0312` maxDD `-3.7803`
- `market_context_high->commodity_24h` score `-0.109` n `176` status `ready` deltaP `7.9704` edge `0.1246` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3726` n `176` status `ready` deltaP `0.034` edge `0.0005` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.5796` n `176` status `ready` deltaP `-0.5682` edge `0.0009` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6133` n `176` status `ready` deltaP `-0.1531` edge `-0.0093` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.702` n `176` status `ready` deltaP `-5.1409` edge `-0.0032` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.104` n `176` status `ready` deltaP `3.5554` edge `-0.013` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.2089` n `176` status `ready` deltaP `6.7489` edge `-0.012` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2177` n `176` status `ready` deltaP `7.5388` edge `0.0` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4376` n `176` status `ready` deltaP `-1.7738` edge `-0.0235` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7273` n `176` status `ready` deltaP `-7.1754` edge `-0.006` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.4201` n `176` status `ready` deltaP `4.5732` edge `-0.0093` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.5166` n `176` status `ready` deltaP `3.7416` edge `-0.0074` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.6503` n `176` status `ready` deltaP `-6.3193` edge `-0.0116` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-3.6607` n `176` status `ready` deltaP `-16.02` edge `0.0383` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.1112` n `176` status `ready` deltaP `3.7694` edge `-0.1253` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.2475` n `176` status `ready` deltaP `-7.3548` edge `-0.0013` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-8.2869` n `176` status `ready` deltaP `-12.4211` edge `-0.1311` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
