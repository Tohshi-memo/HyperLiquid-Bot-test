# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T01:52:30.776417+00:00`
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

- `market_context_high->commodity_24h` score `1.5964` n `67` status `ready` deltaP `19.3174` edge `0.0894` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `1.0357` n `39` status `ready` deltaP `18.275` edge `0.0533` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `1.0357` n `39` status `ready` deltaP `18.275` edge `0.0533` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.6476` n `39` status `ready` deltaP `15.1313` edge `0.0092` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.6476` n `39` status `ready` deltaP `15.1313` edge `0.0092` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.1338` n `39` status `ready` deltaP `15.1843` edge `-0.0103` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1338` n `39` status `ready` deltaP `15.1843` edge `-0.0103` maxDD `-1.7154`
- `market_context_high->index_1h` score `0.0304` n `85` status `ready` deltaP `5.3575` edge `0.0037` maxDD `-0.5082`
- `risk_on_high->index_4h` score `-0.0753` n `39` status `ready` deltaP `8.5718` edge `0.0177` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.0753` n `39` status `ready` deltaP `8.5718` edge `0.0177` maxDD `-0.7604`
- `risk_on_high->equity_4h` score `-0.0775` n `39` status `ready` deltaP `5.7301` edge `0.0773` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.0775` n `39` status `ready` deltaP `5.7301` edge `0.0773` maxDD `-4.0351`
- `risk_on_high->fx_1h` score `-0.2598` n `39` status `ready` deltaP `0.2342` edge `-0.0003` maxDD `-0.0985`
- `risk_on_and_context->fx_1h` score `-0.2598` n `39` status `ready` deltaP `0.2342` edge `-0.0003` maxDD `-0.0985`
- `market_context_high->metal_1h` score `-0.2645` n `85` status `ready` deltaP `-0.2254` edge `0.0051` maxDD `-0.6669`
- `risk_on_high->metal_1h` score `-0.2662` n `39` status `ready` deltaP `-2.5181` edge `0.0087` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.2662` n `39` status `ready` deltaP `-2.5181` edge `0.0087` maxDD `-0.0831`
- `risk_on_high->fx_4h` score `-0.3645` n `39` status `ready` deltaP `-2.7791` edge `-0.0018` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.3645` n `39` status `ready` deltaP `-2.7791` edge `-0.0018` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.4566` n `85` status `ready` deltaP `1.7858` edge `-0.0019` maxDD `-1.1503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
