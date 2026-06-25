# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T06:37:33.477628+00:00`
- Price records: `672`
- Market context records: `4698`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9752`

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

- `market_context_high->unknown_1h` score `78.968` n `142` status `ready` deltaP `13.8189` edge `6.5303` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.2508` n `135` status `ready` deltaP `11.2218` edge `0.4838` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.4191` n `135` status `ready` deltaP `12.7084` edge `0.2092` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3661` n `142` status `ready` deltaP `1.5244` edge `0.0225` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.7914` n `135` status `ready` deltaP `3.6168` edge `-0.0133` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.9101` n `135` status `ready` deltaP `-1.0253` edge `-0.0016` maxDD `-1.9927`
- `market_context_high->index_1h` score `-1.0761` n `142` status `ready` deltaP `-3.9976` edge `-0.0109` maxDD `-2.6999`
- `market_context_high->equity_1h` score `-1.1614` n `142` status `ready` deltaP `-1.4527` edge `0.0116` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.2305` n `135` status `ready` deltaP `5.5511` edge `0.016` maxDD `-9.1941`
- `market_context_high->fx_1h` score `-1.2978` n `142` status `ready` deltaP `-5.1573` edge `-0.0058` maxDD `-1.1038`
- `market_context_high->equity_4h` score `-1.3243` n `135` status `ready` deltaP `0.7848` edge `0.0019` maxDD `-8.8203`
- `market_context_high->metal_1h` score `-2.8548` n `142` status `ready` deltaP `-4.9191` edge `-0.0764` maxDD `-17.2107`
- `market_context_high->crypto_alt_1h` score `-3.3237` n `142` status `ready` deltaP `-1.4527` edge `-0.0877` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-3.9792` n `142` status `ready` deltaP `-3.3714` edge `-0.1124` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-4.651` n `135` status `ready` deltaP `15.0231` edge `0.0627` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-4.7877` n `135` status `ready` deltaP `-13.044` edge `-0.016` maxDD `-5.3476`
- `market_context_high->index_24h` score `-8.4047` n `135` status `ready` deltaP `-10.6366` edge `-0.092` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.608` n `135` status `ready` deltaP `-3.1595` edge `-0.2168` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.0945` n `135` status `ready` deltaP `-0.2439` edge `-0.279` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.5643` n `135` status `ready` deltaP `-3.5953` edge `-0.3686` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
