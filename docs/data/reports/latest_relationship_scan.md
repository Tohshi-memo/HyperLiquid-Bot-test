# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T20:07:21.127112+00:00`
- Price records: `672`
- Market context records: `2384`
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

- `news_risk_high->crypto_alt_24h` score `21.758` n `43` status `ready` deltaP `50.2099` edge `1.5373` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.1296` n `43` status `ready` deltaP `49.5841` edge `1.2242` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.2947` n `43` status `ready` deltaP `29.7925` edge `1.1074` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.8382` n `43` status `ready` deltaP `19.7674` edge `0.9128` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.3141` n `43` status `ready` deltaP `28.1613` edge `0.5277` maxDD `-1.4744`
- `market_context_high->crypto_major_24h` score `6.1128` n `127` status `ready` deltaP `16.9291` edge `0.7858` maxDD `-25.1408`
- `news_risk_high->index_24h` score `5.4073` n `43` status `ready` deltaP `13.6184` edge `0.4017` maxDD `-1.3507`
- `market_context_high->unknown_24h` score `5.3124` n `127` status `ready` deltaP `23.3637` edge `0.3281` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `5.0507` n `143` status `ready` deltaP `23.4437` edge `0.4456` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `3.8164` n `143` status `ready` deltaP `18.2` edge `0.4646` maxDD `-15.4319`
- `news_risk_high->commodity_4h` score `3.6007` n `43` status `ready` deltaP `31.8526` edge `0.3164` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.5616` n `43` status `ready` deltaP `37.7504` edge `0.0636` maxDD `-0.1442`
- `market_context_high->unknown_4h` score `3.3234` n `143` status `ready` deltaP `17.958` edge `0.2182` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.0491` n `43` status `ready` deltaP `26.2124` edge `0.0144` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `1.5725` n `150` status `ready` deltaP `13.523` edge `0.1603` maxDD `-4.2199`
- `news_risk_high->unknown_4h` score `1.4786` n `43` status `ready` deltaP `14.3151` edge `0.1001` maxDD `-2.7857`
- `market_context_high->index_24h` score `1.3919` n `127` status `ready` deltaP `10.9266` edge `0.0949` maxDD `-1.4737`
- `market_context_high->index_4h` score `1.1921` n `143` status `ready` deltaP `15.6789` edge `0.0774` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.0865` n `150` status `ready` deltaP `8.9521` edge `0.1496` maxDD `-6.1656`
- `news_risk_high->unknown_1h` score `0.9743` n `43` status `ready` deltaP `19.3984` edge `-0.0012` maxDD `-1.7548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
