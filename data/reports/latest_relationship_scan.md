# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T22:37:26.886946+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11760`

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

- `market_context_high->unknown_24h` score `310.1125` n `84` status `ready` deltaP `6.2996` edge `25.8148` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `75.891` n `94` status `ready` deltaP `8.1053` edge `6.315` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `29.6363` n `53` status `ready` deltaP `24.8133` edge `2.3749` maxDD `-3.6503`
- `market_context_high->equity_24h` score `21.6189` n `84` status `ready` deltaP `22.5446` edge `1.7219` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.7903` n `53` status `ready` deltaP `37.3559` edge `1.4591` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.2317` n `53` status `ready` deltaP `32.7341` edge `0.6641` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `8.7733` n `84` status `ready` deltaP `42.6092` edge `1.2503` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.2887` n `53` status `ready` deltaP `43.2292` edge `0.3192` maxDD `0.0`
- `market_context_high->metal_24h` score `6.3431` n `84` status `ready` deltaP `38.8641` edge `0.3108` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.6202` n `53` status `ready` deltaP `43.9571` edge `0.1296` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.2535` n `84` status `ready` deltaP `24.504` edge `0.2006` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.8452` n `53` status `ready` deltaP `22.707` edge `0.1994` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.0203` n `53` status `ready` deltaP `17.1167` edge `0.2006` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9211` n `53` status `ready` deltaP `26.7114` edge `0.0907` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.6823` n `53` status `ready` deltaP `19.6762` edge `0.2411` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.1942` n `53` status `ready` deltaP `25.8897` edge `0.0357` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6535` n `53` status `ready` deltaP `18.0022` edge `0.0614` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.3391` n `53` status `ready` deltaP `24.5168` edge `0.1721` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.3357` n `53` status `ready` deltaP `12.69` edge `0.5372` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.1543` n `53` status `ready` deltaP `16.2778` edge `0.0178` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
