# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T09:37:18.971016+00:00`
- Price records: `672`
- Market context records: `1514`
- Flow alert records: `6270`
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

- `market_context_high->metal_24h` score `14.2431` n `158` status `ready` deltaP `23.7561` edge `1.1286` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.1705` n `158` status `ready` deltaP `28.8305` edge `0.9403` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.8817` n `158` status `ready` deltaP `28.0349` edge `0.8331` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.6769` n `158` status `ready` deltaP `19.6114` edge `0.2843` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.4286` n `158` status `ready` deltaP `12.7901` edge `0.3498` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.0228` n `158` status `ready` deltaP `19.0115` edge `0.0634` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.9419` n `184` status `ready` deltaP `6.1175` edge `0.1207` maxDD `-3.6396`
- `market_context_high->index_1h` score `-0.3594` n `194` status `ready` deltaP `1.8088` edge `0.0045` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.4742` n `194` status `ready` deltaP `-0.27` edge `0.0223` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.5133` n `194` status `ready` deltaP `0.0324` edge `-0.0028` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5149` n `194` status `ready` deltaP `0.2485` edge `0.0347` maxDD `-4.1892`
- `market_context_high->metal_1h` score `-0.7797` n `194` status `ready` deltaP `5.1037` edge `-0.0004` maxDD `-6.3532`
- `market_context_high->crypto_alt_4h` score `-0.7928` n `184` status `ready` deltaP `8.9276` edge `0.1708` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.8471` n `184` status `ready` deltaP `4.7985` edge `0.1303` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-0.9587` n `194` status `ready` deltaP `-0.3333` edge `0.015` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.0951` n `184` status `ready` deltaP `11.4794` edge `0.1014` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.1722` n `194` status `ready` deltaP `-0.5324` edge `-0.002` maxDD `-4.7041`
- `market_context_high->index_4h` score `-1.2994` n `184` status `ready` deltaP `-4.1821` edge `0.0285` maxDD `-3.7119`
- `market_context_high->unknown_24h` score `-1.3884` n `158` status `ready` deltaP `-2.6305` edge `0.1748` maxDD `-10.1706`
- `market_context_high->fx_4h` score `-1.6516` n `184` status `ready` deltaP `-5.1365` edge `-0.0105` maxDD `-1.4313`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
