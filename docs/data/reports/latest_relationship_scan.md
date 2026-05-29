# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T19:52:18.516913+00:00`
- Price records: `672`
- Market context records: `2275`
- Flow alert records: `8444`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9287`

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

- `news_risk_high->crypto_alt_24h` score `20.8848` n `43` status `ready` deltaP `50.9044` edge `1.4599` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.6161` n `43` status `ready` deltaP `41.2508` edge `1.0703` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.0162` n `43` status `ready` deltaP `31.1813` edge `0.9916` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.7625` n `43` status `ready` deltaP `21.1563` edge `0.8139` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `8.297` n `157` status `ready` deltaP `26.2972` edge `0.784` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `8.2213` n `115` status `ready` deltaP `27.4154` edge `0.5435` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `8.0415` n `157` status `ready` deltaP `30.9189` edge `0.645` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `7.7848` n `43` status `ready` deltaP `31.4599` edge `0.4616` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.5863` n `157` status `ready` deltaP `22.1542` edge `0.3788` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `5.274` n `115` status `ready` deltaP `14.8672` edge `0.9663` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.7688` n `43` status `ready` deltaP `32.3099` edge `0.3349` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.7639` n `43` status `ready` deltaP `12.5767` edge `0.2717` maxDD `-1.3507`
- `news_risk_high->fx_24h` score `3.6003` n `43` status `ready` deltaP `37.2295` edge `0.0703` maxDD `-0.1442`
- `news_risk_high->commodity_24h` score `3.3788` n `43` status `ready` deltaP `3.5934` edge `0.3393` maxDD `-3.202`
- `market_context_high->index_24h` score `3.3743` n `115` status `ready` deltaP `14.3765` edge `0.2371` maxDD `-1.4737`
- `market_context_high->index_4h` score `2.5645` n `157` status `ready` deltaP `24.2388` edge `0.1347` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `2.3616` n `159` status `ready` deltaP `13.9711` edge `0.2224` maxDD `-6.1656`
- `market_context_high->equity_4h` score `2.3237` n `157` status `ready` deltaP `18.7781` edge `0.2089` maxDD `-5.9024`
- `news_risk_high->fx_4h` score `2.0856` n `43` status `ready` deltaP `26.6697` edge `0.0144` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `2.0139` n `159` status `ready` deltaP `13.9711` edge `0.1941` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
