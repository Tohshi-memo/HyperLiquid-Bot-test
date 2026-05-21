# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T10:52:18.908975+00:00`
- Price records: `672`
- Market context records: `1416`
- Flow alert records: `5990`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8785`

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

- `market_context_high->crypto_major_24h` score `11.8952` n `154` status `ready` deltaP `27.3539` edge `0.9221` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.4461` n `154` status `ready` deltaP `28.7811` edge `0.9636` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.3705` n `154` status `ready` deltaP `10.5993` edge `1.0436` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.6957` n `154` status `ready` deltaP `19.3813` edge `0.2874` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.2071` n `154` status `ready` deltaP `12.5271` edge `0.3331` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.8942` n `202` status `ready` deltaP `5.2373` edge `0.1226` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0395` n `154` status `ready` deltaP `9.3592` edge `0.0458` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0364` n `202` status `ready` deltaP `4.5563` edge `0.0131` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1098` n `202` status `ready` deltaP `2.9554` edge `0.027` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.3087` n `202` status `ready` deltaP `3.3957` edge `-0.0018` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5519` n `202` status `ready` deltaP `1.4036` edge `0.0317` maxDD `-3.6309`
- `market_context_high->metal_1h` score `-0.7155` n `202` status `ready` deltaP `4.9149` edge `-0.007` maxDD `-5.0663`
- `market_context_high->commodity_1h` score `-0.8146` n `202` status `ready` deltaP `-1.1398` edge `0.0012` maxDD `-2.252`
- `market_context_high->index_4h` score `-0.844` n `202` status `ready` deltaP `-1.2346` edge `0.0468` maxDD `-3.7119`
- `market_context_high->crypto_major_4h` score `-1.4092` n `202` status `ready` deltaP `5.1376` edge `0.1192` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-1.4129` n `202` status `ready` deltaP `-1.1635` edge `0.0007` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.4407` n `202` status `ready` deltaP `6.7344` edge `0.167` maxDD `-19.5565`
- `market_context_high->fx_4h` score `-1.5848` n `202` status `ready` deltaP `-3.811` edge `-0.0096` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-2.5891` n `202` status `ready` deltaP `-10.0896` edge `-0.01` maxDD `-8.04`
- `market_context_high->metal_4h` score `-2.8253` n `202` status `ready` deltaP `4.3015` edge `-0.0043` maxDD `-11.7852`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
