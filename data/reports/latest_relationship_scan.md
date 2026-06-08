# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T23:22:21.780274+00:00`
- Price records: `672`
- Market context records: `3326`
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

- `risk_on_high->crypto_major_4h` score `15.8303` n `32` status `ready` deltaP `30.1829` edge `1.2302` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8303` n `32` status `ready` deltaP `30.1829` edge `1.2302` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `15.2727` n `141` status `ready` deltaP `22.7985` edge `2.7902` maxDD `-70.3986`
- `market_context_high->index_24h` score `11.3276` n `141` status `ready` deltaP `34.3823` edge `0.9702` maxDD `-16.1026`
- `market_context_high->equity_24h` score `9.9707` n `141` status `ready` deltaP `27.6928` edge `1.9353` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.2584` n `32` status `ready` deltaP `9.2226` edge `0.7278` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.2584` n `32` status `ready` deltaP `9.2226` edge `0.7278` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.5147` n `32` status `ready` deltaP `13.6433` edge `0.4731` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5147` n `32` status `ready` deltaP `13.6433` edge `0.4731` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `3.4663` n `141` status `ready` deltaP `24.2723` edge `2.3525` maxDD `-152.2601`
- `risk_on_high->crypto_major_1h` score `2.0899` n `32` status `ready` deltaP `7.1669` edge `0.3271` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.0899` n `32` status `ready` deltaP `7.1669` edge `0.3271` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `1.7694` n `186` status `ready` deltaP `16.9158` edge `0.1305` maxDD `-3.9989`
- `market_context_high->commodity_24h` score `1.4141` n `141` status `ready` deltaP `23.9029` edge `0.4556` maxDD `-23.6927`
- `risk_on_high->index_4h` score `1.0147` n `32` status `ready` deltaP `0.3811` edge `0.1863` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.0147` n `32` status `ready` deltaP `0.3811` edge `0.1863` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.2876` n `32` status `ready` deltaP `6.3997` edge `0.0627` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2876` n `32` status `ready` deltaP `6.3997` edge `0.0627` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2821` n `32` status `ready` deltaP `0.7485` edge `0.1749` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2821` n `32` status `ready` deltaP `0.7485` edge `0.1749` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
