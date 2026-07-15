# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T21:22:30.336277+00:00`
- Price records: `672`
- Market context records: `6856`
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

- `market_context_high->unknown_24h` score `1.1339` n `176` status `ready` deltaP `-1.5467` edge `0.5309` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2523` n `223` status `ready` deltaP `2.169` edge `0.0017` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.5496` n `176` status `ready` deltaP `6.4079` edge `0.0983` maxDD `-5.2791`
- `market_context_high->crypto_alt_1h` score `-0.6264` n `223` status `ready` deltaP `1.5628` edge `0.0138` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.6501` n `223` status `ready` deltaP `3.5062` edge `0.0126` maxDD `-4.2122`
- `market_context_high->commodity_1h` score `-0.693` n `223` status `ready` deltaP `-2.171` edge `-0.0059` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.881` n `223` status `ready` deltaP `-2.7651` edge `-0.0034` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.9472` n `223` status `ready` deltaP `-5.4523` edge `-0.0083` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-1.0054` n `218` status `ready` deltaP `10.6917` edge `0.0062` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4323` n `218` status `ready` deltaP `-3.5019` edge `-0.0113` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6358` n `223` status `ready` deltaP `-2.7618` edge `-0.0278` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.9815` n `223` status `ready` deltaP `-0.3773` edge `-0.0335` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.0641` n `218` status `ready` deltaP `2.7662` edge `-0.0251` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.4557` n `218` status `ready` deltaP `-0.6321` edge `-0.0123` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.0899` n `218` status `ready` deltaP `-1.2041` edge `-0.0554` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.176` n `218` status `ready` deltaP `-9.1967` edge `0.0332` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-3.1818` n `218` status `ready` deltaP `-0.5972` edge `-0.0456` maxDD `-20.6678`
- `market_context_high->fx_24h` score `-4.5092` n `176` status `ready` deltaP `-9.7853` edge `-0.0069` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.6061` n `218` status `ready` deltaP `0.007` edge `-0.1807` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-9.0593` n `176` status `ready` deltaP `-18.8447` edge `-0.1873` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
