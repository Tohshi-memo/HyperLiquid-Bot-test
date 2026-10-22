# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T14:07:29.627091+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7664`

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

- `risk_on_high->commodity_24h` score `0.5577` n `37` status `ready` deltaP `15.7907` edge `0.046` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.5577` n `37` status `ready` deltaP `15.7907` edge `0.046` maxDD `-1.7154`
- `risk_on_high->index_1h` score `0.4951` n `37` status `ready` deltaP `13.0523` edge `0.0035` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4951` n `37` status `ready` deltaP `13.0523` edge `0.0035` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.4815` n `37` status `ready` deltaP `15.2978` edge `0.0021` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.4815` n `37` status `ready` deltaP `15.2978` edge `0.0021` maxDD `-0.7219`
- `market_context_high->commodity_24h` score `0.2634` n `78` status `ready` deltaP `12.7415` edge `0.0564` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.0814` n `37` status `ready` deltaP `5.2517` edge `0.0013` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0814` n `37` status `ready` deltaP `5.2517` edge `0.0013` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.1467` n `37` status `ready` deltaP `0.6303` edge `0.0034` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1467` n `37` status `ready` deltaP `0.6303` edge `0.0034` maxDD `-0.1126`
- `market_context_high->index_1h` score `-0.1612` n `83` status `ready` deltaP `4.1952` edge `-0.0001` maxDD `-0.5491`
- `market_context_high->commodity_1h` score `-0.333` n `83` status `ready` deltaP `1.9714` edge `0.0107` maxDD `-0.9891`
- `risk_on_high->index_4h` score `-0.4549` n `37` status `ready` deltaP `4.8575` edge `-0.0062` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4549` n `37` status `ready` deltaP `4.8575` edge `-0.0062` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.4797` n `78` status `ready` deltaP `4.796` edge `0.0097` maxDD `-2.9203`
- `market_context_high->metal_1h` score `-0.5605` n `83` status `ready` deltaP `-4.5379` edge `-0.0041` maxDD `-0.6669`
- `market_context_high->fx_1h` score `-0.66` n `83` status `ready` deltaP `-5.4289` edge `-0.0042` maxDD `-0.5374`
- `risk_on_high->metal_1h` score `-0.7998` n `37` status `ready` deltaP `-6.1661` edge `0.0005` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.7998` n `37` status `ready` deltaP `-6.1661` edge `0.0005` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
