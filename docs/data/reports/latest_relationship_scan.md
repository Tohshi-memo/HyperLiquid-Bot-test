# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T23:37:13.858536+00:00`
- Price records: `672`
- Market context records: `1368`
- Flow alert records: `5851`
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

- `market_context_high->crypto_major_24h` score `13.0899` n `141` status `ready` deltaP `31.6674` edge `0.9929` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.4306` n `141` status `ready` deltaP `13.5897` edge `1.112` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.3457` n `141` status `ready` deltaP `28.6015` edge `0.8731` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.1149` n `141` status `ready` deltaP `22.5362` edge `0.3013` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.618` n `141` status `ready` deltaP `15.5622` edge `0.3471` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.7979` n `166` status `ready` deltaP `9.4035` edge `0.1618` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.6723` n `141` status `ready` deltaP `11.1296` edge `0.049` maxDD `-1.0402`
- `market_context_high->metal_4h` score `-0.0467` n `166` status `ready` deltaP `11.4164` edge `0.0631` maxDD `-6.4478`
- `market_context_high->index_1h` score `-0.0678` n `178` status `ready` deltaP `3.7526` edge `0.0128` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1448` n `178` status `ready` deltaP `2.0689` edge `0.0235` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.2276` n `166` status `ready` deltaP `2.0588` edge `0.066` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.3331` n `178` status `ready` deltaP `1.1623` edge `-0.0039` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.4282` n `178` status `ready` deltaP `6.2202` edge `0.0025` maxDD `-3.5762`
- `market_context_high->commodity_1h` score `-0.7251` n `178` status `ready` deltaP `-0.4861` edge `0.0043` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.8644` n `178` status `ready` deltaP `-0.3717` edge `0.0175` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.051` n `178` status `ready` deltaP `-2.5079` edge `-0.0115` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.3696` n `166` status `ready` deltaP `-9.5155` edge `-0.0155` maxDD `-1.3986`
- `market_context_high->crypto_alt_4h` score `-1.5768` n `166` status `ready` deltaP `7.1481` edge `0.1529` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.9727` n `166` status `ready` deltaP `2.7145` edge `0.0884` maxDD `-13.3376`
- `market_context_high->unknown_4h` score `-2.9148` n `166` status `ready` deltaP `0.3636` edge `-0.149` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
