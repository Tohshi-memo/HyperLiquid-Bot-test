# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T22:07:38.999736+00:00`
- Price records: `672`
- Market context records: `3321`
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

- `risk_on_high->crypto_major_4h` score `15.8133` n `32` status `ready` deltaP `30.0305` edge `1.2298` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8133` n `32` status `ready` deltaP `30.0305` edge `1.2298` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `15.6169` n `136` status `ready` deltaP `22.2324` edge `2.8381` maxDD `-70.3986`
- `market_context_high->index_24h` score `11.0552` n `136` status `ready` deltaP `33.7826` edge `0.9515` maxDD `-16.1026`
- `market_context_high->equity_24h` score `9.6211` n `136` status `ready` deltaP `26.6237` edge `1.8976` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.226` n `32` status `ready` deltaP `9.2226` edge `0.7251` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.226` n `32` status `ready` deltaP `9.2226` edge `0.7251` maxDD `-11.7537`
- `market_context_high->crypto_major_24h` score `3.6776` n `136` status `ready` deltaP `23.5499` edge `2.3844` maxDD `-152.2601`
- `risk_on_high->equity_4h` score `3.5383` n `32` status `ready` deltaP `13.7957` edge `0.4751` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5383` n `32` status `ready` deltaP `13.7957` edge `0.4751` maxDD `-5.7426`
- `market_context_high->commodity_24h` score `2.2602` n `136` status `ready` deltaP `25.8681` edge `0.4865` maxDD `-20.2016`
- `risk_on_high->crypto_major_1h` score `2.0463` n `32` status `ready` deltaP `7.0172` edge `0.3225` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.0463` n `32` status `ready` deltaP `7.0172` edge `0.3225` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `1.8914` n `185` status `ready` deltaP `17.9004` edge `0.1341` maxDD `-3.9989`
- `risk_on_high->index_4h` score `1.046` n `32` status `ready` deltaP `0.5335` edge `0.1893` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.046` n `32` status `ready` deltaP `0.5335` edge `0.1893` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.2642` n `32` status `ready` deltaP `6.1003` edge `0.0617` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2642` n `32` status `ready` deltaP `6.1003` edge `0.0617` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2041` n `32` status `ready` deltaP `0.2994` edge `0.1679` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2041` n `32` status `ready` deltaP `0.2994` edge `0.1679` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
