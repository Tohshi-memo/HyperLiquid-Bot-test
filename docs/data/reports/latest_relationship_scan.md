# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T13:07:25.310022+00:00`
- Price records: `672`
- Market context records: `3180`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8856`

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

- `market_context_high->commodity_24h` score `13.8605` n `102` status `ready` deltaP `47.1405` edge `0.8836` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `12.3429` n `102` status `ready` deltaP `20.2308` edge `0.9425` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.3963` n `102` status `ready` deltaP `13.991` edge `2.3654` maxDD `-71.142`
- `market_context_high->index_24h` score `6.2047` n `102` status `ready` deltaP `29.4934` edge `0.8543` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.3748` n `102` status `ready` deltaP `12.4489` edge `1.3195` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.1162` n `134` status `ready` deltaP `19.8125` edge `0.1734` maxDD `-1.9973`
- `market_context_high->unknown_4h` score `0.7198` n `134` status `ready` deltaP `11.3555` edge `0.2065` maxDD `-14.7778`
- `market_context_high->fx_24h` score `0.7029` n `102` status `ready` deltaP `11.7953` edge `0.0027` maxDD `-0.4876`
- `market_context_high->commodity_1h` score `0.3468` n `140` status `ready` deltaP `5.9795` edge `0.0313` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.3322` n `140` status `ready` deltaP `6.4628` edge `0.0206` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.4158` n `140` status `ready` deltaP `6.2318` edge `0.1181` maxDD `-14.7034`
- `market_context_high->index_4h` score `-0.8467` n `134` status `ready` deltaP `16.5384` edge `0.0721` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0033` n `140` status `ready` deltaP `3.7297` edge `0.0728` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.2226` n `140` status `ready` deltaP `4.6193` edge `0.0159` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3378` n `134` status `ready` deltaP `-11.4352` edge `-0.0068` maxDD `-1.4115`
- `market_context_high->fx_1h` score `-1.6` n `140` status `ready` deltaP `-8.9179` edge `-0.0052` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-2.0726` n `140` status `ready` deltaP `-3.8024` edge `-0.008` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.2243` n `134` status `ready` deltaP `17.5078` edge `0.4026` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.0608` n `140` status `ready` deltaP `2.9513` edge `-0.0721` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.6366` n `134` status `ready` deltaP `10.4455` edge `0.2565` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
