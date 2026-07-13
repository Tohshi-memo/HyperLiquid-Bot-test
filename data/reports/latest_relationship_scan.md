# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T22:37:31.682935+00:00`
- Price records: `672`
- Market context records: `6649`
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

- `market_context_high->unknown_1h` score `2.4266` n `202` status `ready` deltaP `-4.9623` edge `0.3254` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.8431` n `196` status `ready` deltaP `11.2475` edge `0.1821` maxDD `-5.2791`
- `market_context_high->unknown_24h` score `0.3645` n `196` status `ready` deltaP `-2.5422` edge `0.4088` maxDD `-11.9426`
- `market_context_high->crypto_major_1h` score `0.1333` n `202` status `ready` deltaP `9.0606` edge `0.051` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `0.0119` n `202` status `ready` deltaP `6.6313` edge `0.0457` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.2435` n `202` status `ready` deltaP `2.8221` edge `0.0007` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.4821` n `202` status `ready` deltaP `0.7144` edge `0.0052` maxDD `-0.7417`
- `market_context_high->unknown_4h` score `-0.6187` n `202` status `ready` deltaP `-15.268` edge `0.2908` maxDD `-10.5788`
- `market_context_high->commodity_1h` score `-0.6603` n `202` status `ready` deltaP `-1.2213` edge `-0.0082` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.759` n `202` status `ready` deltaP `11.5009` edge `0.014` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.8651` n `202` status `ready` deltaP `3.1659` edge `0.0095` maxDD `-3.8827`
- `market_context_high->crypto_major_4h` score `-0.9852` n `202` status `ready` deltaP `11.122` edge `0.131` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.1421` n `202` status `ready` deltaP `-3.3379` edge `0.0012` maxDD `-1.5966`
- `market_context_high->crypto_alt_4h` score `-1.3173` n `202` status `ready` deltaP `8.2649` edge `0.1162` maxDD `-19.2145`
- `market_context_high->commodity_4h` score `-1.4325` n `202` status `ready` deltaP `-1.3765` edge `-0.025` maxDD `-5.6246`
- `market_context_high->fx_4h` score `-1.4621` n `202` status `ready` deltaP `5.0335` edge `0.0002` maxDD `-3.3635`
- `market_context_high->metal_4h` score `-1.9225` n `202` status `ready` deltaP `1.227` edge `0.0314` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.3534` n `202` status `ready` deltaP `8.9139` edge `0.0047` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-6.2359` n `196` status `ready` deltaP `-11.2651` edge `-0.0083` maxDD `-10.5675`
- `market_context_high->metal_24h` score `-6.2568` n `196` status `ready` deltaP `-3.6439` edge `0.0188` maxDD `-26.0664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
