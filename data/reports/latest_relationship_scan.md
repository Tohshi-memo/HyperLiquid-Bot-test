# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T21:52:29.642023+00:00`
- Price records: `672`
- Market context records: `6646`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11766`

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

- `market_context_high->unknown_1h` score `2.4445` n `202` status `ready` deltaP `-4.8126` edge `0.3259` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.7217` n `193` status `ready` deltaP `10.7796` edge `0.1751` maxDD `-5.2791`
- `market_context_high->unknown_24h` score `0.6497` n `193` status `ready` deltaP `-1.8126` edge `0.428` maxDD `-11.9426`
- `market_context_high->crypto_major_1h` score `0.1294` n `202` status `ready` deltaP `8.9109` edge `0.0515` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `0.0011` n `202` status `ready` deltaP `6.4816` edge `0.0458` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.2435` n `202` status `ready` deltaP `2.8221` edge `0.0007` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.4821` n `202` status `ready` deltaP `0.7144` edge `0.0052` maxDD `-0.7417`
- `market_context_high->unknown_4h` score `-0.6115` n `202` status `ready` deltaP `-15.268` edge `0.2914` maxDD `-10.5788`
- `market_context_high->commodity_1h` score `-0.6688` n `202` status `ready` deltaP `-1.371` edge `-0.0083` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.7771` n `202` status `ready` deltaP `11.196` edge `0.0137` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.8687` n `202` status `ready` deltaP `3.1659` edge `0.0092` maxDD `-3.8827`
- `market_context_high->crypto_major_4h` score `-0.9953` n `202` status `ready` deltaP `11.122` edge `0.1297` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.1146` n `202` status `ready` deltaP `-3.0385` edge `0.0015` maxDD `-1.5966`
- `market_context_high->crypto_alt_4h` score `-1.3637` n `202` status `ready` deltaP `7.8076` edge `0.1133` maxDD `-19.2145`
- `market_context_high->commodity_4h` score `-1.442` n `202` status `ready` deltaP `-1.5289` edge `-0.0252` maxDD `-5.6246`
- `market_context_high->fx_4h` score `-1.4867` n `202` status `ready` deltaP `4.5762` edge `0.0001` maxDD `-3.3635`
- `market_context_high->metal_4h` score `-1.8955` n `202` status `ready` deltaP `1.6844` edge `0.0318` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.357` n `202` status `ready` deltaP `8.9139` edge `0.0044` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-6.0177` n `193` status `ready` deltaP `-3.168` edge `0.0217` maxDD `-25.1002`
- `market_context_high->fx_24h` score `-6.1724` n `193` status `ready` deltaP `-10.7813` edge `-0.0075` maxDD `-10.4659`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
