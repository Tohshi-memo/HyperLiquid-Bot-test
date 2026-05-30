# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T11:22:17.036936+00:00`
- Price records: `672`
- Market context records: `2344`
- Flow alert records: `8636`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9176`

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

- `news_risk_high->crypto_alt_24h` score `21.1093` n `43` status `ready` deltaP `50.0363` edge `1.4844` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.8801` n `43` status `ready` deltaP `44.3758` edge `1.1548` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.5207` n `43` status `ready` deltaP `29.7925` edge `1.0429` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.8662` n `43` status `ready` deltaP `19.7674` edge `0.8318` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `10.3708` n `139` status `ready` deltaP `19.7842` edge `1.1216` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.5417` n `43` status `ready` deltaP `27.6405` edge `0.4668` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `7.2355` n `139` status `ready` deltaP `24.378` edge `0.4816` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `6.5642` n `159` status `ready` deltaP `22.9368` edge `0.662` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `6.4768` n `159` status `ready` deltaP `25.6251` edge `0.5499` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `5.4882` n `159` status `ready` deltaP `22.3079` edge `0.3696` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.6422` n `43` status `ready` deltaP `12.2295` edge `0.3472` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.0152` n `43` status `ready` deltaP `34.1392` edge `0.3543` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4102` n `43` status `ready` deltaP `36.1879` edge `0.0614` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.2845` n `139` status `ready` deltaP `15.1741` edge `0.2243` maxDD `-1.4737`
- `market_context_high->equity_24h` score `2.4322` n `139` status `ready` deltaP `19.8879` edge `0.2228` maxDD `-6.8828`
- `news_risk_high->fx_4h` score `2.0295` n `43` status `ready` deltaP `25.9075` edge `0.0148` maxDD `-0.1382`
- `market_context_high->index_4h` score `2.0248` n `159` status `ready` deltaP `20.0423` edge `0.1177` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.7495` n `166` status `ready` deltaP `12.9644` edge `0.1781` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.5458` n `166` status `ready` deltaP `12.9644` edge `0.1618` maxDD `-4.2199`
- `market_context_high->equity_4h` score `1.1142` n `159` status `ready` deltaP `11.2201` edge `0.1585` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
