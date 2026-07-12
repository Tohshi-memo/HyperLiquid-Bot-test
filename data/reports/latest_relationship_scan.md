# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T02:07:27.651479+00:00`
- Price records: `672`
- Market context records: `6452`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5875`

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

- `news_risk_high->crypto_alt_24h` score `11.6967` n `32` status `ready` deltaP `29.8611` edge `0.7904` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `8.0611` n `145` status `ready` deltaP `18.0735` edge `0.8813` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.307` n `32` status `ready` deltaP `52.2569` edge `0.1772` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1096` n `32` status `ready` deltaP `42.7591` edge `0.062` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.8085` n `32` status `ready` deltaP `33.3333` edge `0.1157` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.3626` n `32` status `ready` deltaP `11.9792` edge `0.4292` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4697` n `32` status `ready` deltaP `29.7904` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4812` n `32` status `ready` deltaP `13.3795` edge `0.1474` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.3319` n `177` status `ready` deltaP `-5.9855` edge `0.241` maxDD `-3.2083`
- `news_risk_high->crypto_alt_1h` score `0.8428` n `32` status `ready` deltaP `9.375` edge `0.0917` maxDD `-1.6923`
- `market_context_high->index_4h` score `0.1288` n `177` status `ready` deltaP `7.9147` edge `0.0256` maxDD `-0.4108`
- `market_context_high->metal_4h` score `-0.0807` n `177` status `ready` deltaP `8.9991` edge `0.0421` maxDD `-2.7056`
- `market_context_high->commodity_24h` score `-0.085` n `145` status `ready` deltaP `4.1307` edge `0.1522` maxDD `-5.2791`
- `market_context_high->unknown_4h` score `-0.1036` n `177` status `ready` deltaP `-15.2947` edge `0.3339` maxDD `-10.5788`
- `market_context_high->crypto_alt_4h` score `-0.1136` n `177` status `ready` deltaP `7.4032` edge `0.1027` maxDD `-7.2552`
- `news_risk_high->unknown_1h` score `-0.2272` n `32` status `ready` deltaP `5.9319` edge `-0.024` maxDD `-0.7581`
- `news_risk_high->metal_1h` score `-0.5059` n `32` status `ready` deltaP `1.3473` edge `-0.0241` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.5497` n `177` status `ready` deltaP `6.4972` edge `0.0175` maxDD `-5.8368`
- `news_risk_high->index_24h` score `-0.5833` n `32` status `ready` deltaP `2.9514` edge `-0.0073` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.6006` n `177` status `ready` deltaP `-0.0651` edge `0.0012` maxDD `-1.8877`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
