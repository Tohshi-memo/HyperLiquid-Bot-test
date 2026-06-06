# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T20:37:19.829715+00:00`
- Price records: `672`
- Market context records: `3109`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6925`

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

- `market_context_high->crypto_alt_24h` score `15.6604` n `89` status `ready` deltaP `13.2218` edge `2.5068` maxDD `-38.3099`
- `market_context_high->commodity_24h` score `14.8284` n `89` status `ready` deltaP `45.964` edge `0.9721` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `13.8235` n `89` status `ready` deltaP `22.7489` edge `1.0491` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.3346` n `89` status `ready` deltaP `31.9601` edge `0.9036` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.5248` n `89` status `ready` deltaP `15.8396` edge `1.3503` maxDD `-41.5508`
- `market_context_high->commodity_4h` score `2.9906` n `120` status `ready` deltaP `17.9878` edge `0.1751` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `-0.0494` n `127` status `ready` deltaP `1.7469` edge `0.0265` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4897` n `127` status `ready` deltaP `4.0643` edge `0.0164` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.5454` n `89` status `ready` deltaP `4.2018` edge `-0.0007` maxDD `-0.4876`
- `market_context_high->fx_1h` score `-0.8331` n `127` status `ready` deltaP `-9.094` edge `-0.0051` maxDD `-0.6202`
- `market_context_high->crypto_alt_1h` score `-0.8383` n `127` status `ready` deltaP `2.9386` edge `0.0859` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.1092` n `127` status `ready` deltaP `-0.0943` edge `0.007` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3209` n `120` status `ready` deltaP `-12.2662` edge `-0.0032` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4305` n `120` status `ready` deltaP `9.4817` edge `0.0443` maxDD `-17.6057`
- `market_context_high->unknown_4h` score `-1.8706` n `120` status `ready` deltaP `4.746` edge `0.0142` maxDD `-13.8046`
- `market_context_high->crypto_major_1h` score `-2.3275` n `127` status `ready` deltaP `-1.7198` edge `0.0438` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.3717` n `127` status `ready` deltaP `-7.2257` edge `-0.0101` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.7824` n `127` status `ready` deltaP `2.5013` edge `-0.0459` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.9391` n `120` status `ready` deltaP `12.2053` edge `0.2181` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-4.0656` n `120` status `ready` deltaP `5.9146` edge `-0.0301` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
