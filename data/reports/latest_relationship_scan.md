# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T00:07:20.779273+00:00`
- Price records: `672`
- Market context records: `2404`
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

- `news_risk_high->crypto_alt_24h` score `20.78` n `43` status `ready` deltaP `47.7794` edge `1.472` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.1558` n `43` status `ready` deltaP `49.2369` edge `1.2287` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.3067` n `43` status `ready` deltaP `29.7925` edge `1.1084` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.2379` n `43` status `ready` deltaP `19.073` edge `0.8674` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.2475` n `43` status `ready` deltaP `27.9877` edge `0.5233` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.4265` n `114` status `ready` deltaP `22.9898` edge `0.3401` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.4081` n `43` status `ready` deltaP `12.924` edge `0.4064` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.9155` n `137` status `ready` deltaP `24.1388` edge `0.4297` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `3.7734` n `137` status `ready` deltaP `18.9826` edge `0.4558` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.6031` n `43` status `ready` deltaP `37.924` edge `0.0659` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.2623` n `43` status `ready` deltaP `30.1758` edge `0.2842` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `3.0492` n `114` status `ready` deltaP `14.2179` edge `0.6854` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.5226` n `137` status `ready` deltaP `13.7529` edge `0.1795` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.1402` n `43` status `ready` deltaP `27.127` edge `0.0159` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.6693` n `43` status `ready` deltaP `15.2297` edge `0.1099` maxDD `-2.7857`
- `market_context_high->index_24h` score `1.4018` n `114` status `ready` deltaP `9.2928` edge `0.1026` maxDD `-1.1522`
- `market_context_high->crypto_major_1h` score `1.3985` n `137` status `ready` deltaP `12.9988` edge `0.1493` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.1169` n `43` status `ready` deltaP `20.1469` edge `0.0057` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `0.9012` n `137` status `ready` deltaP `8.5253` edge `0.137` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.7935` n `137` status `ready` deltaP `13.606` edge `0.058` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
