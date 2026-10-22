# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T11:52:30.241177+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7500`

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

- `risk_on_high->commodity_24h` score `0.6122` n `37` status `ready` deltaP `16.4195` edge `0.0488` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.6122` n `37` status `ready` deltaP `16.4195` edge `0.0488` maxDD `-1.7154`
- `risk_on_high->equity_1h` score `0.5571` n `37` status `ready` deltaP `15.8966` edge `0.0078` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.5571` n `37` status `ready` deltaP `15.8966` edge `0.0078` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5433` n `37` status `ready` deltaP `13.8008` edge `0.0047` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5433` n `37` status `ready` deltaP `13.8008` edge `0.0047` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.318` n `78` status `ready` deltaP `13.3703` edge `0.0592` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.1056` n `37` status `ready` deltaP `5.7008` edge `0.0014` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1056` n `37` status `ready` deltaP `5.7008` edge `0.0014` maxDD `-0.0698`
- `market_context_high->index_1h` score `0.0177` n `78` status `ready` deltaP `5.6234` edge `0.0003` maxDD `-0.5082`
- `risk_on_high->fx_4h` score `-0.2121` n `37` status `ready` deltaP `-0.1319` edge `0.0001` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2121` n `37` status `ready` deltaP `-0.1319` edge `0.0001` maxDD `-0.1126`
- `risk_on_high->index_4h` score `-0.3399` n `37` status `ready` deltaP `6.2294` edge `-0.0006` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.3399` n `37` status `ready` deltaP `6.2294` edge `-0.0006` maxDD `-0.7604`
- `market_context_high->commodity_1h` score `-0.4088` n `78` status `ready` deltaP `0.9174` edge `0.008` maxDD `-0.9891`
- `market_context_high->commodity_4h` score `-0.4183` n `78` status `ready` deltaP `5.4057` edge `0.0135` maxDD `-2.9203`
- `market_context_high->metal_1h` score `-0.609` n `78` status `ready` deltaP `-5.3816` edge `-0.0047` maxDD `-0.6669`
- `risk_on_high->metal_1h` score `-0.7758` n `37` status `ready` deltaP `-5.8667` edge `0.0005` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.7758` n `37` status `ready` deltaP `-5.8667` edge `0.0005` maxDD `-0.0831`
- `risk_on_high->commodity_1h` score `-0.8386` n `37` status `ready` deltaP `-2.9981` edge `-0.021` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
