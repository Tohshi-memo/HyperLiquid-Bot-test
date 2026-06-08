# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T21:37:26.379980+00:00`
- Price records: `672`
- Market context records: `3319`
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

- `risk_on_high->crypto_major_4h` score `15.8507` n `32` status `ready` deltaP `30.1829` edge `1.2319` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8507` n `32` status `ready` deltaP `30.1829` edge `1.2319` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `15.4764` n `134` status `ready` deltaP `21.976` edge `2.8218` maxDD `-70.3986`
- `market_context_high->index_24h` score `10.909` n `134` status `ready` deltaP `33.5302` edge `0.941` maxDD `-16.1026`
- `market_context_high->equity_24h` score `9.4222` n `134` status `ready` deltaP `26.1738` edge `1.8751` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.2597` n `32` status `ready` deltaP `9.375` edge `0.7269` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.2597` n `32` status `ready` deltaP `9.375` edge `0.7269` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.5531` n `32` status `ready` deltaP `13.7957` edge `0.477` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5531` n `32` status `ready` deltaP `13.7957` edge `0.477` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `3.4978` n `134` status `ready` deltaP `23.2276` edge `2.3635` maxDD `-152.2601`
- `market_context_high->commodity_24h` score `2.694` n `134` status `ready` deltaP `26.8138` edge `0.5039` maxDD `-18.3151`
- `risk_on_high->crypto_major_1h` score `2.0237` n `32` status `ready` deltaP `6.8675` edge `0.3206` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.0237` n `32` status `ready` deltaP `6.8675` edge `0.3206` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `1.9204` n `185` status `ready` deltaP `18.0529` edge `0.1355` maxDD `-3.9989`
- `risk_on_high->index_4h` score `1.0664` n `32` status `ready` deltaP `0.686` edge `0.1909` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.0664` n `32` status `ready` deltaP `0.686` edge `0.1909` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.2635` n `32` status `ready` deltaP `6.1003` edge `0.0616` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2635` n `32` status `ready` deltaP `6.1003` edge `0.0616` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.1838` n `32` status `ready` deltaP `0.1497` edge `0.1663` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.1838` n `32` status `ready` deltaP `0.1497` edge `0.1663` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
