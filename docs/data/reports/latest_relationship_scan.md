# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T21:22:25.084337+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9210`

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

- `market_context_high->unknown_24h` score `576.365` n `66` status `ready` deltaP `3.9931` edge `48.0038` maxDD `0.0`
- `news_risk_high->equity_24h` score `40.6858` n `53` status `ready` deltaP `44.4314` edge `3.1649` maxDD `-3.6503`
- `market_context_high->equity_24h` score `36.9321` n `66` status `ready` deltaP `39.4571` edge `2.9688` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `26.3714` n `66` status `ready` deltaP `57.7652` edge `1.9202` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `19.1078` n `53` status `ready` deltaP `42.9114` edge `2.3602` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.6223` n `53` status `ready` deltaP `37.6121` edge `0.8308` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.3619` n `53` status `ready` deltaP `51.3889` edge `0.2709` maxDD `0.0`
- `market_context_high->index_24h` score `7.2248` n `66` status `ready` deltaP `42.077` edge `0.3307` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.8668` n `53` status `ready` deltaP `38.332` edge `0.2637` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.3429` n `66` status `ready` deltaP `51.5152` edge `0.4307` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.158` n `53` status `ready` deltaP `21.6579` edge `0.4342` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `4.9649` n `53` status `ready` deltaP `46.0913` edge `0.1441` maxDD `-1.0104`
- `news_risk_high->crypto_alt_24h` score `4.3002` n `53` status `ready` deltaP `14.4261` edge `0.9057` maxDD `-29.0448`
- `news_risk_high->equity_1h` score `3.7758` n `53` status `ready` deltaP `20.1107` edge `0.2436` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.5885` n `53` status `ready` deltaP `33.4187` edge `0.1016` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.9975` n `53` status `ready` deltaP `27.4131` edge `0.3654` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.495` n `53` status `ready` deltaP `25.7766` edge `0.0797` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2853` n `53` status `ready` deltaP `26.3388` edge `0.0403` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4035` n `53` status `ready` deltaP `18.673` edge `0.0226` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.0774` n `53` status `ready` deltaP `19.2407` edge `0.1078` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
