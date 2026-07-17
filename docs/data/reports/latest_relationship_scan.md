# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T00:52:24.441332+00:00`
- Price records: `672`
- Market context records: `6976`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11735`

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

- `market_context_high->fx_1h` score `-0.2507` n `237` status `ready` deltaP `2.1842` edge `0.0018` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.377` n `237` status `ready` deltaP `1.9809` edge `0.0249` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.7099` n `237` status `ready` deltaP `0.0606` edge `-0.0003` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7263` n `237` status `ready` deltaP `-2.0901` edge `-0.0024` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9069` n `237` status `ready` deltaP `12.2401` edge `0.0085` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.216` n `237` status `ready` deltaP `2.43` edge `0.0177` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2598` n `237` status `ready` deltaP `-2.5247` edge `-0.016` maxDD `-2.4388`
- `market_context_high->unknown_24h` score `-1.6259` n `224` status `ready` deltaP `-9.2014` edge `0.3079` maxDD `-18.7342`
- `market_context_high->unknown_1h` score `-1.6261` n `237` status `ready` deltaP `-2.2803` edge `-0.0302` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6687` n `237` status `ready` deltaP `-4.4329` edge `-0.0354` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.8442` n `237` status `ready` deltaP `7.2096` edge `-0.0146` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.9609` n `237` status `ready` deltaP `2.6876` edge `-0.0139` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.9889` n `237` status `ready` deltaP `5.4807` edge `0.0068` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.9459` n `237` status `ready` deltaP `0.6683` edge `-0.0036` maxDD `-22.2831`
- `market_context_high->unknown_4h` score `-3.148` n `237` status `ready` deltaP `-7.4959` edge `0.0242` maxDD `-10.2579`
- `market_context_high->crypto_major_4h` score `-3.5978` n `237` status `ready` deltaP `-0.5866` edge `-0.0289` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.7897` n `224` status `ready` deltaP `-6.4485` edge `-0.086` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.4353` n `224` status `ready` deltaP `-7.3661` edge `-0.0158` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.5854` n `237` status `ready` deltaP `4.7732` edge `-0.0826` maxDD `-66.7371`
- `market_context_high->index_24h` score `-12.1429` n `224` status `ready` deltaP `-4.6627` edge `-0.1187` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
