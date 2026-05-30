# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T08:22:20.214187+00:00`
- Price records: `672`
- Market context records: `2330`
- Flow alert records: `8598`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9168`

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

- `news_risk_high->crypto_alt_24h` score `20.7817` n `43` status `ready` deltaP `50.0363` edge `1.4571` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.486` n `43` status `ready` deltaP `43.3341` edge `1.1289` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.1919` n `43` status `ready` deltaP `29.7925` edge `1.0155` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.4942` n `43` status `ready` deltaP `19.7674` edge `0.8008` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `7.388` n `127` status `ready` deltaP `24.2441` edge `0.4952` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `7.073` n `43` status `ready` deltaP `27.4669` edge `0.4289` maxDD `-1.4744`
- `market_context_high->crypto_alt_4h` score `6.8285` n `159` status `ready` deltaP `23.2416` edge `0.682` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `6.7975` n `159` status `ready` deltaP `26.8446` edge `0.5685` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `5.8952` n `127` status `ready` deltaP `16.9291` edge `1.0322` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.3373` n `159` status `ready` deltaP `21.5457` edge `0.3621` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.3012` n `43` status `ready` deltaP `11.8823` edge `0.3211` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.016` n `43` status `ready` deltaP `34.1392` edge `0.3544` maxDD `-3.0367`
- `market_context_high->index_24h` score `3.4399` n `127` status `ready` deltaP `14.7023` edge `0.2404` maxDD `-1.4737`
- `news_risk_high->fx_24h` score `3.4071` n `43` status `ready` deltaP `36.0142` edge `0.0623` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `2.1574` n `43` status `ready` deltaP `27.4319` edge `0.0153` maxDD `-0.1382`
- `market_context_high->index_4h` score `2.0684` n `159` status `ready` deltaP `20.3472` edge `0.1193` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.8903` n `159` status `ready` deltaP `12.3244` edge `0.1941` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.8538` n `127` status `ready` deltaP `18.7323` edge `0.1823` maxDD `-6.8828`
- `news_risk_high->commodity_24h` score `1.6715` n `43` status `ready` deltaP `4.2878` edge `0.1924` maxDD `-3.202`
- `market_context_high->crypto_major_1h` score `1.6445` n `159` status `ready` deltaP `12.4741` edge `0.1733` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
