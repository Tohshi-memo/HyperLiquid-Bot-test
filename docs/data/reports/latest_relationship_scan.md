# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T19:52:23.630846+00:00`
- Price records: `672`
- Market context records: `3000`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6984`

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

- `market_context_high->crypto_alt_24h` score `18.9678` n `98` status `ready` deltaP `6.6787` edge `1.9278` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.4468` n `98` status `ready` deltaP `42.6411` edge `0.764` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `11.9369` n `98` status `ready` deltaP `18.9166` edge `0.9151` maxDD `-1.7175`
- `market_context_high->equity_24h` score `9.2389` n `98` status `ready` deltaP `17.6517` edge `0.8526` maxDD `-12.6963`
- `market_context_high->index_24h` score `5.7259` n `98` status `ready` deltaP `17.4355` edge `0.459` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.2413` n `102` status `ready` deltaP `16.843` edge `0.1392` maxDD `-2.8438`
- `market_context_high->index_4h` score `1.4203` n `102` status `ready` deltaP `18.9533` edge `0.1204` maxDD `-5.9381`
- `market_context_high->equity_4h` score `1.0812` n `102` status `ready` deltaP `14.3592` edge `0.1849` maxDD `-9.0276`
- `market_context_high->commodity_1h` score `-0.0716` n `106` status `ready` deltaP `0.8389` edge `0.0182` maxDD `-0.9706`
- `market_context_high->index_1h` score `-0.0879` n `106` status `ready` deltaP `5.4655` edge `0.0228` maxDD `-2.9736`
- `market_context_high->equity_1h` score `-0.2581` n `106` status `ready` deltaP `4.4035` edge `0.0395` maxDD `-5.1553`
- `market_context_high->crypto_alt_4h` score `-0.2707` n `102` status `ready` deltaP `22.6536` edge `0.3644` maxDD `-38.3432`
- `market_context_high->fx_1h` score `-0.3686` n `106` status `ready` deltaP `-2.3359` edge `0.0007` maxDD `-0.2576`
- `market_context_high->fx_4h` score `-1.1141` n `102` status `ready` deltaP `-9.8039` edge `0.0004` maxDD `-0.5631`
- `market_context_high->crypto_alt_1h` score `-1.157` n `106` status `ready` deltaP `6.2592` edge `0.0229` maxDD `-14.7034`
- `market_context_high->metal_1h` score `-1.2185` n `106` status `ready` deltaP `-3.011` edge `-0.0106` maxDD `-6.3768`
- `market_context_high->unknown_4h` score `-1.3873` n `102` status `ready` deltaP `-1.0013` edge `-0.0036` maxDD `-3.7602`
- `market_context_high->crypto_major_1h` score `-1.6048` n `106` status `ready` deltaP `3.7425` edge `-0.0044` maxDD `-15.1032`
- `market_context_high->fx_24h` score `-1.9268` n `98` status `ready` deltaP `-7.0011` edge `-0.0267` maxDD `-0.6418`
- `market_context_high->unknown_1h` score `-1.9547` n `106` status `ready` deltaP `0.7344` edge `-0.0947` maxDD `-3.1801`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
