# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T02:37:30.479187+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9807`

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

- `market_context_high->crypto_alt_4h` score `6.6356` n `117` status `ready` deltaP `16.612` edge `0.5871` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.2656` n `52` status `ready` deltaP `32.0` edge `0.3088` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2656` n `52` status `ready` deltaP `32.0` edge `0.3088` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.096` n `117` status `ready` deltaP `21.12` edge `0.5231` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.2244` n `54` status `ready` deltaP `18.8912` edge `0.3542` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.2244` n `54` status `ready` deltaP `18.8912` edge `0.3542` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.5022` n `54` status `ready` deltaP `34.2254` edge `0.4343` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.5022` n `54` status `ready` deltaP `34.2254` edge `0.4343` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `4.4163` n `117` status `ready` deltaP `-3.7719` edge `0.4578` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `1.801` n `117` status `ready` deltaP `14.0156` edge `0.1634` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.3208` n `117` status `ready` deltaP `6.8594` edge `0.1449` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3276` n `117` status `ready` deltaP `14.3749` edge `0.036` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.2979` n `54` status `ready` deltaP `2.301` edge `0.0187` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2979` n `54` status `ready` deltaP `2.301` edge `0.0187` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3047` n `117` status `ready` deltaP `1.5477` edge `0.0023` maxDD `-0.3742`
- `market_context_high->metal_1h` score `-0.3674` n `117` status `ready` deltaP `7.4147` edge `0.0069` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4532` n `54` status `ready` deltaP `2.0016` edge `0.0017` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4532` n `54` status `ready` deltaP `2.0016` edge `0.0017` maxDD `-0.8513`
- `risk_on_high->crypto_alt_1h` score `-0.5626` n `54` status `ready` deltaP `3.7592` edge `0.0054` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.5626` n `54` status `ready` deltaP `3.7592` edge `0.0054` maxDD `-5.8734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
