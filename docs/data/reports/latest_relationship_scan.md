# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T20:37:26.500881+00:00`
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

- `market_context_high->unknown_24h` score `576.4449` n `66` status `ready` deltaP `4.1667` edge `48.0093` maxDD `0.0`
- `news_risk_high->equity_24h` score `40.4893` n `53` status `ready` deltaP `43.9106` edge `3.152` maxDD `-3.6503`
- `market_context_high->equity_24h` score `36.7356` n `66` status `ready` deltaP `38.9363` edge `2.9559` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `25.9022` n `66` status `ready` deltaP `57.7652` edge `1.8811` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `18.781` n `53` status `ready` deltaP `42.9114` edge `2.3183` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.5801` n `53` status `ready` deltaP `37.4597` edge `0.8283` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.3619` n `53` status `ready` deltaP `51.3889` edge `0.2709` maxDD `0.0`
- `market_context_high->index_24h` score `7.2152` n `66` status `ready` deltaP `42.077` edge `0.3299` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.8572` n `53` status `ready` deltaP `38.332` edge `0.2629` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.3226` n `66` status `ready` deltaP `51.5152` edge `0.4281` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.0062` n `53` status `ready` deltaP `21.2006` edge `0.4246` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `4.9371` n `53` status `ready` deltaP `45.9388` edge `0.1428` maxDD `-1.0104`
- `news_risk_high->crypto_alt_24h` score `3.9953` n `53` status `ready` deltaP `14.4261` edge `0.8666` maxDD `-29.0448`
- `news_risk_high->equity_1h` score `3.7542` n `53` status `ready` deltaP `20.1107` edge `0.2418` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6177` n `53` status `ready` deltaP `33.7236` edge `0.102` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.8984` n `53` status `ready` deltaP `27.4131` edge `0.3527` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.4682` n `53` status `ready` deltaP `25.4717` edge `0.0795` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2709` n `53` status `ready` deltaP `26.3388` edge `0.0391` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3903` n `53` status `ready` deltaP `18.5233` edge `0.0225` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.0329` n `53` status `ready` deltaP `19.2407` edge `0.1021` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
