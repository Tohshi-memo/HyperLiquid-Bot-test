# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T05:52:14.648232+00:00`
- Price records: `672`
- Market context records: `1395`
- Flow alert records: `5928`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `12.7556` n `157` status `ready` deltaP `27.8331` edge `0.9906` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.4935` n `157` status `ready` deltaP `28.8184` edge `0.9673` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.2856` n `157` status `ready` deltaP `11.5622` edge `1.0301` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.988` n `157` status `ready` deltaP `19.555` edge `0.3106` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.3262` n `157` status `ready` deltaP `12.7256` edge `0.3417` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.4628` n `191` status `ready` deltaP `8.2198` edge `0.1501` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0571` n `157` status `ready` deltaP `9.8803` edge `0.0438` maxDD `-1.3925`
- `market_context_high->index_1h` score `0.0235` n `203` status `ready` deltaP `5.0191` edge `0.015` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.0488` n `203` status `ready` deltaP `3.2226` edge `0.0303` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.3081` n `203` status `ready` deltaP `3.463` edge `-0.0022` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.5153` n `191` status `ready` deltaP `0.8635` edge `0.0602` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.6544` n `203` status `ready` deltaP `5.0279` edge `-0.0018` maxDD `-4.9162`
- `market_context_high->crypto_alt_1h` score `-0.7201` n `203` status `ready` deltaP `0.6814` edge `0.0225` maxDD `-3.6309`
- `market_context_high->metal_4h` score `-0.7908` n `191` status `ready` deltaP `7.7903` edge `0.0289` maxDD `-6.7388`
- `market_context_high->commodity_1h` score `-0.9239` n `203` status `ready` deltaP `-1.9365` edge `-0.0026` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.3959` n `191` status `ready` deltaP `7.2796` edge `0.1671` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.4184` n `191` status `ready` deltaP `4.5428` edge `0.1224` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-1.4386` n `203` status `ready` deltaP `-1.5693` edge `-0.0029` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.5899` n `191` status `ready` deltaP `-3.9203` edge `-0.0093` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-4.3413` n `191` status `ready` deltaP `-12.4362` edge `-0.0242` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
