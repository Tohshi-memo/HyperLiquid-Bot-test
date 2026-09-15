# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T21:52:30.117979+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11597`

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

- `news_risk_high->unknown_4h` score `383.9796` n `80` status `ready` deltaP `-22.8659` edge `32.2402` maxDD `-4.1571`
- `news_risk_high->unknown_24h` score `32.2224` n `78` status `ready` deltaP `21.1806` edge `2.544` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `23.9643` n `78` status `ready` deltaP `47.7698` edge `1.7176` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `19.8709` n `78` status `ready` deltaP `39.7303` edge `1.5381` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.7193` n `78` status `ready` deltaP `49.8531` edge `1.155` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.3901` n `78` status `ready` deltaP `59.6821` edge `0.3189` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.7052` n `78` status `ready` deltaP `38.4882` edge `0.3476` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.9224` n `52` status `ready` deltaP `38.1944` edge `0.2389` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9224` n `52` status `ready` deltaP `38.1944` edge `0.2389` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.6254` n `137` status `ready` deltaP `30.8951` edge `0.232` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.7909` n `52` status `ready` deltaP `35.0561` edge `0.0031` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.7909` n `52` status `ready` deltaP `35.0561` edge `0.0031` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.3939` n `137` status `ready` deltaP `31.8697` edge `0.0086` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.7248` n `52` status `ready` deltaP `23.8508` edge `0.0197` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.7248` n `52` status `ready` deltaP `23.8508` edge `0.0197` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.6245` n `149` status `ready` deltaP `20.3531` edge `0.0415` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7491` n `149` status `ready` deltaP `12.7678` edge `0.015` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7337` n `80` status `ready` deltaP `17.8049` edge `0.0382` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.173` n `52` status `ready` deltaP `8.9353` edge `0.1241` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.173` n `52` status `ready` deltaP `8.9353` edge `0.1241` maxDD `-6.2526`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
