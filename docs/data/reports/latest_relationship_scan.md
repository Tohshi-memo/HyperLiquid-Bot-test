# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T02:37:23.056690+00:00`
- Price records: `672`
- Market context records: `3340`
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

- `risk_on_high->crypto_major_24h` score `61.3408` n `31` status `ready` deltaP `66.3194` edge `4.6696` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `61.3408` n `31` status `ready` deltaP `66.3194` edge `4.6696` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `56.9778` n `31` status `ready` deltaP `60.9375` edge `4.3419` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `56.9778` n `31` status `ready` deltaP `60.9375` edge `4.3419` maxDD `0.0`
- `risk_on_high->equity_24h` score `46.9029` n `31` status `ready` deltaP `56.7708` edge `3.5301` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `46.9029` n `31` status `ready` deltaP `56.7708` edge `3.5301` maxDD `0.0`
- `risk_on_high->index_24h` score `23.1674` n `31` status `ready` deltaP `50.8681` edge `1.5915` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.1674` n `31` status `ready` deltaP `50.8681` edge `1.5915` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `16.0993` n `32` status `ready` deltaP `30.3354` edge `1.2516` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.0993` n `32` status `ready` deltaP `30.3354` edge `1.2516` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `16.0517` n `31` status `ready` deltaP `35.2766` edge `1.1286` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.0517` n `31` status `ready` deltaP `35.2766` edge `1.1286` maxDD `-0.7574`
- `market_context_high->crypto_alt_24h` score `13.5929` n `154` status `ready` deltaP `20.0284` edge `2.5933` maxDD `-70.3986`
- `market_context_high->index_24h` score `11.7585` n `154` status `ready` deltaP `35.2837` edge `1.0001` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.4946` n `154` status `ready` deltaP `30.1474` edge `1.9861` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.8211` n `32` status `ready` deltaP `10.1372` edge `0.7686` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.8211` n `32` status `ready` deltaP `10.1372` edge `0.7686` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.6879` n `32` status `ready` deltaP `14.5579` edge `0.4892` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.6879` n `32` status `ready` deltaP `14.5579` edge `0.4892` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `2.1726` n `32` status `ready` deltaP `7.4663` edge `0.3357` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
