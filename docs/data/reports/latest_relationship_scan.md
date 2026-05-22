# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T14:37:28.471762+00:00`
- Price records: `672`
- Market context records: `1535`
- Flow alert records: `6332`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8802`

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

- `market_context_high->metal_24h` score `12.9264` n `175` status `ready` deltaP `23.2569` edge `1.0222` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.7394` n `175` status `ready` deltaP `28.6676` edge `0.9888` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.1127` n `175` status `ready` deltaP `28.0675` edge `0.7688` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.011` n `175` status `ready` deltaP `20.4722` edge `0.3064` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7329` n `175` status `ready` deltaP `13.7738` edge `0.3686` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.8195` n `175` status `ready` deltaP `17.7599` edge `0.0548` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.1653` n `199` status `ready` deltaP `4.0239` edge `0.0964` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.5469` n `199` status `ready` deltaP `11.1204` edge `0.1877` maxDD `-19.5565`
- `market_context_high->crypto_alt_1h` score `-0.5748` n `199` status `ready` deltaP `-0.3799` edge `0.0312` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.5821` n `199` status `ready` deltaP `-1.2457` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_major_4h` score `-0.5948` n `199` status `ready` deltaP `7.1455` edge `0.147` maxDD `-13.3376`
- `market_context_high->index_1h` score `-0.75` n `199` status `ready` deltaP `0.0256` edge `0.0005` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7547` n `199` status `ready` deltaP `4.8484` edge `0.0045` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.7718` n `199` status `ready` deltaP `-0.7966` edge `-0.0015` maxDD `-4.7041`
- `market_context_high->equity_1h` score `-0.8763` n `199` status `ready` deltaP `-1.6316` edge `0.0187` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-1.0914` n `199` status `ready` deltaP `-1.7911` edge `0.0077` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.2771` n `199` status `ready` deltaP `-8.7204` edge `-0.0127` maxDD `-1.4313`
- `market_context_high->index_4h` score `-1.3838` n `199` status `ready` deltaP `-4.5923` edge `0.0242` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.5751` n `199` status `ready` deltaP `8.8392` edge `0.079` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-5.3632` n `199` status `ready` deltaP `-16.3769` edge `-0.1157` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
