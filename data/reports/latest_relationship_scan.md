# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T09:52:16.694352+00:00`
- Price records: `672`
- Market context records: `1515`
- Flow alert records: `6273`
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

- `market_context_high->metal_24h` score `14.394` n `157` status `ready` deltaP `24.1872` edge `1.1383` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.1947` n `157` status `ready` deltaP `28.8184` edge `0.9424` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.9526` n `157` status `ready` deltaP `28.0067` edge `0.8392` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.6796` n `157` status `ready` deltaP `19.555` edge `0.2849` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.3886` n `157` status `ready` deltaP `12.7256` edge `0.3469` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.0259` n `157` status `ready` deltaP `18.9148` edge `0.0643` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.8386` n `184` status `ready` deltaP `5.7264` edge `0.1147` maxDD `-3.6396`
- `market_context_high->index_1h` score `-0.3958` n `194` status `ready` deltaP `1.443` edge `0.0039` maxDD `-1.7205`
- `market_context_high->crypto_alt_1h` score `-0.5289` n `194` status `ready` deltaP `0.2485` edge `0.0329` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5299` n `194` status `ready` deltaP `-0.6358` edge `0.0201` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.5331` n `194` status `ready` deltaP `-0.3333` edge `-0.0029` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.7726` n `194` status `ready` deltaP `5.1037` edge `0.0005` maxDD `-6.3532`
- `market_context_high->crypto_alt_4h` score `-0.8474` n `184` status `ready` deltaP `8.5366` edge `0.1664` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.8806` n `184` status `ready` deltaP `4.4075` edge `0.1286` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-0.9933` n `194` status `ready` deltaP `-0.6991` edge `0.013` maxDD `-6.1883`
- `market_context_high->unknown_24h` score `-1.0285` n `157` status `ready` deltaP `-2.8563` edge `0.2063` maxDD `-10.1706`
- `market_context_high->metal_4h` score `-1.1059` n `184` status `ready` deltaP `11.4794` edge `0.1005` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.1614` n `194` status `ready` deltaP `-0.5324` edge `-0.0011` maxDD `-4.7041`
- `market_context_high->index_4h` score `-1.345` n `184` status `ready` deltaP `-4.5732` edge `0.0273` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.6841` n `184` status `ready` deltaP `-5.5276` edge `-0.0106` maxDD `-1.4313`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
