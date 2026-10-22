# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T18:22:33.082027+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6680`

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

- `risk_on_high->equity_1h` score `0.6054` n `37` status `ready` deltaP `15.8966` edge `0.014` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6054` n `37` status `ready` deltaP `15.8966` edge `0.014` maxDD `-0.7219`
- `risk_on_high->commodity_24h` score `0.4753` n `37` status `ready` deltaP `14.6262` edge `0.0432` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.4753` n `37` status `ready` deltaP `14.6262` edge `0.0432` maxDD `-1.7154`
- `risk_on_high->index_1h` score `0.4678` n `37` status `ready` deltaP `12.6032` edge `0.003` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4678` n `37` status `ready` deltaP `12.6032` edge `0.003` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.3272` n `75` status `ready` deltaP `13.8334` edge `0.0573` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.0877` n `37` status `ready` deltaP `5.2517` edge `0.0021` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0877` n `37` status `ready` deltaP `5.2517` edge `0.0021` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.2037` n `37` status `ready` deltaP `-0.4368` edge `0.0032` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2037` n `37` status `ready` deltaP `-0.4368` edge `0.0032` maxDD `-0.1126`
- `market_context_high->index_1h` score `-0.294` n `90` status `ready` deltaP `3.1437` edge `-0.005` maxDD `-0.9588`
- `market_context_high->fx_1h` score `-0.3019` n `90` status `ready` deltaP `0.0865` edge `-0.0006` maxDD `-0.4278`
- `risk_on_high->index_4h` score `-0.4313` n `37` status `ready` deltaP `5.1624` edge `-0.0052` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4313` n `37` status `ready` deltaP `5.1624` edge `-0.0052` maxDD `-0.7604`
- `market_context_high->fx_4h` score `-0.456` n `84` status `ready` deltaP `-0.2759` edge `0.004` maxDD `-0.5168`
- `market_context_high->commodity_1h` score `-0.4997` n `90` status `ready` deltaP `0.0399` edge `0.0024` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.6602` n `84` status `ready` deltaP `2.5987` edge `0.0012` maxDD `-2.9203`
- `risk_on_high->metal_1h` score `-0.6907` n `37` status `ready` deltaP `-5.1182` edge `0.0026` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.6907` n `37` status `ready` deltaP `-5.1182` edge `0.0026` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
