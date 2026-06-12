# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T10:47:56.306198+00:00`
- Price records: `672`
- Market context records: `3678`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12897`

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

- `risk_on_high->crypto_major_24h` score `33.0271` n `32` status `ready` deltaP `36.9792` edge `2.51` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `33.0271` n `32` status `ready` deltaP `36.9792` edge `2.51` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `27.1065` n `32` status `ready` deltaP `39.2361` edge `1.9973` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `27.1065` n `32` status `ready` deltaP `39.2361` edge `1.9973` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `24.7764` n `32` status `ready` deltaP `36.1111` edge `1.8391` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `24.7764` n `32` status `ready` deltaP `36.1111` edge `1.8391` maxDD `-0.8779`
- `risk_on_high->index_24h` score `14.9738` n `32` status `ready` deltaP `39.0625` edge `0.9874` maxDD `0.0`
- `risk_on_and_context->index_24h` score `14.9738` n `32` status `ready` deltaP `39.0625` edge `0.9874` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.2812` n `32` status `ready` deltaP `19.9695` edge `0.9192` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.2812` n `32` status `ready` deltaP `19.9695` edge `0.9192` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `6.059` n `32` status `ready` deltaP `24.6528` edge `0.3667` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `6.059` n `32` status `ready` deltaP `24.6528` edge `0.3667` maxDD `-0.7574`
- `market_context_high->index_24h` score `4.5778` n `157` status `ready` deltaP `24.4128` edge `0.3903` maxDD `-11.3924`
- `market_context_high->equity_24h` score `2.8185` n `157` status `ready` deltaP `16.3062` edge `0.6926` maxDD `-35.3144`
- `risk_on_high->equity_4h` score `2.4656` n `32` status `ready` deltaP `9.8323` edge `0.364` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4656` n `32` status `ready` deltaP `9.8323` edge `0.364` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `2.3854` n `32` status `ready` deltaP `0.0762` edge `0.3827` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.3854` n `32` status `ready` deltaP `0.0762` edge `0.3827` maxDD `-11.7537`
- `risk_on_high->crypto_major_1h` score `1.2581` n `32` status `ready` deltaP `2.9753` edge `0.2484` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.2581` n `32` status `ready` deltaP `2.9753` edge `0.2484` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
