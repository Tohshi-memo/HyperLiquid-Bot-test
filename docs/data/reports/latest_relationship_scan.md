# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T01:22:27.458398+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8382`

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

- `risk_on_high->equity_1h` score `0.6862` n `37` status `ready` deltaP `16.3252` edge `0.0215` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6862` n `37` status `ready` deltaP `16.3252` edge `0.0215` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.594` n `37` status `ready` deltaP `14.5341` edge `0.0063` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.594` n `37` status `ready` deltaP `14.5341` edge `0.0063` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.5433` n `37` status `ready` deltaP `16.4454` edge `0.0398` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.5433` n `37` status `ready` deltaP `16.4454` edge `0.0398` maxDD `-1.7154`
- `market_context_high->commodity_24h` score `0.2491` n `78` status `ready` deltaP `13.3962` edge `0.0502` maxDD `-3.6055`
- `market_context_high->index_1h` score `0.0683` n `78` status `ready` deltaP `6.3567` edge `0.0019` maxDD `-0.5082`
- `risk_on_high->fx_1h` score `0.0145` n `37` status `ready` deltaP `4.0541` edge `0.0007` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0145` n `37` status `ready` deltaP `4.0541` edge `0.0007` maxDD `-0.0698`
- `risk_on_high->index_4h` score `-0.2008` n `37` status `ready` deltaP `7.7042` edge `0.0074` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.2008` n `37` status `ready` deltaP `7.7042` edge `0.0074` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.3132` n `78` status `ready` deltaP `6.2723` edge `0.0212` maxDD `-2.9203`
- `market_context_high->commodity_1h` score `-0.3208` n `78` status `ready` deltaP `2.2656` edge `0.0103` maxDD `-0.9891`
- `risk_on_high->fx_4h` score `-0.3222` n `37` status `ready` deltaP `-1.8746` edge `-0.0024` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.3222` n `37` status `ready` deltaP `-1.8746` edge `-0.0024` maxDD `-0.1126`
- `market_context_high->metal_1h` score `-0.6041` n `78` status `ready` deltaP `-5.5416` edge `-0.003` maxDD `-0.6669`
- `risk_on_high->equity_4h` score `-0.719` n `37` status `ready` deltaP `4.8398` edge `0.001` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.719` n `37` status `ready` deltaP `4.8398` edge `0.001` maxDD `-4.0351`
- `risk_on_high->commodity_1h` score `-0.7506` n `37` status `ready` deltaP `-1.6499` edge `-0.0187` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
