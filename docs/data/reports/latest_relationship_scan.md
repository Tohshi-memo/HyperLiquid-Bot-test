# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T15:22:36.535198+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6396`

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

- `risk_on_high->equity_1h` score `0.5555` n `37` status `ready` deltaP `15.7469` edge `0.0086` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.5555` n `37` status `ready` deltaP `15.7469` edge `0.0086` maxDD `-0.7219`
- `risk_on_high->commodity_24h` score `0.5172` n `37` status `ready` deltaP `15.3419` edge `0.0438` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.5172` n `37` status `ready` deltaP `15.3419` edge `0.0438` maxDD `-1.7154`
- `risk_on_high->index_1h` score `0.4958` n `37` status `ready` deltaP `13.0523` edge `0.0036` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4958` n `37` status `ready` deltaP `13.0523` edge `0.0036` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.2229` n `78` status `ready` deltaP `12.2927` edge `0.0542` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.111` n `37` status `ready` deltaP `5.7008` edge `0.0021` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.111` n `37` status `ready` deltaP `5.7008` edge `0.0021` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.1389` n `37` status `ready` deltaP `0.6303` edge `0.0044` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1389` n `37` status `ready` deltaP `0.6303` edge `0.0044` maxDD `-0.1126`
- `market_context_high->index_1h` score `-0.3611` n `87` status `ready` deltaP `1.8687` edge `-0.0054` maxDD `-0.935`
- `market_context_high->commodity_1h` score `-0.4551` n `87` status `ready` deltaP `0.6281` edge `0.004` maxDD `-0.9891`
- `risk_on_high->index_4h` score `-0.4666` n `37` status `ready` deltaP `4.8575` edge `-0.0077` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4666` n `37` status `ready` deltaP `4.8575` edge `-0.0077` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.5009` n `78` status `ready` deltaP `4.6435` edge `0.008` maxDD `-2.9203`
- `market_context_high->metal_1h` score `-0.6005` n `87` status `ready` deltaP `-4.8782` edge `-0.0048` maxDD `-0.8404`
- `risk_on_high->metal_1h` score `-0.747` n `37` status `ready` deltaP `-5.717` edge `0.0019` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.747` n `37` status `ready` deltaP `-5.717` edge `0.0019` maxDD `-0.0831`
- `risk_on_high->commodity_1h` score `-0.8745` n `37` status `ready` deltaP `-3.5969` edge `-0.0216` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
