# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T20:37:20.175782+00:00`
- Price records: `672`
- Market context records: `2386`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `news_risk_high->crypto_alt_24h` score `21.7172` n `43` status `ready` deltaP `50.2099` edge `1.5339` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.1814` n `43` status `ready` deltaP `49.9313` edge `1.2262` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.3247` n `43` status `ready` deltaP `29.7925` edge `1.1099` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.8262` n `43` status `ready` deltaP `19.7674` edge `0.9118` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.3429` n `43` status `ready` deltaP `28.1613` edge `0.5301` maxDD `-1.4744`
- `news_risk_high->index_24h` score `5.4337` n `43` status `ready` deltaP `13.6184` edge `0.4039` maxDD `-1.3507`
- `market_context_high->unknown_24h` score `5.2643` n `125` status `ready` deltaP `23.2125` edge `0.3251` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.9115` n `143` status `ready` deltaP `23.4437` edge `0.434` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `3.7602` n `125` status `ready` deltaP `16.4` edge `0.762` maxDD `-25.1408`
- `market_context_high->crypto_alt_4h` score `3.604` n `143` status `ready` deltaP `18.2` edge `0.4469` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.5791` n `43` status `ready` deltaP `37.924` edge `0.0639` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.5255` n `43` status `ready` deltaP `31.5477` edge `0.3088` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.8423` n `143` status `ready` deltaP `16.8643` edge `0.1854` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.0515` n `43` status `ready` deltaP `26.2124` edge `0.0146` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.6121` n `43` status `ready` deltaP `14.62` edge `0.1092` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.5052` n `148` status `ready` deltaP `13.2222` edge `0.1567` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.3208` n `125` status `ready` deltaP `10.5486` edge `0.0915` maxDD `-1.4737`
- `market_context_high->index_4h` score `1.0608` n `143` status `ready` deltaP `15.132` edge `0.0701` maxDD `-2.2732`
- `news_risk_high->unknown_1h` score `1.0594` n `43` status `ready` deltaP `19.6978` edge `0.0039` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `0.9593` n `148` status `ready` deltaP `8.4116` edge `0.1426` maxDD `-6.1656`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
