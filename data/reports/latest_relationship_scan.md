# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T04:07:20.497121+00:00`
- Price records: `672`
- Market context records: `2421`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `news_risk_high->crypto_alt_24h` score `19.8962` n `43` status `ready` deltaP `45.5224` edge `1.4134` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.5796` n `43` status `ready` deltaP `50.7994` edge `1.2536` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.0775` n `43` status `ready` deltaP `29.7925` edge `1.0893` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.5398` n `43` status `ready` deltaP `18.5521` edge `0.8127` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.8327` n `43` status `ready` deltaP `26.5988` edge `0.498` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.6787` n `103` status `ready` deltaP `23.483` edge `0.3495` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.1525` n `43` status `ready` deltaP `10.4934` edge `0.4013` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.588` n `126` status `ready` deltaP `21.7698` edge `0.4182` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.4969` n `126` status `ready` deltaP `22.1908` edge `0.4947` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.536` n `43` status `ready` deltaP `37.0559` edge `0.0661` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.244` n `43` status `ready` deltaP `29.7185` edge `0.2849` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.6131` n `126` status `ready` deltaP `13.5187` edge `0.1886` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `2.6094` n `103` status `ready` deltaP `10.9206` edge `0.651` maxDD `-25.1408`
- `market_context_high->index_24h` score `2.3954` n `103` status `ready` deltaP `12.977` edge `0.1388` maxDD `-0.3888`
- `news_risk_high->fx_4h` score `2.1122` n `43` status `ready` deltaP `26.8221` edge `0.0156` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7255` n `43` status `ready` deltaP `15.9919` edge `0.1095` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.1828` n `126` status `ready` deltaP `11.142` edge `0.1437` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.0557` n `43` status `ready` deltaP `20.1469` edge `0.0006` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `0.9609` n `126` status `ready` deltaP `8.3262` edge `0.1433` maxDD `-6.1656`
- `news_risk_high->commodity_1h` score `0.5694` n `43` status `ready` deltaP `9.5669` edge `0.0772` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
