# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T23:22:12.594552+00:00`
- Price records: `672`
- Market context records: `1574`
- Flow alert records: `6442`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8813`

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

- `market_context_high->metal_24h` score `13.1965` n `182` status `ready` deltaP `26.7685` edge `1.0213` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.361` n `182` status `ready` deltaP `26.9974` edge `0.9684` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.8481` n `182` status `ready` deltaP `26.7399` edge `0.7556` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0116` n `182` status `ready` deltaP `20.7799` edge `0.3044` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.7583` n `182` status `ready` deltaP `17.3668` edge `0.4301` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.8048` n `199` status `ready` deltaP `7.6825` edge `0.1253` maxDD `-5.0894`
- `market_context_high->fx_24h` score `0.2593` n `182` status `ready` deltaP `12.3626` edge `0.0441` maxDD `-1.3925`
- `market_context_high->crypto_alt_4h` score `0.1966` n `199` status `ready` deltaP `13.2545` edge `0.2688` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.0248` n `199` status `ready` deltaP `9.2796` edge `0.2122` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.3168` n `199` status `ready` deltaP `0.9674` edge `0.0553` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.6163` n `199` status `ready` deltaP `0.4642` edge `0.0264` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.6257` n `199` status `ready` deltaP `-1.9942` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6554` n `199` status `ready` deltaP `0.9238` edge `0.0024` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7096` n `199` status `ready` deltaP `5.5969` edge `0.0053` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.7352` n `199` status `ready` deltaP `-0.3475` edge `0.0002` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.8747` n `199` status `ready` deltaP `-0.4438` edge `0.0265` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.2024` n `199` status `ready` deltaP `-2.6106` edge `0.0261` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.3102` n `199` status `ready` deltaP `10.516` edge `0.0899` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3791` n `199` status `ready` deltaP `-10.3973` edge `-0.0146` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.1193` n `199` status `ready` deltaP `-13.9379` edge `-0.1007` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
