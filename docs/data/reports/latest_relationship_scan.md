# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T21:22:27.545749+00:00`
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

- `market_context_high->unknown_24h` score `14591.61` n `56` status `ready` deltaP `10.2093` edge `1215.9196` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `7078.9963` n `34` status `ready` deltaP `10.3144` edge `589.8541` maxDD `-0.1869`
- `risk_on_and_context->unknown_24h` score `7078.9963` n `34` status `ready` deltaP `10.3144` edge `589.8541` maxDD `-0.1869`
- `news_risk_high->unknown_1h` score `433.6696` n `82` status `ready` deltaP `-5.4002` edge `36.2173` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.7111` n `82` status `ready` deltaP `36.2027` edge `1.3667` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3112` n `82` status `ready` deltaP `38.0236` edge `1.4195` maxDD `-9.098`
- `news_risk_high->equity_24h` score `9.8525` n `82` status `ready` deltaP `29.1674` edge `0.8046` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.3532` n `82` status `ready` deltaP `52.9394` edge `0.2775` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.8503` n `82` status `ready` deltaP `27.3465` edge `0.2673` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.8242` n `34` status `ready` deltaP `39.8276` edge `0.1365` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.8242` n `34` status `ready` deltaP `39.8276` edge `0.1365` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.7378` n `56` status `ready` deltaP `39.8276` edge `0.1293` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `3.5499` n `56` status `ready` deltaP `5.0616` edge `0.4282` maxDD `-9.6226`
- `risk_on_high->crypto_alt_24h` score `3.2297` n `34` status `ready` deltaP `0.3347` edge `0.4005` maxDD `-7.0204`
- `risk_on_and_context->crypto_alt_24h` score `3.2297` n `34` status `ready` deltaP `0.3347` edge `0.4005` maxDD `-7.0204`
- `risk_on_high->fx_24h` score `2.1247` n `34` status `ready` deltaP `44.574` edge `0.0213` maxDD `-1.0186`
- `risk_on_and_context->fx_24h` score `2.1247` n `34` status `ready` deltaP `44.574` edge `0.0213` maxDD `-1.0186`
- `risk_on_high->commodity_4h` score `1.3009` n `58` status `ready` deltaP `19.1074` edge `0.016` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.3009` n `58` status `ready` deltaP `19.1074` edge `0.016` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.0529` n `129` status `ready` deltaP `17.0625` edge `0.0158` maxDD `-0.345`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
