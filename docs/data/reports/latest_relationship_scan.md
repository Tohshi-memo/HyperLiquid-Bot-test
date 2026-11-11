# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T14:22:25.875788+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11758`

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

- `market_context_high->unknown_4h` score `76.0086` n `88` status `ready` deltaP `8.1347` edge `6.3246` maxDD `-0.9161`
- `market_context_high->equity_24h` score `30.4064` n `88` status `ready` deltaP `26.3573` edge `2.5973` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.7278` n `53` status `ready` deltaP `35.478` edge `0.853` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `9.2607` n `88` status `ready` deltaP `39.0151` edge `1.4366` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.4612` n `88` status `ready` deltaP `26.4678` edge `0.3249` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.2949` n `88` status `ready` deltaP `31.2026` edge `0.2052` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.6615` n `53` status `ready` deltaP `19.6762` edge `0.3227` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5814` n `53` status `ready` deltaP `18.1646` edge `0.2486` maxDD `-3.6997`
- `news_risk_high->metal_4h` score `3.5653` n `53` status `ready` deltaP `36.3352` edge `0.0925` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `2.9772` n `53` status `ready` deltaP `25.4919` edge `0.1035` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.3217` n `53` status `ready` deltaP `21.6607` edge `0.0927` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8905` n `53` status `ready` deltaP `23.4497` edge `0.2499` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.697` n `53` status `ready` deltaP `21.0993` edge `0.0262` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3425` n `53` status `ready` deltaP `17.4754` edge `0.0255` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6221` n `53` status `ready` deltaP `17.594` edge `0.0604` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6201` n `53` status `ready` deltaP `18.6419` edge `0.0604` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.2522` n `53` status `ready` deltaP `-3.2482` edge `0.0341` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.3053` n `88` status `ready` deltaP `3.9467` edge `0.0159` maxDD `-1.4122`
- `market_context_high->crypto_major_24h` score `-0.4203` n `88` status `ready` deltaP `17.2191` edge `1.0127` maxDD `-80.6681`
- `market_context_high->commodity_1h` score `-0.5017` n `88` status `ready` deltaP `1.4902` edge `-0.006` maxDD `-1.7935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
