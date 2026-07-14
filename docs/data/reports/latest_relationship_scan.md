# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T03:07:23.863494+00:00`
- Price records: `672`
- Market context records: `6668`
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

- `market_context_high->unknown_1h` score `2.6041` n `202` status `ready` deltaP `-4.6629` edge `0.3382` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.213` n `202` status `ready` deltaP `12.2852` edge `0.206` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.0562` n `202` status `ready` deltaP `8.0127` edge `0.0481` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.0888` n `202` status `ready` deltaP `5.7331` edge `0.0433` maxDD `-3.7803`
- `market_context_high->unknown_4h` score `-0.1195` n `202` status `ready` deltaP `-14.3534` edge `0.3263` maxDD `-10.5788`
- `market_context_high->unknown_24h` score `-0.236` n `202` status `ready` deltaP `-3.9346` edge `0.3712` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2411` n `202` status `ready` deltaP `2.8221` edge `0.001` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.472` n `202` status `ready` deltaP `0.8641` edge `0.0055` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6346` n `202` status `ready` deltaP `-0.6225` edge `-0.0089` maxDD `-2.1314`
- `market_context_high->equity_1h` score `-0.8304` n `202` status `ready` deltaP `3.615` edge `0.0094` maxDD `-3.8827`
- `market_context_high->index_4h` score `-0.8329` n `202` status `ready` deltaP `10.7387` edge `0.0096` maxDD `-5.7046`
- `market_context_high->metal_1h` score `-1.1972` n `202` status `ready` deltaP `-3.9367` edge `0.0006` maxDD `-1.5966`
- `market_context_high->crypto_major_4h` score `-1.2028` n `202` status `ready` deltaP `10.2074` edge `0.1092` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.3979` n `202` status `ready` deltaP `6.253` edge `0.0003` maxDD `-3.3635`
- `market_context_high->commodity_4h` score `-1.4707` n `202` status `ready` deltaP `-1.3765` edge `-0.0299` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.5059` n `202` status `ready` deltaP `7.5027` edge `0.0971` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.0266` n `202` status `ready` deltaP `-0.1449` edge `0.0272` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.6594` n `202` status `ready` deltaP `7.9993` edge `-0.0147` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-6.4254` n `202` status `ready` deltaP `-12.3367` edge `-0.0133` maxDD `-10.8591`
- `market_context_high->metal_24h` score `-6.8388` n `202` status `ready` deltaP `-4.672` edge `0.0029` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
