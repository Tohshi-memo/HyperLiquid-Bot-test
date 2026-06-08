# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T21:09:16.349583+00:00`
- Price records: `672`
- Market context records: `3317`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13151`

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

- `risk_on_high->crypto_major_4h` score `15.9013` n `32` status `ready` deltaP `30.3354` edge `1.2351` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.9013` n `32` status `ready` deltaP `30.3354` edge `1.2351` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `15.2781` n `132` status `ready` deltaP `21.7014` edge `2.7982` maxDD `-70.3986`
- `market_context_high->index_24h` score `10.8018` n `132` status `ready` deltaP `33.2702` edge `0.9338` maxDD `-16.1026`
- `market_context_high->equity_24h` score `9.221` n `132` status `ready` deltaP `25.7102` edge `1.8524` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.3079` n `32` status `ready` deltaP `9.5274` edge `0.7299` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.3079` n `32` status `ready` deltaP `9.5274` edge `0.7299` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.5671` n `32` status `ready` deltaP `13.7957` edge `0.4788` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5671` n `32` status `ready` deltaP `13.7957` edge `0.4788` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `3.2623` n `132` status `ready` deltaP `22.8851` edge `2.3356` maxDD `-152.2601`
- `market_context_high->commodity_24h` score `3.0232` n `132` status `ready` deltaP `27.6199` edge `0.5142` maxDD `-16.8593`
- `risk_on_high->crypto_major_1h` score `2.0509` n `32` status `ready` deltaP `7.0172` edge `0.3231` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.0509` n `32` status `ready` deltaP `7.0172` edge `0.3231` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `1.9604` n `185` status `ready` deltaP `18.3577` edge `0.1368` maxDD `-3.9989`
- `risk_on_high->index_4h` score `1.0837` n `32` status `ready` deltaP `0.8384` edge `0.1921` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.0837` n `32` status `ready` deltaP `0.8384` edge `0.1921` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.2775` n `32` status `ready` deltaP `6.25` edge `0.0624` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2775` n `32` status `ready` deltaP `6.25` edge `0.0624` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.222` n `32` status `ready` deltaP `0.4491` edge `0.1692` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.222` n `32` status `ready` deltaP `0.4491` edge `0.1692` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
