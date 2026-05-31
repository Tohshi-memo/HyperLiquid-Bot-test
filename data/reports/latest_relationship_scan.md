# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T05:37:18.552821+00:00`
- Price records: `672`
- Market context records: `2427`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9180`

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

- `news_risk_high->crypto_alt_24h` score `19.5225` n `43` status `ready` deltaP `44.4807` edge `1.3892` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.6782` n `43` status `ready` deltaP `51.1466` edge `1.2595` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.9863` n `43` status `ready` deltaP `29.7925` edge `1.0817` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.1194` n `43` status `ready` deltaP `17.8577` edge `0.7823` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.6078` n `43` status `ready` deltaP `25.5571` edge `0.4862` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.8507` n `101` status `ready` deltaP `24.2677` edge `0.3586` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.0331` n `43` status `ready` deltaP `9.4517` edge `0.3983` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.6299` n `124` status `ready` deltaP `22.4282` edge `0.5042` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.5798` n `124` status `ready` deltaP `21.2333` edge `0.4211` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.4419` n `43` status `ready` deltaP `36.0142` edge `0.0652` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.1715` n `43` status `ready` deltaP `28.8038` edge `0.2817` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.6912` n `124` status `ready` deltaP `13.6851` edge `0.194` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.5337` n `101` status `ready` deltaP `13.5502` edge `0.1465` maxDD `-0.3888`
- `market_context_high->crypto_major_24h` score `2.4564` n `101` status `ready` deltaP `10.4665` edge `0.6344` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.111` n `43` status `ready` deltaP `26.8221` edge `0.0155` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7615` n `43` status `ready` deltaP `15.9919` edge `0.1125` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.1953` n `124` status `ready` deltaP `11.073` edge `0.1452` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.1217` n `43` status `ready` deltaP `20.596` edge `0.0031` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `0.9898` n `124` status `ready` deltaP `8.5378` edge `0.1443` maxDD `-6.1656`
- `news_risk_high->commodity_1h` score `0.5452` n `43` status `ready` deltaP `9.2675` edge `0.0761` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
