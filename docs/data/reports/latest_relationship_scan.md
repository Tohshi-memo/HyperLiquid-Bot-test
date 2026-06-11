# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T17:07:34.122937+00:00`
- Price records: `672`
- Market context records: `3604`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13138`

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

- `risk_on_high->crypto_major_24h` score `45.7828` n `32` status `ready` deltaP `49.3056` edge `3.4908` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `45.7828` n `32` status `ready` deltaP `49.3056` edge `3.4908` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `42.4036` n `32` status `ready` deltaP `51.2153` edge `3.1922` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `42.4036` n `32` status `ready` deltaP `51.2153` edge `3.1922` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `38.9373` n `32` status `ready` deltaP `48.4375` edge `2.937` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `38.9373` n `32` status `ready` deltaP `48.4375` edge `2.937` maxDD `-0.8779`
- `risk_on_high->index_24h` score `24.7775` n `32` status `ready` deltaP `51.3889` edge `1.7222` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.7775` n `32` status `ready` deltaP `51.3889` edge `1.7222` maxDD `0.0`
- `risk_on_high->metal_24h` score `17.7988` n `32` status `ready` deltaP `36.8056` edge `1.264` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `17.7988` n `32` status `ready` deltaP `36.8056` edge `1.264` maxDD `-0.7574`
- `market_context_high->equity_24h` score `16.6293` n `157` status `ready` deltaP `27.6484` edge `1.8427` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `13.3927` n `32` status `ready` deltaP `25.1524` edge `1.0606` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.3927` n `32` status `ready` deltaP `25.1524` edge `1.0606` maxDD `-5.9781`
- `market_context_high->index_24h` score `13.3755` n `157` status `ready` deltaP `36.1023` edge `1.0956` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `10.3296` n `157` status `ready` deltaP `14.851` edge `1.5349` maxDD `-54.8486`
- `market_context_high->metal_24h` score `7.0049` n `157` status `ready` deltaP `30.476` edge `1.1489` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `5.1731` n `32` status `ready` deltaP `5.7165` edge `0.5774` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.1731` n `32` status `ready` deltaP `5.7165` edge `0.5774` maxDD `-11.7537`
- `market_context_high->crypto_alt_24h` score `4.8853` n `157` status `ready` deltaP `8.8873` edge `1.1521` maxDD `-56.6728`
- `risk_on_high->equity_4h` score `3.6765` n `32` status `ready` deltaP `15.0152` edge `0.4847` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
