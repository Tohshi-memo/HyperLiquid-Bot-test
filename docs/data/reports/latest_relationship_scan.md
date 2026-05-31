# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T05:52:23.431496+00:00`
- Price records: `672`
- Market context records: `2428`
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

- `news_risk_high->crypto_alt_24h` score `19.475` n `43` status `ready` deltaP `44.3071` edge `1.3864` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.6878` n `43` status `ready` deltaP `51.1466` edge `1.2603` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.9755` n `43` status `ready` deltaP `29.7925` edge `1.0808` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.0503` n `43` status `ready` deltaP `17.6841` edge `0.7777` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.5747` n `43` status `ready` deltaP `25.3835` edge `0.4846` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.8176` n `101` status `ready` deltaP `24.0941` edge `0.357` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.0144` n `43` status `ready` deltaP `9.2781` edge `0.3979` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.6093` n `124` status `ready` deltaP `22.2757` edge `0.5035` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.5786` n `124` status `ready` deltaP `21.2333` edge `0.421` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.4256` n `43` status `ready` deltaP `35.8406` edge `0.065` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.1715` n `43` status `ready` deltaP `28.8038` edge `0.2817` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.7068` n `124` status `ready` deltaP `13.6851` edge `0.1953` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.515` n `101` status `ready` deltaP `13.3766` edge `0.1461` maxDD `-0.3888`
- `market_context_high->crypto_major_24h` score `2.4114` n `101` status `ready` deltaP `10.2929` edge `0.6298` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.111` n `43` status `ready` deltaP `26.8221` edge `0.0155` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7771` n `43` status `ready` deltaP `15.9919` edge `0.1138` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.1821` n `124` status `ready` deltaP `10.9233` edge `0.1451` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.1265` n `43` status `ready` deltaP `20.596` edge `0.0035` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `0.9922` n `124` status `ready` deltaP `8.5378` edge `0.1445` maxDD `-6.1656`
- `news_risk_high->commodity_1h` score `0.5335` n `43` status `ready` deltaP `9.1178` edge `0.0756` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
