# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T08:07:16.021227+00:00`
- Price records: `672`
- Market context records: `2438`
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

- `news_risk_high->crypto_alt_24h` score `19.2453` n `43` status `ready` deltaP `43.2655` edge `1.3742` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.9136` n `43` status `ready` deltaP `52.7091` edge `1.2687` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.8663` n `43` status `ready` deltaP `29.7925` edge `1.0717` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.6684` n `43` status `ready` deltaP `16.9896` edge `0.7505` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.2915` n `43` status `ready` deltaP `24.1682` edge `0.4691` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.5344` n `101` status `ready` deltaP `22.8788` edge `0.3415` maxDD `-1.626`
- `news_risk_high->index_24h` score `4.9663` n `43` status `ready` deltaP `8.9309` edge `0.3962` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.7838` n `124` status `ready` deltaP `22.148` edge `0.432` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.6901` n `124` status `ready` deltaP `22.5806` edge `0.5082` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.279` n `43` status `ready` deltaP `34.2781` edge `0.0632` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.1738` n `43` status `ready` deltaP `28.8038` edge `0.282` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.8442` n `124` status `ready` deltaP `14.1424` edge `0.2037` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.4668` n `101` status `ready` deltaP `13.0294` edge `0.1444` maxDD `-0.3888`
- `market_context_high->crypto_major_24h` score `2.1632` n `101` status `ready` deltaP `9.5984` edge `0.6026` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.122` n `43` status `ready` deltaP `26.9746` edge `0.0154` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.9145` n `43` status `ready` deltaP `16.4492` edge `0.1222` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.1433` n `43` status `ready` deltaP `20.596` edge `0.0049` maxDD `-1.7548`
- `market_context_high->crypto_major_1h` score `1.0372` n `127` status `ready` deltaP `10.2975` edge `0.1372` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.771` n `127` status `ready` deltaP `7.5581` edge `0.1326` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.5477` n `124` status `ready` deltaP `12.6033` edge `0.0442` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
