# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T22:04:43.912449+00:00`
- Price records: `672`
- Market context records: `3010`
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

- `market_context_high->crypto_alt_24h` score `20.6444` n `98` status `ready` deltaP `8.2412` edge `2.0571` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.7921` n `98` status `ready` deltaP `43.1619` edge `0.7893` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `12.4087` n `98` status `ready` deltaP `20.4791` edge `0.944` maxDD `-1.7175`
- `market_context_high->equity_24h` score `10.7187` n `98` status `ready` deltaP `19.2142` edge `0.9655` maxDD `-12.6963`
- `market_context_high->index_24h` score `6.6698` n `98` status `ready` deltaP `18.8244` edge `0.5284` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.4668` n `105` status `ready` deltaP `18.4176` edge `0.1475` maxDD `-2.8438`
- `market_context_high->equity_4h` score `0.6232` n `105` status `ready` deltaP `13.313` edge `0.1716` maxDD `-12.1029`
- `market_context_high->index_4h` score `0.3168` n `105` status `ready` deltaP `17.8107` edge `0.0999` maxDD `-9.9084`
- `market_context_high->equity_1h` score `-0.1583` n `114` status `ready` deltaP `5.4785` edge `0.051` maxDD `-5.6254`
- `market_context_high->commodity_1h` score `-0.1586` n `114` status `ready` deltaP `0.1287` edge `0.0152` maxDD `-1.245`
- `market_context_high->crypto_alt_4h` score `-0.267` n `105` status `ready` deltaP `22.2707` edge `0.3721` maxDD `-38.7172`
- `market_context_high->index_1h` score `-0.3414` n `114` status `ready` deltaP `4.9848` edge `0.0244` maxDD `-4.1126`
- `market_context_high->fx_1h` score `-0.5609` n `114` status `ready` deltaP `-1.6257` edge `0.0007` maxDD `-0.2615`
- `market_context_high->crypto_alt_1h` score `-0.6315` n `114` status `ready` deltaP `7.5953` edge `0.1097` maxDD `-14.7034`
- `market_context_high->crypto_major_1h` score `-0.9281` n `114` status `ready` deltaP `5.3262` edge `0.0718` maxDD `-15.1032`
- `market_context_high->unknown_1h` score `-0.9914` n `114` status `ready` deltaP `3.5955` edge `-0.0335` maxDD `-3.1801`
- `market_context_high->fx_4h` score `-1.1934` n `105` status `ready` deltaP `-10.9524` edge `-0.001` maxDD `-0.6521`
- `market_context_high->unknown_4h` score `-1.6541` n `105` status `ready` deltaP `-2.6103` edge `-0.0151` maxDD `-3.7602`
- `market_context_high->metal_1h` score `-1.7646` n `114` status `ready` deltaP `-1.6704` edge `-0.0041` maxDD `-6.8783`
- `market_context_high->fx_24h` score `-1.8163` n `98` status `ready` deltaP `-5.7858` edge `-0.0256` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
