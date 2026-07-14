# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T02:07:29.123559+00:00`
- Price records: `672`
- Market context records: `6664`
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

- `market_context_high->unknown_1h` score `2.4218` n `202` status `ready` deltaP `-5.2617` edge `0.327` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.1655` n `202` status `ready` deltaP `12.1416` edge `0.203` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.0499` n `202` status `ready` deltaP `7.863` edge `0.0483` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1128` n `202` status `ready` deltaP `5.5834` edge `0.0423` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.2248` n `202` status `ready` deltaP `3.1215` edge `0.0011` maxDD `-0.7249`
- `market_context_high->unknown_24h` score `-0.229` n `202` status `ready` deltaP `-3.9364` edge `0.3721` maxDD `-12.3511`
- `market_context_high->unknown_4h` score `-0.2359` n `202` status `ready` deltaP `-14.3534` edge `0.3166` maxDD `-10.5788`
- `market_context_high->index_1h` score `-0.4767` n `202` status `ready` deltaP `0.8641` edge `0.0049` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6517` n `202` status `ready` deltaP `-0.9219` edge `-0.0091` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.8235` n `202` status `ready` deltaP `10.7387` edge `0.0108` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.8484` n `202` status `ready` deltaP `3.615` edge `0.0079` maxDD `-3.8827`
- `market_context_high->crypto_major_4h` score `-1.0907` n `202` status `ready` deltaP `10.8171` edge `0.1195` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.1373` n `202` status `ready` deltaP `-3.3379` edge `0.0016` maxDD `-1.5966`
- `market_context_high->fx_4h` score `-1.3869` n `202` status `ready` deltaP `6.4055` edge `0.0007` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.397` n `202` status `ready` deltaP `8.1124` edge `0.107` maxDD `-19.2145`
- `market_context_high->commodity_4h` score `-1.4684` n `202` status `ready` deltaP `-1.3765` edge `-0.0296` maxDD `-5.6246`
- `market_context_high->metal_4h` score `-1.98` n `202` status `ready` deltaP `0.4649` edge `0.0291` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.6006` n `202` status `ready` deltaP `7.9993` edge `-0.0098` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-6.3992` n `202` status `ready` deltaP `-12.1895` edge `-0.0121` maxDD `-10.8591`
- `market_context_high->metal_24h` score `-6.8037` n `202` status `ready` deltaP `-4.5531` edge `0.0066` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
