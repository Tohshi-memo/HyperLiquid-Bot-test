# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T20:52:24.607427+00:00`
- Price records: `672`
- Market context records: `3005`
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

- `market_context_high->crypto_alt_24h` score `19.7998` n `98` status `ready` deltaP `7.3732` edge `1.9925` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.5752` n `98` status `ready` deltaP `42.6411` edge `0.7747` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `12.1473` n `98` status `ready` deltaP `19.611` edge `0.928` maxDD `-1.7175`
- `market_context_high->equity_24h` score `9.9124` n `98` status `ready` deltaP `18.3461` edge `0.9041` maxDD `-12.6963`
- `market_context_high->index_24h` score `6.142` n `98` status `ready` deltaP `17.9564` edge `0.4902` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.3106` n `103` status `ready` deltaP `17.424` edge `0.1411` maxDD `-2.8438`
- `market_context_high->index_4h` score `1.1146` n `103` status `ready` deltaP `18.6109` edge `0.1159` maxDD `-7.434`
- `market_context_high->equity_4h` score `0.9178` n `103` status `ready` deltaP `13.8453` edge `0.1824` maxDD `-10.229`
- `market_context_high->commodity_1h` score `-0.1462` n `109` status `ready` deltaP `0.4779` edge `0.0176` maxDD `-0.9706`
- `market_context_high->crypto_alt_4h` score `-0.3166` n `103` status `ready` deltaP `22.1969` edge `0.3635` maxDD `-38.4988`
- `market_context_high->equity_1h` score `-0.3737` n `109` status `ready` deltaP `3.8867` edge `0.034` maxDD `-5.6254`
- `market_context_high->fx_1h` score `-0.3917` n `109` status `ready` deltaP `-2.1246` edge `0.0005` maxDD `-0.2577`
- `market_context_high->index_1h` score `-0.4264` n `109` status `ready` deltaP `3.9595` edge `0.0149` maxDD `-4.0101`
- `market_context_high->crypto_alt_1h` score `-0.7284` n `109` status `ready` deltaP `7.0304` edge `0.0727` maxDD `-14.7034`
- `market_context_high->fx_4h` score `-1.1375` n `103` status `ready` deltaP `-10.1942` edge `0.0` maxDD `-0.5631`
- `market_context_high->crypto_major_1h` score `-1.218` n `109` status `ready` deltaP `4.5198` edge `0.04` maxDD `-15.1032`
- `market_context_high->unknown_4h` score `-1.4073` n `103` status `ready` deltaP `-1.1914` edge `-0.004` maxDD `-3.7602`
- `market_context_high->unknown_1h` score `-1.4752` n `109` status `ready` deltaP `1.8829` edge `-0.0624` maxDD `-3.1801`
- `market_context_high->fx_24h` score `-1.8942` n `98` status `ready` deltaP `-6.6539` edge `-0.0263` maxDD `-0.6418`
- `market_context_high->metal_1h` score `-2.0778` n `109` status `ready` deltaP `-4.2054` edge `-0.0133` maxDD `-6.8783`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
