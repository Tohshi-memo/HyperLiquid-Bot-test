# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-23T01:52:32.436225+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7196`

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

- `risk_on_high->equity_1h` score `0.5213` n `37` status `ready` deltaP `15.1481` edge `0.0082` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.5213` n `37` status `ready` deltaP `15.1481` edge `0.0082` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.4701` n `37` status `ready` deltaP `12.6032` edge `0.0033` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4701` n `37` status `ready` deltaP `12.6032` edge `0.0033` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.4173` n `72` status `ready` deltaP `15.625` edge `0.0569` maxDD `-3.6055`
- `risk_on_high->commodity_24h` score `0.414` n `37` status `ready` deltaP `13.9734` edge `0.0397` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.414` n `37` status `ready` deltaP `13.9734` edge `0.0397` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1375` n `37` status `ready` deltaP `6.1499` edge `0.0025` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1375` n `37` status `ready` deltaP `6.1499` edge `0.0025` maxDD `-0.0698`
- `market_context_high->fx_1h` score `-0.116` n `87` status `ready` deltaP `2.6705` edge `0.0028` maxDD `-0.1712`
- `risk_on_high->fx_4h` score `-0.1491` n `37` status `ready` deltaP `0.4779` edge `0.0041` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1491` n `37` status `ready` deltaP `0.4779` edge `0.0041` maxDD `-0.1126`
- `market_context_high->fx_4h` score `-0.1621` n `87` status `ready` deltaP `5.8523` edge `0.0081` maxDD `-0.5168`
- `risk_on_high->index_4h` score `-0.3594` n `37` status `ready` deltaP `6.2294` edge `-0.0031` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.3594` n `37` status `ready` deltaP `6.2294` edge `-0.0031` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.3872` n `87` status `ready` deltaP `5.9591` edge `0.0138` maxDD `-2.9203`
- `market_context_high->commodity_1h` score `-0.4615` n `87` status `ready` deltaP `0.7296` edge `0.0027` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.5019` n `87` status `ready` deltaP `2.569` edge `-0.0053` maxDD `-0.9588`
- `risk_on_high->metal_1h` score `-0.505` n `37` status `ready` deltaP `-3.1721` edge `0.0051` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.505` n `37` status `ready` deltaP `-3.1721` edge `0.0051` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
