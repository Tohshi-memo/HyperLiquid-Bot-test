# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-23T14:22:39.085727+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6668`

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

- `market_context_high->commodity_24h` score `0.7003` n `81` status `ready` deltaP `15.9336` edge `0.0597` maxDD `-3.6055`
- `risk_on_high->equity_1h` score `0.5865` n `37` status `ready` deltaP `14.699` edge `0.0195` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.5865` n `37` status `ready` deltaP `14.699` edge `0.0195` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.5005` n `37` status `ready` deltaP `12.9026` edge `0.0052` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5005` n `37` status `ready` deltaP `12.9026` edge `0.0052` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.1268` n `37` status `ready` deltaP `11.1956` edge `0.0214` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1268` n `37` status `ready` deltaP `11.1956` edge `0.0214` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1141` n `37` status `ready` deltaP `5.7008` edge `0.0025` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1141` n `37` status `ready` deltaP `5.7008` edge `0.0025` maxDD `-0.0698`
- `market_context_high->fx_4h` score `-0.0284` n `87` status `ready` deltaP `7.2242` edge `0.0101` maxDD `-0.5168`
- `risk_on_high->fx_4h` score `-0.0622` n `37` status `ready` deltaP `1.8498` edge `0.0061` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0622` n `37` status `ready` deltaP `1.8498` edge `0.0061` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.1393` n `87` status `ready` deltaP `2.2214` edge `0.0028` maxDD `-0.1712`
- `risk_on_high->index_4h` score `-0.2263` n `37` status `ready` deltaP `7.7538` edge `0.0038` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.2263` n `37` status `ready` deltaP `7.7538` edge `0.0038` maxDD `-0.7604`
- `market_context_high->index_1h` score `-0.4551` n `87` status `ready` deltaP `2.8684` edge `-0.0034` maxDD `-0.9588`
- `market_context_high->commodity_1h` score `-0.4763` n `87` status `ready` deltaP `0.5799` edge `0.0018` maxDD `-1.0053`
- `risk_on_high->metal_1h` score `-0.5134` n `37` status `ready` deltaP `-3.3218` edge `0.0054` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.5134` n `37` status `ready` deltaP `-3.3218` edge `0.0054` maxDD `-0.0831`
- `market_context_high->commodity_4h` score `-0.6205` n `87` status `ready` deltaP `2.1481` edge `0.0093` maxDD `-2.9203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
