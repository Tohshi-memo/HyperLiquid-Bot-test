# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T12:22:29.108588+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8748`

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

- `market_context_high->commodity_24h` score `0.8745` n `62` status `ready` deltaP `16.549` edge `0.0477` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.8027` n `37` status `ready` deltaP `16.3457` edge `0.0363` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.8027` n `37` status `ready` deltaP `16.3457` edge `0.0363` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.594` n `37` status `ready` deltaP `14.2499` edge `0.0082` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.594` n `37` status `ready` deltaP `14.2499` edge `0.0082` maxDD `-0.1637`
- `market_context_high->index_1h` score `0.0684` n `78` status `ready` deltaP `6.0725` edge `0.0038` maxDD `-0.5082`
- `risk_on_high->fx_1h` score `0.0402` n `37` status `ready` deltaP `4.5032` edge `0.001` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0402` n `37` status `ready` deltaP `4.5032` edge `0.001` maxDD `-0.0698`
- `risk_on_high->equity_4h` score `-0.0046` n `37` status `ready` deltaP `6.0069` edge `0.0848` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.0046` n `37` status `ready` deltaP `6.0069` edge `0.0848` maxDD `-4.0351`
- `risk_on_high->index_4h` score `-0.0118` n `37` status `ready` deltaP `9.5831` edge `0.0191` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.0118` n `37` status `ready` deltaP `9.5831` edge `0.0191` maxDD `-0.7604`
- `risk_on_high->commodity_24h` score `-0.0141` n `37` status `ready` deltaP `13.1053` edge `-0.0094` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.0141` n `37` status `ready` deltaP `13.1053` edge `-0.0094` maxDD `-1.7154`
- `risk_on_high->fx_4h` score `-0.1407` n `37` status `ready` deltaP `1.2401` edge `0.0001` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1407` n `37` status `ready` deltaP `1.2401` edge `0.0001` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.3778` n `78` status `ready` deltaP `2.4144` edge `0.002` maxDD `-0.9891`
- `market_context_high->metal_1h` score `-0.5553` n `78` status `ready` deltaP `-4.7828` edge `-0.0018` maxDD `-0.6669`
- `market_context_high->commodity_4h` score `-0.5885` n `78` status `ready` deltaP `5.2533` edge `-0.0073` maxDD `-2.9203`
- `risk_on_high->metal_1h` score `-0.6931` n `37` status `ready` deltaP `-5.2679` edge `0.0034` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
