# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-23T04:52:29.020135+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7268`

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

- `risk_on_high->index_1h` score `0.4546` n `37` status `ready` deltaP `12.3038` edge `0.0033` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4546` n `37` status `ready` deltaP `12.3038` edge `0.0033` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.4496` n `37` status `ready` deltaP `14.3996` edge `0.004` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.4496` n `37` status `ready` deltaP `14.3996` edge `0.004` maxDD `-0.7219`
- `market_context_high->commodity_24h` score `0.2882` n `72` status `ready` deltaP `14.5833` edge `0.0473` maxDD `-3.6055`
- `risk_on_high->commodity_24h` score `0.285` n `37` status `ready` deltaP `12.9317` edge `0.0301` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.285` n `37` status `ready` deltaP `12.9317` edge `0.0301` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1359` n `37` status `ready` deltaP `6.1499` edge `0.0023` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1359` n `37` status `ready` deltaP `6.1499` edge `0.0023` maxDD `-0.0698`
- `market_context_high->fx_1h` score `-0.1175` n `87` status `ready` deltaP `2.6705` edge `0.0026` maxDD `-0.1712`
- `risk_on_high->fx_4h` score `-0.1412` n `37` status `ready` deltaP `0.6303` edge `0.0041` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1412` n `37` status `ready` deltaP `0.6303` edge `0.0041` maxDD `-0.1126`
- `market_context_high->fx_4h` score `-0.1499` n `87` status `ready` deltaP `6.0047` edge `0.0081` maxDD `-0.5168`
- `risk_on_high->index_4h` score `-0.3075` n `37` status `ready` deltaP `6.6868` edge `0.0005` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.3075` n `37` status `ready` deltaP `6.6868` edge `0.0005` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.374` n `87` status `ready` deltaP `5.9591` edge `0.0155` maxDD `-2.9203`
- `market_context_high->commodity_1h` score `-0.428` n `87` status `ready` deltaP `1.3284` edge `0.003` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.5259` n `87` status `ready` deltaP `2.2696` edge `-0.0053` maxDD `-0.9588`
- `risk_on_high->metal_1h` score `-0.5434` n `37` status `ready` deltaP `-3.6212` edge `0.0049` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.5434` n `37` status `ready` deltaP `-3.6212` edge `0.0049` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
