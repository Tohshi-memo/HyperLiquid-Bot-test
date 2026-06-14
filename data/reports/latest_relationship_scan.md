# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T06:52:33.658935+00:00`
- Price records: `672`
- Market context records: `3868`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13656`

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

- `risk_on_high->unknown_4h` score `48.5997` n `72` status `ready` deltaP `7.876` edge `6.3924` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `48.5997` n `72` status `ready` deltaP `7.876` edge `6.3924` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.2298` n `32` status `ready` deltaP `34.0278` edge `2.6299` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.2298` n `32` status `ready` deltaP `34.0278` edge `2.6299` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.8895` n `32` status `ready` deltaP `42.0139` edge `1.9607` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.8895` n `32` status `ready` deltaP `42.0139` edge `1.9607` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.3629` n `32` status `ready` deltaP `31.5972` edge `1.7514` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.3629` n `32` status `ready` deltaP `31.5972` edge `1.7514` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.1906` n `32` status `ready` deltaP `30.3819` edge `0.73` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.1906` n `32` status `ready` deltaP `30.3819` edge `0.73` maxDD `0.0`
- `market_context_high->unknown_4h` score `7.9271` n `206` status `ready` deltaP `0.0281` edge `1.557` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.6414` n `136` status `ready` deltaP `16.2786` edge `0.7479` maxDD `-14.5715`
- `market_context_high->index_24h` score `5.6326` n `136` status `ready` deltaP `25.2348` edge `0.4151` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `5.596` n `72` status `ready` deltaP `19.6138` edge `0.4478` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.596` n `72` status `ready` deltaP `19.6138` edge `0.4478` maxDD `-5.9781`
- `market_context_high->metal_24h` score `3.4791` n `136` status `ready` deltaP `20.864` edge `0.294` maxDD `-9.1203`
- `market_context_high->unknown_24h` score `3.1498` n `136` status `ready` deltaP `-21.6299` edge `3.3962` maxDD `-200.1879`
- `risk_on_high->equity_4h` score `2.6531` n `72` status `ready` deltaP `26.0162` edge `0.1611` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6531` n `72` status `ready` deltaP `26.0162` edge `0.1611` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.2251` n `136` status `ready` deltaP `2.594` edge `0.6145` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
