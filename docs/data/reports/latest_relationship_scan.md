# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T07:22:31.489652+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8726`

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

- `market_context_high->equity_24h` score `9.4556` n `32` status `ready` deltaP `16.4931` edge `0.9153` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.4545` n `32` status `ready` deltaP `7.8125` edge `0.2112` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.3693` n `32` status `ready` deltaP `16.6667` edge `0.1107` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.7826` n `32` status `ready` deltaP `11.6319` edge `-0.0035` maxDD `-0.0397`
- `market_context_high->metal_4h` score `0.49` n `73` status `ready` deltaP `8.6034` edge `0.058` maxDD `-1.2025`
- `market_context_high->commodity_4h` score `0.3755` n `73` status `ready` deltaP `2.8086` edge `0.0612` maxDD `-1.2241`
- `market_context_high->metal_1h` score `0.1619` n `85` status `ready` deltaP `6.6203` edge `0.0192` maxDD `-0.9875`
- `market_context_high->index_4h` score `-0.0866` n `73` status `ready` deltaP `8.902` edge `0.0224` maxDD `-2.4279`
- `market_context_high->commodity_1h` score `-0.3264` n `85` status `ready` deltaP `2.279` edge `0.0059` maxDD `-1.7019`
- `market_context_high->equity_1h` score `-0.5981` n `85` status `ready` deltaP `-3.776` edge `0.0922` maxDD `-5.8303`
- `market_context_high->index_1h` score `-0.6141` n `85` status `ready` deltaP `-3.6263` edge `0.0124` maxDD `-0.6895`
- `market_context_high->crypto_alt_1h` score `-1.3495` n `85` status `ready` deltaP `3.7742` edge `-0.0089` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-1.4212` n `85` status `ready` deltaP `-16.0743` edge `-0.0066` maxDD `-0.8088`
- `market_context_high->metal_24h` score `-1.7519` n `32` status `ready` deltaP `-1.2153` edge `-0.1612` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.3585` n `73` status `ready` deltaP `-13.4773` edge `-0.0138` maxDD `-2.2313`
- `market_context_high->crypto_major_1h` score `-2.6781` n `85` status `ready` deltaP `-2.7281` edge `-0.0843` maxDD `-14.2689`
- `market_context_high->equity_4h` score `-3.4219` n `73` status `ready` deltaP `6.1686` edge `0.0517` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-4.4914` n `32` status `ready` deltaP `-4.8611` edge `0.0224` maxDD `-23.1423`
- `market_context_high->crypto_alt_4h` score `-7.7524` n `73` status `ready` deltaP `2.5268` edge `-0.196` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-9.2206` n `32` status `ready` deltaP `-18.75` edge `-0.1855` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
