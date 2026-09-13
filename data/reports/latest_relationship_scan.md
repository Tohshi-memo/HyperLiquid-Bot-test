# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T08:37:30.319683+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12880`

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

- `market_context_high->unknown_24h` score `16560.226` n `59` status `ready` deltaP `13.6241` edge `1379.9332` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `389.1087` n `82` status `ready` deltaP `-5.2505` edge `32.5029` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `17.6738` n `82` status `ready` deltaP `31.7115` edge `1.3102` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.6476` n `82` status `ready` deltaP `37.589` edge `1.3671` maxDD `-9.098`
- `market_context_high->crypto_alt_24h` score `9.954` n `59` status `ready` deltaP `21.6661` edge `0.7678` maxDD `-3.9523`
- `market_context_high->equity_24h` score `8.4529` n `59` status `ready` deltaP `42.5671` edge `0.4966` maxDD `-4.4114`
- `news_risk_high->equity_24h` score `7.1306` n `82` status `ready` deltaP `20.5539` edge `0.6352` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.4503` n `82` status `ready` deltaP `45.7782` edge `0.25` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.5505` n `82` status `ready` deltaP `23.7043` edge `0.2666` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.2273` n `59` status `ready` deltaP `41.6667` edge `0.0745` maxDD `0.0`
- `market_context_high->index_24h` score `3.601` n `59` status `ready` deltaP `39.598` edge `0.0782` maxDD `-0.7014`
- `market_context_high->metal_24h` score `0.8936` n `59` status `ready` deltaP `12.9767` edge `0.1155` maxDD `-1.9958`
- `news_risk_high->index_4h` score `0.3589` n `82` status `ready` deltaP `11.7378` edge `0.0306` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.3153` n `65` status `ready` deltaP `10.1524` edge `0.1402` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.3153` n `65` status `ready` deltaP `10.1524` edge `0.1402` maxDD `-6.7304`
- `risk_on_high->fx_1h` score `0.134` n `65` status `ready` deltaP `5.0023` edge `0.0034` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.134` n `65` status `ready` deltaP `5.0023` edge `0.0034` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.1119` n `65` status `ready` deltaP `3.3141` edge `0.0016` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.1119` n `65` status `ready` deltaP `3.3141` edge `0.0016` maxDD `-0.3081`
- `market_context_high->fx_1h` score `-0.2408` n `134` status `ready` deltaP `1.9483` edge `-0.0014` maxDD `-0.5323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
