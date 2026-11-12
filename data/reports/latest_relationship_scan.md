# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T07:37:24.242204+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11530`

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

- `market_context_high->unknown_24h` score `206.1446` n `88` status `ready` deltaP `6.0318` edge `17.1526` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `89.055` n `88` status `ready` deltaP `7.2201` edge `7.4179` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `30.6359` n `52` status `ready` deltaP `23.9486` edge `2.4545` maxDD `-3.2263`
- `market_context_high->equity_24h` score `15.4041` n `88` status `ready` deltaP `16.5185` edge `1.4127` maxDD `-16.7984`
- `news_risk_high->crypto_major_24h` score `12.6823` n `52` status `ready` deltaP `37.9491` edge `1.5695` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.4602` n `53` status `ready` deltaP `34.5633` edge `0.8368` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.7775` n `52` status `ready` deltaP `40.1384` edge `0.2972` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.3006` n `88` status `ready` deltaP `34.9638` edge `0.9559` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.8729` n `88` status `ready` deltaP `35.0071` edge `0.228` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.2977` n `53` status `ready` deltaP `41.3657` edge `0.12` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.1048` n `53` status `ready` deltaP `21.9628` edge `0.3444` maxDD `-9.2335`
- `news_risk_high->index_24h` score `4.0849` n `52` status `ready` deltaP `21.0074` edge `0.2264` maxDD `-0.4168`
- `news_risk_high->equity_1h` score `3.573` n `53` status `ready` deltaP `18.464` edge `0.2459` maxDD `-3.6997`
- `market_context_high->index_24h` score `2.953` n `88` status `ready` deltaP `16.9864` edge `0.1791` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.7652` n `53` status `ready` deltaP `24.8821` edge `0.0899` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.2888` n `53` status `ready` deltaP `25.8887` edge `0.2847` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.2179` n `53` status `ready` deltaP `21.2034` edge `0.0871` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.1223` n `53` status `ready` deltaP `25.2909` edge `0.0337` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3425` n `53` status `ready` deltaP `17.6251` edge `0.0245` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.8002` n `53` status `ready` deltaP `19.3904` edge `0.0785` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
