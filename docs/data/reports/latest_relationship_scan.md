# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T08:37:28.178475+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11540`

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

- `market_context_high->unknown_24h` score `224.4434` n `88` status `ready` deltaP `6.0318` edge `18.6775` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `87.909` n `88` status `ready` deltaP `7.2201` edge `7.3224` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `30.1847` n `52` status `ready` deltaP `23.9486` edge `2.4169` maxDD `-3.2263`
- `market_context_high->equity_24h` score `14.9529` n `88` status `ready` deltaP `16.5185` edge `1.3751` maxDD `-16.7984`
- `news_risk_high->crypto_major_24h` score `12.4007` n `52` status `ready` deltaP `37.9491` edge `1.5334` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.5472` n `53` status `ready` deltaP `35.0207` edge `0.841` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.8603` n `52` status `ready` deltaP `40.1384` edge `0.3041` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.157` n `88` status `ready` deltaP `34.9638` edge `0.9375` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.8861` n `88` status `ready` deltaP `35.0071` edge `0.2291` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.3573` n `53` status `ready` deltaP `41.9754` edge `0.1209` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.1544` n `53` status `ready` deltaP `22.2676` edge `0.3465` maxDD `-9.2335`
- `news_risk_high->index_24h` score `4.0261` n `52` status `ready` deltaP `21.0074` edge `0.2215` maxDD `-0.4168`
- `news_risk_high->equity_1h` score `3.5574` n `53` status `ready` deltaP `18.3143` edge `0.2456` maxDD `-3.6997`
- `market_context_high->index_24h` score `2.8942` n `88` status `ready` deltaP `16.9864` edge `0.1742` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.77` n `53` status `ready` deltaP `24.8821` edge `0.0903` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.3053` n `53` status `ready` deltaP `26.0411` edge `0.2858` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.2775` n `53` status `ready` deltaP `21.8132` edge `0.088` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.0816` n `53` status `ready` deltaP `24.8418` edge `0.0333` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3568` n `53` status `ready` deltaP `17.7748` edge `0.0247` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7889` n `53` status `ready` deltaP `18.0431` edge `0.0788` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
