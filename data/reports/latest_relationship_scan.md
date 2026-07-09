# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T13:23:54.252309+00:00`
- Price records: `672`
- Market context records: `6184`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11110`

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

- `news_risk_high->crypto_alt_24h` score `12.6122` n `32` status `ready` deltaP `42.2194` edge `0.7843` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.018` n `32` status `ready` deltaP `61.5646` edge `0.1744` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0578` n `32` status `ready` deltaP `42.2917` edge `0.0608` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.352` n `32` status `ready` deltaP `28.3632` edge `0.0208` maxDD `-0.1113`
- `news_risk_high->crypto_major_24h` score `1.9516` n `32` status `ready` deltaP `15.625` edge `0.224` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `1.8739` n `192` status `ready` deltaP `1.3009` edge `0.2483` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3339` n `32` status `ready` deltaP `13.7565` edge `0.126` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6931` n `32` status `ready` deltaP `8.8518` edge `0.076` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.4782` n `192` status `ready` deltaP `-1.2027` edge `0.3011` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.0466` n `192` status `ready` deltaP `19.8023` edge `0.1308` maxDD `-11.8809`
- `market_context_high->equity_4h` score `-0.109` n `192` status `ready` deltaP `2.4053` edge `0.0666` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.1415` n `32` status `ready` deltaP `9.4813` edge `0.0058` maxDD `-2.3058`
- `news_risk_high->commodity_24h` score `-0.1951` n `32` status `ready` deltaP `15.3274` edge `-0.0979` maxDD `-0.3101`
- `market_context_high->fx_1h` score `-0.2881` n `192` status `ready` deltaP `1.2799` edge `-0.0009` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.68` n `192` status `ready` deltaP `3.3997` edge `0.0089` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.8084` n `192` status `ready` deltaP `-2.7653` edge `-0.0043` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.8397` n `32` status `ready` deltaP `-3.9611` edge `-0.0315` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.9511` n `192` status `ready` deltaP `1.2472` edge `-0.0077` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.9658` n `192` status `ready` deltaP `3.8607` edge `0.0272` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.9706` n `192` status `ready` deltaP `3.1226` edge `0.03` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
