# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T06:07:22.496047+00:00`
- Price records: `672`
- Market context records: `2429`
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

- `news_risk_high->crypto_alt_24h` score `19.4323` n `43` status `ready` deltaP `44.1335` edge `1.384` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.7125` n `43` status `ready` deltaP `51.3202` edge `1.2612` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.9635` n `43` status `ready` deltaP `29.7925` edge `1.0798` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.9825` n `43` status `ready` deltaP `17.5105` edge `0.7732` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.5392` n `43` status `ready` deltaP `25.2099` edge `0.4828` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.7821` n `101` status `ready` deltaP `23.9205` edge `0.3552` maxDD `-1.626`
- `news_risk_high->index_24h` score `4.9922` n `43` status `ready` deltaP `9.1045` edge `0.3972` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.6117` n `124` status `ready` deltaP `22.2757` edge `0.5037` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.581` n `124` status `ready` deltaP `21.2333` edge `0.4212` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.4093` n `43` status `ready` deltaP `35.667` edge `0.0648` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.173` n `43` status `ready` deltaP `28.8038` edge `0.2819` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.7056` n `124` status `ready` deltaP `13.6851` edge `0.1952` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.4927` n `101` status `ready` deltaP `13.203` edge `0.1454` maxDD `-0.3888`
- `market_context_high->crypto_major_24h` score `2.3673` n `101` status `ready` deltaP `10.1193` edge `0.6253` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.111` n `43` status `ready` deltaP `26.8221` edge `0.0155` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7759` n `43` status `ready` deltaP `15.9919` edge `0.1137` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.1833` n `124` status `ready` deltaP `10.9233` edge `0.1452` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.1217` n `43` status `ready` deltaP `20.596` edge `0.0031` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0126` n `124` status `ready` deltaP `8.6875` edge `0.1452` maxDD `-6.1656`
- `news_risk_high->commodity_1h` score `0.5328` n `43` status `ready` deltaP `9.1178` edge `0.0755` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
