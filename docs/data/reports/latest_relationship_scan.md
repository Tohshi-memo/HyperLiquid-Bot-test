# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T13:22:29.184121+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7698`

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

- `risk_on_high->commodity_24h` score `0.5765` n `37` status `ready` deltaP `16.0023` edge `0.047` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.5765` n `37` status `ready` deltaP `16.0023` edge `0.047` maxDD `-1.7154`
- `risk_on_high->index_1h` score `0.5231` n `37` status `ready` deltaP `13.5014` edge `0.0041` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5231` n `37` status `ready` deltaP `13.5014` edge `0.0041` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.5134` n `37` status `ready` deltaP `15.5972` edge `0.0042` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.5134` n `37` status `ready` deltaP `15.5972` edge `0.0042` maxDD `-0.7219`
- `market_context_high->commodity_24h` score `0.2822` n `78` status `ready` deltaP `12.9531` edge `0.0574` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.0729` n `37` status `ready` deltaP `5.102` edge `0.0012` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0729` n `37` status `ready` deltaP `5.102` edge `0.0012` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.1537` n `37` status `ready` deltaP `0.6303` edge `0.0025` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1537` n `37` status `ready` deltaP `0.6303` edge `0.0025` maxDD `-0.1126`
- `market_context_high->index_1h` score `-0.2059` n `81` status `ready` deltaP `3.4246` edge `-0.0007` maxDD `-0.5491`
- `market_context_high->commodity_1h` score `-0.3213` n `81` status `ready` deltaP `2.2252` edge `0.0105` maxDD `-0.9891`
- `risk_on_high->index_4h` score `-0.4171` n `37` status `ready` deltaP `5.3148` edge `-0.0044` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4171` n `37` status `ready` deltaP `5.3148` edge `-0.0044` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.4513` n `78` status `ready` deltaP `5.1008` edge `0.0113` maxDD `-2.9203`
- `market_context_high->metal_1h` score `-0.49` n `81` status `ready` deltaP `-3.4967` edge `-0.002` maxDD `-0.6669`
- `risk_on_high->metal_1h` score `-0.8046` n `37` status `ready` deltaP `-6.1661` edge `0.0001` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.8046` n `37` status `ready` deltaP `-6.1661` edge `0.0001` maxDD `-0.0831`
- `risk_on_high->commodity_1h` score `-0.8682` n `37` status `ready` deltaP `-3.4472` edge `-0.0218` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
