# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T05:22:29.968076+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8369`

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

- `risk_on_high->equity_1h` score `0.798` n `37` status `ready` deltaP `16.6451` edge `0.0337` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.798` n `37` status `ready` deltaP `16.6451` edge `0.0337` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5512` n `37` status `ready` deltaP `13.5014` edge `0.0077` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5512` n `37` status `ready` deltaP `13.5014` edge `0.0077` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.2524` n `60` status `ready` deltaP `15.3125` edge `0.0041` maxDD `-1.8119`
- `market_context_high->index_1h` score `0.0255` n `78` status `ready` deltaP `5.324` edge `0.0033` maxDD `-0.5082`
- `risk_on_high->fx_1h` score `-0.0151` n `37` status `ready` deltaP `3.4553` edge `0.0009` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `-0.0151` n `37` status `ready` deltaP `3.4553` edge `0.0009` maxDD `-0.0698`
- `risk_on_high->index_4h` score `-0.1042` n `37` status `ready` deltaP `8.2112` edge `0.0164` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.1042` n `37` status `ready` deltaP `8.2112` edge `0.0164` maxDD `-0.7604`
- `risk_on_high->equity_4h` score `-0.1663` n `37` status `ready` deltaP `4.7874` edge `0.0722` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.1663` n `37` status `ready` deltaP `4.7874` edge `0.0722` maxDD `-4.0351`
- `risk_on_high->fx_4h` score `-0.2214` n `37` status `ready` deltaP `-0.1319` edge `-0.0011` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2214` n `37` status `ready` deltaP `-0.1319` edge `-0.0011` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.289` n `78` status `ready` deltaP `3.9114` edge `0.0034` maxDD `-0.9891`
- `risk_on_high->commodity_24h` score `-0.2949` n `37` status `ready` deltaP `13.1053` edge `-0.0454` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.2949` n `37` status `ready` deltaP `13.1053` edge `-0.0454` maxDD `-1.7154`
- `market_context_high->metal_1h` score `-0.549` n `78` status `ready` deltaP `-4.6331` edge `-0.002` maxDD `-0.6669`
- `market_context_high->commodity_4h` score `-0.5703` n `78` status `ready` deltaP `6.4728` edge `-0.0131` maxDD `-2.9203`
- `risk_on_high->metal_1h` score `-0.6835` n `37` status `ready` deltaP `-5.1182` edge `0.0032` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
