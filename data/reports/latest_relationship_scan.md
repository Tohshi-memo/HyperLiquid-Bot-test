# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T19:37:29.674993+00:00`
- Price records: `672`
- Market context records: `3512`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13184`

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

- `risk_on_high->crypto_major_24h` score `53.85` n `32` status `ready` deltaP `57.8802` edge `4.1059` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `53.85` n `32` status `ready` deltaP `57.8802` edge `4.1059` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `50.1206` n `32` status `ready` deltaP `57.5336` edge `3.8083` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `50.1206` n `32` status `ready` deltaP `57.5336` edge `3.8083` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.2494` n `32` status `ready` deltaP `54.5927` edge `3.3235` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.2494` n `32` status `ready` deltaP `54.5927` edge `3.3235` maxDD `0.0`
- `risk_on_high->index_24h` score `24.48` n `32` status `ready` deltaP `51.2998` edge `1.698` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.48` n `32` status `ready` deltaP `51.2998` edge `1.698` maxDD `0.0`
- `market_context_high->equity_24h` score `18.6055` n `156` status `ready` deltaP `31.5158` edge `1.9816` maxDD `-40.9667`
- `market_context_high->crypto_major_24h` score `18.4159` n `156` status `ready` deltaP `23.1847` edge `2.1532` maxDD `-54.8486`
- `risk_on_high->metal_24h` score `16.8684` n `32` status `ready` deltaP `33.3947` edge `1.2092` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.8684` n `32` status `ready` deltaP `33.3947` edge `1.2092` maxDD `-0.7574`
- `market_context_high->crypto_alt_24h` score `16.0335` n `156` status `ready` deltaP `17.7099` edge `2.0223` maxDD `-56.6728`
- `risk_on_high->crypto_major_4h` score `14.9973` n `32` status `ready` deltaP `28.1107` edge `1.1746` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.9973` n `32` status `ready` deltaP `28.1107` edge `1.1746` maxDD `-5.9781`
- `market_context_high->index_24h` score `13.0953` n `156` status `ready` deltaP `35.9152` edge `1.0735` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.3467` n `32` status `ready` deltaP `9.4416` edge `0.7337` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.3467` n `32` status `ready` deltaP `9.4416` edge `0.7337` maxDD `-11.7537`
- `market_context_high->metal_24h` score `6.456` n `156` status `ready` deltaP `27.4652` edge `1.0986` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `3.8266` n `32` status `ready` deltaP `16.3099` edge `0.4953` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
