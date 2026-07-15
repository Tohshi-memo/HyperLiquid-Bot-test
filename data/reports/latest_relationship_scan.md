# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T10:52:25.885077+00:00`
- Price records: `672`
- Market context records: `6809`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11680`

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

- `market_context_high->unknown_24h` score `0.8258` n `176` status `ready` deltaP `-1.5467` edge `0.4914` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.3741` n `176` status `ready` deltaP `10.5745` edge `0.1475` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.3177` n `191` status `ready` deltaP `6.242` edge `0.0179` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.4291` n `191` status `ready` deltaP `3.4745` edge `0.0175` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.4533` n `191` status `ready` deltaP `-1.3826` edge `-0.0004` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.6494` n `191` status `ready` deltaP `-1.0863` edge `-0.0077` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.7305` n `191` status `ready` deltaP `-2.8804` edge `-0.0016` maxDD `-0.8285`
- `market_context_high->metal_1h` score `-0.8406` n `191` status `ready` deltaP `-6.4677` edge `-0.0058` maxDD `-1.7081`
- `market_context_high->fx_4h` score `-1.3643` n `185` status `ready` deltaP `5.0651` edge `-0.0023` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.3931` n `185` status `ready` deltaP `-2.5981` edge `-0.0123` maxDD `-5.5853`
- `market_context_high->equity_1h` score `-1.4071` n `191` status `ready` deltaP `1.381` edge `-0.0194` maxDD `-4.2318`
- `market_context_high->index_4h` score `-1.6539` n `185` status `ready` deltaP `1.8375` edge `-0.0283` maxDD `-6.3458`
- `market_context_high->unknown_1h` score `-1.7582` n `191` status `ready` deltaP `-6.6174` edge `-0.0123` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.8352` n `185` status `ready` deltaP `-6.0094` edge `-0.0251` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.2807` n `185` status `ready` deltaP `-0.6576` edge `-0.0835` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.491` n `185` status `ready` deltaP `-1.517` edge `-0.0791` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.5001` n `185` status `ready` deltaP `-14.1175` edge `0.039` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4864` n `176` status `ready` deltaP `-9.7853` edge `-0.005` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-5.022` n `185` status `ready` deltaP `-0.81` edge `-0.1846` maxDD `-29.3079`
- `market_context_high->metal_24h` score `-9.585` n `176` status `ready` deltaP `-21.2753` edge `-0.2385` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
