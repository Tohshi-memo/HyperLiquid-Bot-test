# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T13:52:37.768143+00:00`
- Price records: `672`
- Market context records: `4729`
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

- `market_context_high->unknown_1h` score `79.317` n `141` status `ready` deltaP `15.0911` edge `6.5509` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.3599` n `141` status `ready` deltaP `14.685` edge `0.4698` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.3213` n `132` status `ready` deltaP `16.6667` edge `0.258` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3479` n `141` status `ready` deltaP `1.859` edge `0.0226` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.5852` n `141` status `ready` deltaP `5.2197` edge `-0.0004` maxDD `-5.7542`
- `market_context_high->fx_4h` score `-0.8392` n `141` status `ready` deltaP `0.2152` edge `-0.0016` maxDD `-1.9274`
- `market_context_high->index_1h` score `-1.0092` n `141` status `ready` deltaP `-3.1596` edge `-0.0079` maxDD `-2.6999`
- `market_context_high->equity_1h` score `-1.0152` n `141` status `ready` deltaP `-1.6626` edge `-0.0215` maxDD `-5.4726`
- `market_context_high->equity_4h` score `-1.1809` n `141` status `ready` deltaP `3.4434` edge `-0.0016` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-1.3869` n `141` status `ready` deltaP `-6.2418` edge `-0.006` maxDD `-1.1038`
- `market_context_high->commodity_4h` score `-1.5351` n `141` status `ready` deltaP `8.6457` edge `0.0252` maxDD `-9.1941`
- `market_context_high->metal_1h` score `-2.744` n `141` status `ready` deltaP `-5.3829` edge `-0.0749` maxDD `-15.9475`
- `market_context_high->crypto_alt_1h` score `-2.9379` n `141` status `ready` deltaP `-0.0159` edge `-0.062` maxDD `-21.1642`
- `market_context_high->crypto_major_1h` score `-3.6012` n `141` status `ready` deltaP `-0.6466` edge `-0.0833` maxDD `-27.2597`
- `market_context_high->commodity_24h` score `-4.0261` n `132` status `ready` deltaP `17.4558` edge `0.0729` maxDD `-28.6488`
- `market_context_high->fx_24h` score `-4.7004` n `132` status `ready` deltaP `-13.4628` edge `-0.0191` maxDD `-5.2943`
- `market_context_high->crypto_alt_4h` score `-7.2941` n `141` status `ready` deltaP `-1.0574` edge `-0.1171` maxDD `-59.5456`
- `market_context_high->index_24h` score `-8.0355` n `132` status `ready` deltaP `-11.0322` edge `-0.0963` maxDD `-27.3155`
- `market_context_high->metal_4h` score `-8.4916` n `141` status `ready` deltaP `2.4553` edge `-0.2554` maxDD `-62.6377`
- `market_context_high->crypto_major_4h` score `-10.2603` n `141` status `ready` deltaP `-0.6465` edge `-0.2375` maxDD `-80.5555`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
