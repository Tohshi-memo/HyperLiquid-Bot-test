# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T14:07:34.517350+00:00`
- Price records: `672`
- Market context records: `4730`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7432`

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

- `market_context_high->unknown_1h` score `79.3362` n `141` status `ready` deltaP `15.0911` edge `6.5525` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.3791` n `141` status `ready` deltaP `14.685` edge `0.4714` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.3544` n `132` status `ready` deltaP `16.8403` edge `0.2596` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3471` n `141` status `ready` deltaP `1.859` edge `0.0227` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.5837` n `141` status `ready` deltaP `5.2197` edge `-0.0002` maxDD `-5.7542`
- `market_context_high->fx_4h` score `-0.84` n `141` status `ready` deltaP `0.2152` edge `-0.0017` maxDD `-1.9274`
- `market_context_high->equity_1h` score `-0.9762` n `141` status `ready` deltaP `-1.5129` edge `-0.0175` maxDD `-5.4726`
- `market_context_high->index_1h` score `-1.0068` n `141` status `ready` deltaP `-3.1596` edge `-0.0076` maxDD `-2.6999`
- `market_context_high->equity_4h` score `-1.1505` n `141` status `ready` deltaP `3.4434` edge `0.0023` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-1.3989` n `141` status `ready` deltaP `-6.3915` edge `-0.006` maxDD `-1.1038`
- `market_context_high->commodity_4h` score `-1.5291` n `141` status `ready` deltaP `8.6457` edge `0.0257` maxDD `-9.1941`
- `market_context_high->metal_1h` score `-2.7417` n `141` status `ready` deltaP `-5.3829` edge `-0.0746` maxDD `-15.9475`
- `market_context_high->crypto_alt_1h` score `-2.9091` n `141` status `ready` deltaP `-0.0159` edge `-0.0583` maxDD `-21.1642`
- `market_context_high->crypto_major_1h` score `-3.5676` n `141` status `ready` deltaP `-0.6466` edge `-0.079` maxDD `-27.2597`
- `market_context_high->commodity_24h` score `-4.0687` n `132` status `ready` deltaP `17.2822` edge `0.0705` maxDD `-28.6488`
- `market_context_high->fx_24h` score `-4.7155` n `132` status `ready` deltaP `-13.6364` edge `-0.0192` maxDD `-5.2943`
- `market_context_high->crypto_alt_4h` score `-7.2707` n `141` status `ready` deltaP `-1.0574` edge `-0.1141` maxDD `-59.5456`
- `market_context_high->index_24h` score `-8.0746` n `132` status `ready` deltaP `-11.2058` edge `-0.0984` maxDD `-27.3155`
- `market_context_high->metal_4h` score `-8.5066` n `141` status `ready` deltaP `2.3029` edge `-0.2563` maxDD `-62.6377`
- `market_context_high->crypto_major_4h` score `-10.2244` n `141` status `ready` deltaP `-0.6465` edge `-0.2329` maxDD `-80.5555`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
