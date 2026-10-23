# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-23T21:37:28.464528+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6270`

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

- `market_context_high->commodity_24h` score `0.9994` n `84` status `ready` deltaP `17.2123` edge `0.0761` maxDD `-3.6055`
- `risk_on_high->equity_1h` score `0.6387` n `37` status `ready` deltaP `15.4475` edge `0.0212` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.6387` n `37` status `ready` deltaP `15.4475` edge `0.0212` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.5145` n `37` status `ready` deltaP `13.202` edge `0.005` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5145` n `37` status `ready` deltaP `13.202` edge `0.005` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.2056` n `37` status `ready` deltaP `11.1956` edge `0.0315` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2056` n `37` status `ready` deltaP `11.1956` edge `0.0315` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1134` n `37` status `ready` deltaP `5.7008` edge `0.0024` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1134` n `37` status `ready` deltaP `5.7008` edge `0.0024` maxDD `-0.0698`
- `market_context_high->fx_1h` score `-0.0603` n `84` status `ready` deltaP `4.0277` edge `0.0036` maxDD `-0.1712`
- `risk_on_high->fx_4h` score `-0.1199` n `37` status `ready` deltaP `0.9352` edge `0.0048` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1199` n `37` status `ready` deltaP `0.9352` edge `0.0048` maxDD `-0.1126`
- `market_context_high->fx_4h` score `-0.1485` n `84` status `ready` deltaP `5.858` edge `0.0092` maxDD `-0.5168`
- `market_context_high->index_1h` score `-0.2473` n `84` status `ready` deltaP `3.7425` edge `-0.003` maxDD `-0.9588`
- `risk_on_high->index_4h` score `-0.265` n `37` status `ready` deltaP `7.1441` edge `0.0029` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.265` n `37` status `ready` deltaP `7.1441` edge `0.0029` maxDD `-0.7604`
- `risk_on_high->metal_1h` score `-0.4475` n `37` status `ready` deltaP `-2.723` edge `0.0069` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4475` n `37` status `ready` deltaP `-2.723` edge `0.0069` maxDD `-0.0831`
- `market_context_high->commodity_1h` score `-0.5551` n `84` status `ready` deltaP `-0.4705` edge `-0.0013` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.7323` n `84` status `ready` deltaP `-6.3587` edge `-0.0055` maxDD `-1.3465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
