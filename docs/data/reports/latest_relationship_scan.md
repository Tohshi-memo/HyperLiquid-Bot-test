# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T11:22:15.824711+00:00`
- Price records: `672`
- Market context records: `1521`
- Flow alert records: `6292`
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

- `market_context_high->metal_24h` score `14.0182` n `162` status `ready` deltaP `23.9005` edge `1.1089` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.3338` n `162` status `ready` deltaP `28.8773` edge `0.9536` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.5964` n `162` status `ready` deltaP `28.1443` edge `0.8086` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.7436` n `162` status `ready` deltaP `19.8302` edge `0.2884` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.4462` n `162` status `ready` deltaP `13.0402` edge `0.3496` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.9949` n `162` status `ready` deltaP `18.9622` edge `0.0614` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.6616` n `187` status `ready` deltaP `4.8944` edge `0.1055` maxDD `-3.6396`
- `market_context_high->fx_1h` score `-0.5821` n `199` status `ready` deltaP `-1.2457` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5928` n `199` status `ready` deltaP `-0.2302` edge `0.0279` maxDD `-4.1892`
- `market_context_high->index_1h` score `-0.7081` n `199` status `ready` deltaP `0.325` edge `0.002` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7625` n `199` status `ready` deltaP `4.9981` edge `0.0025` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.7866` n `199` status `ready` deltaP `-0.7966` edge `-0.0034` maxDD `-4.7041`
- `market_context_high->crypto_alt_4h` score `-0.8233` n `187` status `ready` deltaP `9.0607` edge `0.166` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.858` n `187` status `ready` deltaP `4.7827` edge `0.129` maxDD `-13.3376`
- `market_context_high->equity_1h` score `-0.9051` n `199` status `ready` deltaP `-1.7813` edge `0.0173` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-1.0649` n `199` status `ready` deltaP `-1.4917` edge `0.0091` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.2234` n `187` status `ready` deltaP `10.5802` edge `0.0967` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.4015` n `187` status `ready` deltaP `-4.8137` edge `0.0242` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.7541` n `187` status `ready` deltaP `-6.3722` edge `-0.0108` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-2.5834` n `162` status `ready` deltaP `-2.1026` edge `0.0717` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
