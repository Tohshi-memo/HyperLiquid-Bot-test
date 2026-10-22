# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T04:22:30.742206+00:00`
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

- `risk_on_high->equity_1h` score `0.6709` n `37` status `ready` deltaP `16.4954` edge `0.0184` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6709` n `37` status `ready` deltaP `16.4954` edge `0.0184` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5924` n `37` status `ready` deltaP `14.5493` edge `0.006` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5924` n `37` status `ready` deltaP `14.5493` edge `0.006` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.5745` n `37` status `ready` deltaP `16.4454` edge `0.0438` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.5745` n `37` status `ready` deltaP `16.4454` edge `0.0438` maxDD `-1.7154`
- `market_context_high->commodity_24h` score `0.2803` n `78` status `ready` deltaP `13.3962` edge `0.0542` maxDD `-3.6055`
- `market_context_high->index_1h` score `0.0668` n `78` status `ready` deltaP `6.3719` edge `0.0016` maxDD `-0.5082`
- `risk_on_high->fx_1h` score `0.0285` n `37` status `ready` deltaP `4.3535` edge `0.0005` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0285` n `37` status `ready` deltaP `4.3535` edge `0.0005` maxDD `-0.0698`
- `risk_on_high->index_4h` score `-0.2801` n `37` status `ready` deltaP `6.9745` edge `0.0021` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.2801` n `37` status `ready` deltaP `6.9745` edge `0.0021` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.375` n `78` status `ready` deltaP `5.5646` edge `0.018` maxDD `-2.9203`
- `risk_on_high->fx_4h` score `-0.3817` n `37` status `ready` deltaP `-2.7192` edge `-0.0044` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.3817` n `37` status `ready` deltaP `-2.7192` edge `-0.0044` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.3878` n `78` status `ready` deltaP `1.2168` edge `0.0087` maxDD `-0.9891`
- `market_context_high->metal_1h` score `-0.6129` n `78` status `ready` deltaP `-5.5313` edge `-0.0042` maxDD `-0.6669`
- `risk_on_high->metal_1h` score `-0.7818` n `37` status `ready` deltaP `-6.0164` edge `0.001` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.7818` n `37` status `ready` deltaP `-6.0164` edge `0.001` maxDD `-0.0831`
- `risk_on_high->commodity_1h` score `-0.8176` n `37` status `ready` deltaP `-2.6987` edge `-0.0203` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
