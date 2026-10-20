# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T02:52:25.747664+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8301`

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

- `risk_on_high->equity_1h` score `0.992` n `39` status `ready` deltaP `17.8259` edge `0.0507` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.992` n `39` status `ready` deltaP `17.8259` edge `0.0507` maxDD `-0.7219`
- `market_context_high->commodity_24h` score `0.8196` n `63` status `ready` deltaP `17.1379` edge `0.0392` maxDD `-1.8119`
- `risk_on_high->index_1h` score `0.6204` n `39` status `ready` deltaP `14.6822` edge `0.0087` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.6204` n `39` status `ready` deltaP `14.6822` edge `0.0087` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.2046` n `39` status `ready` deltaP `15.1843` edge `-0.0044` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2046` n `39` status `ready` deltaP `15.1843` edge `-0.0044` maxDD `-1.7154`
- `market_context_high->index_1h` score `0.0789` n `81` status `ready` deltaP `6.2301` edge `0.0041` maxDD `-0.5082`
- `risk_on_high->equity_4h` score `0.0002` n `39` status `ready` deltaP `6.3399` edge `0.0832` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `0.0002` n `39` status `ready` deltaP `6.3399` edge `0.0832` maxDD `-4.0351`
- `risk_on_high->index_4h` score `-0.0351` n `39` status `ready` deltaP `9.1816` edge `0.0188` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.0351` n `39` status `ready` deltaP `9.1816` edge `0.0188` maxDD `-0.7604`
- `risk_on_high->fx_1h` score `-0.2496` n `39` status `ready` deltaP `0.3839` edge `0.0` maxDD `-0.0985`
- `risk_on_and_context->fx_1h` score `-0.2496` n `39` status `ready` deltaP `0.3839` edge `0.0` maxDD `-0.0985`
- `risk_on_high->metal_1h` score `-0.2693` n `39` status `ready` deltaP `-2.5181` edge `0.0083` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.2693` n `39` status `ready` deltaP `-2.5181` edge `0.0083` maxDD `-0.0831`
- `risk_on_high->fx_4h` score `-0.3361` n `39` status `ready` deltaP `-2.3218` edge `-0.0012` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.3361` n `39` status `ready` deltaP `-2.3218` edge `-0.0012` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.3409` n `81` status `ready` deltaP `3.1992` edge `0.0015` maxDD `-0.9891`
- `market_context_high->equity_1h` score `-0.4161` n `81` status `ready` deltaP `6.9047` edge `-0.0042` maxDD `-4.6137`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
