# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T21:22:24.398893+00:00`
- Price records: `672`
- Market context records: `3318`
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

- `risk_on_high->crypto_major_4h` score `15.8893` n `32` status `ready` deltaP `30.3354` edge `1.2341` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8893` n `32` status `ready` deltaP `30.3354` edge `1.2341` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `15.3625` n `133` status `ready` deltaP `21.841` edge `2.8081` maxDD `-70.3986`
- `market_context_high->index_24h` score `10.8591` n `133` status `ready` deltaP `33.4012` edge `0.9377` maxDD `-16.1026`
- `market_context_high->equity_24h` score `9.3252` n `133` status `ready` deltaP `25.9437` edge `1.8642` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.2995` n `32` status `ready` deltaP `9.5274` edge `0.7292` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.2995` n `32` status `ready` deltaP `9.5274` edge `0.7292` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.5593` n `32` status `ready` deltaP `13.7957` edge `0.4778` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5593` n `32` status `ready` deltaP `13.7957` edge `0.4778` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `3.3743` n `133` status `ready` deltaP `23.0589` edge `2.3488` maxDD `-152.2601`
- `market_context_high->commodity_24h` score `2.885` n `133` status `ready` deltaP `27.2125` edge `0.5109` maxDD `-17.4618`
- `risk_on_high->crypto_major_1h` score `2.0431` n `32` status `ready` deltaP `7.0172` edge `0.3221` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.0431` n `32` status `ready` deltaP `7.0172` edge `0.3221` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `1.941` n `185` status `ready` deltaP `18.2053` edge `0.1362` maxDD `-3.9989`
- `risk_on_high->index_4h` score `1.0696` n `32` status `ready` deltaP `0.686` edge `0.1913` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.0696` n `32` status `ready` deltaP `0.686` edge `0.1913` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.2658` n `32` status `ready` deltaP `6.1003` edge `0.0619` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2658` n `32` status `ready` deltaP `6.1003` edge `0.0619` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2065` n `32` status `ready` deltaP `0.2994` edge `0.1682` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2065` n `32` status `ready` deltaP `0.2994` edge `0.1682` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
