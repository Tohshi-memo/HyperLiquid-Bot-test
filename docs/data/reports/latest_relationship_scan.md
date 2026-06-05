# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T16:37:27.865553+00:00`
- Price records: `672`
- Market context records: `2986`
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

- `market_context_high->crypto_alt_24h` score `16.0987` n `98` status `ready` deltaP `4.5954` edge `1.7026` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `11.9344` n `98` status `ready` deltaP `41.4258` edge `0.7294` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `11.1733` n `98` status `ready` deltaP `17.0068` edge `0.8642` maxDD `-1.7175`
- `market_context_high->equity_24h` score `7.0351` n `98` status `ready` deltaP `15.3947` edge `0.684` maxDD `-12.6963`
- `market_context_high->index_24h` score `4.5052` n `98` status `ready` deltaP `15.5258` edge `0.37` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.2505` n `99` status `ready` deltaP `14.762` edge `0.2114` maxDD `-0.7819`
- `market_context_high->index_4h` score `2.2983` n `99` status `ready` deltaP `19.4491` edge `0.1407` maxDD `-1.9733`
- `market_context_high->commodity_4h` score `2.279` n `99` status `ready` deltaP `17.0301` edge `0.1411` maxDD `-2.8438`
- `market_context_high->crypto_alt_4h` score `0.9372` n `99` status `ready` deltaP `24.4026` edge `0.4136` maxDD `-30.8239`
- `market_context_high->index_1h` score `0.3186` n `102` status `ready` deltaP `6.713` edge `0.0287` maxDD `-1.4189`
- `market_context_high->equity_1h` score `0.0535` n `102` status `ready` deltaP `5.2307` edge `0.0421` maxDD `-3.609`
- `market_context_high->commodity_1h` score `-0.2401` n `102` status `ready` deltaP `-0.5166` edge `0.0164` maxDD `-0.9706`
- `market_context_high->fx_1h` score `-0.4912` n `102` status `ready` deltaP `-1.6467` edge `0.0013` maxDD `-0.1672`
- `market_context_high->crypto_alt_1h` score `-0.932` n `102` status `ready` deltaP `8.1425` edge `0.0433` maxDD `-11.6869`
- `market_context_high->crypto_major_1h` score `-1.0109` n `102` status `ready` deltaP `5.7033` edge `0.0155` maxDD `-11.9831`
- `market_context_high->fx_4h` score `-1.039` n `99` status `ready` deltaP `-8.5859` edge `0.0019` maxDD `-0.5631`
- `market_context_high->metal_1h` score `-1.0463` n `102` status `ready` deltaP `-2.2896` edge `-0.0054` maxDD `-5.4112`
- `market_context_high->unknown_4h` score `-1.1126` n `99` status `ready` deltaP `-0.1616` edge `0.0137` maxDD `-3.7602`
- `market_context_high->unknown_1h` score `-1.679` n `102` status `ready` deltaP `1.9755` edge `-0.08` maxDD `-3.1801`
- `market_context_high->crypto_major_4h` score `-1.9114` n `99` status `ready` deltaP `9.6128` edge `0.2034` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
