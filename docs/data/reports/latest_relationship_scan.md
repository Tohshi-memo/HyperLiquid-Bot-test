# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T03:52:23.112012+00:00`
- Price records: `672`
- Market context records: `6671`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->unknown_1h` score `2.6557` n `202` status `ready` deltaP `-4.3635` edge `0.3405` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.2058` n `202` status `ready` deltaP `12.2852` edge `0.2054` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.0826` n `202` status `ready` deltaP `8.3121` edge `0.0495` maxDD `-4.2122`
- `market_context_high->unknown_4h` score `-0.0169` n `202` status `ready` deltaP `-13.8961` edge `0.3318` maxDD `-10.5788`
- `market_context_high->crypto_alt_1h` score `-0.0708` n `202` status `ready` deltaP `5.8828` edge `0.0438` maxDD `-3.7803`
- `market_context_high->unknown_24h` score `-0.2297` n `202` status `ready` deltaP `-3.9346` edge `0.372` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2318` n `202` status `ready` deltaP `2.9718` edge `0.0012` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.4743` n `202` status `ready` deltaP `0.8641` edge `0.0052` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6463` n `202` status `ready` deltaP `-0.7722` edge `-0.0094` maxDD `-2.1314`
- `market_context_high->equity_1h` score `-0.834` n `202` status `ready` deltaP `3.615` edge `0.0091` maxDD `-3.8827`
- `market_context_high->index_4h` score `-0.8415` n `202` status `ready` deltaP `10.7387` edge `0.0085` maxDD `-5.7046`
- `market_context_high->metal_1h` score `-1.2308` n `202` status `ready` deltaP `-4.2361` edge `-0.0002` maxDD `-1.5966`
- `market_context_high->crypto_major_4h` score `-1.2647` n `202` status `ready` deltaP `9.9025` edge `0.1033` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.3987` n `202` status `ready` deltaP `6.253` edge `0.0002` maxDD `-3.3635`
- `market_context_high->commodity_4h` score `-1.4897` n `202` status `ready` deltaP `-1.6814` edge `-0.0303` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.5693` n `202` status `ready` deltaP `7.1978` edge `0.091` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.0644` n `202` status `ready` deltaP `-0.6022` edge `0.0254` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.7256` n `202` status `ready` deltaP `7.8468` edge `-0.0192` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-6.4242` n `202` status `ready` deltaP `-12.3367` edge `-0.0132` maxDD `-10.8591`
- `market_context_high->metal_24h` score `-6.8826` n `202` status `ready` deltaP `-5.0192` edge `-0.0004` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
