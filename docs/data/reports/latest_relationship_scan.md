# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-23T19:07:29.065844+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6402`

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

- `market_context_high->commodity_24h` score `1.295` n `87` status `ready` deltaP `18.4028` edge `0.0928` maxDD `-3.6055`
- `risk_on_high->equity_1h` score `0.659` n `37` status `ready` deltaP `15.5972` edge `0.0228` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.659` n `37` status `ready` deltaP `15.5972` edge `0.0228` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.5504` n `37` status `ready` deltaP `13.8008` edge `0.0056` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5504` n `37` status `ready` deltaP `13.8008` edge `0.0056` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.1791` n `37` status `ready` deltaP `11.1956` edge `0.0281` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1791` n `37` status `ready` deltaP `11.1956` edge `0.0281` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1647` n `37` status `ready` deltaP `6.599` edge `0.003` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1647` n `37` status `ready` deltaP `6.599` edge `0.003` maxDD `-0.0698`
- `market_context_high->fx_1h` score `-0.0887` n `87` status `ready` deltaP `3.1196` edge `0.0033` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.1246` n `87` status `ready` deltaP `6.1571` edge `0.0092` maxDD `-0.5168`
- `risk_on_high->fx_4h` score `-0.1247` n `37` status `ready` deltaP `0.7827` edge `0.0052` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1247` n `37` status `ready` deltaP `0.7827` edge `0.0052` maxDD `-0.1126`
- `risk_on_high->index_4h` score `-0.2532` n `37` status `ready` deltaP `7.2965` edge `0.0034` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.2532` n `37` status `ready` deltaP `7.2965` edge `0.0034` maxDD `-0.7604`
- `market_context_high->index_1h` score `-0.3785` n `87` status `ready` deltaP `3.7666` edge `-0.003` maxDD `-0.9588`
- `risk_on_high->metal_1h` score `-0.4343` n `37` status `ready` deltaP `-2.5733` edge `0.007` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4343` n `37` status `ready` deltaP `-2.5733` edge `0.007` maxDD `-0.0831`
- `market_context_high->commodity_1h` score `-0.4981` n `87` status `ready` deltaP `0.2805` edge `0.001` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6579` n `87` status `ready` deltaP `-5.1828` edge `-0.0038` maxDD `-1.3465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
