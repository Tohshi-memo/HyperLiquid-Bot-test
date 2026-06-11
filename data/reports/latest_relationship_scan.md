# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T16:07:35.739454+00:00`
- Price records: `672`
- Market context records: `3599`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13138`

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

- `risk_on_high->crypto_major_24h` score `46.395` n `32` status `ready` deltaP `49.9079` edge `3.5378` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `46.395` n `32` status `ready` deltaP `49.9079` edge `3.5378` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `42.8694` n `32` status `ready` deltaP `51.4731` edge `3.2293` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `42.8694` n `32` status `ready` deltaP `51.4731` edge `3.2293` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `39.726` n `32` status `ready` deltaP `49.0414` edge `2.9987` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `39.726` n `32` status `ready` deltaP `49.0414` edge `2.9987` maxDD `-0.8779`
- `risk_on_high->index_24h` score `25.0538` n `32` status `ready` deltaP `51.9931` edge `1.7412` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.0538` n `32` status `ready` deltaP `51.9931` edge `1.7412` maxDD `0.0`
- `risk_on_high->metal_24h` score `18.0721` n `32` status `ready` deltaP `36.8609` edge `1.2864` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.0721` n `32` status `ready` deltaP `36.8609` edge `1.2864` maxDD `-0.7574`
- `market_context_high->equity_24h` score `17.2255` n `156` status `ready` deltaP `28.3962` edge `1.8874` maxDD `-40.9667`
- `market_context_high->index_24h` score `13.6692` n `156` status `ready` deltaP `36.6085` edge `1.1167` maxDD `-15.0661`
- `risk_on_high->crypto_major_4h` score `13.4567` n `32` status `ready` deltaP `25.4573` edge `1.0639` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.4567` n `32` status `ready` deltaP `25.4573` edge `1.0639` maxDD `-5.9781`
- `market_context_high->crypto_major_24h` score `10.9609` n `156` status `ready` deltaP `15.2124` edge `1.5851` maxDD `-54.8486`
- `market_context_high->metal_24h` score `7.2384` n `156` status `ready` deltaP `30.9314` edge `1.1758` maxDD `-25.9879`
- `market_context_high->crypto_alt_24h` score `5.6389` n `156` status `ready` deltaP `9.2177` edge `1.2127` maxDD `-56.6728`
- `risk_on_high->crypto_alt_4h` score `5.2838` n `32` status `ready` deltaP `6.0213` edge `0.5846` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.2838` n `32` status `ready` deltaP `6.0213` edge `0.5846` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.7464` n `32` status `ready` deltaP `15.4726` edge `0.4906` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
