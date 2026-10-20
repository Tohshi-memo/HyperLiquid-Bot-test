# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T00:07:27.809701+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8202`

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

- `market_context_high->commodity_24h` score `2.6333` n `73` status `ready` deltaP `22.139` edge `0.157` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.9143` n `40` status `ready` deltaP `16.8862` edge `0.047` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.9143` n `40` status `ready` deltaP `16.8862` edge `0.047` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5621` n `40` status `ready` deltaP `13.7425` edge `0.0075` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5621` n `40` status `ready` deltaP `13.7425` edge `0.0075` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.3308` n `40` status `ready` deltaP `16.1458` edge `-0.0003` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.3308` n `40` status `ready` deltaP `16.1458` edge `-0.0003` maxDD `-1.7154`
- `risk_on_high->equity_4h` score `-0.0801` n `40` status `ready` deltaP `6.25` edge `0.0735` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.0801` n `40` status `ready` deltaP `6.25` edge `0.0735` maxDD `-4.0351`
- `market_context_high->crypto_major_1h` score `-0.1328` n `92` status `ready` deltaP `1.5816` edge `0.0741` maxDD `-4.8007`
- `risk_on_high->index_4h` score `-0.1908` n `40` status `ready` deltaP `6.9207` edge `0.0139` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.1908` n `40` status `ready` deltaP `6.9207` edge `0.0139` maxDD `-0.7604`
- `risk_on_high->fx_1h` score `-0.2128` n `40` status `ready` deltaP `1.1527` edge `-0.0004` maxDD `-0.0985`
- `risk_on_and_context->fx_1h` score `-0.2128` n `40` status `ready` deltaP `1.1527` edge `-0.0004` maxDD `-0.0985`
- `market_context_high->metal_1h` score `-0.2951` n `92` status `ready` deltaP `-0.755` edge `0.0047` maxDD `-0.6669`
- `risk_on_high->metal_1h` score `-0.3462` n `40` status `ready` deltaP `-3.9072` edge `0.0077` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.3462` n `40` status `ready` deltaP `-3.9072` edge `0.0077` maxDD `-0.0831`
- `market_context_high->index_1h` score `-0.4993` n `92` status `ready` deltaP `1.5686` edge `-0.002` maxDD `-0.6722`
- `risk_on_high->fx_4h` score `-0.5301` n `40` status `ready` deltaP `-2.5` edge `-0.0011` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.5301` n `40` status `ready` deltaP `-2.5` edge `-0.0011` maxDD `-0.1126`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
