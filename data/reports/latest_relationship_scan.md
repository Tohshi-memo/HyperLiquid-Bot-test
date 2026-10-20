# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T22:37:29.550319+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8889`

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

- `risk_on_high->equity_1h` score `0.692` n `37` status `ready` deltaP `16.3457` edge `0.0221` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.692` n `37` status `ready` deltaP `16.3457` edge `0.0221` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5527` n `37` status `ready` deltaP `13.8008` edge `0.0059` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5527` n `37` status `ready` deltaP `13.8008` edge `0.0059` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.2628` n `37` status `ready` deltaP `15.5359` edge `0.0099` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2628` n `37` status `ready` deltaP `15.5359` edge `0.0099` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.0308` n `37` status `ready` deltaP `4.3535` edge `0.0008` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0308` n `37` status `ready` deltaP `4.3535` edge `0.0008` maxDD `-0.0698`
- `market_context_high->index_1h` score `0.0271` n `78` status `ready` deltaP `5.6234` edge `0.0015` maxDD `-0.5082`
- `market_context_high->commodity_24h` score `-0.0314` n `78` status `ready` deltaP `12.4867` edge `0.0203` maxDD `-3.6055`
- `risk_on_high->index_4h` score `-0.0451` n `37` status `ready` deltaP `9.888` edge `0.0128` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.0451` n `37` status `ready` deltaP `9.888` edge `0.0128` maxDD `-0.7604`
- `risk_on_high->fx_4h` score `-0.2048` n `37` status `ready` deltaP `0.173` edge `-0.001` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2048` n `37` status `ready` deltaP `0.173` edge `-0.001` maxDD `-0.1126`
- `risk_on_high->equity_4h` score `-0.2063` n `37` status `ready` deltaP `7.3788` edge `0.0498` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.2063` n `37` status `ready` deltaP `7.3788` edge `0.0498` maxDD `-4.0351`
- `market_context_high->commodity_1h` score `-0.2298` n `78` status `ready` deltaP `4.0611` edge `0.01` maxDD `-0.9891`
- `market_context_high->commodity_4h` score `-0.2396` n `78` status `ready` deltaP `8.3021` edge `0.0171` maxDD `-2.9203`
- `risk_on_high->commodity_1h` score `-0.6596` n `37` status `ready` deltaP `0.1456` edge `-0.019` maxDD `-0.9891`
- `risk_on_and_context->commodity_1h` score `-0.6596` n `37` status `ready` deltaP `0.1456` edge `-0.019` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
