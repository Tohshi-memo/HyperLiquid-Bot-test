# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T20:52:21.217189+00:00`
- Price records: `672`
- Market context records: `2388`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `news_risk_high->crypto_alt_24h` score `21.6649` n `43` status `ready` deltaP `50.0363` edge `1.5307` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.1898` n `43` status `ready` deltaP `49.9313` edge `1.2269` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.3367` n `43` status `ready` deltaP `29.7925` edge `1.1109` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.8082` n `43` status `ready` deltaP `19.7674` edge `0.9103` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.3513` n `43` status `ready` deltaP `28.1613` edge `0.5308` maxDD `-1.4744`
- `news_risk_high->index_24h` score `5.4457` n `43` status `ready` deltaP `13.6184` edge `0.4049` maxDD `-1.3507`
- `market_context_high->unknown_24h` score `5.2605` n `124` status `ready` deltaP `23.1351` edge `0.3253` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.8791` n `143` status `ready` deltaP `23.4437` edge `0.4313` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `3.686` n `124` status `ready` deltaP `16.129` edge `0.7543` maxDD `-25.1408`
- `news_risk_high->fx_24h` score `3.5803` n `43` status `ready` deltaP `37.924` edge `0.064` maxDD `-0.1442`
- `market_context_high->crypto_alt_4h` score `3.5524` n `143` status `ready` deltaP `18.2` edge `0.4426` maxDD `-15.4319`
- `news_risk_high->commodity_4h` score `3.5021` n `43` status `ready` deltaP `31.5477` edge `0.3058` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.7566` n `143` status `ready` deltaP `16.3174` edge `0.1819` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.0649` n `43` status `ready` deltaP `26.3648` edge `0.0147` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.6363` n `43` status `ready` deltaP `14.7724` edge `0.1102` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.524` n `147` status `ready` deltaP `13.2918` edge `0.1578` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.2922` n `124` status `ready` deltaP `10.3551` edge `0.0904` maxDD `-1.4737`
- `news_risk_high->unknown_1h` score `1.081` n `43` status `ready` deltaP `19.8475` edge `0.0047` maxDD `-1.7548`
- `market_context_high->index_4h` score `1.0248` n `143` status `ready` deltaP `15.132` edge `0.0671` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `0.9396` n `147` status `ready` deltaP `8.1358` edge `0.1428` maxDD `-6.1656`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
