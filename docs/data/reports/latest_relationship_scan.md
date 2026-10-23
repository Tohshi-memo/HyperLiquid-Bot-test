# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-23T20:26:23.599560+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6342`

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

- `market_context_high->commodity_24h` score `1.3166` n `87` status `ready` deltaP `18.4028` edge `0.0946` maxDD `-3.6055`
- `risk_on_high->equity_1h` score `0.6808` n `37` status `ready` deltaP `15.8966` edge `0.0236` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.6808` n `37` status `ready` deltaP `15.8966` edge `0.0236` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.5496` n `37` status `ready` deltaP `13.8008` edge `0.0055` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5496` n `37` status `ready` deltaP `13.8008` edge `0.0055` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.1931` n `37` status `ready` deltaP `11.1956` edge `0.0299` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1931` n `37` status `ready` deltaP `11.1956` edge `0.0299` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1383` n `37` status `ready` deltaP `6.1499` edge `0.0026` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1383` n `37` status `ready` deltaP `6.1499` edge `0.0026` maxDD `-0.0698`
- `market_context_high->fx_1h` score `-0.1152` n `87` status `ready` deltaP `2.6705` edge `0.0029` maxDD `-0.1712`
- `risk_on_high->fx_4h` score `-0.1286` n `37` status `ready` deltaP `0.7827` edge `0.0047` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1286` n `37` status `ready` deltaP `0.7827` edge `0.0047` maxDD `-0.1126`
- `market_context_high->fx_4h` score `-0.1306` n `87` status `ready` deltaP `6.1571` edge `0.0087` maxDD `-0.5168`
- `risk_on_high->index_4h` score `-0.254` n `37` status `ready` deltaP `7.2965` edge `0.0033` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.254` n `37` status `ready` deltaP `7.2965` edge `0.0033` maxDD `-0.7604`
- `market_context_high->index_1h` score `-0.3797` n `87` status `ready` deltaP `3.7666` edge `-0.0031` maxDD `-0.9588`
- `risk_on_high->metal_1h` score `-0.4367` n `37` status `ready` deltaP `-2.5733` edge `0.0068` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4367` n `37` status `ready` deltaP `-2.5733` edge `0.0068` maxDD `-0.0831`
- `market_context_high->commodity_1h` score `-0.5277` n `87` status `ready` deltaP `-0.1686` edge `0.0002` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6595` n `87` status `ready` deltaP `-5.1828` edge `-0.004` maxDD `-1.3465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
