# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T18:22:24.604977+00:00`
- Price records: `672`
- Market context records: `3304`
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

- `risk_on_high->crypto_major_4h` score `15.8177` n `32` status `ready` deltaP `29.7256` edge `1.2322` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8177` n `32` status `ready` deltaP `29.7256` edge `1.2322` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `14.3396` n `121` status `ready` deltaP `19.8233` edge `2.6904` maxDD `-70.3986`
- `market_context_high->index_24h` score `10.1202` n `121` status `ready` deltaP `31.8598` edge `0.8864` maxDD `-16.1026`
- `market_context_high->commodity_24h` score `8.4695` n `121` status `ready` deltaP `34.1239` edge `0.6193` maxDD `-6.9466`
- `market_context_high->equity_24h` score `8.038` n `121` status `ready` deltaP `23.0601` edge `1.7184` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.4445` n `32` status `ready` deltaP `10.2896` edge `0.7362` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.4445` n `32` status `ready` deltaP `10.2896` edge `0.7362` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.5836` n `32` status `ready` deltaP `13.9482` edge `0.4799` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5836` n `32` status `ready` deltaP `13.9482` edge `0.4799` maxDD `-5.7426`
- `market_context_high->commodity_4h` score `2.1353` n `182` status `ready` deltaP `19.6596` edge `0.1427` maxDD `-3.9989`
- `risk_on_high->crypto_major_1h` score `2.0736` n `32` status `ready` deltaP `7.1669` edge `0.325` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.0736` n `32` status `ready` deltaP `7.1669` edge `0.325` maxDD `-5.8885`
- `market_context_high->crypto_major_24h` score `2.0348` n `121` status `ready` deltaP `20.5937` edge `2.1935` maxDD `-152.2601`
- `risk_on_high->index_4h` score `1.0963` n `32` status `ready` deltaP `0.9909` edge `0.1927` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.0963` n `32` status `ready` deltaP `0.9909` edge `0.1927` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.2954` n `32` status `ready` deltaP `6.5494` edge `0.0627` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2954` n `32` status `ready` deltaP `6.5494` edge `0.0627` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2314` n `32` status `ready` deltaP `0.4491` edge `0.1704` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2314` n `32` status `ready` deltaP `0.4491` edge `0.1704` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
