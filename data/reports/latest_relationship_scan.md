# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T17:07:27.552950+00:00`
- Price records: `672`
- Market context records: `3299`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13141`

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

- `risk_on_high->crypto_major_4h` score `15.8479` n `32` status `ready` deltaP `29.878` edge `1.2337` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8479` n `32` status `ready` deltaP `29.878` edge `1.2337` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `14.0473` n `116` status `ready` deltaP `18.732` edge `2.6602` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `9.8975` n `116` status `ready` deltaP `37.0629` edge `0.6615` maxDD `-4.037`
- `market_context_high->index_24h` score `9.8117` n `116` status `ready` deltaP `31.2141` edge `0.865` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `7.5701` n `32` status `ready` deltaP `10.8994` edge `0.7426` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.5701` n `32` status `ready` deltaP `10.8994` edge `0.7426` maxDD `-11.7537`
- `market_context_high->equity_24h` score `7.55` n `116` status `ready` deltaP `22.1205` edge `1.6621` maxDD `-53.663`
- `risk_on_high->equity_4h` score `3.6886` n `32` status `ready` deltaP `14.5579` edge `0.4893` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.6886` n `32` status `ready` deltaP `14.5579` edge `0.4893` maxDD `-5.7426`
- `market_context_high->commodity_4h` score `2.0649` n `177` status `ready` deltaP `18.9894` edge `0.1413` maxDD `-3.9989`
- `risk_on_high->crypto_major_1h` score `2.0463` n `32` status `ready` deltaP `6.8675` edge `0.3235` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.0463` n `32` status `ready` deltaP `6.8675` edge `0.3235` maxDD `-5.8885`
- `market_context_high->crypto_major_24h` score `1.5177` n `116` status `ready` deltaP `19.2888` edge `2.1359` maxDD `-152.2601`
- `risk_on_high->index_4h` score `1.1332` n `32` status `ready` deltaP `1.2957` edge `0.1954` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.1332` n `32` status `ready` deltaP `1.2957` edge `0.1954` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.2806` n `32` status `ready` deltaP `6.3997` edge `0.0618` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2806` n `32` status `ready` deltaP `6.3997` edge `0.0618` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2423` n `32` status `ready` deltaP `0.5988` edge `0.1708` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2423` n `32` status `ready` deltaP `0.5988` edge `0.1708` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
