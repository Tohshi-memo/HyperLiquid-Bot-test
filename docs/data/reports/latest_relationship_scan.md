# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-21T04:07:26.401080+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8808`

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

- `risk_on_high->equity_1h` score `0.7075` n `37` status `ready` deltaP `16.6451` edge `0.0221` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.7075` n `37` status `ready` deltaP `16.6451` edge `0.0221` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.6025` n `37` status `ready` deltaP `14.699` edge `0.0063` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.6025` n `37` status `ready` deltaP `14.699` edge `0.0063` maxDD `-0.1637`
- `market_context_high->index_1h` score `0.0769` n `78` status `ready` deltaP `6.5216` edge `0.0019` maxDD `-0.5082`
- `risk_on_high->fx_1h` score `0.0238` n `37` status `ready` deltaP `4.2038` edge `0.0009` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0238` n `37` status `ready` deltaP `4.2038` edge `0.0009` maxDD `-0.0698`
- `risk_on_high->commodity_24h` score `0.0202` n `37` status `ready` deltaP `13.1053` edge `-0.005` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.0202` n `37` status `ready` deltaP `13.1053` edge `-0.005` maxDD `-1.7154`
- `risk_on_high->index_4h` score `-0.1438` n `37` status `ready` deltaP `8.516` edge `0.0093` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.1438` n `37` status `ready` deltaP `8.516` edge `0.0093` maxDD `-0.7604`
- `risk_on_high->fx_4h` score `-0.2468` n `37` status `ready` deltaP `-0.5892` edge `-0.0013` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2468` n `37` status `ready` deltaP `-0.5892` edge `-0.0013` maxDD `-0.1126`
- `market_context_high->commodity_24h` score `-0.274` n `78` status `ready` deltaP `10.0561` edge `0.0054` maxDD `-3.6055`
- `market_context_high->commodity_1h` score `-0.3232` n `78` status `ready` deltaP `2.4144` edge `0.009` maxDD `-0.9891`
- `market_context_high->commodity_4h` score `-0.422` n `78` status `ready` deltaP `5.7106` edge `0.011` maxDD `-2.9203`
- `risk_on_high->equity_4h` score `-0.5871` n `37` status `ready` deltaP `5.2447` edge `0.0152` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.5871` n `37` status `ready` deltaP `5.2447` edge `0.0152` maxDD `-4.0351`
- `market_context_high->metal_1h` score `-0.5958` n `78` status `ready` deltaP `-5.3816` edge `-0.003` maxDD `-0.6669`
- `risk_on_high->commodity_1h` score `-0.753` n `37` status `ready` deltaP `-1.5011` edge `-0.02` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
