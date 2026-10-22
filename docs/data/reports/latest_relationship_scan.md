# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T16:06:21.593578+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6560`

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

- `risk_on_high->equity_1h` score `0.5711` n `37` status `ready` deltaP `15.7469` edge `0.0106` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.5711` n `37` status `ready` deltaP `15.7469` edge `0.0106` maxDD `-0.7219`
- `risk_on_high->commodity_24h` score `0.502` n `37` status `ready` deltaP `15.1245` edge `0.0433` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.502` n `37` status `ready` deltaP `15.1245` edge `0.0433` maxDD `-1.7154`
- `risk_on_high->index_1h` score `0.4772` n `37` status `ready` deltaP `12.7529` edge `0.0032` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4772` n `37` status `ready` deltaP `12.7529` edge `0.0032` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.2077` n `78` status `ready` deltaP `12.0753` edge `0.0537` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.1126` n `37` status `ready` deltaP `5.7008` edge `0.0023` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1126` n `37` status `ready` deltaP `5.7008` edge `0.0023` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.1389` n `37` status `ready` deltaP `0.6303` edge `0.0044` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1389` n `37` status `ready` deltaP `0.6303` edge `0.0044` maxDD `-0.1126`
- `market_context_high->index_1h` score `-0.3402` n `90` status `ready` deltaP `2.1823` edge `-0.0048` maxDD `-0.9361`
- `risk_on_high->index_4h` score `-0.465` n `37` status `ready` deltaP `4.8575` edge `-0.0075` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.465` n `37` status `ready` deltaP `4.8575` edge `-0.0075` maxDD `-0.7604`
- `market_context_high->fx_1h` score `-0.5091` n `90` status `ready` deltaP `-2.7977` edge `-0.0024` maxDD `-0.5374`
- `market_context_high->commodity_1h` score `-0.5787` n `90` status `ready` deltaP `-1.1344` edge `0.0001` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.6047` n `80` status `ready` deltaP `3.2012` edge `0.0043` maxDD `-2.9203`
- `market_context_high->metal_1h` score `-0.6735` n `90` status `ready` deltaP `-5.8084` edge `-0.0059` maxDD `-1.0042`
- `risk_on_high->metal_1h` score `-0.7039` n `37` status `ready` deltaP `-5.2679` edge `0.0025` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.7039` n `37` status `ready` deltaP `-5.2679` edge `0.0025` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
