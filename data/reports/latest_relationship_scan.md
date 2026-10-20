# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T20:07:37.518180+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8719`

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

- `risk_on_high->equity_1h` score `0.7731` n `37` status `ready` deltaP `16.6451` edge `0.0305` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.7731` n `37` status `ready` deltaP `16.6451` edge `0.0305` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.608` n `37` status `ready` deltaP `14.699` edge `0.007` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.608` n `37` status `ready` deltaP `14.699` edge `0.007` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.2828` n `37` status `ready` deltaP `15.7095` edge `0.0113` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2828` n `37` status `ready` deltaP `15.7095` edge `0.0113` maxDD `-1.7154`
- `market_context_high->index_1h` score `0.0824` n `78` status `ready` deltaP `6.5216` edge `0.0026` maxDD `-0.5082`
- `risk_on_high->fx_1h` score `0.0152` n `37` status `ready` deltaP `4.0541` edge `0.0008` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0152` n `37` status `ready` deltaP `4.0541` edge `0.0008` maxDD `-0.0698`
- `risk_on_high->index_4h` score `-0.0096` n `37` status `ready` deltaP `10.3453` edge `0.0143` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.0096` n `37` status `ready` deltaP `10.3453` edge `0.0143` maxDD `-0.7604`
- `market_context_high->commodity_24h` score `-0.0114` n `78` status `ready` deltaP `12.6603` edge `0.0217` maxDD `-3.6055`
- `risk_on_high->equity_4h` score `-0.1048` n `37` status `ready` deltaP `7.5313` edge `0.0618` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.1048` n `37` status `ready` deltaP `7.5313` edge `0.0618` maxDD `-4.0351`
- `risk_on_high->fx_4h` score `-0.2135` n `37` status `ready` deltaP `0.0206` edge `-0.0011` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2135` n `37` status `ready` deltaP `0.0206` edge `-0.0011` maxDD `-0.1126`
- `market_context_high->commodity_4h` score `-0.2176` n `78` status `ready` deltaP `8.6069` edge `0.0179` maxDD `-2.9203`
- `market_context_high->commodity_1h` score `-0.2204` n `78` status `ready` deltaP `4.2108` edge `0.0102` maxDD `-0.9891`
- `market_context_high->metal_1h` score `-0.6293` n `78` status `ready` deltaP `-5.8307` edge `-0.0043` maxDD `-0.6669`
- `risk_on_high->commodity_1h` score `-0.6502` n `37` status `ready` deltaP `0.2953` edge `-0.0188` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
