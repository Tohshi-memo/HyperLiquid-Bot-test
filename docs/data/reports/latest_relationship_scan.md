# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T17:07:26.925156+00:00`
- Price records: `672`
- Market context records: `6836`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11754`

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

- `market_context_high->unknown_24h` score `0.9552` n `176` status `ready` deltaP `-1.5467` edge `0.508` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.1137` n `176` status `ready` deltaP `9.3592` edge `0.1339` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.297` n `214` status `ready` deltaP `1.3837` edge `0.0012` maxDD `-0.5468`
- `market_context_high->crypto_major_1h` score `-0.5151` n `214` status `ready` deltaP `4.3693` edge `0.0181` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.5394` n `214` status `ready` deltaP `2.2008` edge `0.0168` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.9081` n `214` status `ready` deltaP `-2.9716` edge `-0.0055` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-1.0321` n `214` status `ready` deltaP `-6.6512` edge `-0.0112` maxDD `-2.1427`
- `market_context_high->commodity_1h` score `-1.1049` n `214` status `ready` deltaP `-2.5813` edge `-0.0064` maxDD `-2.1443`
- `market_context_high->fx_4h` score `-1.1065` n `203` status `ready` deltaP `9.1824` edge `0.0033` maxDD `-2.1765`
- `market_context_high->unknown_1h` score `-1.6079` n `214` status `ready` deltaP `-3.3438` edge `-0.0216` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-2.036` n `214` status `ready` deltaP `-0.3763` edge `-0.0405` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.2055` n `203` status `ready` deltaP `0.6345` edge `-0.0354` maxDD `-10.7939`
- `market_context_high->commodity_4h` score `-2.3508` n `203` status `ready` deltaP `-4.7729` edge `-0.0151` maxDD `-5.5853`
- `market_context_high->metal_4h` score `-2.7217` n `203` status `ready` deltaP `-3.3912` edge `-0.028` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.9021` n `203` status `ready` deltaP `0.3537` edge `-0.0417` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.0944` n `203` status `ready` deltaP `0.3649` edge `-0.0408` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.2187` n `203` status `ready` deltaP `-9.7599` edge `0.0334` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4552` n `176` status `ready` deltaP `-9.7853` edge `-0.0024` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.5717` n `203` status `ready` deltaP `-1.6296` edge `-0.218` maxDD `-52.3497`
- `market_context_high->metal_24h` score `-9.3157` n `176` status `ready` deltaP `-19.3656` edge `-0.2167` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
