# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T10:22:17.330382+00:00`
- Price records: `672`
- Market context records: `1517`
- Flow alert records: `6279`
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

- `market_context_high->metal_24h` score `14.3759` n `158` status `ready` deltaP `24.5011` edge `1.1347` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.2196` n `158` status `ready` deltaP `28.8305` edge `0.9444` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.8361` n `158` status `ready` deltaP `28.0349` edge `0.8293` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.6913` n `158` status `ready` deltaP `19.6114` edge `0.2855` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.353` n `158` status `ready` deltaP `12.7901` edge `0.3435` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.0553` n `158` status `ready` deltaP `19.2972` edge `0.0642` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.8595` n `183` status `ready` deltaP `5.8976` edge `0.1153` maxDD `-3.6396`
- `market_context_high->index_1h` score `-0.425` n `195` status `ready` deltaP `1.1232` edge `0.0036` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.5589` n `195` status `ready` deltaP `-0.8137` edge `-0.003` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5838` n `195` status `ready` deltaP `-0.2372` edge `0.0291` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.6425` n `195` status `ready` deltaP `-1.1638` edge `0.0184` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.8524` n `183` status `ready` deltaP `8.6366` edge `0.1651` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.9013` n `183` status `ready` deltaP `4.1758` edge `0.1275` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-1.0392` n `195` status `ready` deltaP `-1.1769` edge `0.0103` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.0941` n `183` status `ready` deltaP `11.5071` edge `0.1013` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-1.0981` n `195` status `ready` deltaP `5.5313` edge `0.0052` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-1.2208` n `195` status `ready` deltaP `-1.0049` edge `-0.0029` maxDD `-4.7041`
- `market_context_high->unknown_24h` score `-1.26` n `158` status `ready` deltaP `-2.6305` edge `0.1855` maxDD `-10.1706`
- `market_context_high->index_4h` score `-1.2947` n `183` status `ready` deltaP `-4.0792` edge `0.0282` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.6813` n `183` status `ready` deltaP `-5.5078` edge `-0.0105` maxDD `-1.4313`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
