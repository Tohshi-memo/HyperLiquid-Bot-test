# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T01:22:31.679092+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9354`

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

- `market_context_high->unknown_24h` score `565.5192` n `66` status `ready` deltaP `2.4306` edge `47.1104` maxDD `0.0`
- `news_risk_high->equity_24h` score `41.115` n `53` status `ready` deltaP `44.9522` edge `3.1972` maxDD `-3.6503`
- `market_context_high->equity_24h` score `37.3614` n `66` status `ready` deltaP `39.9779` edge `3.0011` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `28.4534` n `66` status `ready` deltaP `57.7652` edge `2.0937` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `20.5832` n `53` status `ready` deltaP `43.0851` edge `2.5482` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.8643` n `53` status `ready` deltaP `39.1365` edge `0.8408` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.2956` n `53` status `ready` deltaP `50.6944` edge `0.27` maxDD `0.0`
- `market_context_high->index_24h` score `7.2404` n `66` status `ready` deltaP `42.077` edge `0.332` maxDD `-0.0653`
- `news_risk_high->crypto_major_4h` score `6.1292` n `53` status `ready` deltaP `22.8774` edge `0.507` maxDD `-9.2335`
- `news_risk_high->index_24h` score `5.8824` n `53` status `ready` deltaP `38.332` edge `0.265` maxDD `-0.4279`
- `news_risk_high->crypto_alt_24h` score `5.6535` n `53` status `ready` deltaP `14.4261` edge `1.0792` maxDD `-29.0448`
- `market_context_high->metal_24h` score `5.5031` n `66` status `ready` deltaP `52.5568` edge `0.4443` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `5.0639` n `53` status `ready` deltaP `46.5486` edge `0.1493` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.8345` n `53` status `ready` deltaP `20.7095` edge `0.2445` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.4366` n `53` status `ready` deltaP `31.8943` edge `0.0991` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `3.4144` n `53` status `ready` deltaP `27.8704` edge `0.4158` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.5096` n `53` status `ready` deltaP `25.929` edge `0.0799` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2793` n `53` status `ready` deltaP `26.1891` edge `0.0408` maxDD `-0.3692`
- `market_context_high->crypto_major_24h` score `1.6669` n `66` status `ready` deltaP `12.6105` edge `1.0874` maxDD `-76.2717`
- `news_risk_high->index_1h` score `1.4155` n `53` status `ready` deltaP `18.8227` edge `0.0226` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
