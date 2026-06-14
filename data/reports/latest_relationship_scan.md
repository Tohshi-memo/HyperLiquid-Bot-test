# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T04:07:28.330157+00:00`
- Price records: `672`
- Market context records: `3856`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13683`

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

- `risk_on_high->unknown_4h` score `49.9428` n `71` status `ready` deltaP `8.85` edge `6.5581` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `49.9428` n `71` status `ready` deltaP `8.85` edge `6.5581` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.0954` n `32` status `ready` deltaP `34.0278` edge `2.6187` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.0954` n `32` status `ready` deltaP `34.0278` edge `2.6187` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.8967` n `32` status `ready` deltaP `42.0139` edge `1.9613` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.8967` n `32` status `ready` deltaP `42.0139` edge `1.9613` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.6343` n `32` status `ready` deltaP `31.9444` edge `1.7717` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.6343` n `32` status `ready` deltaP `31.9444` edge `1.7717` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.3128` n `32` status `ready` deltaP `31.25` edge `0.7344` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.3128` n `32` status `ready` deltaP `31.25` edge `0.7344` maxDD `0.0`
- `market_context_high->unknown_24h` score `8.8754` n `128` status `ready` deltaP `-19.7917` edge `4.118` maxDD `-200.1879`
- `market_context_high->unknown_4h` score `8.3721` n `205` status `ready` deltaP `0.4268` edge `1.6114` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.7683` n `128` status `ready` deltaP `14.6701` edge `0.7692` maxDD `-14.5715`
- `market_context_high->index_24h` score `6.0867` n `128` status `ready` deltaP `25.7812` edge `0.4493` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `5.1604` n `71` status `ready` deltaP `17.6786` edge `0.4244` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.1604` n `71` status `ready` deltaP `17.6786` edge `0.4244` maxDD `-5.9781`
- `market_context_high->metal_24h` score `3.7508` n `128` status `ready` deltaP `21.441` edge `0.3128` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.5729` n `71` status `ready` deltaP `25.6291` edge `0.157` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5729` n `71` status `ready` deltaP `25.6291` edge `0.157` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `1.5051` n `128` status `ready` deltaP `0.434` edge `0.5689` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
