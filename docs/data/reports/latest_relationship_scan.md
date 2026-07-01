# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T13:37:27.801116+00:00`
- Price records: `672`
- Market context records: `5356`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11494`

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

- `market_context_high->unknown_24h` score `13.4198` n `165` status `ready` deltaP `18.6711` edge `1.007` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `5.301` n `165` status `ready` deltaP `21.8813` edge `0.7499` maxDD `-29.6555`
- `market_context_high->equity_24h` score `4.2147` n `165` status `ready` deltaP `17.1306` edge `0.7999` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.4895` n `194` status `ready` deltaP `13.3361` edge `0.3478` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.1148` n `194` status `ready` deltaP `9.9022` edge `0.2743` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.6366` n `194` status `ready` deltaP `9.7875` edge `0.235` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.7603` n `165` status `ready` deltaP `23.6805` edge `0.1031` maxDD `-7.413`
- `market_context_high->fx_24h` score `0.1564` n `165` status `ready` deltaP `9.7601` edge `0.0375` maxDD `-0.8294`
- `market_context_high->equity_1h` score `-0.0159` n `201` status `ready` deltaP `5.6551` edge `0.0575` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `-0.0644` n `201` status `ready` deltaP `4.0925` edge `0.0919` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.1084` n `201` status `ready` deltaP `1.5476` edge `0.0768` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.1328` n `201` status `ready` deltaP `4.4709` edge `0.0095` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.4172` n `194` status `ready` deltaP `5.6119` edge `0.025` maxDD `-2.9391`
- `market_context_high->fx_1h` score `-0.4654` n `201` status `ready` deltaP `-1.3979` edge `-0.0014` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.4679` n `201` status `ready` deltaP `0.6494` edge `0.0032` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.6842` n `194` status `ready` deltaP `1.8308` edge `0.003` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.1893` n `194` status `ready` deltaP `8.0604` edge `-0.0346` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.5413` n `201` status `ready` deltaP `-4.0836` edge `-0.0079` maxDD `-3.4655`
- `market_context_high->metal_4h` score `-2.717` n `194` status `ready` deltaP `-8.2914` edge `-0.0406` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.7697` n `165` status `ready` deltaP `11.673` edge `0.3086` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
