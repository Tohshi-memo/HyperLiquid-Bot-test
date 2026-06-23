# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T12:22:34.859406+00:00`
- Price records: `672`
- Market context records: `4515`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9771`

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

- `risk_on_high->unknown_4h` score `132.3878` n `47` status `ready` deltaP `7.2619` edge `11.1155` maxDD `-7.5275`
- `risk_on_and_context->unknown_4h` score `132.3878` n `47` status `ready` deltaP `7.2619` edge `11.1155` maxDD `-7.5275`
- `market_context_high->unknown_1h` score `44.8628` n `194` status `ready` deltaP `5.0019` edge `3.8029` maxDD `-5.4807`
- `market_context_high->unknown_4h` score `26.3658` n `194` status `ready` deltaP `6.1871` edge `2.3125` maxDD `-7.5275`
- `risk_on_high->equity_4h` score `5.0923` n `47` status `ready` deltaP `41.7683` edge `0.1459` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.0923` n `47` status `ready` deltaP `41.7683` edge `0.1459` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.6823` n `47` status `ready` deltaP `27.6563` edge `0.2588` maxDD `-2.2387`
- `risk_on_and_context->crypto_major_4h` score `4.6823` n `47` status `ready` deltaP `27.6563` edge `0.2588` maxDD `-2.2387`
- `risk_on_high->unknown_24h` score `3.5774` n `47` status `ready` deltaP `13.2794` edge `0.2515` maxDD `-2.6864`
- `risk_on_and_context->unknown_24h` score `3.5774` n `47` status `ready` deltaP `13.2794` edge `0.2515` maxDD `-2.6864`
- `risk_on_high->metal_24h` score `2.8602` n `47` status `ready` deltaP `-12.3116` edge `0.5467` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `2.8602` n `47` status `ready` deltaP `-12.3116` edge `0.5467` maxDD `-4.834`
- `risk_on_high->metal_4h` score `2.114` n `47` status `ready` deltaP `16.4147` edge `0.1003` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `2.114` n `47` status `ready` deltaP `16.4147` edge `0.1003` maxDD `-1.3516`
- `risk_on_high->index_24h` score `1.2417` n `47` status `ready` deltaP `21.1325` edge `0.0143` maxDD `-2.4702`
- `risk_on_and_context->index_24h` score `1.2417` n `47` status `ready` deltaP `21.1325` edge `0.0143` maxDD `-2.4702`
- `risk_on_high->equity_1h` score `1.1958` n `47` status `ready` deltaP `14.9733` edge `0.0341` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.1958` n `47` status `ready` deltaP `14.9733` edge `0.0341` maxDD `-0.7415`
- `risk_on_high->fx_4h` score `0.5588` n `47` status `ready` deltaP `14.7509` edge `0.0073` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.5588` n `47` status `ready` deltaP `14.7509` edge `0.0073` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
