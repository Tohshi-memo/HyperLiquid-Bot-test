# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T01:07:18.729205+00:00`
- Price records: `672`
- Market context records: `1479`
- Flow alert records: `6166`
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

- `market_context_high->crypto_alt_24h` score `12.7692` n `172` status `ready` deltaP `28.985` edge `1.0725` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `11.701` n `172` status `ready` deltaP `27.7616` edge `0.9032` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.0826` n `172` status `ready` deltaP `16.4204` edge `0.9808` maxDD `-6.3373`
- `market_context_high->equity_24h` score `4.3809` n `172` status `ready` deltaP `13.6144` edge `0.507` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.2602` n `172` status `ready` deltaP `20.3327` edge `0.3281` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.5689` n `215` status `ready` deltaP `6.9661` edge `0.1673` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.409` n `172` status `ready` deltaP `13.7234` edge `0.0475` maxDD `-1.3925`
- `market_context_high->crypto_alt_4h` score `-0.0584` n `215` status `ready` deltaP `11.4889` edge `0.2505` maxDD `-19.5565`
- `market_context_high->equity_1h` score `-0.1099` n `215` status `ready` deltaP `2.1083` edge `0.0368` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.2097` n `215` status `ready` deltaP `2.5094` edge `0.0123` maxDD `-1.7205`
- `market_context_high->crypto_alt_1h` score `-0.4723` n `215` status `ready` deltaP `2.0554` edge `0.0493` maxDD `-4.1892`
- `market_context_high->index_4h` score `-0.498` n `215` status `ready` deltaP `0.6892` edge `0.0628` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.5511` n `215` status `ready` deltaP `-0.6496` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_major_4h` score `-0.8974` n `215` status `ready` deltaP `6.0599` edge `0.1557` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.0355` n `215` status `ready` deltaP `-4.5555` edge `-0.0095` maxDD `-1.4313`
- `market_context_high->metal_1h` score `-1.1731` n `215` status `ready` deltaP `5.3433` edge `0.0002` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-1.1961` n `215` status `ready` deltaP `-1.1308` edge `0.0` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.5419` n `215` status `ready` deltaP `-0.5856` edge `0.0111` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.7782` n `215` status `ready` deltaP `7.9949` edge `0.0677` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.0646` n `215` status `ready` deltaP `-11.8761` edge `-0.0703` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
