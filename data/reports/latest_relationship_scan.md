# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T06:37:29.001052+00:00`
- Price records: `672`
- Market context records: `3867`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13676`

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

- `risk_on_high->unknown_4h` score `48.6567` n `72` status `ready` deltaP `7.876` edge `6.3997` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `48.6567` n `72` status `ready` deltaP `7.876` edge `6.3997` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.213` n `32` status `ready` deltaP `34.0278` edge `2.6285` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.213` n `32` status `ready` deltaP `34.0278` edge `2.6285` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.9039` n `32` status `ready` deltaP `42.0139` edge `1.9619` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.9039` n `32` status `ready` deltaP `42.0139` edge `1.9619` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.3761` n `32` status `ready` deltaP `31.5972` edge `1.7525` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.3761` n `32` status `ready` deltaP `31.5972` edge `1.7525` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.2116` n `32` status `ready` deltaP `30.5556` edge `0.7306` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.2116` n `32` status `ready` deltaP `30.5556` edge `0.7306` maxDD `0.0`
- `market_context_high->unknown_4h` score `7.984` n `206` status `ready` deltaP `0.0281` edge `1.5643` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.6729` n `135` status `ready` deltaP `16.088` edge `0.7518` maxDD `-14.5715`
- `market_context_high->index_24h` score `5.6926` n `135` status `ready` deltaP `25.3704` edge `0.4192` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `5.5718` n `72` status `ready` deltaP `19.4613` edge `0.4468` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.5718` n `72` status `ready` deltaP `19.4613` edge `0.4468` maxDD `-5.9781`
- `market_context_high->unknown_24h` score `3.7929` n `135` status `ready` deltaP `-21.4121` edge `3.4772` maxDD `-200.1879`
- `market_context_high->metal_24h` score `3.5067` n `135` status `ready` deltaP `20.8796` edge `0.2962` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.6701` n `72` status `ready` deltaP `26.1687` edge `0.1615` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6701` n `72` status `ready` deltaP `26.1687` edge `0.1615` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.1915` n `135` status `ready` deltaP `2.338` edge `0.6134` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
