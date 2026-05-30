# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T21:52:18.385315+00:00`
- Price records: `672`
- Market context records: `2393`
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

- `news_risk_high->crypto_alt_24h` score `21.4186` n `43` status `ready` deltaP `49.3419` edge `1.5148` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.2162` n `43` status `ready` deltaP `49.9313` edge `1.2291` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.3451` n `43` status `ready` deltaP `29.7925` edge `1.1116` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.7002` n `43` status `ready` deltaP `19.7674` edge `0.9013` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.3693` n `43` status `ready` deltaP `28.1613` edge `0.5323` maxDD `-1.4744`
- `news_risk_high->index_24h` score `5.4625` n `43` status `ready` deltaP `13.6184` edge `0.4063` maxDD `-1.3507`
- `market_context_high->unknown_24h` score `5.2731` n `120` status `ready` deltaP `22.8125` edge `0.3285` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.8011` n `143` status `ready` deltaP `23.4437` edge `0.4248` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.5851` n `43` status `ready` deltaP `37.924` edge `0.0644` maxDD `-0.1442`
- `market_context_high->crypto_alt_4h` score `3.52` n `143` status `ready` deltaP `18.2` edge `0.4399` maxDD `-15.4319`
- `news_risk_high->commodity_4h` score `3.3862` n `43` status `ready` deltaP `30.938` edge `0.295` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `3.352` n `120` status `ready` deltaP `15.0` edge `0.719` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.506` n `143` status `ready` deltaP `14.13` edge `0.1756` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.0685` n `43` status `ready` deltaP `26.3648` edge `0.015` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7067` n `43` status `ready` deltaP `15.3822` edge `0.112` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.5434` n `143` status `ready` deltaP `13.0397` edge `0.1611` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.2468` n `120` status `ready` deltaP `9.5486` edge `0.092` maxDD `-1.4737`
- `news_risk_high->unknown_1h` score `1.0606` n `43` status `ready` deltaP `19.6978` edge `0.004` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `0.9878` n `143` status `ready` deltaP `8.243` edge `0.1461` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.8869` n `143` status `ready` deltaP `14.0383` edge `0.0629` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
