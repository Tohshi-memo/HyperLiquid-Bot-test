# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T13:22:34.471842+00:00`
- Price records: `672`
- Market context records: `4520`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9771`

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

- `risk_on_high->unknown_4h` score `148.3745` n `43` status `ready` deltaP `13.5954` edge `12.393` maxDD `-7.5275`
- `risk_on_and_context->unknown_4h` score `148.3745` n `43` status `ready` deltaP `13.5954` edge `12.393` maxDD `-7.5275`
- `market_context_high->unknown_1h` score `47.3977` n `190` status `ready` deltaP `6.3584` edge `3.9658` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `27.6619` n `190` status `ready` deltaP `7.5979` edge `2.4111` maxDD `-7.5275`
- `risk_on_high->crypto_major_4h` score `6.4362` n `43` status `ready` deltaP `34.6745` edge `0.3189` maxDD `-0.4302`
- `risk_on_and_context->crypto_major_4h` score `6.4362` n `43` status `ready` deltaP `34.6745` edge `0.3189` maxDD `-0.4302`
- `risk_on_high->unknown_24h` score `5.6873` n `43` status `ready` deltaP `17.3611` edge `0.3582` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5.6873` n `43` status `ready` deltaP `17.3611` edge `0.3582` maxDD `0.0`
- `risk_on_high->equity_4h` score `5.2679` n `43` status `ready` deltaP `42.0732` edge `0.1585` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.2679` n `43` status `ready` deltaP `42.0732` edge `0.1585` maxDD `0.0`
- `risk_on_high->metal_24h` score `3.2753` n `43` status `ready` deltaP `-9.1449` edge `0.5788` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `3.2753` n `43` status `ready` deltaP `-9.1449` edge `0.5788` maxDD `-4.834`
- `risk_on_high->equity_1h` score `1.5789` n `43` status `ready` deltaP `17.1529` edge `0.0414` maxDD `-0.601`
- `risk_on_and_context->equity_1h` score `1.5789` n `43` status `ready` deltaP `17.1529` edge `0.0414` maxDD `-0.601`
- `risk_on_high->crypto_major_1h` score `1.551` n `43` status `ready` deltaP `10.3955` edge `0.0846` maxDD `-0.972`
- `risk_on_and_context->crypto_major_1h` score `1.551` n `43` status `ready` deltaP `10.3955` edge `0.0846` maxDD `-0.972`
- `risk_on_high->index_24h` score `1.3369` n `43` status `ready` deltaP `20.8374` edge `0.0242` maxDD `-2.4702`
- `risk_on_and_context->index_24h` score `1.3369` n `43` status `ready` deltaP `20.8374` edge `0.0242` maxDD `-2.4702`
- `risk_on_high->metal_4h` score `1.3241` n `43` status `ready` deltaP `15.5736` edge `0.0995` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.3241` n `43` status `ready` deltaP `15.5736` edge `0.0995` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
