# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T21:52:37.292690+00:00`
- Price records: `672`
- Market context records: `3624`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13163`

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

- `risk_on_high->crypto_major_24h` score `41.4521` n `32` status `ready` deltaP `46.0069` edge `3.1519` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `41.4521` n `32` status `ready` deltaP `46.0069` edge `3.1519` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `38.4768` n `32` status `ready` deltaP `48.0903` edge `2.8858` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `38.4768` n `32` status `ready` deltaP `48.0903` edge `2.8858` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `33.9838` n `32` status `ready` deltaP `45.1389` edge `2.5462` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `33.9838` n `32` status `ready` deltaP `45.1389` edge `2.5462` maxDD `-0.8779`
- `risk_on_high->index_24h` score `22.1976` n `32` status `ready` deltaP `48.0903` edge `1.5292` maxDD `0.0`
- `risk_on_and_context->index_24h` score `22.1976` n `32` status `ready` deltaP `48.0903` edge `1.5292` maxDD `0.0`
- `risk_on_high->metal_24h` score `14.8008` n `32` status `ready` deltaP `33.6806` edge `1.035` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `14.8008` n `32` status `ready` deltaP `33.6806` edge `1.035` maxDD `-0.7574`
- `market_context_high->equity_24h` score `12.7468` n `158` status `ready` deltaP `24.6726` edge `1.539` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `12.4006` n `32` status `ready` deltaP `22.561` edge `0.9952` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `12.4006` n `32` status `ready` deltaP `22.561` edge `0.9952` maxDD `-5.9781`
- `market_context_high->index_24h` score `10.8477` n `158` status `ready` deltaP `32.9004` edge `0.9063` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `6.1295` n `158` status `ready` deltaP `11.7901` edge `1.2053` maxDD `-54.8486`
- `market_context_high->metal_24h` score `5.145` n `158` status `ready` deltaP `27.5888` edge `0.9297` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `3.9769` n `32` status `ready` deltaP `3.125` edge `0.495` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `3.9769` n `32` status `ready` deltaP `3.125` edge `0.495` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.9099` n `32` status `ready` deltaP `12.2713` edge `0.4047` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.9099` n `32` status `ready` deltaP `12.2713` edge `0.4047` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
