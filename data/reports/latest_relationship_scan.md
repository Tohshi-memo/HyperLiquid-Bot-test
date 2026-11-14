# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T19:52:26.330683+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9384`

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

- `market_context_high->unknown_24h` score `576.5819` n `66` status `ready` deltaP `4.5139` edge `48.0184` maxDD `0.0`
- `news_risk_high->equity_24h` score `40.2904` n `53` status `ready` deltaP `43.3897` edge `3.1389` maxDD `-3.6503`
- `market_context_high->equity_24h` score `36.5368` n `66` status `ready` deltaP `38.4154` edge `2.9428` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `25.4798` n `66` status `ready` deltaP `57.7652` edge `1.8459` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `18.4932` n `53` status `ready` deltaP `42.9114` edge `2.2814` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.5619` n `53` status `ready` deltaP `37.3072` edge `0.8278` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.3667` n `53` status `ready` deltaP `51.3889` edge `0.2713` maxDD `0.0`
- `market_context_high->index_24h` score `7.1615` n `66` status `ready` deltaP `41.5561` edge `0.3289` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.8035` n `53` status `ready` deltaP `37.8111` edge `0.2619` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.3117` n `66` status `ready` deltaP `51.5152` edge `0.4267` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.9364` n `53` status `ready` deltaP `21.0481` edge `0.4198` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `4.9226` n `53` status `ready` deltaP `45.7864` edge `0.1426` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.7662` n `53` status `ready` deltaP `20.2604` edge `0.2418` maxDD `-3.7082`
- `news_risk_high->crypto_alt_24h` score `3.7207` n `53` status `ready` deltaP `14.4261` edge `0.8314` maxDD `-29.0448`
- `news_risk_high->commodity_4h` score `3.6165` n `53` status `ready` deltaP `33.7236` edge `0.1019` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.832` n `53` status `ready` deltaP `27.2607` edge `0.3452` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.4938` n `53` status `ready` deltaP `25.7766` edge `0.0796` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2685` n `53` status `ready` deltaP `26.3388` edge `0.0389` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3903` n `53` status `ready` deltaP `18.5233` edge `0.0225` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.0064` n `53` status `ready` deltaP `19.2407` edge `0.0987` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
