# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T05:22:33.229140+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8292`

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

- `risk_on_high->equity_1h` score `0.6545` n `37` status `ready` deltaP `16.4954` edge `0.0163` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6545` n `37` status `ready` deltaP `16.4954` edge `0.0163` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5916` n `37` status `ready` deltaP `14.5493` edge `0.0059` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5916` n `37` status `ready` deltaP `14.5493` edge `0.0059` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.5831` n `37` status `ready` deltaP `16.4454` edge `0.0449` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.5831` n `37` status `ready` deltaP `16.4454` edge `0.0449` maxDD `-1.7154`
- `market_context_high->commodity_24h` score `0.2889` n `78` status `ready` deltaP `13.3962` edge `0.0553` maxDD `-3.6055`
- `market_context_high->index_1h` score `0.066` n `78` status `ready` deltaP `6.3719` edge `0.0015` maxDD `-0.5082`
- `risk_on_high->fx_1h` score `0.0199` n `37` status `ready` deltaP `4.2038` edge `0.0004` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0199` n `37` status `ready` deltaP `4.2038` edge `0.0004` maxDD `-0.0698`
- `risk_on_high->index_4h` score `-0.2934` n `37` status `ready` deltaP `6.8392` edge `0.0013` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.2934` n `37` status `ready` deltaP `6.8392` edge `0.0013` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.3689` n `78` status `ready` deltaP `5.7106` edge `0.0178` maxDD `-2.9203`
- `risk_on_high->fx_4h` score `-0.3891` n `37` status `ready` deltaP `-2.8758` edge `-0.0043` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.3891` n `37` status `ready` deltaP `-2.8758` edge `-0.0043` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.4174` n `78` status `ready` deltaP `0.7677` edge `0.0079` maxDD `-0.9891`
- `market_context_high->metal_1h` score `-0.6184` n `78` status `ready` deltaP `-5.5313` edge `-0.0049` maxDD `-0.6669`
- `risk_on_high->metal_1h` score `-0.7902` n `37` status `ready` deltaP `-6.0164` edge `0.0003` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.7902` n `37` status `ready` deltaP `-6.0164` edge `0.0003` maxDD `-0.0831`
- `risk_on_high->commodity_1h` score `-0.8472` n `37` status `ready` deltaP `-3.1478` edge `-0.0211` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
