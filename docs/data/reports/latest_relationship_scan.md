# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T22:22:22.879093+00:00`
- Price records: `672`
- Market context records: `2395`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9201`

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

- `news_risk_high->crypto_alt_24h` score `21.308` n `43` status `ready` deltaP `48.9946` edge `1.5079` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.2282` n `43` status `ready` deltaP `49.9313` edge `1.2301` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.3523` n `43` status `ready` deltaP `29.7925` edge `1.1122` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.6594` n `43` status `ready` deltaP `19.7674` edge `0.8979` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.3717` n `43` status `ready` deltaP `28.1613` edge `0.5325` maxDD `-1.4744`
- `news_risk_high->index_24h` score `5.4721` n `43` status `ready` deltaP `13.6184` edge `0.4071` maxDD `-1.3507`
- `market_context_high->unknown_24h` score `5.3075` n `118` status `ready` deltaP `22.643` edge `0.3325` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.7829` n `141` status `ready` deltaP `23.441` edge `0.4233` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.5887` n `43` status `ready` deltaP `37.924` edge `0.0647` maxDD `-0.1442`
- `market_context_high->crypto_alt_4h` score `3.4963` n `141` status `ready` deltaP `18.0387` edge `0.439` maxDD `-15.4319`
- `news_risk_high->commodity_4h` score `3.3259` n `43` status `ready` deltaP `30.6331` edge `0.2893` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `3.1916` n `118` status `ready` deltaP `14.4068` edge `0.7024` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.448` n `141` status `ready` deltaP `13.5844` edge `0.1744` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.0721` n `43` status `ready` deltaP `26.3648` edge `0.0153` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.6887` n `43` status `ready` deltaP `15.3822` edge `0.1105` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.4385` n `141` status `ready` deltaP `12.853` edge `0.1536` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.2225` n `118` status `ready` deltaP `9.1249` edge `0.0928` maxDD `-1.4737`
- `news_risk_high->unknown_1h` score `1.0546` n `43` status `ready` deltaP `19.6978` edge `0.0035` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `0.8925` n `141` status `ready` deltaP `7.967` edge `0.14` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.8393` n `141` status `ready` deltaP `13.8038` edge `0.0605` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
