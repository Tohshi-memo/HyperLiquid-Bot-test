# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T00:22:26.321190+00:00`
- Price records: `672`
- Market context records: `6867`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11786`

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

- `market_context_high->unknown_24h` score `1.1752` n `176` status `ready` deltaP `-2.1467` edge `0.5402` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2487` n `224` status `ready` deltaP `2.2375` edge `0.0017` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.6112` n `224` status `ready` deltaP `-0.8982` edge `-0.0039` maxDD `-2.1443`
- `market_context_high->crypto_alt_1h` score `-0.6656` n `224` status `ready` deltaP `1.3126` edge `0.0122` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.6916` n `224` status `ready` deltaP `3.0983` edge `0.0121` maxDD `-4.2314`
- `market_context_high->index_1h` score `-0.867` n `224` status `ready` deltaP `-2.5262` edge `-0.0032` maxDD `-2.2895`
- `market_context_high->commodity_24h` score `-0.9332` n `176` status `ready` deltaP `4.7789` edge `0.0772` maxDD `-5.2791`
- `market_context_high->metal_1h` score `-0.9655` n `224` status `ready` deltaP `-5.7902` edge `-0.0084` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9835` n `223` status `ready` deltaP `11.1282` edge `0.0061` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.3298` n `223` status `ready` deltaP `-2.1759` edge `-0.007` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7117` n `224` status `ready` deltaP `-3.8601` edge `-0.0268` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.9211` n `224` status `ready` deltaP `0.2887` edge `-0.0302` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.0331` n `223` status `ready` deltaP `3.2134` edge `-0.0241` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.4419` n `223` status `ready` deltaP `-0.3215` edge `-0.0126` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.1524` n `223` status `ready` deltaP `-1.8961` edge `-0.0588` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.1873` n `223` status `ready` deltaP `-9.5781` edge `0.0348` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-3.1904` n `223` status `ready` deltaP `-0.8225` edge `-0.0452` maxDD `-20.6678`
- `market_context_high->fx_24h` score `-4.5426` n `176` status `ready` deltaP `-9.7083` edge `-0.0102` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.4961` n `223` status `ready` deltaP `0.4279` edge `-0.1694` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.9722` n `176` status `ready` deltaP `-18.7599` edge `-0.1767` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
