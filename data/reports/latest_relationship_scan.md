# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T20:22:15.501433+00:00`
- Price records: `672`
- Market context records: `2385`
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

- `news_risk_high->crypto_alt_24h` score `21.7388` n `43` status `ready` deltaP `50.2099` edge `1.5357` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.1555` n `43` status `ready` deltaP `49.7577` edge `1.2252` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.3103` n `43` status `ready` deltaP `29.7925` edge `1.1087` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.837` n `43` status `ready` deltaP `19.7674` edge `0.9127` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.3321` n `43` status `ready` deltaP `28.1613` edge `0.5292` maxDD `-1.4744`
- `news_risk_high->index_24h` score `5.4205` n `43` status `ready` deltaP `13.6184` edge `0.4028` maxDD `-1.3507`
- `market_context_high->unknown_24h` score `5.2704` n `126` status `ready` deltaP `23.2887` edge `0.3251` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.9907` n `143` status `ready` deltaP `23.4437` edge `0.4406` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `3.8575` n `126` status `ready` deltaP `16.6667` edge `0.7727` maxDD `-25.1408`
- `market_context_high->crypto_alt_4h` score `3.7192` n `143` status `ready` deltaP `18.2` edge `0.4565` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.5779` n `43` status `ready` deltaP `37.924` edge `0.0638` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.5616` n `43` status `ready` deltaP `31.7002` edge `0.3124` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `3.0541` n `143` status `ready` deltaP `17.4111` edge `0.1994` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.0503` n `43` status `ready` deltaP `26.2124` edge `0.0145` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.5531` n `43` status `ready` deltaP `14.4675` edge `0.1053` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.5353` n `149` status `ready` deltaP `13.449` edge `0.1577` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.3565` n `126` status `ready` deltaP `10.7391` edge `0.0932` maxDD `-1.4737`
- `market_context_high->index_4h` score `1.1501` n `143` status `ready` deltaP `15.6789` edge `0.0739` maxDD `-2.2732`
- `news_risk_high->unknown_1h` score `1.0366` n `43` status `ready` deltaP `19.5481` edge `0.003` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0146` n `149` status `ready` deltaP `8.6836` edge `0.1454` maxDD `-6.1656`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
