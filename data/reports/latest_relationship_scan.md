# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T19:37:27.209833+00:00`
- Price records: `672`
- Market context records: `2999`
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

- `market_context_high->crypto_alt_24h` score `18.7379` n `98` status `ready` deltaP `6.5051` edge `1.9098` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.4156` n `98` status `ready` deltaP `42.6411` edge `0.7614` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `11.893` n `98` status `ready` deltaP `18.7429` edge `0.9126` maxDD `-1.7175`
- `market_context_high->equity_24h` score `9.0726` n `98` status `ready` deltaP `17.4781` edge `0.8399` maxDD `-12.6963`
- `market_context_high->index_24h` score `5.6208` n `98` status `ready` deltaP `17.2619` edge `0.4514` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.2219` n `102` status `ready` deltaP `16.6906` edge `0.1386` maxDD `-2.8438`
- `market_context_high->index_4h` score `1.3757` n `102` status `ready` deltaP `18.8008` edge `0.1177` maxDD `-5.9381`
- `market_context_high->equity_4h` score `1.0522` n `102` status `ready` deltaP `14.2068` edge `0.1822` maxDD `-9.0276`
- `market_context_high->commodity_1h` score `-0.0731` n `106` status `ready` deltaP `0.8389` edge `0.018` maxDD `-0.9706`
- `market_context_high->index_1h` score `-0.0871` n `106` status `ready` deltaP `5.4655` edge `0.0229` maxDD `-2.9736`
- `market_context_high->equity_1h` score `-0.2503` n `106` status `ready` deltaP `4.4035` edge `0.0405` maxDD `-5.1553`
- `market_context_high->crypto_alt_4h` score `-0.273` n `102` status `ready` deltaP `22.6536` edge `0.3641` maxDD `-38.3432`
- `market_context_high->fx_1h` score `-0.3678` n `106` status `ready` deltaP `-2.3359` edge `0.0008` maxDD `-0.2576`
- `market_context_high->fx_4h` score `-1.1141` n `102` status `ready` deltaP `-9.8039` edge `0.0004` maxDD `-0.5631`
- `market_context_high->crypto_alt_1h` score `-1.1406` n `106` status `ready` deltaP `6.2592` edge `0.025` maxDD `-14.7034`
- `market_context_high->metal_1h` score `-1.2084` n `106` status `ready` deltaP `-2.8613` edge `-0.0103` maxDD `-6.3768`
- `market_context_high->unknown_4h` score `-1.3511` n `102` status `ready` deltaP `-0.8489` edge `-0.0016` maxDD `-3.7602`
- `market_context_high->crypto_major_1h` score `-1.5775` n `106` status `ready` deltaP `3.8922` edge `-0.0019` maxDD `-15.1032`
- `market_context_high->unknown_1h` score `-1.9139` n `106` status `ready` deltaP `0.8841` edge `-0.0923` maxDD `-3.1801`
- `market_context_high->fx_24h` score `-1.9268` n `98` status `ready` deltaP `-7.0011` edge `-0.0267` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
