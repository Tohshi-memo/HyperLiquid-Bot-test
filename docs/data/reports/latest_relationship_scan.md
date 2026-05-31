# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T14:22:23.563966+00:00`
- Price records: `672`
- Market context records: `2465`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9236`

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

- `news_risk_high->crypto_alt_24h` score `22.1985` n `32` status `ready` deltaP `45.4861` edge `1.6055` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `21.8494` n `32` status `ready` deltaP `56.0764` edge `1.4909` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `19.6456` n `32` status `ready` deltaP `28.9931` edge `1.4753` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `13.6389` n `32` status `ready` deltaP `26.7361` edge `1.0164` maxDD `-3.3119`
- `news_risk_high->index_24h` score `9.341` n `32` status `ready` deltaP `27.4306` edge `0.6166` maxDD `-1.3507`
- `news_risk_high->unknown_24h` score `7.1746` n `32` status `ready` deltaP `24.1319` edge `0.4596` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.7564` n `114` status `ready` deltaP `21.9937` edge `0.3659` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `3.9439` n `136` status `ready` deltaP `20.5882` edge `0.4593` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8863` n `136` status `ready` deltaP `18.0236` edge `0.3847` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.641` n `32` status `ready` deltaP `35.9375` edge `0.0823` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.2622` n `32` status `ready` deltaP `22.2561` edge `0.1906` maxDD `-3.0367`
- `news_risk_high->metal_4h` score `3.1243` n `32` status `ready` deltaP `14.7104` edge `0.3829` maxDD `-3.4337`
- `market_context_high->crypto_major_24h` score `2.4341` n `114` status `ready` deltaP `12.1528` edge `0.6203` maxDD `-25.1408`
- `news_risk_high->equity_4h` score `2.2306` n `32` status `ready` deltaP `-7.4695` edge `0.409` maxDD `-2.8579`
- `news_risk_high->fx_4h` score `1.77` n `32` status `ready` deltaP `22.4085` edge `0.0165` maxDD `-0.1382`
- `market_context_high->unknown_4h` score `1.5539` n `136` status `ready` deltaP `9.8458` edge `0.1659` maxDD `-3.4972`
- `news_risk_high->crypto_alt_4h` score `1.5319` n `32` status `ready` deltaP `6.25` edge `0.1568` maxDD `-2.9979`
- `news_risk_high->unknown_1h` score `1.4465` n `32` status `ready` deltaP `18.1512` edge `0.0427` maxDD `-1.4536`
- `news_risk_high->fx_1h` score `1.0642` n `32` status `ready` deltaP `14.8765` edge `0.0151` maxDD `-0.0473`
- `news_risk_high->index_4h` score `0.8304` n `32` status `ready` deltaP `-5.4878` edge `0.2304` maxDD `-2.9886`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
