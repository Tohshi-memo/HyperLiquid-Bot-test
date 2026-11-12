# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T07:07:23.047765+00:00`
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

- `market_context_high->unknown_24h` score `196.5032` n `88` status `ready` deltaP `5.8588` edge `16.3503` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `88.4766` n `88` status `ready` deltaP `7.2201` edge `7.3697` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `30.8687` n `52` status `ready` deltaP `23.9486` edge `2.4739` maxDD `-3.2263`
- `market_context_high->equity_24h` score `15.6369` n `88` status `ready` deltaP `16.5185` edge `1.4321` maxDD `-16.7984`
- `news_risk_high->crypto_major_24h` score `12.8235` n `52` status `ready` deltaP `37.9491` edge `1.5876` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.389` n `53` status `ready` deltaP `34.2585` edge `0.8329` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.7343` n `52` status `ready` deltaP `40.1384` edge `0.2936` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.3817` n `88` status `ready` deltaP `34.9638` edge `0.9663` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.8633` n `88` status `ready` deltaP `35.0071` edge `0.2272` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.2819` n `53` status `ready` deltaP `41.2132` edge `0.1197` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.1137` n `52` status `ready` deltaP `21.0074` edge `0.2288` maxDD `-0.4168`
- `news_risk_high->crypto_major_4h` score `4.0576` n `53` status `ready` deltaP `21.6579` edge `0.3425` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.543` n `53` status `ready` deltaP `18.3143` edge `0.2444` maxDD `-3.6997`
- `market_context_high->index_24h` score `2.9818` n `88` status `ready` deltaP `16.9864` edge `0.1815` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.758` n `53` status `ready` deltaP `24.8821` edge `0.0893` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.2581` n `53` status `ready` deltaP `25.5838` edge `0.2828` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.1864` n `53` status `ready` deltaP `20.8985` edge `0.0865` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.1067` n `53` status `ready` deltaP `25.1412` edge `0.0334` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3161` n `53` status `ready` deltaP `17.3257` edge `0.0243` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7948` n `53` status `ready` deltaP `19.3904` edge `0.0778` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
