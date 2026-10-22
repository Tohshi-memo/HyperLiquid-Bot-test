# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T02:22:28.215319+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8382`

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

- `risk_on_high->equity_1h` score `0.7013` n `37` status `ready` deltaP `16.3457` edge `0.0233` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.7013` n `37` status `ready` deltaP `16.3457` edge `0.0233` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5971` n `37` status `ready` deltaP `14.5493` edge `0.0066` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5971` n `37` status `ready` deltaP `14.5493` edge `0.0066` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.5504` n `37` status `ready` deltaP `16.4454` edge `0.0407` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.5504` n `37` status `ready` deltaP `16.4454` edge `0.0407` maxDD `-1.7154`
- `market_context_high->commodity_24h` score `0.2561` n `78` status `ready` deltaP `13.3962` edge `0.0511` maxDD `-3.6055`
- `market_context_high->index_1h` score `0.0714` n `78` status `ready` deltaP `6.3719` edge `0.0022` maxDD `-0.5082`
- `risk_on_high->fx_1h` score `0.0394` n `37` status `ready` deltaP `4.5032` edge `0.0009` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0394` n `37` status `ready` deltaP `4.5032` edge `0.0009` maxDD `-0.0698`
- `risk_on_high->index_4h` score `-0.2269` n `37` status `ready` deltaP `7.4416` edge `0.0058` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.2269` n `37` status `ready` deltaP `7.4416` edge `0.0058` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.341` n `78` status `ready` deltaP `5.963` edge `0.0197` maxDD `-2.9203`
- `risk_on_high->fx_4h` score `-0.3434` n `37` status `ready` deltaP `-2.1785` edge `-0.0031` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.3434` n `37` status `ready` deltaP `-2.1785` edge `-0.0031` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.3473` n `78` status `ready` deltaP `1.8156` edge `0.0099` maxDD `-0.9891`
- `market_context_high->metal_1h` score `-0.5997` n `78` status `ready` deltaP `-5.5313` edge `-0.0025` maxDD `-0.6669`
- `risk_on_high->metal_1h` score `-0.7614` n `37` status `ready` deltaP `-6.0164` edge `0.0027` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.7614` n `37` status `ready` deltaP `-6.0164` edge `0.0027` maxDD `-0.0831`
- `risk_on_high->commodity_1h` score `-0.7771` n `37` status `ready` deltaP `-2.0999` edge `-0.0191` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
