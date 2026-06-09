# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T10:07:25.638739+00:00`
- Price records: `672`
- Market context records: `3372`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13080`

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

- `risk_on_high->crypto_major_24h` score `56.4049` n `32` status `ready` deltaP `59.2014` edge `4.31` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `56.4049` n `32` status `ready` deltaP `59.2014` edge `4.31` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `53.5565` n `32` status `ready` deltaP `54.6875` edge `4.1136` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `53.5565` n `32` status `ready` deltaP `54.6875` edge `4.1136` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.8025` n `32` status `ready` deltaP `56.7708` edge `3.4384` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.8025` n `32` status `ready` deltaP `56.7708` edge `3.4384` maxDD `0.0`
- `risk_on_high->index_24h` score `23.1338` n `32` status `ready` deltaP `50.8681` edge `1.5887` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.1338` n `32` status `ready` deltaP `50.8681` edge `1.5887` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `21.9123` n `154` status `ready` deltaP `19.5008` edge `2.5195` maxDD `-58.8781`
- `risk_on_high->crypto_major_4h` score `15.4932` n `32` status `ready` deltaP `28.3537` edge `1.2143` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.4932` n `32` status `ready` deltaP `28.3537` edge `1.2143` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `14.6955` n `32` status `ready` deltaP `31.9444` edge `1.0378` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `14.6955` n `32` status `ready` deltaP `31.9444` edge `1.0378` maxDD `-0.7574`
- `market_context_high->index_24h` score `11.7693` n `154` status `ready` deltaP `35.2837` edge `1.001` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.6678` n `154` status `ready` deltaP `30.1474` edge `2.0083` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.4814` n `32` status `ready` deltaP `9.0701` edge `0.7474` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.4814` n `32` status `ready` deltaP `9.0701` edge `0.7474` maxDD `-11.7537`
- `market_context_high->crypto_major_24h` score `6.3182` n `154` status `ready` deltaP `22.716` edge `2.1914` maxDD `-113.2922`
- `risk_on_high->equity_4h` score `3.5298` n `32` status `ready` deltaP `13.9482` edge `0.473` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5298` n `32` status `ready` deltaP `13.9482` edge `0.473` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
