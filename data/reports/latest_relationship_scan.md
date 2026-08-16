# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T11:31:00.523701+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11798`

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

- `market_context_high->unknown_24h` score `198.9775` n `88` status `ready` deltaP `-21.512` edge `25.9217` maxDD `-7.8016`
- `news_risk_high->equity_24h` score `17.3045` n `30` status `ready` deltaP `32.9514` edge `1.2323` maxDD `-0.4616`
- `news_risk_high->equity_4h` score `8.3388` n `30` status `ready` deltaP `37.5` edge `0.4449` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5277` n `88` status `ready` deltaP `41.3037` edge `0.3577` maxDD `-0.1266`
- `news_risk_high->index_24h` score `4.032` n `30` status `ready` deltaP `30.5556` edge `0.1323` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.0071` n `30` status `ready` deltaP `7.6847` edge `0.1479` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.9009` n `116` status `ready` deltaP `18.4977` edge `0.0822` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.7817` n `30` status `ready` deltaP `19.6138` edge `0.0309` maxDD `-0.0546`
- `news_risk_high->fx_4h` score `0.2431` n `30` status `ready` deltaP `8.8923` edge `-0.0062` maxDD `-0.0863`
- `news_risk_high->index_1h` score `0.2131` n `30` status `ready` deltaP `3.4132` edge `0.0176` maxDD `-0.141`
- `news_risk_high->fx_1h` score `-0.0239` n `30` status `ready` deltaP `4.4212` edge `-0.0016` maxDD `-0.1414`
- `market_context_high->fx_4h` score `-0.053` n `116` status `ready` deltaP `6.8808` edge `0.0078` maxDD `-0.504`
- `market_context_high->commodity_1h` score `-0.0639` n `125` status `ready` deltaP `2.3557` edge `0.0201` maxDD `-0.624`
- `market_context_high->fx_1h` score `-0.1799` n `125` status `ready` deltaP `0.5545` edge `0.0014` maxDD `-0.2527`
- `news_risk_high->commodity_1h` score `-0.3206` n `30` status `ready` deltaP `0.489` edge `-0.015` maxDD `-0.6824`
- `market_context_high->metal_1h` score `-0.5276` n `125` status `ready` deltaP `1.5042` edge `-0.0061` maxDD `-1.7257`
- `news_risk_high->metal_1h` score `-0.7635` n `30` status `ready` deltaP `-8.7625` edge `-0.0126` maxDD `-0.8156`
- `market_context_high->index_1h` score `-0.7944` n `125` status `ready` deltaP `-6.9868` edge `-0.0031` maxDD `-0.5064`
- `market_context_high->metal_4h` score `-1.0703` n `116` status `ready` deltaP `5.3196` edge `-0.0153` maxDD `-4.5909`
- `market_context_high->index_4h` score `-1.2844` n `116` status `ready` deltaP `-11.1333` edge `-0.0092` maxDD `-0.8328`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
