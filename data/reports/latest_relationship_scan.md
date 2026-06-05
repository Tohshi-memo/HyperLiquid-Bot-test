# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T17:37:21.394221+00:00`
- Price records: `672`
- Market context records: `2990`
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

- `market_context_high->crypto_alt_24h` score `16.8184` n `98` status `ready` deltaP `5.1162` edge `1.7591` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.1057` n `98` status `ready` deltaP `41.9466` edge `0.7402` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `11.4161` n `98` status `ready` deltaP `17.7013` edge `0.8798` maxDD `-1.7175`
- `market_context_high->equity_24h` score `7.6439` n `98` status `ready` deltaP `16.0892` edge `0.7301` maxDD `-12.6963`
- `market_context_high->index_24h` score `4.8065` n `98` status `ready` deltaP `15.873` edge `0.3928` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.5377` n `99` status `ready` deltaP `15.0669` edge `0.2333` maxDD `-0.7819`
- `market_context_high->index_4h` score `2.4581` n `99` status `ready` deltaP `19.6015` edge `0.153` maxDD `-1.9733`
- `market_context_high->commodity_4h` score `2.4238` n `99` status `ready` deltaP `17.6398` edge `0.1491` maxDD `-2.8438`
- `market_context_high->crypto_alt_4h` score `0.9699` n `99` status `ready` deltaP `24.4026` edge `0.4178` maxDD `-30.8239`
- `market_context_high->index_1h` score `0.3618` n `102` status `ready` deltaP `6.8627` edge `0.0313` maxDD `-1.4189`
- `market_context_high->equity_1h` score `0.0707` n `102` status `ready` deltaP `5.2307` edge `0.0443` maxDD `-3.609`
- `market_context_high->commodity_1h` score `-0.2137` n `102` status `ready` deltaP `-0.3669` edge `0.0176` maxDD `-0.9706`
- `market_context_high->fx_1h` score `-0.4792` n `102` status `ready` deltaP `-1.497` edge `0.0013` maxDD `-0.1672`
- `market_context_high->fx_4h` score `-1.0312` n `99` status `ready` deltaP `-8.5859` edge `0.0029` maxDD `-0.5631`
- `market_context_high->crypto_alt_1h` score `-1.0556` n `102` status `ready` deltaP `7.8431` edge `0.035` maxDD `-11.6869`
- `market_context_high->metal_1h` score `-1.0619` n `102` status `ready` deltaP `-2.4393` edge `-0.0064` maxDD `-5.4112`
- `market_context_high->crypto_major_1h` score `-1.0803` n `102` status `ready` deltaP `5.2542` edge `0.0096` maxDD `-11.9831`
- `market_context_high->unknown_4h` score `-1.1092` n `99` status `ready` deltaP `-0.3141` edge `0.015` maxDD `-3.7602`
- `market_context_high->unknown_1h` score `-1.7569` n `102` status `ready` deltaP `1.6761` edge `-0.0845` maxDD `-3.1801`
- `market_context_high->crypto_major_4h` score `-1.8451` n `99` status `ready` deltaP `9.6128` edge `0.2119` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
