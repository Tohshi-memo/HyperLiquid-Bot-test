# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T21:07:28.224915+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12657`

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

- `market_context_high->unknown_24h` score `16136.4228` n `56` status `ready` deltaP `10.2093` edge `1344.654` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `9096.1565` n `35` status `ready` deltaP `10.5665` edge `757.9491` maxDD `-0.1869`
- `risk_on_and_context->unknown_24h` score `9096.1565` n `35` status `ready` deltaP `10.5665` edge `757.9491` maxDD `-0.1869`
- `news_risk_high->unknown_1h` score `431.3284` n `82` status `ready` deltaP `-5.4002` edge `36.0222` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.7123` n `82` status `ready` deltaP `36.2027` edge `1.3668` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3232` n `82` status `ready` deltaP `38.0236` edge `1.4205` maxDD `-9.098`
- `news_risk_high->equity_24h` score `9.8087` n `82` status `ready` deltaP `28.995` edge `0.8021` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.3334` n `82` status `ready` deltaP `52.767` edge `0.277` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.8341` n `82` status `ready` deltaP `27.1741` edge `0.2671` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.8062` n `35` status `ready` deltaP `39.8276` edge `0.135` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.8062` n `35` status `ready` deltaP `39.8276` edge `0.135` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.7234` n `56` status `ready` deltaP `39.8276` edge `0.1281` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `3.5283` n `56` status `ready` deltaP `5.0616` edge `0.4264` maxDD `-9.6226`
- `risk_on_high->crypto_alt_24h` score `3.4827` n `35` status `ready` deltaP `1.8473` edge `0.4115` maxDD `-7.0204`
- `risk_on_and_context->crypto_alt_24h` score `3.4827` n `35` status `ready` deltaP `1.8473` edge `0.4115` maxDD `-7.0204`
- `risk_on_high->fx_24h` score `1.954` n `35` status `ready` deltaP `42.5616` edge `0.0186` maxDD `-1.1462`
- `risk_on_and_context->fx_24h` score `1.954` n `35` status `ready` deltaP `42.5616` edge `0.0186` maxDD `-1.1462`
- `risk_on_high->commodity_4h` score `1.1951` n `59` status `ready` deltaP `18.0034` edge `0.0149` maxDD `-0.1596`
- `risk_on_and_context->commodity_4h` score `1.1951` n `59` status `ready` deltaP `18.0034` edge `0.0149` maxDD `-0.1596`
- `market_context_high->commodity_4h` score `0.997` n `129` status `ready` deltaP `16.4398` edge `0.0153` maxDD `-0.345`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
