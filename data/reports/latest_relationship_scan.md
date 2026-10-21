# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-21T15:29:06.362693+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8656`

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

- `risk_on_high->equity_1h` score `0.6849` n `37` status `ready` deltaP `16.3895` edge `0.0209` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6849` n `37` status `ready` deltaP `16.3895` edge `0.0209` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.6052` n `37` status `ready` deltaP `14.7501` edge `0.0063` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.6052` n `37` status `ready` deltaP `14.7501` edge `0.0063` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.1886` n `37` status `ready` deltaP `13.8688` edge `0.0115` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1886` n `37` status `ready` deltaP `13.8688` edge `0.0115` maxDD `-1.7154`
- `market_context_high->index_1h` score `0.0796` n `78` status `ready` deltaP `6.5727` edge `0.0019` maxDD `-0.5082`
- `risk_on_high->fx_1h` score `0.0106` n `37` status `ready` deltaP `3.9796` edge `0.0007` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0106` n `37` status `ready` deltaP `3.9796` edge `0.0007` maxDD `-0.0698`
- `market_context_high->commodity_24h` score `-0.1056` n `78` status `ready` deltaP `10.8196` edge `0.0219` maxDD `-3.6055`
- `risk_on_high->index_4h` score `-0.1769` n `37` status `ready` deltaP `7.9833` edge `0.0086` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.1769` n `37` status `ready` deltaP `7.9833` edge `0.0086` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.2812` n `78` status `ready` deltaP `6.7236` edge `0.0223` maxDD `-2.9203`
- `risk_on_high->fx_4h` score `-0.3027` n `37` status `ready` deltaP `-1.5749` edge `-0.0019` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.3027` n `37` status `ready` deltaP `-1.5749` edge `-0.0019` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.3177` n `78` status `ready` deltaP `2.3406` edge `0.0102` maxDD `-0.9891`
- `market_context_high->metal_1h` score `-0.6199` n `78` status `ready` deltaP `-5.7702` edge `-0.0035` maxDD `-0.6669`
- `risk_on_high->equity_4h` score `-0.6362` n `37` status `ready` deltaP `5.1113` edge `0.0098` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.6362` n `37` status `ready` deltaP `5.1113` edge `0.0098` maxDD `-4.0351`
- `risk_on_high->commodity_1h` score `-0.7475` n `37` status `ready` deltaP `-1.5749` edge `-0.0188` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
