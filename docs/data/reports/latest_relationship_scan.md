# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T16:07:35.659289+00:00`
- Price records: `672`
- Market context records: `2984`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6970`

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

- `market_context_high->crypto_alt_24h` score `15.8237` n `99` status `ready` deltaP `4.8769` edge `1.6778` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `11.7794` n `99` status `ready` deltaP `41.3037` edge `0.7173` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `11.0303` n `99` status `ready` deltaP `16.8245` edge `0.8535` maxDD `-1.7175`
- `market_context_high->equity_24h` score `6.8173` n `99` status `ready` deltaP `15.3567` edge `0.6661` maxDD `-12.6963`
- `market_context_high->index_24h` score `4.3517` n `99` status `ready` deltaP `15.4672` edge `0.3576` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.1031` n `100` status `ready` deltaP `14.75` edge `0.1992` maxDD `-0.7819`
- `market_context_high->commodity_4h` score `2.2482` n `100` status `ready` deltaP `17.1402` edge `0.1378` maxDD `-2.8438`
- `market_context_high->index_4h` score `2.2186` n `100` status `ready` deltaP `19.4573` edge `0.134` maxDD `-1.9733`
- `market_context_high->crypto_alt_4h` score `0.8263` n `100` status `ready` deltaP `23.7561` edge `0.4037` maxDD `-30.8239`
- `market_context_high->index_1h` score `0.3114` n `103` status `ready` deltaP `6.8325` edge `0.0273` maxDD `-1.4189`
- `market_context_high->equity_1h` score `0.0447` n `103` status `ready` deltaP `5.3311` edge `0.0403` maxDD `-3.609`
- `market_context_high->commodity_1h` score `-0.2308` n `103` status `ready` deltaP `-0.1904` edge `0.015` maxDD `-0.9706`
- `market_context_high->fx_1h` score `-0.4787` n `103` status `ready` deltaP `-1.4607` edge `0.0011` maxDD `-0.1672`
- `market_context_high->crypto_alt_1h` score `-0.8525` n `103` status `ready` deltaP `8.5518` edge `0.0472` maxDD `-11.6869`
- `market_context_high->crypto_major_1h` score `-0.9593` n `103` status `ready` deltaP `6.1697` edge `0.019` maxDD `-11.9831`
- `market_context_high->fx_4h` score `-1.0291` n `100` status `ready` deltaP `-8.3049` edge `0.0013` maxDD `-0.5631`
- `market_context_high->unknown_4h` score `-1.2184` n `100` status `ready` deltaP `-0.5244` edge `0.0073` maxDD `-3.7602`
- `market_context_high->unknown_1h` score `-1.6468` n `103` status `ready` deltaP `2.2731` edge `-0.0793` maxDD `-3.1801`
- `market_context_high->metal_1h` score `-1.6691` n `103` status `ready` deltaP `-2.7179` edge `-0.0075` maxDD `-5.4112`
- `market_context_high->crypto_major_4h` score `-2.0037` n `100` status `ready` deltaP `9.128` edge `0.1948` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
