# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T01:22:28.710094+00:00`
- Price records: `672`
- Market context records: `3437`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13160`

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

- `risk_on_high->crypto_alt_24h` score `56.8445` n `32` status `ready` deltaP `60.4167` edge `4.3494` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `56.8445` n `32` status `ready` deltaP `60.4167` edge `4.3494` maxDD `-0.8779`
- `risk_on_high->crypto_major_24h` score `56.3973` n `32` status `ready` deltaP `58.5069` edge `4.314` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `56.3973` n `32` status `ready` deltaP `58.5069` edge `4.314` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `45.1925` n `32` status `ready` deltaP `56.0764` edge `3.3922` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.1925` n `32` status `ready` deltaP `56.0764` edge `3.3922` maxDD `0.0`
- `risk_on_high->index_24h` score `23.8835` n `32` status `ready` deltaP `51.3889` edge `1.6477` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.8835` n `32` status `ready` deltaP `51.3889` edge `1.6477` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `23.0702` n `154` status `ready` deltaP `21.3339` edge `2.5762` maxDD `-56.6728`
- `market_context_high->crypto_major_24h` score `21.5198` n `154` status `ready` deltaP `24.6189` edge `2.4023` maxDD `-54.8486`
- `market_context_high->equity_24h` score `19.9737` n `154` status `ready` deltaP `33.3491` edge `2.0834` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `14.8242` n `32` status `ready` deltaP `26.9817` edge `1.1677` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.8242` n `32` status `ready` deltaP `26.9817` edge `1.1677` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.3638` n `32` status `ready` deltaP `28.9931` edge `0.9465` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.3638` n `32` status `ready` deltaP `28.9931` edge `0.9465` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.6908` n `154` status `ready` deltaP `36.4538` edge `1.0362` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `6.5672` n `32` status `ready` deltaP `7.3933` edge `0.6824` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.5672` n `32` status `ready` deltaP `7.3933` edge `0.6824` maxDD `-11.7537`
- `market_context_high->metal_24h` score `4.4256` n `154` status `ready` deltaP `23.8795` edge `0.8622` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `4.3594` n `32` status `ready` deltaP `17.3018` edge `0.557` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
