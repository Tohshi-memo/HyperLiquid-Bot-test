# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T06:22:28.994966+00:00`
- Price records: `672`
- Market context records: `2636`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `7.4973` n `140` status `ready` deltaP `18.0903` edge `0.537` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.0885` n `140` status `ready` deltaP `24.7256` edge `0.5271` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.3833` n `140` status `ready` deltaP `14.1812` edge `0.3684` maxDD `-10.1468`
- `market_context_high->crypto_alt_24h` score `1.8913` n `140` status `ready` deltaP `4.9603` edge `0.709` maxDD `-36.7566`
- `market_context_high->index_24h` score `1.2821` n `140` status `ready` deltaP `11.5377` edge `0.128` maxDD `-2.5127`
- `market_context_high->crypto_alt_1h` score `1.2188` n `140` status `ready` deltaP `10.5304` edge `0.1501` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.0635` n `140` status `ready` deltaP `7.1994` edge `0.1456` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.6493` n `140` status `ready` deltaP `7.7887` edge `0.1216` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.4075` n `140` status `ready` deltaP `9.9608` edge `0.0517` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1469` n `140` status `ready` deltaP `3.1352` edge `0.021` maxDD `-1.665`
- `market_context_high->index_1h` score `-0.2268` n `140` status `ready` deltaP `2.9855` edge `0.0106` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.3221` n `140` status `ready` deltaP `6.0137` edge `0.0209` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.4557` n `140` status `ready` deltaP `0.1839` edge `0.0054` maxDD `-2.2038`
- `market_context_high->metal_4h` score `-0.5102` n `140` status `ready` deltaP `3.297` edge `0.0298` maxDD `-3.2105`
- `market_context_high->fx_1h` score `-0.5574` n `140` status `ready` deltaP `-0.7827` edge `0.0034` maxDD `-0.2373`
- `market_context_high->fx_24h` score `-0.8945` n `140` status `ready` deltaP `3.2292` edge `-0.0023` maxDD `-1.1685`
- `market_context_high->commodity_4h` score `-0.928` n `140` status `ready` deltaP `5.1132` edge `0.0412` maxDD `-10.2078`
- `market_context_high->fx_4h` score `-0.9821` n `140` status `ready` deltaP `-1.372` edge `0.0104` maxDD `-0.6474`
- `market_context_high->equity_1h` score `-1.092` n `140` status `ready` deltaP `-2.887` edge `0.0121` maxDD `-2.7085`
- `market_context_high->equity_4h` score `-1.3477` n `140` status `ready` deltaP `1.9555` edge `0.0151` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
