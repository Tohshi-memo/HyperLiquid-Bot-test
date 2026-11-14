# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T20:22:27.502781+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9390`

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

- `market_context_high->unknown_24h` score `576.5032` n `66` status `ready` deltaP `4.3403` edge `48.013` maxDD `0.0`
- `news_risk_high->equity_24h` score `40.4214` n `53` status `ready` deltaP `43.7369` edge `3.1475` maxDD `-3.6503`
- `market_context_high->equity_24h` score `36.6677` n `66` status `ready` deltaP `38.7626` edge `2.9514` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `25.7558` n `66` status `ready` deltaP `57.7652` edge `1.8689` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `18.6804` n `53` status `ready` deltaP `42.9114` edge `2.3054` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.5643` n `53` status `ready` deltaP `37.3072` edge `0.828` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.3643` n `53` status `ready` deltaP `51.3889` edge `0.2711` maxDD `0.0`
- `market_context_high->index_24h` score `7.1977` n `66` status `ready` deltaP `41.9034` edge `0.3296` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.8397` n `53` status `ready` deltaP `38.1584` edge `0.2626` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.3179` n `66` status `ready` deltaP `51.5152` edge `0.4275` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.9688` n `53` status `ready` deltaP `21.0481` edge `0.4225` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `4.9226` n `53` status `ready` deltaP `45.7864` edge `0.1426` maxDD `-1.0104`
- `news_risk_high->crypto_alt_24h` score `3.9001` n `53` status `ready` deltaP `14.4261` edge `0.8544` maxDD `-29.0448`
- `news_risk_high->equity_1h` score `3.753` n `53` status `ready` deltaP `20.1107` edge `0.2417` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6311` n `53` status `ready` deltaP `33.876` edge `0.1021` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.8671` n `53` status `ready` deltaP `27.2607` edge `0.3497` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.4816` n `53` status `ready` deltaP `25.6241` edge `0.0796` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2697` n `53` status `ready` deltaP `26.3388` edge `0.039` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3903` n `53` status `ready` deltaP `18.5233` edge `0.0225` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.0251` n `53` status `ready` deltaP `19.2407` edge `0.1011` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
