# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T08:22:24.703346+00:00`
- Price records: `672`
- Market context records: `2952`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `17.1337` n `130` status `ready` deltaP `14.188` edge `1.7249` maxDD `-22.6673`
- `market_context_high->equity_24h` score `8.1469` n `130` status `ready` deltaP `18.4162` edge `0.7565` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `7.9191` n `130` status `ready` deltaP `16.7094` edge `0.595` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `4.7021` n `130` status `ready` deltaP `21.8135` edge `0.4423` maxDD `-7.337`
- `market_context_high->index_24h` score `3.1169` n `130` status `ready` deltaP `14.2227` edge `0.263` maxDD `-2.5127`
- `market_context_high->equity_4h` score `2.399` n `131` status `ready` deltaP `13.0656` edge `0.1825` maxDD `-3.2415`
- `market_context_high->crypto_alt_4h` score `1.221` n `131` status `ready` deltaP `19.4528` edge `0.4282` maxDD `-30.8239`
- `market_context_high->index_4h` score `0.7193` n `131` status `ready` deltaP `14.2745` edge `0.0812` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.5793` n `131` status `ready` deltaP `5.1165` edge `0.1195` maxDD `-3.7602`
- `market_context_high->index_1h` score `0.0917` n `131` status `ready` deltaP `5.9046` edge `0.0218` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.094` n `131` status `ready` deltaP `2.2969` edge `0.0523` maxDD `-2.0358`
- `market_context_high->fx_1h` score `-0.2518` n `131` status `ready` deltaP `0.8902` edge `0.0038` maxDD `-0.1244`
- `market_context_high->crypto_alt_1h` score `-0.3786` n `131` status `ready` deltaP `5.5755` edge `0.0903` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.5764` n `131` status `ready` deltaP `0.9359` edge `0.0086` maxDD `-3.4325`
- `market_context_high->commodity_1h` score `-0.6293` n `131` status `ready` deltaP `-1.3999` edge `-0.0071` maxDD `-3.4734`
- `market_context_high->crypto_major_1h` score `-0.665` n `131` status `ready` deltaP `4.7527` edge `0.07` maxDD `-9.622`
- `market_context_high->fx_4h` score `-0.686` n `131` status `ready` deltaP `1.6058` edge `0.01` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-0.8501` n `131` status `ready` deltaP `5.1259` edge `0.0358` maxDD `-8.9839`
- `market_context_high->unknown_1h` score `-0.891` n `131` status `ready` deltaP `1.0251` edge `-0.008` maxDD `-3.1801`
- `market_context_high->crypto_major_4h` score `-1.1156` n `131` status `ready` deltaP `9.5268` edge `0.306` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
