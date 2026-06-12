# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T15:22:30.576777+00:00`
- Price records: `672`
- Market context records: `3698`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12897`

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

- `risk_on_high->crypto_major_24h` score `30.8331` n `32` status `ready` deltaP `33.8542` edge `2.348` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `30.8331` n `32` status `ready` deltaP `33.8542` edge `2.348` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `23.8385` n `32` status `ready` deltaP `36.1111` edge `1.7458` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `23.8385` n `32` status `ready` deltaP `36.1111` edge `1.7458` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `22.6748` n `32` status `ready` deltaP `32.9861` edge `1.6848` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `22.6748` n `32` status `ready` deltaP `32.9861` edge `1.6848` maxDD `-0.8779`
- `risk_on_high->index_24h` score `12.9022` n `32` status `ready` deltaP `35.9375` edge `0.8356` maxDD `0.0`
- `risk_on_and_context->index_24h` score `12.9022` n `32` status `ready` deltaP `35.9375` edge `0.8356` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.1037` n `32` status `ready` deltaP `17.8354` edge `0.8353` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.1037` n `32` status `ready` deltaP `17.8354` edge `0.8353` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.1792` n `156` status `ready` deltaP `23.117` edge `0.3081` maxDD `-7.1159`
- `risk_on_high->metal_24h` score `3.4558` n `32` status `ready` deltaP `21.5278` edge `0.1706` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `3.4558` n `32` status `ready` deltaP `21.5278` edge `0.1706` maxDD `-0.7574`
- `market_context_high->equity_24h` score `3.0005` n `156` status `ready` deltaP `14.9573` edge `0.5575` maxDD `-23.5737`
- `risk_on_high->equity_4h` score `1.7527` n `32` status `ready` deltaP `8.9177` edge `0.2787` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.7527` n `32` status `ready` deltaP `8.9177` edge `0.2787` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.4493` n `32` status `ready` deltaP `-1.9055` edge `0.3179` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.4493` n `32` status `ready` deltaP `-1.9055` edge `0.3179` maxDD `-11.7537`
- `risk_on_high->crypto_major_1h` score `0.9806` n `32` status `ready` deltaP `1.628` edge `0.2218` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `0.9806` n `32` status `ready` deltaP `1.628` edge `0.2218` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
