# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T11:37:15.622089+00:00`
- Price records: `672`
- Market context records: `1522`
- Flow alert records: `6295`
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

- `market_context_high->metal_24h` score `13.9402` n `163` status `ready` deltaP `23.7496` edge `1.1034` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.3767` n `163` status `ready` deltaP `28.8887` edge `0.9571` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.5566` n `163` status `ready` deltaP `28.1708` edge `0.8051` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.755` n `163` status `ready` deltaP `19.8832` edge `0.289` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.469` n `163` status `ready` deltaP `13.1007` edge `0.3511` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.9808` n `163` status `ready` deltaP `18.8757` edge `0.0608` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.6196` n `188` status `ready` deltaP `4.6543` edge `0.1036` maxDD `-3.6396`
- `market_context_high->fx_1h` score `-0.5821` n `199` status `ready` deltaP `-1.2457` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.6014` n `199` status `ready` deltaP `-0.3799` edge `0.0278` maxDD `-4.1892`
- `market_context_high->index_1h` score `-0.7081` n `199` status `ready` deltaP `0.325` edge `0.002` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7633` n `199` status `ready` deltaP `4.9981` edge `0.0024` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.7889` n `199` status `ready` deltaP `-0.7966` edge `-0.0037` maxDD `-4.7041`
- `market_context_high->crypto_alt_4h` score `-0.8176` n `188` status `ready` deltaP `9.2599` edge `0.1654` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.8575` n `188` status `ready` deltaP `4.8521` edge `0.1286` maxDD `-13.3376`
- `market_context_high->equity_1h` score `-0.9003` n `199` status `ready` deltaP `-1.7813` edge `0.0177` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-1.0743` n `199` status `ready` deltaP `-1.6414` edge `0.0089` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.226` n `188` status `ready` deltaP `10.6383` edge `0.0961` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.4226` n `188` status `ready` deltaP `-4.9883` edge `0.0236` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.7763` n `188` status `ready` deltaP `-6.6197` edge `-0.011` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-2.8952` n `163` status `ready` deltaP `-1.8905` edge `0.0443` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
