# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T22:22:19.902915+00:00`
- Price records: `672`
- Market context records: `1466`
- Flow alert records: `6131`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_alt_24h` score `13.0122` n `167` status `ready` deltaP `28.9328` edge `1.0931` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `12.0347` n `167` status `ready` deltaP `27.6572` edge `0.9317` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.2745` n `167` status `ready` deltaP `15.3692` edge `1.0038` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.2059` n `167` status `ready` deltaP `20.089` edge `0.3252` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.193` n `167` status `ready` deltaP `13.3359` edge `0.4932` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5686` n `221` status `ready` deltaP `7.3819` edge `0.1645` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2766` n `167` status `ready` deltaP `12.0987` edge `0.0473` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.1094` n `221` status `ready` deltaP `3.4784` edge `0.0142` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1292` n `221` status `ready` deltaP `1.9881` edge `0.036` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.1906` n `221` status `ready` deltaP `11.4709` edge `0.2396` maxDD `-19.5565`
- `market_context_high->index_4h` score `-0.3996` n `221` status `ready` deltaP `1.3954` edge `0.0663` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.4768` n `221` status `ready` deltaP `0.6889` edge `-0.0025` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5515` n `221` status `ready` deltaP `1.7707` edge `0.0446` maxDD `-4.1892`
- `market_context_high->fx_4h` score `-1.0459` n `221` status `ready` deltaP `-4.1607` edge `-0.0093` maxDD `-1.4313`
- `market_context_high->crypto_major_4h` score `-1.0814` n `221` status `ready` deltaP `5.4409` edge `0.1445` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-1.1902` n `221` status `ready` deltaP `4.9347` edge `0.0015` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-1.2279` n `221` status `ready` deltaP `-1.4238` edge `-0.0007` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.5805` n `221` status `ready` deltaP `-0.6482` edge `0.0083` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.7733` n `221` status `ready` deltaP `8.0565` edge `0.0677` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.0508` n `221` status `ready` deltaP `-11.6861` edge `-0.0698` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
