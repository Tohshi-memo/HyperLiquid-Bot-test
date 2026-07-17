# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T00:22:26.826925+00:00`
- Price records: `672`
- Market context records: `6974`
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

- `market_context_high->fx_1h` score `-0.2593` n `237` status `ready` deltaP `2.0345` edge `0.0017` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3661` n `237` status `ready` deltaP `2.1306` edge `0.0253` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.7091` n `237` status `ready` deltaP `0.0606` edge `-0.0002` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7185` n `237` status `ready` deltaP `-1.9404` edge `-0.0024` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9156` n `237` status `ready` deltaP `12.0877` edge `0.0084` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.1981` n `237` status `ready` deltaP `2.5797` edge `0.0182` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2718` n `237` status `ready` deltaP `-2.6744` edge `-0.016` maxDD `-2.4388`
- `market_context_high->unknown_24h` score `-1.6369` n `224` status `ready` deltaP `-9.2014` edge `0.3065` maxDD `-18.7342`
- `market_context_high->unknown_1h` score `-1.6392` n `237` status `ready` deltaP `-2.43` edge `-0.0303` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6703` n `237` status `ready` deltaP `-4.4329` edge `-0.0356` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.8474` n `237` status `ready` deltaP `7.2096` edge `-0.015` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.9609` n `237` status `ready` deltaP `2.6876` edge `-0.0139` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-2.0023` n `237` status `ready` deltaP `5.3283` edge `0.0061` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-3.0047` n `237` status `ready` deltaP `0.3634` edge `-0.0091` maxDD `-22.2831`
- `market_context_high->unknown_4h` score `-3.2119` n `237` status `ready` deltaP `-7.8008` edge `0.0209` maxDD `-10.2579`
- `market_context_high->crypto_major_4h` score `-3.6636` n `237` status `ready` deltaP `-0.8915` edge `-0.0353` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.7837` n `224` status `ready` deltaP `-6.4485` edge `-0.0855` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.4353` n `224` status `ready` deltaP `-7.3661` edge `-0.0158` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.6207` n `237` status `ready` deltaP `4.6208` edge `-0.0861` maxDD `-66.7371`
- `market_context_high->index_24h` score `-12.1765` n `224` status `ready` deltaP `-5.0099` edge `-0.1207` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
