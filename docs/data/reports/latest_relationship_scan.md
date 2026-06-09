# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T04:41:30.245262+00:00`
- Price records: `672`
- Market context records: `3349`
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

- `risk_on_high->crypto_major_24h` score `58.7965` n `32` status `ready` deltaP `62.8472` edge `4.485` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `58.7965` n `32` status `ready` deltaP `62.8472` edge `4.485` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `54.6494` n `32` status `ready` deltaP `57.6389` edge `4.185` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `54.6494` n `32` status `ready` deltaP `57.6389` edge `4.185` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `46.6593` n `32` status `ready` deltaP `56.7708` edge `3.5098` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `46.6593` n `32` status `ready` deltaP `56.7708` edge `3.5098` maxDD `0.0`
- `risk_on_high->index_24h` score `23.2274` n `32` status `ready` deltaP `50.8681` edge `1.5965` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.2274` n `32` status `ready` deltaP `50.8681` edge `1.5965` maxDD `0.0`
- `risk_on_high->metal_24h` score `16.0535` n `32` status `ready` deltaP `35.7639` edge `1.1255` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.0535` n `32` status `ready` deltaP `35.7639` edge `1.1255` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `16.0259` n `32` status `ready` deltaP `30.1829` edge `1.2465` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.0259` n `32` status `ready` deltaP `30.1829` edge `1.2465` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `12.4822` n `162` status `ready` deltaP `17.554` edge `2.4674` maxDD `-70.3986`
- `market_context_high->index_24h` score `12.1297` n `162` status `ready` deltaP `36.0533` edge `1.0259` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.8352` n `162` status `ready` deltaP `31.4622` edge `2.021` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.8737` n `32` status `ready` deltaP `9.9848` edge `0.774` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.8737` n `32` status `ready` deltaP `9.9848` edge `0.774` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.7215` n `32` status `ready` deltaP `14.7104` edge `0.4925` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.7215` n `32` status `ready` deltaP `14.7104` edge `0.4925` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `2.0993` n `32` status `ready` deltaP `6.8675` edge `0.3303` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
