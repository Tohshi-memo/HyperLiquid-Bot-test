# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T13:22:21.750265+00:00`
- Price records: `672`
- Market context records: `1426`
- Flow alert records: `6021`
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

- `market_context_high->crypto_alt_24h` score `11.7629` n `154` status `ready` deltaP `28.7811` edge `0.99` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `11.7584` n `154` status `ready` deltaP `27.3539` edge `0.9107` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.7187` n `154` status `ready` deltaP `12.1618` edge `1.0622` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.8277` n `154` status `ready` deltaP `19.3813` edge `0.2984` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7147` n `154` status `ready` deltaP `12.5271` edge `0.3754` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.9678` n `202` status `ready` deltaP `5.5422` edge `0.1267` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0719` n `154` status `ready` deltaP `9.3592` edge `0.0485` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.215` n `212` status `ready` deltaP `2.9686` edge `0.0088` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.3343` n `212` status `ready` deltaP `1.9884` edge `0.0189` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.4395` n `212` status `ready` deltaP `1.8501` edge `-0.0024` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.6142` n `212` status `ready` deltaP `-0.2994` edge `0.0123` maxDD `-2.252`
- `market_context_high->index_4h` score `-0.6586` n `202` status `ready` deltaP `0.1374` edge `0.0531` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `-0.8078` n `212` status `ready` deltaP `1.1468` edge `0.0274` maxDD `-4.1892`
- `market_context_high->metal_1h` score `-0.9365` n `212` status `ready` deltaP `3.8499` edge `-0.0136` maxDD `-6.2374`
- `market_context_high->crypto_alt_4h` score `-1.1354` n `202` status `ready` deltaP `8.1064` edge `0.1833` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.2746` n `202` status `ready` deltaP `5.29` edge `0.1294` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.5958` n `202` status `ready` deltaP `-3.9634` edge `-0.0095` maxDD `-1.4313`
- `market_context_high->crypto_major_1h` score `-1.8313` n `212` status `ready` deltaP `-1.8783` edge `-0.0044` maxDD `-6.1883`
- `market_context_high->commodity_4h` score `-2.6634` n `202` status `ready` deltaP `-10.3945` edge `-0.0175` maxDD `-8.04`
- `market_context_high->metal_4h` score `-2.7627` n `202` status `ready` deltaP `4.4539` edge `-0.0001` maxDD `-11.7852`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
