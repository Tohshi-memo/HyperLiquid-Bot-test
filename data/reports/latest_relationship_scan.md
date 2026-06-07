# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T22:07:23.727066+00:00`
- Price records: `672`
- Market context records: `3220`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9724`

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

- `market_context_high->commodity_24h` score `13.7772` n `102` status `ready` deltaP `48.7541` edge `0.8659` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.4967` n `102` status `ready` deltaP `15.8293` edge `2.4913` maxDD `-70.9086`
- `market_context_high->index_24h` score `9.5469` n `102` status `ready` deltaP `30.9334` edge `0.8448` maxDD `-16.1026`
- `market_context_high->equity_24h` score `5.8015` n `102` status `ready` deltaP `15.9008` edge `1.4794` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.4435` n `128` status `ready` deltaP `23.5137` edge `0.176` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.3572` n `140` status `ready` deltaP `6.5441` edge `0.0284` maxDD `-1.7142`
- `market_context_high->fx_24h` score `-0.7259` n `102` status `ready` deltaP `1.4808` edge `-0.0133` maxDD `-1.5041`
- `market_context_high->unknown_4h` score `-0.829` n `128` status `ready` deltaP `6.9741` edge `0.0738` maxDD `-15.1257`
- `market_context_high->index_1h` score `-0.9058` n `140` status `ready` deltaP `3.3747` edge `0.0083` maxDD `-4.5023`
- `market_context_high->crypto_major_24h` score `-1.5008` n `102` status `ready` deltaP `17.4223` edge `1.8972` maxDD `-160.4604`
- `market_context_high->equity_1h` score `-1.6476` n `140` status `ready` deltaP `2.6262` edge `0.0021` maxDD `-8.8863`
- `market_context_high->crypto_alt_1h` score `-1.6888` n `140` status `ready` deltaP `3.2592` edge `0.063` maxDD `-14.7034`
- `market_context_high->fx_1h` score `-1.7855` n `140` status `ready` deltaP `-11.2104` edge `-0.0053` maxDD `-0.8335`
- `market_context_high->fx_4h` score `-1.8313` n `128` status `ready` deltaP `-8.4794` edge `-0.0076` maxDD `-1.4115`
- `market_context_high->crypto_major_1h` score `-1.8478` n `140` status `ready` deltaP `2.8657` edge `0.0532` maxDD `-15.1032`
- `market_context_high->index_4h` score `-2.039` n `128` status `ready` deltaP `10.9184` edge `0.0482` maxDD `-17.6057`
- `market_context_high->metal_1h` score `-2.33` n `140` status `ready` deltaP `-4.5509` edge `-0.0143` maxDD `-8.2956`
- `market_context_high->unknown_1h` score `-2.9539` n `140` status `ready` deltaP `0.9581` edge `-0.1372` maxDD `-17.8311`
- `market_context_high->crypto_major_4h` score `-5.1543` n `128` status `ready` deltaP `2.2676` edge `0.1149` maxDD `-54.2659`
- `market_context_high->equity_4h` score `-5.3787` n `128` status `ready` deltaP `10.8804` edge `0.0098` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
