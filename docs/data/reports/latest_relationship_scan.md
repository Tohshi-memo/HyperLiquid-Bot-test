# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T23:37:28.354604+00:00`
- Price records: `672`
- Market context records: `6654`
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

- `market_context_high->unknown_1h` score `2.3954` n `202` status `ready` deltaP `-5.2617` edge `0.3248` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.0593` n `200` status `ready` deltaP `11.8495` edge `0.1961` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.0998` n `202` status `ready` deltaP `8.6115` edge `0.0497` maxDD `-4.2122`
- `market_context_high->unknown_24h` score `-0.0077` n `200` status `ready` deltaP `-3.481` edge `0.384` maxDD `-11.9426`
- `market_context_high->crypto_alt_1h` score `-0.0385` n `202` status `ready` deltaP `6.1822` edge `0.0445` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.2349` n `202` status `ready` deltaP `2.9718` edge `0.0008` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.4798` n `202` status `ready` deltaP `0.7144` edge `0.0055` maxDD `-0.7417`
- `market_context_high->unknown_4h` score `-0.5379` n `202` status `ready` deltaP `-14.9631` edge `0.2955` maxDD `-10.5788`
- `market_context_high->commodity_1h` score `-0.6836` n `202` status `ready` deltaP `-1.5207` edge `-0.0092` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.7582` n `202` status `ready` deltaP `11.5009` edge `0.0141` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.8304` n `202` status `ready` deltaP `3.3156` edge `0.0114` maxDD `-3.8827`
- `market_context_high->crypto_major_4h` score `-0.9584` n `202` status `ready` deltaP `11.4269` edge `0.1324` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.1529` n `202` status `ready` deltaP `-3.4876` edge `0.0013` maxDD `-1.5966`
- `market_context_high->crypto_alt_4h` score `-1.2662` n `202` status `ready` deltaP `8.7222` edge `0.1197` maxDD `-19.2145`
- `market_context_high->fx_4h` score `-1.4281` n `202` status `ready` deltaP `5.6433` edge `0.0005` maxDD `-3.3635`
- `market_context_high->commodity_4h` score `-1.4426` n `202` status `ready` deltaP `-1.3765` edge `-0.0263` maxDD `-5.6246`
- `market_context_high->metal_4h` score `-1.9486` n `202` status `ready` deltaP `0.7697` edge `0.0311` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.3606` n `202` status `ready` deltaP `8.9139` edge `0.0041` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-6.3308` n `200` status `ready` deltaP `-11.8875` edge `-0.0096` maxDD `-10.7639`
- `market_context_high->metal_24h` score `-6.5818` n `200` status `ready` deltaP `-4.2561` edge `0.0132` maxDD `-27.2913`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
