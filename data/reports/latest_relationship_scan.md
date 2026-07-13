# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T22:22:26.228199+00:00`
- Price records: `672`
- Market context records: `6648`
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

- `market_context_high->unknown_1h` score `2.429` n `202` status `ready` deltaP `-4.9623` edge `0.3256` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.7972` n `195` status `ready` deltaP `11.0931` edge `0.1793` maxDD `-5.2791`
- `market_context_high->unknown_24h` score `0.4595` n `195` status `ready` deltaP `-2.3015` edge `0.4152` maxDD `-11.9426`
- `market_context_high->crypto_major_1h` score `0.1395` n `202` status `ready` deltaP `9.0606` edge `0.0518` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `0.0322` n `202` status `ready` deltaP `6.781` edge `0.0464` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.2442` n `202` status `ready` deltaP `2.8221` edge `0.0006` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.4821` n `202` status `ready` deltaP `0.7144` edge `0.0052` maxDD `-0.7417`
- `market_context_high->unknown_4h` score `-0.6163` n `202` status `ready` deltaP `-15.268` edge `0.291` maxDD `-10.5788`
- `market_context_high->commodity_1h` score `-0.6603` n `202` status `ready` deltaP `-1.2213` edge `-0.0082` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.759` n `202` status `ready` deltaP `11.5009` edge `0.014` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.8675` n `202` status `ready` deltaP `3.1659` edge `0.0093` maxDD `-3.8827`
- `market_context_high->crypto_major_4h` score `-0.9875` n `202` status `ready` deltaP `11.122` edge `0.1307` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.1409` n `202` status `ready` deltaP `-3.3379` edge `0.0013` maxDD `-1.5966`
- `market_context_high->crypto_alt_4h` score `-1.3322` n `202` status `ready` deltaP `8.1124` edge `0.1153` maxDD `-19.2145`
- `market_context_high->commodity_4h` score `-1.4317` n `202` status `ready` deltaP `-1.3765` edge `-0.0249` maxDD `-5.6246`
- `market_context_high->fx_4h` score `-1.4708` n `202` status `ready` deltaP `4.8811` edge `0.0001` maxDD `-3.3635`
- `market_context_high->metal_4h` score `-1.9137` n `202` status `ready` deltaP `1.3795` edge `0.0315` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.34` n `202` status `ready` deltaP `9.0664` edge `0.0048` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-6.1801` n `195` status `ready` deltaP `-3.4869` edge `0.0198` maxDD `-25.7765`
- `market_context_high->fx_24h` score `-6.2103` n `195` status `ready` deltaP `-11.1054` edge `-0.008` maxDD `-10.5061`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
