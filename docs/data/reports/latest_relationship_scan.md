# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T12:07:26.866172+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `6933`

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

- `market_context_high->unknown_24h` score `358.8152` n `53` status `ready` deltaP `-15.0255` edge `30.0378` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `43.3486` n `85` status `ready` deltaP `-6.8041` edge `3.7158` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.9996` n `53` status `ready` deltaP `33.7133` edge `0.5681` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `4.4883` n `53` status `ready` deltaP `-1.4773` edge `0.9001` maxDD `-17.8526`
- `market_context_high->index_24h` score `3.2219` n `53` status `ready` deltaP `29.812` edge `0.1346` maxDD `-0.8552`
- `market_context_high->fx_4h` score `1.2664` n `85` status `ready` deltaP `18.6298` edge `0.0097` maxDD `-0.2692`
- `market_context_high->fx_24h` score `0.6499` n `53` status `ready` deltaP `18.596` edge `0.0215` maxDD `-0.6386`
- `market_context_high->commodity_1h` score `0.3716` n `85` status `ready` deltaP `6.8352` edge `0.0105` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `0.0612` n `85` status `ready` deltaP `8.2173` edge `0.0064` maxDD `-1.6002`
- `market_context_high->fx_1h` score `-0.0884` n `85` status `ready` deltaP `2.2579` edge `0.0018` maxDD `-0.271`
- `market_context_high->metal_1h` score `-0.4856` n `85` status `ready` deltaP `-0.7591` edge `0.0019` maxDD `-0.7275`
- `market_context_high->metal_4h` score `-0.5697` n `85` status `ready` deltaP `-2.4839` edge `0.0158` maxDD `-1.1153`
- `market_context_high->crypto_major_1h` score `-0.6938` n `85` status `ready` deltaP `-2.3635` edge `0.0157` maxDD `-3.7778`
- `market_context_high->unknown_1h` score `-0.7442` n `85` status `ready` deltaP `-8.4748` edge `0.0281` maxDD `-1.0231`
- `market_context_high->crypto_alt_1h` score `-1.0507` n `85` status `ready` deltaP `-2.2561` edge `0.0309` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `-1.2468` n `85` status `ready` deltaP `-4.7076` edge `0.0821` maxDD `-11.1784`
- `market_context_high->index_4h` score `-1.4251` n `85` status `ready` deltaP `-13.377` edge `-0.0003` maxDD `-1.1242`
- `market_context_high->index_1h` score `-1.7505` n `85` status `ready` deltaP `-8.3956` edge `-0.0037` maxDD `-0.5627`
- `market_context_high->equity_1h` score `-1.8412` n `85` status `ready` deltaP `-8.5012` edge `-0.0098` maxDD `-2.2898`
- `market_context_high->crypto_alt_4h` score `-1.9307` n `85` status `ready` deltaP `-7.3619` edge `0.0574` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
