# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T22:07:25.747978+00:00`
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

- `market_context_high->unknown_24h` score `576.3313` n `66` status `ready` deltaP `3.6458` edge `48.0033` maxDD `0.0`
- `news_risk_high->equity_24h` score `40.8311` n `53` status `ready` deltaP `44.7786` edge `3.1747` maxDD `-3.6503`
- `market_context_high->equity_24h` score `37.0775` n `66` status `ready` deltaP `39.8043` edge `2.9786` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `26.8862` n `66` status `ready` deltaP `57.7652` edge `1.9631` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `19.4717` n `53` status `ready` deltaP `43.0851` edge `2.4057` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.6961` n `53` status `ready` deltaP `38.0694` edge `0.8339` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.3643` n `53` status `ready` deltaP `51.3889` edge `0.2711` maxDD `0.0`
- `market_context_high->index_24h` score `7.2308` n `66` status `ready` deltaP `42.077` edge `0.3312` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.8728` n `53` status `ready` deltaP `38.332` edge `0.2642` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `5.4238` n `53` status `ready` deltaP `22.1152` edge `0.4533` maxDD `-9.2335`
- `market_context_high->metal_24h` score `5.3624` n `66` status `ready` deltaP `51.5152` edge `0.4332` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `5.0207` n `53` status `ready` deltaP `46.5486` edge `0.1457` maxDD `-1.0104`
- `news_risk_high->crypto_alt_24h` score `4.6349` n `53` status `ready` deltaP `14.4261` edge `0.9486` maxDD `-29.0448`
- `news_risk_high->equity_1h` score `3.7782` n `53` status `ready` deltaP `20.1107` edge `0.2438` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.5727` n `53` status `ready` deltaP `33.2662` edge `0.1013` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `3.1726` n `53` status `ready` deltaP `27.8704` edge `0.3848` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.5206` n `53` status `ready` deltaP `26.0815` edge `0.0798` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2913` n `53` status `ready` deltaP `26.3388` edge `0.0408` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4035` n `53` status `ready` deltaP `18.673` edge `0.0226` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.1483` n `53` status `ready` deltaP `19.6898` edge `0.1139` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
