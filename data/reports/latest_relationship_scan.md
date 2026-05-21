# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T20:37:14.621955+00:00`
- Price records: `672`
- Market context records: `1458`
- Flow alert records: `6109`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_alt_24h` score `12.9151` n `163` status `ready` deltaP `28.8887` edge `1.0853` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `12.0012` n `163` status `ready` deltaP `27.569` edge `0.9295` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.5134` n `163` status `ready` deltaP `15.0094` edge `1.0261` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.2278` n `163` status `ready` deltaP `19.8832` edge `0.3284` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.0926` n `163` status `ready` deltaP `13.1007` edge `0.4864` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5082` n `221` status `ready` deltaP `7.077` edge `0.1615` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2484` n `163` status `ready` deltaP `11.6404` edge `0.048` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.08` n `224` status `ready` deltaP `3.8014` edge `0.0145` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1295` n `224` status `ready` deltaP `1.9995` edge `0.0359` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.336` n `221` status `ready` deltaP `11.3184` edge `0.2285` maxDD `-19.5565`
- `market_context_high->fx_1h` score `-0.4676` n `224` status `ready` deltaP `0.8822` edge `-0.0026` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.4733` n `221` status `ready` deltaP `0.9381` edge `0.0632` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `-0.5453` n `224` status `ready` deltaP `2.0584` edge `0.0432` maxDD `-4.1892`
- `market_context_high->fx_4h` score `-1.0452` n `221` status `ready` deltaP `-4.1607` edge `-0.0092` maxDD `-1.4313`
- `market_context_high->metal_1h` score `-1.1405` n `224` status `ready` deltaP `5.031` edge `0.005` maxDD `-6.3532`
- `market_context_high->crypto_major_4h` score `-1.1541` n `221` status `ready` deltaP `5.1312` edge `0.1405` maxDD `-13.3376`
- `market_context_high->commodity_1h` score `-1.2549` n `224` status `ready` deltaP `-1.6414` edge `-0.0015` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.62` n `224` status `ready` deltaP `-0.9169` edge `0.0068` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.8119` n `221` status `ready` deltaP `7.904` edge `0.0655` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-3.8805` n `221` status `ready` deltaP `-11.5337` edge `-0.0653` maxDD `-16.0917`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
