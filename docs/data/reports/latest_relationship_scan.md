# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T13:37:30.945369+00:00`
- Price records: `672`
- Market context records: `6821`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `0.8687` n `176` status `ready` deltaP `-1.5467` edge `0.4969` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.3323` n `176` status `ready` deltaP `10.9217` edge `0.1417` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.1753` n `202` status `ready` deltaP `6.2963` edge `0.0294` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.3101` n `202` status `ready` deltaP `3.867` edge `0.0248` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3823` n `202` status `ready` deltaP `-0.0919` edge `0.0001` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.7793` n `202` status `ready` deltaP `-3.3275` edge `-0.0035` maxDD `-0.9382`
- `market_context_high->metal_1h` score `-0.929` n `202` status `ready` deltaP `-5.6293` edge `-0.0077` maxDD `-1.9098`
- `market_context_high->commodity_1h` score `-1.0774` n `202` status `ready` deltaP `-2.2914` edge `-0.0062` maxDD `-2.1314`
- `market_context_high->fx_4h` score `-1.3126` n `190` status `ready` deltaP `6.0141` edge `-0.002` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4106` n `190` status `ready` deltaP `-2.9943` edge `-0.0119` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.6232` n `190` status `ready` deltaP `2.3091` edge `-0.0268` maxDD `-6.4024`
- `market_context_high->equity_1h` score `-1.6385` n `202` status `ready` deltaP `0.5632` edge `-0.0276` maxDD `-4.6821`
- `market_context_high->unknown_1h` score `-1.6876` n `202` status `ready` deltaP `-4.9846` edge `-0.0173` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.7697` n `190` status `ready` deltaP `-4.3309` edge `-0.0279` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.135` n `190` status `ready` deltaP `-0.3915` edge `-0.0666` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.3139` n `190` status `ready` deltaP `-0.751` edge `-0.0615` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.4026` n `190` status `ready` deltaP `-12.5995` edge `0.037` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.46` n `176` status `ready` deltaP `-9.7853` edge `-0.0028` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-4.919` n `190` status `ready` deltaP `-0.2246` edge `-0.1753` maxDD `-29.3079`
- `market_context_high->metal_24h` score `-9.6098` n `176` status `ready` deltaP `-21.7961` edge `-0.2382` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
