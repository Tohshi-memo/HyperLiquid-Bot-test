# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T07:07:28.387943+00:00`
- Price records: `672`
- Market context records: `3663`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13157`

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

- `risk_on_high->crypto_major_24h` score `34.709` n `32` status `ready` deltaP `39.5833` edge `2.6328` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.709` n `32` status `ready` deltaP `39.5833` edge `2.6328` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `29.9841` n `32` status `ready` deltaP `41.6667` edge `2.2209` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `29.9841` n `32` status `ready` deltaP `41.6667` edge `2.2209` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `26.5783` n `32` status `ready` deltaP `38.7153` edge `1.9719` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `26.5783` n `32` status `ready` deltaP `38.7153` edge `1.9719` maxDD `-0.8779`
- `risk_on_high->index_24h` score `16.8993` n `32` status `ready` deltaP `41.6667` edge `1.1305` maxDD `0.0`
- `risk_on_and_context->index_24h` score `16.8993` n `32` status `ready` deltaP `41.6667` edge `1.1305` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.4018` n `32` status `ready` deltaP `20.4268` edge `0.9262` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.4018` n `32` status `ready` deltaP `20.4268` edge `0.9262` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `8.4825` n `32` status `ready` deltaP `27.2569` edge `0.5513` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `8.4825` n `32` status `ready` deltaP `27.2569` edge `0.5513` maxDD `-0.7574`
- `market_context_high->index_24h` score `6.5033` n `157` status `ready` deltaP `27.017` edge `0.5334` maxDD `-11.3924`
- `market_context_high->equity_24h` score `5.6962` n `157` status `ready` deltaP `18.7368` edge `0.9162` maxDD `-35.3144`
- `risk_on_high->crypto_alt_4h` score `2.601` n `32` status `ready` deltaP `0.686` edge `0.3966` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.601` n `32` status `ready` deltaP `0.686` edge `0.3966` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.5819` n `32` status `ready` deltaP `9.9848` edge `0.3779` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5819` n `32` status `ready` deltaP `9.9848` edge `0.3779` maxDD `-5.7426`
- `market_context_high->metal_24h` score `1.7328` n `157` status `ready` deltaP `21.5642` edge `0.4736` maxDD `-21.6171`
- `risk_on_high->crypto_major_1h` score `1.3033` n `32` status `ready` deltaP `3.5741` edge `0.2502` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
