# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T06:37:20.620524+00:00`
- Price records: `672`
- Market context records: `1398`
- Flow alert records: `5938`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8784`

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

- `market_context_high->crypto_major_24h` score `12.7264` n `156` status `ready` deltaP `28.0982` edge `0.9864` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.4637` n `156` status `ready` deltaP `28.8061` edge `0.9649` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.3651` n `156` status `ready` deltaP `11.5518` edge `1.0368` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.927` n `156` status `ready` deltaP `19.4978` edge `0.3059` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.2742` n `156` status `ready` deltaP `12.6603` edge `0.3378` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.4874` n `193` status `ready` deltaP `8.4813` edge `0.1504` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0458` n `156` status `ready` deltaP `9.7088` edge `0.044` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0061` n `204` status `ready` deltaP `4.6496` edge `0.015` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.0559` n `204` status `ready` deltaP `3.0439` edge `0.0309` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.2885` n `204` status `ready` deltaP `3.6779` edge `-0.002` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.4825` n `193` status `ready` deltaP `1.2282` edge `0.0605` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.6569` n `204` status `ready` deltaP `5.2307` edge `-0.0016` maxDD `-5.0663`
- `market_context_high->crypto_alt_1h` score `-0.725` n `204` status `ready` deltaP `0.5607` edge `0.0229` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.9184` n `204` status `ready` deltaP `-1.6878` edge `-0.0038` maxDD `-2.252`
- `market_context_high->metal_4h` score `-1.2891` n `193` status `ready` deltaP `7.1772` edge `0.0227` maxDD `-8.571`
- `market_context_high->crypto_major_4h` score `-1.4098` n `193` status `ready` deltaP `4.8299` edge `0.1212` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-1.4837` n `204` status `ready` deltaP `-1.6731` edge `-0.0018` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.5167` n `193` status `ready` deltaP `6.5351` edge `0.162` maxDD `-19.5565`
- `market_context_high->fx_4h` score `-1.5422` n `193` status `ready` deltaP `-3.3994` edge `-0.0088` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-2.7955` n `193` status `ready` deltaP `-11.7797` edge `-0.0252` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
