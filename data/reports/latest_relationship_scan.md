# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-21T08:37:28.587506+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9062`

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

- `risk_on_high->equity_1h` score `0.6701` n `37` status `ready` deltaP `16.3457` edge `0.0193` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6701` n `37` status `ready` deltaP `16.3457` edge `0.0193` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5924` n `37` status `ready` deltaP `14.5493` edge `0.006` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5924` n `37` status `ready` deltaP `14.5493` edge `0.006` maxDD `-0.1637`
- `market_context_high->index_1h` score `0.0668` n `78` status `ready` deltaP `6.3719` edge `0.0016` maxDD `-0.5082`
- `risk_on_high->fx_1h` score `0.0152` n `37` status `ready` deltaP `4.0541` edge `0.0008` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0152` n `37` status `ready` deltaP `4.0541` edge `0.0008` maxDD `-0.0698`
- `risk_on_high->commodity_24h` score `-0.1217` n `37` status `ready` deltaP `11.8901` edge `-0.0151` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.1217` n `37` status `ready` deltaP `11.8901` edge `-0.0151` maxDD `-1.7154`
- `risk_on_high->index_4h` score `-0.1391` n `37` status `ready` deltaP `8.516` edge `0.0099` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.1391` n `37` status `ready` deltaP `8.516` edge `0.0099` maxDD `-0.7604`
- `risk_on_high->fx_4h` score `-0.2199` n `37` status `ready` deltaP `-0.1319` edge `-0.0009` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2199` n `37` status `ready` deltaP `-0.1319` edge `-0.0009` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.3185` n `78` status `ready` deltaP `2.4144` edge `0.0096` maxDD `-0.9891`
- `market_context_high->commodity_4h` score `-0.3714` n `78` status `ready` deltaP `6.4728` edge `0.0124` maxDD `-2.9203`
- `market_context_high->commodity_24h` score `-0.416` n `78` status `ready` deltaP `8.8409` edge `-0.0047` maxDD `-3.6055`
- `risk_on_high->equity_4h` score `-0.6208` n `37` status `ready` deltaP `5.0922` edge `0.0119` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.6208` n `37` status `ready` deltaP `5.0922` edge `0.0119` maxDD `-4.0351`
- `market_context_high->metal_1h` score `-0.6401` n `78` status `ready` deltaP `-6.1301` edge `-0.0037` maxDD `-0.6669`
- `risk_on_high->commodity_1h` score `-0.7483` n `37` status `ready` deltaP `-1.5011` edge `-0.0194` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
