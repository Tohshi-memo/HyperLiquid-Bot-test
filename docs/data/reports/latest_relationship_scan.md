# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T11:37:17.679402+00:00`
- Price records: `672`
- Market context records: `2345`
- Flow alert records: `8639`
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

- `news_risk_high->crypto_alt_24h` score `21.1657` n `43` status `ready` deltaP `50.0363` edge `1.4891` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.9216` n `43` status `ready` deltaP `44.5494` edge `1.1571` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.5495` n `43` status `ready` deltaP `29.7925` edge `1.0453` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.913` n `43` status `ready` deltaP `19.7674` edge `0.8357` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `10.2196` n `139` status `ready` deltaP `19.7842` edge `1.109` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.5957` n `43` status `ready` deltaP `27.6405` edge `0.4713` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `7.0651` n `139` status `ready` deltaP `24.378` edge `0.4674` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `6.573` n `158` status `ready` deltaP `22.7617` edge `0.6639` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `6.5005` n `158` status `ready` deltaP `25.5017` edge `0.5527` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `5.4727` n `158` status `ready` deltaP `22.1288` edge `0.3695` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.6848` n `43` status `ready` deltaP `12.4031` edge `0.3496` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.016` n `43` status `ready` deltaP `34.1392` edge `0.3544` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4102` n `43` status `ready` deltaP `36.1879` edge `0.0614` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.146` n `139` status `ready` deltaP `14.6283` edge `0.2164` maxDD `-1.4737`
- `market_context_high->equity_24h` score `2.3422` n `139` status `ready` deltaP `19.8879` edge `0.2153` maxDD `-6.8828`
- `market_context_high->index_4h` score `2.0401` n `158` status `ready` deltaP `20.0834` edge `0.1187` maxDD `-2.2732`
- `news_risk_high->fx_4h` score `2.0307` n `43` status `ready` deltaP `25.9075` edge `0.0149` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `1.7254` n `165` status `ready` deltaP `12.9024` edge `0.1765` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.53` n `165` status `ready` deltaP `12.7527` edge `0.1619` maxDD `-4.2199`
- `market_context_high->equity_4h` score `1.1224` n `158` status `ready` deltaP `11.1126` edge `0.1599` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
