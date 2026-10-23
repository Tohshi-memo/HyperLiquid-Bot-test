# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-23T17:06:14.936920+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6426`

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

- `market_context_high->commodity_24h` score `1.2362` n `87` status `ready` deltaP `18.4028` edge `0.0879` maxDD `-3.6055`
- `risk_on_high->equity_1h` score `0.5764` n `37` status `ready` deltaP `14.699` edge `0.0182` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.5764` n `37` status `ready` deltaP `14.699` edge `0.0182` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.506` n `37` status `ready` deltaP `13.0523` edge `0.0049` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.506` n `37` status `ready` deltaP `13.0523` edge `0.0049` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.1409` n `37` status `ready` deltaP `11.1956` edge `0.0232` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1409` n `37` status `ready` deltaP `11.1956` edge `0.0232` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1313` n `37` status `ready` deltaP `6.0002` edge `0.0027` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1313` n `37` status `ready` deltaP `6.0002` edge `0.0027` maxDD `-0.0698`
- `market_context_high->fx_4h` score `-0.0784` n `87` status `ready` deltaP `6.6145` edge `0.01` maxDD `-0.5168`
- `risk_on_high->fx_4h` score `-0.0947` n `37` status `ready` deltaP `1.2401` edge `0.006` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0947` n `37` status `ready` deltaP `1.2401` edge `0.006` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.1222` n `87` status `ready` deltaP `2.5208` edge `0.003` maxDD `-0.1712`
- `risk_on_high->index_4h` score `-0.2168` n `37` status `ready` deltaP `7.9063` edge `0.004` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.2168` n `37` status `ready` deltaP `7.9063` edge `0.004` maxDD `-0.7604`
- `market_context_high->index_1h` score `-0.4468` n `87` status `ready` deltaP `3.0181` edge `-0.0037` maxDD `-0.9588`
- `risk_on_high->metal_1h` score `-0.4978` n `37` status `ready` deltaP `-3.1721` edge `0.0057` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4978` n `37` status `ready` deltaP `-3.1721` edge `0.0057` maxDD `-0.0831`
- `market_context_high->commodity_1h` score `-0.5005` n `87` status `ready` deltaP `0.2805` edge `0.0007` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6992` n `87` status `ready` deltaP `-5.7816` edge `-0.0051` maxDD `-1.3465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
