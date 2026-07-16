# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T23:07:27.406194+00:00`
- Price records: `672`
- Market context records: `6968`
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

- `market_context_high->fx_1h` score `-0.2429` n `237` status `ready` deltaP `2.3339` edge `0.0018` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3723` n `237` status `ready` deltaP `2.2803` edge `0.0235` maxDD `-4.5815`
- `market_context_high->metal_1h` score `-0.7014` n `237` status `ready` deltaP `-1.641` edge `-0.0022` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.7247` n `237` status `ready` deltaP `-0.2388` edge `-0.0002` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.9061` n `237` status `ready` deltaP `12.2401` edge `0.0086` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.2053` n `237` status `ready` deltaP `2.7294` edge `0.0166` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.3221` n `237` status `ready` deltaP `-3.2732` edge `-0.0162` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.6333` n `237` status `ready` deltaP `-2.2803` edge `-0.0308` maxDD `-3.2083`
- `market_context_high->unknown_24h` score `-1.661` n `224` status `ready` deltaP `-9.2014` edge `0.3034` maxDD `-18.7342`
- `market_context_high->commodity_4h` score `-1.6695` n `237` status `ready` deltaP `-4.4329` edge `-0.0355` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.8481` n `237` status `ready` deltaP `7.2096` edge `-0.0151` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-2.003` n `237` status `ready` deltaP `2.2385` edge `-0.0163` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-2.0464` n `237` status `ready` deltaP `4.7185` edge `0.0045` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-3.1426` n `237` status `ready` deltaP `-0.3988` edge `-0.0217` maxDD `-22.2831`
- `market_context_high->unknown_4h` score `-3.3281` n `237` status `ready` deltaP `-8.563` edge `0.0163` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.7705` n `224` status `ready` deltaP `-6.4485` edge `-0.0844` maxDD `-5.2791`
- `market_context_high->crypto_major_4h` score `-3.8148` n `237` status `ready` deltaP `-1.6537` edge `-0.0496` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-4.4281` n `224` status `ready` deltaP `-7.3661` edge `-0.0152` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.7046` n `237` status `ready` deltaP `4.011` edge `-0.0928` maxDD `-66.7371`
- `market_context_high->index_24h` score `-12.2568` n `224` status `ready` deltaP `-5.8779` edge `-0.1252` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
