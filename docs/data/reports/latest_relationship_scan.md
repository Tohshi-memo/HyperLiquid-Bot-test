# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T00:52:16.343482+00:00`
- Price records: `672`
- Market context records: `1374`
- Flow alert records: `5867`
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

- `market_context_high->crypto_major_24h` score `13.1841` n `146` status `ready` deltaP `30.9694` edge `1.0054` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.1341` n `146` status `ready` deltaP `13.4989` edge `1.0879` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.7764` n `146` status `ready` deltaP `28.6744` edge `0.9085` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.1314` n `146` status `ready` deltaP `22.0082` edge `0.3062` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6432` n `146` status `ready` deltaP `15.0828` edge `0.3524` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5685` n `171` status `ready` deltaP `8.8504` edge `0.1547` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.1869` n `146` status `ready` deltaP `9.3988` edge `0.0447` maxDD `-1.3427`
- `market_context_high->index_1h` score `-0.0754` n `183` status `ready` deltaP `3.6051` edge `0.0128` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.1293` n `171` status `ready` deltaP `10.7438` edge `0.0607` maxDD `-6.4478`
- `market_context_high->equity_1h` score `-0.1662` n `183` status `ready` deltaP `2.3552` edge `0.0263` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.3594` n `171` status `ready` deltaP `0.4832` edge `0.0596` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.4303` n `183` status `ready` deltaP `2.0549` edge `-0.003` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.4338` n `183` status `ready` deltaP `6.0674` edge `0.0028` maxDD `-3.5762`
- `market_context_high->commodity_1h` score `-0.6727` n `183` status `ready` deltaP `-0.1309` edge `0.0063` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.7396` n `183` status `ready` deltaP `0.3035` edge `0.0234` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-0.9541` n `183` status `ready` deltaP `-1.8749` edge `-0.0033` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.3099` n `171` status `ready` deltaP `-8.427` edge `-0.0147` maxDD `-1.4313`
- `market_context_high->crypto_alt_4h` score `-1.5942` n `171` status `ready` deltaP `7.0354` edge `0.1522` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.7879` n `171` status `ready` deltaP `3.3439` edge `0.0996` maxDD `-13.3376`
- `market_context_high->unknown_4h` score `-3.1481` n `171` status `ready` deltaP `1.9665` edge `-0.1896` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
