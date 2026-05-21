# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T06:22:18.811893+00:00`
- Price records: `672`
- Market context records: `1397`
- Flow alert records: `5935`
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

- `market_context_high->crypto_major_24h` score `12.784` n `156` status `ready` deltaP `28.0982` edge `0.9912` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.4613` n `156` status `ready` deltaP `28.8061` edge `0.9647` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.4078` n `156` status `ready` deltaP `11.7254` edge `1.0392` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.9546` n `156` status `ready` deltaP `19.4978` edge `0.3082` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.309` n `156` status `ready` deltaP `12.6603` edge `0.3407` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5374` n `192` status `ready` deltaP `8.5366` edge `0.1542` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0422` n `156` status `ready` deltaP `9.7088` edge `0.0437` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0205` n `204` status `ready` deltaP `4.4999` edge `0.0148` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.0559` n `204` status `ready` deltaP `3.0439` edge `0.0309` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.3017` n `204` status `ready` deltaP `3.5282` edge `-0.0021` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.4618` n `192` status `ready` deltaP `1.2322` edge `0.0622` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.6538` n `204` status `ready` deltaP `5.2307` edge `-0.0012` maxDD `-5.0663`
- `market_context_high->crypto_alt_1h` score `-0.743` n `204` status `ready` deltaP `0.411` edge `0.0224` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.9256` n `204` status `ready` deltaP `-1.6878` edge `-0.0044` maxDD `-2.252`
- `market_context_high->metal_4h` score `-1.0802` n `192` status `ready` deltaP `7.4822` edge `0.027` maxDD `-8.0187`
- `market_context_high->crypto_major_4h` score `-1.3811` n `192` status `ready` deltaP `4.9796` edge `0.1226` maxDD `-13.3376`
- `market_context_high->crypto_alt_4h` score `-1.4971` n `192` status `ready` deltaP `6.7201` edge `0.1624` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-1.4993` n `204` status `ready` deltaP `-1.8228` edge `-0.0021` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.5654` n `192` status `ready` deltaP `-3.6585` edge `-0.009` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-2.8374` n `192` status `ready` deltaP `-12.1062` edge `-0.0284` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
