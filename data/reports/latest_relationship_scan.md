# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T04:37:24.675718+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8297`

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

- `risk_on_high->equity_1h` score `0.7528` n `37` status `ready` deltaP `16.196` edge `0.0309` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.7528` n `37` status `ready` deltaP `16.196` edge `0.0309` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5239` n `37` status `ready` deltaP `13.0523` edge `0.0072` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5239` n `37` status `ready` deltaP `13.0523` edge `0.0072` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.2032` n `60` status `ready` deltaP `15.3125` edge `0.0` maxDD `-1.8119`
- `market_context_high->index_1h` score `-0.0017` n `78` status `ready` deltaP `4.8749` edge `0.0028` maxDD `-0.5082`
- `risk_on_high->fx_1h` score `-0.0322` n `37` status `ready` deltaP `3.1559` edge `0.0007` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `-0.0322` n `37` status `ready` deltaP `3.1559` edge `0.0007` maxDD `-0.0698`
- `risk_on_high->index_4h` score `-0.1343` n `37` status `ready` deltaP `7.7538` edge `0.0156` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.1343` n `37` status `ready` deltaP `7.7538` edge `0.0156` maxDD `-0.7604`
- `risk_on_high->equity_4h` score `-0.2032` n `37` status `ready` deltaP `4.4825` edge `0.0695` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.2032` n `37` status `ready` deltaP `4.4825` edge `0.0695` maxDD `-4.0351`
- `risk_on_high->fx_4h` score `-0.2048` n `37` status `ready` deltaP `0.173` edge `-0.001` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2048` n `37` status `ready` deltaP `0.173` edge `-0.001` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.2991` n `78` status `ready` deltaP `3.7617` edge `0.0031` maxDD `-0.9891`
- `risk_on_high->commodity_24h` score `-0.3269` n `37` status `ready` deltaP `13.1053` edge `-0.0495` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.3269` n `37` status `ready` deltaP `13.1053` edge `-0.0495` maxDD `-1.7154`
- `market_context_high->metal_1h` score `-0.5584` n `78` status `ready` deltaP `-4.7828` edge `-0.0022` maxDD `-0.6669`
- `market_context_high->commodity_4h` score `-0.5593` n `78` status `ready` deltaP `6.6252` edge `-0.0127` maxDD `-2.9203`
- `risk_on_high->metal_1h` score `-0.6979` n `37` status `ready` deltaP `-5.2679` edge `0.003` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
