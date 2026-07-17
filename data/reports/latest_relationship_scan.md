# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T01:07:26.652188+00:00`
- Price records: `672`
- Market context records: `6977`
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

- `market_context_high->fx_1h` score `-0.2499` n `237` status `ready` deltaP `2.1842` edge `0.0019` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3816` n `237` status `ready` deltaP `1.9809` edge `0.0243` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.7099` n `237` status `ready` deltaP `0.0606` edge `-0.0003` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7255` n `237` status `ready` deltaP `-2.0901` edge `-0.0023` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9069` n `237` status `ready` deltaP `12.2401` edge `0.0085` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.222` n `237` status `ready` deltaP `2.43` edge `0.0172` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.273` n `237` status `ready` deltaP `-2.6744` edge `-0.0161` maxDD `-2.4388`
- `market_context_high->unknown_24h` score `-1.6213` n `224` status `ready` deltaP `-9.2014` edge `0.3085` maxDD `-18.7342`
- `market_context_high->unknown_1h` score `-1.6261` n `237` status `ready` deltaP `-2.2803` edge `-0.0302` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6687` n `237` status `ready` deltaP `-4.4329` edge `-0.0354` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.8332` n `237` status `ready` deltaP `7.3621` edge `-0.0142` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.9523` n `237` status `ready` deltaP `2.8373` edge `-0.0138` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.9865` n `237` status `ready` deltaP `5.4807` edge `0.0071` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.9193` n `237` status `ready` deltaP `0.8208` edge `-0.0012` maxDD `-22.2831`
- `market_context_high->unknown_4h` score `-3.1034` n `237` status `ready` deltaP `-7.3435` edge `0.0269` maxDD `-10.2579`
- `market_context_high->crypto_major_4h` score `-3.5673` n `237` status `ready` deltaP `-0.4342` edge `-0.026` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.7933` n `224` status `ready` deltaP `-6.4485` edge `-0.0863` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.4353` n `224` status `ready` deltaP `-7.3661` edge `-0.0158` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.5627` n `237` status `ready` deltaP `4.9256` edge `-0.0807` maxDD `-66.7371`
- `market_context_high->index_24h` score `-12.1261` n `224` status `ready` deltaP `-4.489` edge `-0.1177` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
