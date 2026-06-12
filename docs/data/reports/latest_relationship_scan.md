# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T14:52:34.939505+00:00`
- Price records: `672`
- Market context records: `3696`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12897`

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

- `risk_on_high->crypto_major_24h` score `31.0805` n `32` status `ready` deltaP `34.2014` edge `2.3663` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `31.0805` n `32` status `ready` deltaP `34.2014` edge `2.3663` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `24.1543` n `32` status `ready` deltaP `36.4583` edge `1.7698` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `24.1543` n `32` status `ready` deltaP `36.4583` edge `1.7698` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `22.8982` n `32` status `ready` deltaP `33.3333` edge `1.7011` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `22.8982` n `32` status `ready` deltaP `33.3333` edge `1.7011` maxDD `-0.8779`
- `risk_on_high->index_24h` score `13.1088` n `32` status `ready` deltaP `36.2847` edge `0.8505` maxDD `0.0`
- `risk_on_and_context->index_24h` score `13.1088` n `32` status `ready` deltaP `36.2847` edge `0.8505` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.2973` n `32` status `ready` deltaP `18.1402` edge `0.8494` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.2973` n `32` status `ready` deltaP `18.1402` edge `0.8494` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `3.6852` n `32` status `ready` deltaP `21.875` edge `0.1874` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `3.6852` n `32` status `ready` deltaP `21.875` edge `0.1874` maxDD `-0.7574`
- `market_context_high->index_24h` score `3.4624` n `157` status `ready` deltaP `22.272` edge `0.2782` maxDD `-9.0519`
- `risk_on_high->equity_4h` score `1.8268` n `32` status `ready` deltaP `8.9177` edge `0.2882` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.8268` n `32` status `ready` deltaP `8.9177` edge `0.2882` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.6249` n `32` status `ready` deltaP `-1.6006` edge `0.3305` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.6249` n `32` status `ready` deltaP `-1.6006` edge `0.3305` maxDD `-11.7537`
- `risk_on_high->crypto_major_1h` score `1.0632` n `32` status `ready` deltaP `1.9274` edge `0.2304` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.0632` n `32` status `ready` deltaP `1.9274` edge `0.2304` maxDD `-5.8885`
- `market_context_high->equity_24h` score `1.0254` n `157` status `ready` deltaP `14.1653` edge `0.5047` maxDD `-31.4279`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
