# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T03:52:24.335657+00:00`
- Price records: `672`
- Market context records: `3547`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13200`

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

- `risk_on_high->crypto_major_24h` score `52.5773` n `32` status `ready` deltaP `57.7069` edge `4.001` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `52.5773` n `32` status `ready` deltaP `57.7069` edge `4.001` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `47.4331` n `32` status `ready` deltaP `57.3603` edge `3.5855` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `47.4331` n `32` status `ready` deltaP `57.3603` edge `3.5855` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.955` n `32` status `ready` deltaP `54.5927` edge `3.3823` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.955` n `32` status `ready` deltaP `54.5927` edge `3.3823` maxDD `0.0`
- `risk_on_high->index_24h` score `25.612` n `32` status `ready` deltaP `53.8995` edge `1.775` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.612` n `32` status `ready` deltaP `53.8995` edge `1.775` maxDD `0.0`
- `market_context_high->equity_24h` score `19.3111` n `156` status `ready` deltaP `31.5158` edge `2.0404` maxDD `-40.9667`
- `risk_on_high->metal_24h` score `18.6962` n `32` status `ready` deltaP `37.2075` edge `1.3361` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6962` n `32` status `ready` deltaP `37.2075` edge `1.3361` maxDD `-0.7574`
- `market_context_high->crypto_major_24h` score `17.1432` n `156` status `ready` deltaP `23.0114` edge `2.0483` maxDD `-54.8486`
- `risk_on_high->crypto_major_4h` score `14.5718` n `32` status `ready` deltaP `27.5915` edge `1.1426` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.5718` n `32` status `ready` deltaP `27.5915` edge `1.1426` maxDD `-5.9781`
- `market_context_high->index_24h` score `14.2273` n `156` status `ready` deltaP `38.5149` edge `1.1505` maxDD `-15.0661`
- `market_context_high->crypto_alt_24h` score `13.346` n `156` status `ready` deltaP `17.5366` edge `1.7995` maxDD `-56.6728`
- `market_context_high->metal_24h` score `7.644` n `156` status `ready` deltaP `31.278` edge `1.2255` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `6.2114` n `32` status `ready` deltaP `7.8506` edge `0.6497` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.2114` n `32` status `ready` deltaP `7.8506` edge `0.6497` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.9824` n `32` status `ready` deltaP `16.997` edge `0.5107` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
