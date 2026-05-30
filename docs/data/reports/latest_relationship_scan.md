# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T21:37:24.304789+00:00`
- Price records: `672`
- Market context records: `2391`
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

- `news_risk_high->crypto_alt_24h` score `21.4853` n `43` status `ready` deltaP `49.5155` edge `1.5192` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.2114` n `43` status `ready` deltaP `49.9313` edge `1.2287` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.3451` n `43` status `ready` deltaP `29.7925` edge `1.1116` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.7302` n `43` status `ready` deltaP `19.7674` edge `0.9038` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.3669` n `43` status `ready` deltaP `28.1613` edge `0.5321` maxDD `-1.4744`
- `news_risk_high->index_24h` score `5.4565` n `43` status `ready` deltaP `13.6184` edge `0.4058` maxDD `-1.3507`
- `market_context_high->unknown_24h` score `5.2701` n `121` status `ready` deltaP `22.8951` edge `0.3277` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.8443` n `143` status `ready` deltaP `23.4437` edge `0.4284` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.5839` n `43` status `ready` deltaP `37.924` edge `0.0643` maxDD `-0.1442`
- `market_context_high->crypto_alt_4h` score `3.5332` n `143` status `ready` deltaP `18.2` edge `0.441` maxDD `-15.4319`
- `market_context_high->crypto_major_24h` score `3.4411` n `121` status `ready` deltaP `15.2893` edge `0.7285` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.4128` n `43` status `ready` deltaP `31.0904` edge `0.2974` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.5581` n `143` status `ready` deltaP `14.6768` edge `0.1763` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.0673` n `43` status `ready` deltaP `26.3648` edge `0.0149` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.6921` n `43` status `ready` deltaP `15.2297` edge `0.1118` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.56` n `144` status `ready` deltaP `13.2776` edge `0.1609` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.2598` n `121` status `ready` deltaP `9.7552` edge `0.0917` maxDD `-1.4737`
- `news_risk_high->unknown_1h` score `1.063` n `43` status `ready` deltaP `19.6978` edge `0.0042` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `0.9548` n `144` status `ready` deltaP `7.9799` edge `0.1451` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.9534` n `143` status `ready` deltaP `14.5851` edge `0.0648` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
