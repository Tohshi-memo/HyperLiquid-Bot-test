# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T11:07:27.512504+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2612`

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

- `market_context_high->unknown_1h` score `11329.2887` n `114` status `ready` deltaP `1.6205` edge `944.1164` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7456.1345` n `108` status `ready` deltaP `0.5194` edge `621.3695` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `13.4397` n `102` status `ready` deltaP `30.77` edge `1.3408` maxDD `-29.4102`
- `market_context_high->crypto_alt_24h` score `7.6436` n `102` status `ready` deltaP `16.8812` edge `1.1284` maxDD `-43.6516`
- `market_context_high->crypto_major_4h` score `1.9211` n `108` status `ready` deltaP `5.9225` edge `0.4025` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.649` n `108` status `ready` deltaP `6.9896` edge `0.2984` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.5558` n `108` status `ready` deltaP `18.0217` edge `0.0606` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.0784` n `114` status `ready` deltaP `5.5389` edge `0.0195` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.3413` n `114` status `ready` deltaP `4.3203` edge `0.0671` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.3674` n `114` status `ready` deltaP `3.9132` edge `0.0045` maxDD `-1.2295`
- `market_context_high->equity_1h` score `-1.1261` n `114` status `ready` deltaP `6.9939` edge `0.0374` maxDD `-10.8962`
- `market_context_high->crypto_alt_1h` score `-1.15` n `114` status `ready` deltaP `-1.8201` edge `0.0385` maxDD `-5.4428`
- `market_context_high->fx_1h` score `-1.4289` n `114` status `ready` deltaP `-9.2447` edge `-0.0015` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.6909` n `108` status `ready` deltaP `-0.7001` edge `-0.0019` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.2885` n `114` status `ready` deltaP `-8.0891` edge `-0.0236` maxDD `-4.3877`
- `market_context_high->fx_4h` score `-2.3534` n `108` status `ready` deltaP `-14.493` edge `-0.0035` maxDD `-1.794`
- `market_context_high->metal_24h` score `-4.6703` n `102` status `ready` deltaP `14.5425` edge `0.1102` maxDD `-37.7071`
- `market_context_high->fx_24h` score `-6.5491` n `102` status `ready` deltaP `-16.7177` edge `-0.007` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.8305` n `108` status `ready` deltaP `-27.1285` edge `-0.1024` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-8.837` n `108` status `ready` deltaP `-4.6127` edge `-0.0235` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
