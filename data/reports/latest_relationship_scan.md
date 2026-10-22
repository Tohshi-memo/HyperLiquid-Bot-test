# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T16:22:34.605337+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6570`

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

- `risk_on_high->equity_1h` score `0.5852` n `37` status `ready` deltaP `15.8966` edge `0.0114` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.5852` n `37` status `ready` deltaP `15.8966` edge `0.0114` maxDD `-0.7219`
- `risk_on_high->commodity_24h` score `0.4982` n `37` status `ready` deltaP `15.0516` edge `0.0433` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.4982` n `37` status `ready` deltaP `15.0516` edge `0.0433` maxDD `-1.7154`
- `risk_on_high->index_1h` score `0.4686` n `37` status `ready` deltaP `12.6032` edge `0.0031` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4686` n `37` status `ready` deltaP `12.6032` edge `0.0031` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.2039` n `78` status `ready` deltaP `12.0024` edge `0.0537` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.1126` n `37` status `ready` deltaP `5.7008` edge `0.0023` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1126` n `37` status `ready` deltaP `5.7008` edge `0.0023` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.1389` n `37` status `ready` deltaP `0.6303` edge `0.0044` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1389` n `37` status `ready` deltaP `0.6303` edge `0.0044` maxDD `-0.1126`
- `market_context_high->index_1h` score `-0.3165` n `91` status `ready` deltaP `2.5942` edge `-0.0045` maxDD `-0.9361`
- `risk_on_high->index_4h` score `-0.4556` n `37` status `ready` deltaP `5.0099` edge `-0.0073` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4556` n `37` status `ready` deltaP `5.0099` edge `-0.0073` maxDD `-0.7604`
- `market_context_high->fx_1h` score `-0.4757` n `91` status `ready` deltaP `-2.1995` edge `-0.0021` maxDD `-0.5374`
- `market_context_high->commodity_1h` score `-0.55` n `91` status `ready` deltaP `-0.7468` edge `0.0012` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.6486` n `81` status `ready` deltaP `2.5068` edge `0.0033` maxDD `-2.9203`
- `risk_on_high->metal_1h` score `-0.7039` n `37` status `ready` deltaP `-5.2679` edge `0.0025` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.7039` n `37` status `ready` deltaP `-5.2679` edge `0.0025` maxDD `-0.0831`
- `market_context_high->metal_1h` score `-0.709` n `91` status `ready` deltaP `-6.248` edge `-0.0066` maxDD `-1.0782`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
