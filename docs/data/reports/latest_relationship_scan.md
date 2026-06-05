# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T20:07:24.981704+00:00`
- Price records: `672`
- Market context records: `3001`
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

- `market_context_high->crypto_alt_24h` score `19.1977` n `98` status `ready` deltaP `6.8523` edge `1.9458` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.4792` n `98` status `ready` deltaP `42.6411` edge `0.7667` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `11.9988` n `98` status `ready` deltaP `19.0902` edge `0.9191` maxDD `-1.7175`
- `market_context_high->equity_24h` score `9.4064` n `98` status `ready` deltaP `17.8253` edge `0.8654` maxDD `-12.6963`
- `market_context_high->index_24h` score `5.8159` n `98` status `ready` deltaP `17.4355` edge `0.4665` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.2655` n `102` status `ready` deltaP `16.9954` edge `0.1402` maxDD `-2.8438`
- `market_context_high->index_4h` score `1.4539` n `102` status `ready` deltaP `18.9533` edge `0.1232` maxDD `-5.9381`
- `market_context_high->equity_4h` score `1.1015` n `102` status `ready` deltaP `14.3592` edge `0.1875` maxDD `-9.0276`
- `market_context_high->commodity_1h` score `-0.0606` n `106` status `ready` deltaP `0.9886` edge `0.0186` maxDD `-0.9706`
- `market_context_high->index_1h` score `-0.0855` n `106` status `ready` deltaP `5.4655` edge `0.0231` maxDD `-2.9736`
- `market_context_high->equity_1h` score `-0.2542` n `106` status `ready` deltaP `4.4035` edge `0.04` maxDD `-5.1553`
- `market_context_high->crypto_alt_4h` score `-0.2699` n `102` status `ready` deltaP `22.6536` edge `0.3645` maxDD `-38.3432`
- `market_context_high->fx_1h` score `-0.3686` n `106` status `ready` deltaP `-2.3359` edge `0.0007` maxDD `-0.2576`
- `market_context_high->fx_4h` score `-1.1141` n `102` status `ready` deltaP `-9.8039` edge `0.0004` maxDD `-0.5631`
- `market_context_high->crypto_alt_1h` score `-1.1773` n `106` status `ready` deltaP `6.2592` edge `0.0203` maxDD `-14.7034`
- `market_context_high->metal_1h` score `-1.2162` n `106` status `ready` deltaP `-3.011` edge `-0.0103` maxDD `-6.3768`
- `market_context_high->unknown_4h` score `-1.3813` n `102` status `ready` deltaP `-1.0013` edge `-0.0031` maxDD `-3.7602`
- `market_context_high->crypto_major_1h` score `-1.6274` n `106` status `ready` deltaP `3.5928` edge `-0.0063` maxDD `-15.1032`
- `market_context_high->fx_24h` score `-1.9256` n `98` status `ready` deltaP `-7.0011` edge `-0.0266` maxDD `-0.6418`
- `market_context_high->unknown_1h` score `-1.9882` n `106` status `ready` deltaP `0.5847` edge `-0.0965` maxDD `-3.1801`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
