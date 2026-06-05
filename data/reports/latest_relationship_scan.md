# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T17:52:28.529235+00:00`
- Price records: `672`
- Market context records: `2991`
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

- `market_context_high->crypto_alt_24h` score `17.0111` n `98` status `ready` deltaP `5.2898` edge `1.774` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.1519` n `98` status `ready` deltaP `42.1202` edge `0.7429` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `11.4557` n `98` status `ready` deltaP `17.7013` edge `0.8831` maxDD `-1.7175`
- `market_context_high->equity_24h` score `7.8054` n `98` status `ready` deltaP `16.2628` edge `0.7424` maxDD `-12.6963`
- `market_context_high->index_24h` score `4.896` n `98` status `ready` deltaP `16.0467` edge `0.3991` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.5919` n `99` status `ready` deltaP `15.2193` edge `0.2368` maxDD `-0.7819`
- `market_context_high->index_4h` score `2.4955` n `99` status `ready` deltaP `19.754` edge `0.1551` maxDD `-1.9733`
- `market_context_high->commodity_4h` score `2.4576` n `99` status `ready` deltaP `17.7923` edge `0.1509` maxDD `-2.8438`
- `market_context_high->crypto_alt_4h` score `0.9723` n `99` status `ready` deltaP `24.4026` edge `0.4181` maxDD `-30.8239`
- `market_context_high->index_1h` score `0.252` n `103` status `ready` deltaP `6.3107` edge `0.029` maxDD `-1.6721`
- `market_context_high->equity_1h` score `-0.0306` n `103` status `ready` deltaP `4.6596` edge `0.042` maxDD `-3.8253`
- `market_context_high->commodity_1h` score `-0.1673` n `103` status `ready` deltaP `0.109` edge `0.0183` maxDD `-0.9706`
- `market_context_high->fx_1h` score `-0.5132` n `103` status `ready` deltaP `-1.8327` edge `0.001` maxDD `-0.1908`
- `market_context_high->metal_1h` score `-1.029` n `103` status `ready` deltaP `-1.8967` edge `-0.0058` maxDD `-5.4112`
- `market_context_high->fx_4h` score `-1.0297` n `99` status `ready` deltaP `-8.5859` edge `0.0031` maxDD `-0.5631`
- `market_context_high->unknown_4h` score `-1.0876` n `99` status `ready` deltaP `-0.3141` edge `0.0168` maxDD `-3.7602`
- `market_context_high->crypto_alt_1h` score `-1.2275` n `103` status `ready` deltaP `7.2816` edge `0.0302` maxDD `-12.1494`
- `market_context_high->crypto_major_1h` score `-1.2316` n `103` status `ready` deltaP `4.7497` edge `0.0029` maxDD `-12.7307`
- `market_context_high->crypto_major_4h` score `-1.8381` n `99` status `ready` deltaP `9.6128` edge `0.2128` maxDD `-33.6701`
- `market_context_high->unknown_1h` score `-1.8528` n `103` status `ready` deltaP `1.1526` edge `-0.089` maxDD `-3.1801`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
