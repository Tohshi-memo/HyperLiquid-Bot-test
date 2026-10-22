# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T09:22:30.784102+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7875`

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

- `risk_on_high->commodity_24h` score `0.6479` n `37` status `ready` deltaP `17.0305` edge `0.0493` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.6479` n `37` status `ready` deltaP `17.0305` edge `0.0493` maxDD `-1.7154`
- `risk_on_high->equity_1h` score `0.6093` n `37` status `ready` deltaP `16.3457` edge `0.0115` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6093` n `37` status `ready` deltaP `16.3457` edge `0.0115` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5784` n `37` status `ready` deltaP `14.3996` edge `0.0052` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5784` n `37` status `ready` deltaP `14.3996` edge `0.0052` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.3537` n `78` status `ready` deltaP `13.9813` edge `0.0597` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.0542` n `37` status `ready` deltaP `4.8026` edge `0.0008` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0542` n `37` status `ready` deltaP `4.8026` edge `0.0008` maxDD `-0.0698`
- `market_context_high->index_1h` score `0.0527` n `78` status `ready` deltaP `6.2222` edge `0.0008` maxDD `-0.5082`
- `risk_on_high->index_4h` score `-0.2871` n `37` status `ready` deltaP `6.8392` edge `0.0021` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.2871` n `37` status `ready` deltaP `6.8392` edge `0.0021` maxDD `-0.7604`
- `risk_on_high->fx_4h` score `-0.3021` n `37` status `ready` deltaP `-1.5038` edge `-0.0023` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.3021` n `37` status `ready` deltaP `-1.5038` edge `-0.0023` maxDD `-0.1126`
- `market_context_high->commodity_4h` score `-0.4373` n `78` status `ready` deltaP `5.1008` edge `0.0131` maxDD `-2.9203`
- `market_context_high->commodity_1h` score `-0.44` n `78` status `ready` deltaP `0.4683` edge `0.007` maxDD `-0.9891`
- `market_context_high->metal_1h` score `-0.6285` n `78` status `ready` deltaP `-5.681` edge `-0.0052` maxDD `-0.6669`
- `risk_on_high->metal_1h` score `-0.8058` n `37` status `ready` deltaP `-6.1661` edge `0.0` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.8058` n `37` status `ready` deltaP `-6.1661` edge `0.0` maxDD `-0.0831`
- `risk_on_high->commodity_1h` score `-0.8698` n `37` status `ready` deltaP `-3.4472` edge `-0.022` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
