# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T03:22:28.964930+00:00`
- Price records: `672`
- Market context records: `6669`
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

- `market_context_high->unknown_1h` score `2.6077` n `202` status `ready` deltaP `-4.6629` edge `0.3385` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.2106` n `202` status `ready` deltaP `12.2852` edge `0.2058` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.0702` n `202` status `ready` deltaP `8.1624` edge `0.0489` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.0816` n `202` status `ready` deltaP `5.7331` edge `0.0439` maxDD `-3.7803`
- `market_context_high->unknown_4h` score `-0.0869` n `202` status `ready` deltaP `-14.2009` edge `0.328` maxDD `-10.5788`
- `market_context_high->fx_1h` score `-0.2326` n `202` status `ready` deltaP `2.9718` edge `0.0011` maxDD `-0.7249`
- `market_context_high->unknown_24h` score `-0.2329` n `202` status `ready` deltaP `-3.9346` edge `0.3716` maxDD `-12.3511`
- `market_context_high->index_1h` score `-0.472` n `202` status `ready` deltaP `0.8641` edge `0.0055` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6362` n `202` status `ready` deltaP `-0.6225` edge `-0.0091` maxDD `-2.1314`
- `market_context_high->equity_1h` score `-0.8268` n `202` status `ready` deltaP `3.615` edge `0.0097` maxDD `-3.8827`
- `market_context_high->index_4h` score `-0.8345` n `202` status `ready` deltaP `10.7387` edge `0.0094` maxDD `-5.7046`
- `market_context_high->metal_1h` score `-1.1984` n `202` status `ready` deltaP `-3.9367` edge `0.0005` maxDD `-1.5966`
- `market_context_high->crypto_major_4h` score `-1.2153` n `202` status `ready` deltaP `10.2074` edge `0.1076` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.3987` n `202` status `ready` deltaP `6.253` edge `0.0002` maxDD `-3.3635`
- `market_context_high->commodity_4h` score `-1.4802` n `202` status `ready` deltaP `-1.5289` edge `-0.0301` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.5199` n `202` status `ready` deltaP `7.5027` edge `0.0953` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.0384` n `202` status `ready` deltaP `-0.2973` edge `0.0267` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.6666` n `202` status `ready` deltaP `7.9993` edge `-0.0153` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-6.4254` n `202` status `ready` deltaP `-12.3367` edge `-0.0133` maxDD `-10.8591`
- `market_context_high->metal_24h` score `-6.8466` n `202` status `ready` deltaP `-4.672` edge `0.0019` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
