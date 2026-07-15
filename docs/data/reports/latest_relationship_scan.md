# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T08:22:27.768605+00:00`
- Price records: `672`
- Market context records: `6798`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11656`

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

- `market_context_high->unknown_24h` score `0.8488` n `176` status `ready` deltaP `-1.3731` edge `0.4932` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.2095` n `176` status `ready` deltaP `9.012` edge `0.1442` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.236` n `185` status `ready` deltaP `6.6483` edge `0.022` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.383` n `185` status `ready` deltaP `3.7959` edge `0.0192` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.4355` n `185` status `ready` deltaP `-1.0851` edge `-0.0001` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.6603` n `185` status `ready` deltaP `-1.8587` edge `-0.0007` maxDD `-0.7249`
- `market_context_high->metal_1h` score `-0.6938` n `185` status `ready` deltaP `-4.9935` edge `-0.0028` maxDD `-1.2285`
- `market_context_high->commodity_1h` score `-0.705` n `185` status `ready` deltaP `-1.8255` edge `-0.0099` maxDD `-2.1314`
- `market_context_high->equity_1h` score `-1.2906` n `185` status `ready` deltaP `2.2326` edge `-0.018` maxDD `-4.0213`
- `market_context_high->fx_4h` score `-1.3859` n `183` status `ready` deltaP `4.6939` edge `-0.0026` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.437` n `183` status `ready` deltaP `-2.4823` edge `-0.0187` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5419` n `185` status `ready` deltaP `-4.9935` edge `-0.0051` maxDD `-3.2083`
- `market_context_high->index_4h` score `-1.5553` n `183` status `ready` deltaP `2.4873` edge `-0.0226` maxDD `-6.1373`
- `market_context_high->metal_4h` score `-2.6983` n `183` status `ready` deltaP `-5.7919` edge `-0.009` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.1174` n `183` status `ready` deltaP `0.4023` edge `-0.0709` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-3.2676` n `183` status `ready` deltaP `-0.4748` edge `-0.0615` maxDD `-20.3405`
- `market_context_high->unknown_4h` score `-3.3867` n `183` status `ready` deltaP `-13.8103` edge `0.0464` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.5032` n `176` status `ready` deltaP `-9.7853` edge `-0.0064` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-4.7097` n `183` status `ready` deltaP `-0.055` edge `-0.1589` maxDD `-28.5635`
- `market_context_high->metal_24h` score `-9.352` n `176` status `ready` deltaP `-19.5392` edge `-0.2202` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
