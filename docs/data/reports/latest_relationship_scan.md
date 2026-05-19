# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T06:07:17.169963+00:00`
- Price records: `672`
- Market context records: `1192`
- Flow alert records: `5338`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `18.4873` n `137` status `ready` deltaP `44.3697` edge `1.358` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.6609` n `137` status `ready` deltaP `22.1158` edge `0.6926` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `4.6033` n `137` status `ready` deltaP `3.8945` edge `0.4793` maxDD `-6.7322`
- `market_context_high->metal_24h` score `4.1939` n `137` status `ready` deltaP `-3.9133` edge `0.5423` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.8303` n `137` status `ready` deltaP `15.1182` edge `0.2014` maxDD `-3.6396`
- `market_context_high->equity_24h` score `2.2505` n `137` status `ready` deltaP `16.099` edge `0.3129` maxDD `-14.2815`
- `market_context_high->index_24h` score `2.019` n `137` status `ready` deltaP `15.8227` edge `0.1714` maxDD `-5.3574`
- `market_context_high->commodity_24h` score `1.0798` n `137` status `ready` deltaP `-3.5457` edge `0.5455` maxDD `-25.6744`
- `market_context_high->index_4h` score `0.9696` n `137` status `ready` deltaP `10.6507` edge `0.0781` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5389` n `137` status `ready` deltaP `8.7897` edge `0.018` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4487` n `137` status `ready` deltaP `4.373` edge `0.046` maxDD `-1.3546`
- `market_context_high->fx_24h` score `0.0596` n `137` status `ready` deltaP `8.3105` edge `0.0491` maxDD `-4.4161`
- `market_context_high->crypto_major_4h` score `-0.0422` n `137` status `ready` deltaP `7.4562` edge `0.137` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.1438` n `137` status `ready` deltaP `4.2211` edge `-0.001` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.212` n `137` status `ready` deltaP `8.2456` edge `-0.0116` maxDD `-2.2164`
- `market_context_high->crypto_major_1h` score `-0.2773` n `137` status `ready` deltaP `4.2769` edge `0.0125` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.3995` n `137` status `ready` deltaP `0.3847` edge `0.0305` maxDD `-3.4088`
- `market_context_high->unknown_24h` score `-0.6309` n `137` status `ready` deltaP `2.3533` edge `0.2047` maxDD `-10.1706`
- `market_context_high->commodity_1h` score `-0.8797` n `137` status `ready` deltaP `-2.8541` edge `0.0072` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.073` n `137` status `ready` deltaP `5.2397` edge `0.124` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
