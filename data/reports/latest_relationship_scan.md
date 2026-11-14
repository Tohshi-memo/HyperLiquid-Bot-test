# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T20:52:36.752130+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9180`

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

- `market_context_high->unknown_24h` score `576.4065` n `66` status `ready` deltaP `4.1667` edge `48.0061` maxDD `0.0`
- `news_risk_high->equity_24h` score `40.5608` n `53` status `ready` deltaP `44.0842` edge `3.1568` maxDD `-3.6503`
- `market_context_high->equity_24h` score `36.8071` n `66` status `ready` deltaP `39.1099` edge `2.9607` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `26.0486` n `66` status `ready` deltaP `57.7652` edge `1.8933` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `18.8847` n `53` status `ready` deltaP `42.9114` edge `2.3316` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.5983` n `53` status `ready` deltaP `37.6121` edge `0.8288` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.3607` n `53` status `ready` deltaP `51.3889` edge `0.2708` maxDD `0.0`
- `market_context_high->index_24h` score `7.22` n `66` status `ready` deltaP `42.077` edge `0.3303` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.862` n `53` status `ready` deltaP `38.332` edge `0.2633` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.3273` n `66` status `ready` deltaP `51.5152` edge `0.4287` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.0472` n `53` status `ready` deltaP `21.353` edge `0.427` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `4.9395` n `53` status `ready` deltaP `45.9388` edge `0.143` maxDD `-1.0104`
- `news_risk_high->crypto_alt_24h` score `4.0904` n `53` status `ready` deltaP `14.4261` edge `0.8788` maxDD `-29.0448`
- `news_risk_high->equity_1h` score `3.759` n `53` status `ready` deltaP `20.1107` edge `0.2422` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6043` n `53` status `ready` deltaP `33.5711` edge `0.1019` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.9234` n `53` status `ready` deltaP `27.4131` edge `0.3559` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.4682` n `53` status `ready` deltaP `25.4717` edge `0.0795` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2733` n `53` status `ready` deltaP `26.3388` edge `0.0393` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4023` n `53` status `ready` deltaP `18.673` edge `0.0225` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.0423` n `53` status `ready` deltaP `19.2407` edge `0.1033` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
