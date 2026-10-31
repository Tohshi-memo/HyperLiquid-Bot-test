# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T20:07:27.351793+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7703`

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

- `market_context_high->unknown_24h` score `3065.9238` n `96` status `ready` deltaP `-9.8958` edge `255.6026` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `101.1509` n `96` status `ready` deltaP `0.6351` edge `8.4383` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `77.7148` n `108` status `ready` deltaP `-5.1951` edge `6.5395` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `19.4428` n `74` status `ready` deltaP `45.9084` edge `1.3193` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.7689` n `96` status `ready` deltaP `25.1736` edge `1.0053` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.2663` n `108` status `ready` deltaP `19.6646` edge `0.4464` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.8833` n `96` status `ready` deltaP `43.4028` edge `0.1359` maxDD `-0.1315`
- `market_context_high->metal_4h` score `1.6284` n `96` status `ready` deltaP `20.1728` edge `0.0437` maxDD `-0.7323`
- `news_risk_high->crypto_alt_1h` score `0.8277` n `108` status `ready` deltaP `8.8767` edge `0.1052` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.7915` n `96` status `ready` deltaP `11.4708` edge `0.0185` maxDD `-0.3209`
- `market_context_high->equity_4h` score `0.6545` n `96` status `ready` deltaP `4.4461` edge `0.1936` maxDD `-4.48`
- `market_context_high->equity_1h` score `0.4306` n `96` status `ready` deltaP `6.3997` edge `0.1001` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.3671` n `96` status `ready` deltaP `14.126` edge `0.0596` maxDD `-0.8703`
- `market_context_high->fx_4h` score `0.3598` n `96` status `ready` deltaP `10.2134` edge `0.001` maxDD `-0.1285`
- `market_context_high->crypto_major_1h` score `0.2776` n `96` status `ready` deltaP `8.3333` edge `0.0828` maxDD `-5.2213`
- `market_context_high->fx_1h` score `0.268` n `96` status `ready` deltaP `9.2128` edge `-0.0003` maxDD `-0.1407`
- `market_context_high->metal_24h` score `-0.1092` n `96` status `ready` deltaP `11.4583` edge `0.1743` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-0.251` n `96` status `ready` deltaP `15.3963` edge `0.1392` maxDD `-14.5879`
- `market_context_high->commodity_1h` score `-0.321` n `96` status `ready` deltaP `-0.5739` edge `0.0141` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.3967` n `96` status `ready` deltaP `3.1188` edge `0.002` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
