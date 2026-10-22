# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T15:07:28.614961+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6912`

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

- `risk_on_high->equity_1h` score `0.5524` n `37` status `ready` deltaP `15.7469` edge `0.0082` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.5524` n `37` status `ready` deltaP `15.7469` edge `0.0082` maxDD `-0.7219`
- `risk_on_high->commodity_24h` score `0.5327` n `37` status `ready` deltaP `15.5053` edge `0.0447` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.5327` n `37` status `ready` deltaP `15.5053` edge `0.0447` maxDD `-1.7154`
- `risk_on_high->index_1h` score `0.4974` n `37` status `ready` deltaP `13.0523` edge `0.0038` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4974` n `37` status `ready` deltaP `13.0523` edge `0.0038` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.2385` n `78` status `ready` deltaP `12.4561` edge `0.0551` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.1102` n `37` status `ready` deltaP `5.7008` edge `0.002` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1102` n `37` status `ready` deltaP `5.7008` edge `0.002` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.1397` n `37` status `ready` deltaP `0.6303` edge `0.0043` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1397` n `37` status `ready` deltaP `0.6303` edge `0.0043` maxDD `-0.1126`
- `market_context_high->index_1h` score `-0.3176` n `86` status `ready` deltaP `2.43` edge `-0.0045` maxDD `-0.8606`
- `market_context_high->commodity_1h` score `-0.4059` n `86` status `ready` deltaP `1.2429` edge `0.0062` maxDD `-0.9891`
- `risk_on_high->index_4h` score `-0.4643` n `37` status `ready` deltaP `4.8575` edge `-0.0074` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4643` n `37` status `ready` deltaP `4.8575` edge `-0.0074` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.4985` n `78` status `ready` deltaP `4.6435` edge `0.0083` maxDD `-2.9203`
- `market_context_high->metal_1h` score `-0.6391` n `86` status `ready` deltaP `-5.5598` edge `-0.0052` maxDD `-0.8404`
- `risk_on_high->metal_1h` score `-0.7494` n `37` status `ready` deltaP `-5.717` edge `0.0017` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.7494` n `37` status `ready` deltaP `-5.717` edge `0.0017` maxDD `-0.0831`
- `risk_on_high->commodity_1h` score `-0.8752` n `37` status `ready` deltaP `-3.5969` edge `-0.0217` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
