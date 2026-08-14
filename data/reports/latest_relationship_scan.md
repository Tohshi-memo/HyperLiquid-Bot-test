# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T17:36:36.514000+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `market_context_high->unknown_24h` score `133.6928` n `129` status `ready` deltaP `-32.7439` edge `11.6506` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.7544` n `32` status `ready` deltaP `-46.5278` edge `4.5845` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.7544` n `32` status `ready` deltaP `-46.5278` edge `4.5845` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `10.0892` n `36` status `ready` deltaP `12.1527` edge `0.7977` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.4615` n `36` status `ready` deltaP `39.3293` edge `0.3596` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.9808` n `129` status `ready` deltaP `28.3228` edge `0.232` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.6655` n `32` status `ready` deltaP `31.4236` edge `0.1793` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.6655` n `32` status `ready` deltaP `31.4236` edge `0.1793` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.7758` n `32` status `ready` deltaP `19.2835` edge `0.121` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.7758` n `32` status `ready` deltaP `19.2835` edge `0.121` maxDD `-0.1258`
- `risk_on_high->crypto_major_24h` score `2.4062` n `32` status `ready` deltaP `18.4028` edge `0.3014` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.4062` n `32` status `ready` deltaP `18.4028` edge `0.3014` maxDD `-6.2481`
- `news_risk_high->index_24h` score `2.2606` n `36` status `ready` deltaP `15.9722` edge `0.0819` maxDD `0.0`
- `news_risk_high->index_4h` score `1.8245` n `36` status `ready` deltaP `21.1382` edge `0.0243` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.7517` n `129` status `ready` deltaP `17.1275` edge `0.0789` maxDD `-0.7687`
- `news_risk_high->equity_1h` score `1.7106` n `36` status `ready` deltaP `8.4332` edge `0.1182` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2791` n `32` status `ready` deltaP `13.5105` edge `0.0398` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2791` n `32` status `ready` deltaP `13.5105` edge `0.0398` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.1043` n `32` status `ready` deltaP `13.1944` edge `0.0225` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.1043` n `32` status `ready` deltaP `13.1944` edge `0.0225` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
