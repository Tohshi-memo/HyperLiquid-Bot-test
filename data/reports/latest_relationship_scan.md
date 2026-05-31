# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T00:37:23.700237+00:00`
- Price records: `672`
- Market context records: `2406`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9202`

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

- `news_risk_high->crypto_alt_24h` score `20.5962` n `43` status `ready` deltaP `47.4321` edge `1.459` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.1618` n `43` status `ready` deltaP `49.2369` edge `1.2292` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.2731` n `43` status `ready` deltaP `29.7925` edge `1.1056` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.104` n `43` status `ready` deltaP `18.8993` edge `0.8574` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.2199` n `43` status `ready` deltaP `27.9877` edge `0.521` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.5027` n `112` status `ready` deltaP `22.8175` edge `0.3476` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.3743` n `43` status `ready` deltaP `12.5767` edge `0.4059` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.8979` n `135` status `ready` deltaP `23.8144` edge `0.4304` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `3.9802` n `135` status `ready` deltaP `19.9774` edge `0.4664` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.6067` n `43` status `ready` deltaP `37.924` edge `0.0662` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.2639` n `43` status `ready` deltaP `30.1758` edge `0.2844` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `3.0923` n `112` status `ready` deltaP `14.3105` edge `0.6903` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.5118` n `135` status `ready` deltaP `13.3322` edge `0.1814` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.1658` n `43` status `ready` deltaP `27.4319` edge `0.016` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.6851` n `43` status `ready` deltaP `15.3822` edge `0.1102` maxDD `-2.7857`
- `market_context_high->index_24h` score `1.567` n `112` status `ready` deltaP `10.2926` edge `0.1097` maxDD `-1.1522`
- `market_context_high->crypto_major_1h` score `1.4848` n `135` status `ready` deltaP `13.6727` edge `0.152` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.1373` n `43` status `ready` deltaP `20.2966` edge `0.0064` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0193` n `135` status `ready` deltaP `9.1018` edge `0.143` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.737` n `135` status `ready` deltaP `13.1843` edge `0.0561` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
