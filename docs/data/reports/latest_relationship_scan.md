# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T06:37:20.815543+00:00`
- Price records: `672`
- Market context records: `2432`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `news_risk_high->crypto_alt_24h` score `19.3505` n `43` status `ready` deltaP `43.7863` edge `1.3795` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.7583` n `43` status `ready` deltaP `51.6675` edge `1.2627` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.9443` n `43` status `ready` deltaP `29.7925` edge `1.0782` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.8563` n `43` status `ready` deltaP `17.1632` edge `0.765` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.4623` n `43` status `ready` deltaP `24.8627` edge `0.4787` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.7052` n `101` status `ready` deltaP `23.5733` edge `0.3511` maxDD `-1.626`
- `news_risk_high->index_24h` score `4.9862` n `43` status `ready` deltaP `9.1045` edge `0.3967` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.5935` n `124` status `ready` deltaP `22.1233` edge `0.5032` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.587` n `124` status `ready` deltaP `21.2333` edge `0.4217` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.378` n `43` status `ready` deltaP `35.3198` edge `0.0645` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.1723` n `43` status `ready` deltaP `28.8038` edge `0.2818` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.7032` n `124` status `ready` deltaP `13.6851` edge `0.195` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.4867` n `101` status `ready` deltaP `13.203` edge `0.1449` maxDD `-0.3888`
- `market_context_high->crypto_major_24h` score `2.2853` n `101` status `ready` deltaP `9.772` edge `0.6171` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.1232` n `43` status `ready` deltaP `26.9746` edge `0.0155` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7735` n `43` status `ready` deltaP `15.9919` edge `0.1135` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.2156` n `124` status `ready` deltaP `11.2227` edge `0.1459` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.1157` n `43` status `ready` deltaP `20.596` edge `0.0026` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0341` n `124` status `ready` deltaP `8.8372` edge `0.146` maxDD `-6.1656`
- `news_risk_high->commodity_1h` score `0.5234` n `43` status `ready` deltaP `8.9681` edge `0.0753` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
