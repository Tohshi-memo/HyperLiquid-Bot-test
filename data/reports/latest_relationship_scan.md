# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T18:07:32.727024+00:00`
- Price records: `672`
- Market context records: `3608`
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

- `risk_on_high->crypto_major_24h` score `45.03` n `32` status `ready` deltaP `48.6111` edge `3.4327` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `45.03` n `32` status `ready` deltaP `48.6111` edge `3.4327` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `41.7848` n `32` status `ready` deltaP `50.6944` edge `3.1441` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `41.7848` n `32` status `ready` deltaP `50.6944` edge `3.1441` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `38.0442` n `32` status `ready` deltaP `47.7431` edge `2.8672` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `38.0442` n `32` status `ready` deltaP `47.7431` edge `2.8672` maxDD `-0.8779`
- `risk_on_high->index_24h` score `24.3812` n `32` status `ready` deltaP `50.6944` edge `1.6938` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.3812` n `32` status `ready` deltaP `50.6944` edge `1.6938` maxDD `0.0`
- `risk_on_high->metal_24h` score `17.3588` n `32` status `ready` deltaP `36.2847` edge `1.2308` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `17.3588` n `32` status `ready` deltaP `36.2847` edge `1.2308` maxDD `-0.7574`
- `market_context_high->equity_24h` score `16.0547` n `158` status `ready` deltaP `27.2767` edge `1.7973` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `13.2505` n `32` status `ready` deltaP `24.6951` edge `1.0518` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.2505` n `32` status `ready` deltaP `24.6951` edge `1.0518` maxDD `-5.9781`
- `market_context_high->index_24h` score `13.0312` n `158` status `ready` deltaP `35.5045` edge `1.0709` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `9.7075` n `158` status `ready` deltaP `14.3943` edge `1.4861` maxDD `-54.8486`
- `market_context_high->metal_24h` score `6.8076` n `158` status `ready` deltaP `30.1929` edge `1.1255` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.9685` n `32` status `ready` deltaP `5.2591` edge `0.5634` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.9685` n `32` status `ready` deltaP `5.2591` edge `0.5634` maxDD `-11.7537`
- `market_context_high->crypto_alt_24h` score `4.1709` n `158` status `ready` deltaP `8.463` edge `1.0954` maxDD `-56.6728`
- `risk_on_high->equity_4h` score `3.5865` n `32` status `ready` deltaP `14.5579` edge `0.4762` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
