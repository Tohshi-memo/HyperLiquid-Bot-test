# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T10:37:30.343928+00:00`
- Price records: `672`
- Market context records: `7556`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14475`

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

- `risk_on_high->crypto_major_4h` score `7.1322` n `32` status `ready` deltaP `41.3872` edge `0.3377` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.1322` n `32` status `ready` deltaP `41.3872` edge `0.3377` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `6.8744` n `32` status `ready` deltaP `19.4444` edge `0.5209` maxDD `-4.8796`
- `risk_on_and_context->crypto_major_24h` score `6.8744` n `32` status `ready` deltaP `19.4444` edge `0.5209` maxDD `-4.8796`
- `risk_on_high->unknown_4h` score `4.8032` n `32` status `ready` deltaP `13.5671` edge `0.3528` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.8032` n `32` status `ready` deltaP `13.5671` edge `0.3528` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.1424` n `32` status `ready` deltaP `29.6494` edge `0.1719` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.1424` n `32` status `ready` deltaP `29.6494` edge `0.1719` maxDD `-0.9492`
- `risk_on_high->crypto_alt_24h` score `3.7544` n `32` status `ready` deltaP `18.4028` edge `0.2519` maxDD `-3.6039`
- `risk_on_and_context->crypto_alt_24h` score `3.7544` n `32` status `ready` deltaP `18.4028` edge `0.2519` maxDD `-3.6039`
- `risk_on_high->crypto_major_1h` score `2.7199` n `32` status `ready` deltaP `24.7006` edge `0.0835` maxDD `-0.7209`
- `risk_on_and_context->crypto_major_1h` score `2.7199` n `32` status `ready` deltaP `24.7006` edge `0.0835` maxDD `-0.7209`
- `risk_on_high->equity_24h` score `0.9711` n `31` status `ready` deltaP `12.8639` edge `0.1733` maxDD `-8.4314`
- `risk_on_and_context->equity_24h` score `0.9711` n `31` status `ready` deltaP `12.8639` edge `0.1733` maxDD `-8.4314`
- `risk_on_high->unknown_24h` score `0.8531` n `32` status `ready` deltaP `6.9444` edge `0.047` maxDD `-0.4433`
- `risk_on_and_context->unknown_24h` score `0.8531` n `32` status `ready` deltaP `6.9444` edge `0.047` maxDD `-0.4433`
- `risk_on_high->fx_24h` score `0.743` n `31` status `ready` deltaP `18.8659` edge `0.0151` maxDD `-1.3162`
- `risk_on_and_context->fx_24h` score `0.743` n `31` status `ready` deltaP `18.8659` edge `0.0151` maxDD `-1.3162`
- `risk_on_high->equity_1h` score `0.697` n `32` status `ready` deltaP `10.1539` edge `0.0552` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.697` n `32` status `ready` deltaP `10.1539` edge `0.0552` maxDD `-1.3497`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
