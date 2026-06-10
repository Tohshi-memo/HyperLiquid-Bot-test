# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T02:37:25.230019+00:00`
- Price records: `672`
- Market context records: `3443`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13162`

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

- `risk_on_high->crypto_alt_24h` score `56.5287` n `32` status `ready` deltaP `60.0694` edge `4.3254` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `56.5287` n `32` status `ready` deltaP `60.0694` edge `4.3254` maxDD `-0.8779`
- `risk_on_high->crypto_major_24h` score `56.2677` n `32` status `ready` deltaP `58.5069` edge `4.3032` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `56.2677` n `32` status `ready` deltaP `58.5069` edge `4.3032` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `45.0317` n `32` status `ready` deltaP `56.0764` edge `3.3788` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.0317` n `32` status `ready` deltaP `56.0764` edge `3.3788` maxDD `0.0`
- `risk_on_high->index_24h` score `23.8547` n `32` status `ready` deltaP `51.3889` edge `1.6453` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.8547` n `32` status `ready` deltaP `51.3889` edge `1.6453` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `22.7544` n `154` status `ready` deltaP `20.9866` edge `2.5522` maxDD `-56.6728`
- `market_context_high->crypto_major_24h` score `21.3902` n `154` status `ready` deltaP `24.6189` edge `2.3915` maxDD `-54.8486`
- `market_context_high->equity_24h` score `19.8129` n `154` status `ready` deltaP `33.3491` edge `2.07` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `15.0544` n `32` status `ready` deltaP `27.7439` edge `1.1818` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.0544` n `32` status `ready` deltaP `27.7439` edge `1.1818` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.467` n `32` status `ready` deltaP `28.9931` edge `0.9551` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.467` n `32` status `ready` deltaP `28.9931` edge `0.9551` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.662` n `154` status `ready` deltaP `36.4538` edge `1.0338` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `6.7982` n `32` status `ready` deltaP `7.8506` edge `0.6986` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.7982` n `32` status `ready` deltaP `7.8506` edge `0.6986` maxDD `-11.7537`
- `market_context_high->metal_24h` score `4.4927` n `154` status `ready` deltaP `23.8795` edge `0.8708` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `4.4357` n `32` status `ready` deltaP `18.064` edge `0.5617` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
