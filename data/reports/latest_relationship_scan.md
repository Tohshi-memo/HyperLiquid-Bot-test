# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T09:22:21.173100+00:00`
- Price records: `672`
- Market context records: `1513`
- Flow alert records: `6267`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8791`

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

- `market_context_high->metal_24h` score `14.088` n `159` status `ready` deltaP `23.3327` edge `1.1185` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.1546` n `159` status `ready` deltaP `28.8424` edge `0.9389` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.8203` n `159` status `ready` deltaP `28.0628` edge `0.8278` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.6694` n `159` status `ready` deltaP `19.6672` edge `0.2833` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.4577` n `159` status `ready` deltaP `12.8538` edge `0.3518` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.0221` n `159` status `ready` deltaP `19.1071` edge `0.0627` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.9604` n `185` status `ready` deltaP `6.0942` edge `0.1224` maxDD `-3.6396`
- `market_context_high->index_1h` score `-0.3522` n `194` status `ready` deltaP `1.8088` edge `0.0051` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.4114` n `194` status `ready` deltaP `0.0957` edge `0.0251` maxDD `-2.8014`
- `market_context_high->crypto_alt_1h` score `-0.4787` n `194` status `ready` deltaP `0.6142` edge `0.0369` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.4935` n `194` status `ready` deltaP `0.3982` edge `-0.0027` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.7604` n `194` status `ready` deltaP `-0.5324` edge `-0.0018` maxDD `-4.7041`
- `market_context_high->crypto_alt_4h` score `-0.7778` n `185` status `ready` deltaP `8.9749` edge `0.1724` maxDD `-19.5565`
- `market_context_high->metal_1h` score `-0.7797` n `194` status `ready` deltaP `5.1037` edge `-0.0004` maxDD `-6.3532`
- `market_context_high->crypto_major_4h` score `-0.8283` n `185` status `ready` deltaP `5.0247` edge `0.1312` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-0.9462` n `194` status `ready` deltaP `-0.3333` edge `0.0166` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.1406` n `185` status `ready` deltaP `11.1503` edge `0.0998` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.304` n `185` status `ready` deltaP `-4.1348` edge `0.0278` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.6403` n `185` status `ready` deltaP `-5.0099` edge `-0.0104` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-1.7534` n `159` status `ready` deltaP `-2.4076` edge `0.1429` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
