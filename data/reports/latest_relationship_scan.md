# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-21T02:22:28.628265+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8806`

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

- `risk_on_high->equity_1h` score `0.6974` n `37` status `ready` deltaP `16.4954` edge `0.0218` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6974` n `37` status `ready` deltaP `16.4954` edge `0.0218` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5768` n `37` status `ready` deltaP `14.2499` edge `0.006` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5768` n `37` status `ready` deltaP `14.2499` edge `0.006` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.1318` n `37` status `ready` deltaP `14.3206` edge `0.0012` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1318` n `37` status `ready` deltaP `14.3206` edge `0.0012` maxDD `-1.7154`
- `market_context_high->index_1h` score `0.0512` n `78` status `ready` deltaP `6.0725` edge `0.0016` maxDD `-0.5082`
- `risk_on_high->fx_1h` score `0.0223` n `37` status `ready` deltaP `4.2038` edge `0.0007` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0223` n `37` status `ready` deltaP `4.2038` edge `0.0007` maxDD `-0.0698`
- `risk_on_high->index_4h` score `-0.0861` n `37` status `ready` deltaP `9.4307` edge `0.0106` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.0861` n `37` status `ready` deltaP `9.4307` edge `0.0106` maxDD `-0.7604`
- `market_context_high->commodity_24h` score `-0.1624` n `78` status `ready` deltaP `11.2714` edge `0.0116` maxDD `-3.6055`
- `risk_on_high->fx_4h` score `-0.204` n `37` status `ready` deltaP `0.173` edge `-0.0009` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.204` n `37` status `ready` deltaP `0.173` edge `-0.0009` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.2874` n `78` status `ready` deltaP `3.0132` edge `0.0096` maxDD `-0.9891`
- `market_context_high->commodity_4h` score `-0.3462` n `78` status `ready` deltaP `6.7777` edge `0.0136` maxDD `-2.9203`
- `risk_on_high->equity_4h` score `-0.4678` n `37` status `ready` deltaP `6.1593` edge `0.0244` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.4678` n `37` status `ready` deltaP `6.1593` edge `0.0244` maxDD `-4.0351`
- `market_context_high->metal_1h` score `-0.6222` n `78` status `ready` deltaP `-5.8307` edge `-0.0034` maxDD `-0.6669`
- `risk_on_high->commodity_1h` score `-0.7172` n `37` status `ready` deltaP `-0.9023` edge `-0.0194` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
