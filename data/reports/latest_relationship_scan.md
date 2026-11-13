# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T19:07:24.813810+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10554`

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

- `market_context_high->unknown_24h` score `370.358` n `75` status `ready` deltaP `2.8889` edge `30.858` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `33.9359` n `53` status `ready` deltaP `32.9731` edge `2.6788` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.7022` n `75` status `ready` deltaP `27.5139` edge `2.1126` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `17.278` n `75` status `ready` deltaP `48.4514` edge `1.3683` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.4271` n `53` status `ready` deltaP `42.0434` edge `1.7659` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.0042` n `53` status `ready` deltaP `34.7158` edge `0.7986` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.7082` n `53` status `ready` deltaP `37.1528` edge `0.228` maxDD `0.0`
- `market_context_high->index_24h` score `4.9104` n `75` status `ready` deltaP `26.257` edge `0.2433` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.8022` n `53` status `ready` deltaP `45.4815` edge `0.1346` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.2294` n `53` status `ready` deltaP `24.2695` edge `0.221` maxDD `-0.4279`
- `market_context_high->metal_24h` score `3.9941` n `75` status `ready` deltaP `40.2917` edge `0.3326` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.3755` n `53` status `ready` deltaP `17.2664` edge `0.2292` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.2331` n `53` status `ready` deltaP `29.4553` edge `0.0984` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.2165` n `53` status `ready` deltaP `19.8286` edge `0.2846` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2242` n `53` status `ready` deltaP `26.0394` edge `0.0372` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.0358` n `53` status `ready` deltaP `20.4412` edge `0.077` maxDD `-0.8235`
- `news_risk_high->crypto_alt_24h` score `2.0249` n `53` status `ready` deltaP `15.2941` edge `0.6082` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `1.8258` n `53` status `ready` deltaP `26.346` edge `0.2223` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1867` n `53` status `ready` deltaP `16.1281` edge `0.0215` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6042` n `53` status `ready` deltaP `16.8455` edge `0.0631` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
