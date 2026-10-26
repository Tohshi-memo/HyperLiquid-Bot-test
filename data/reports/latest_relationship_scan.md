# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T07:37:27.464384+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9112`

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

- `market_context_high->unknown_4h` score `18.9744` n `123` status `ready` deltaP `-3.0996` edge `1.6354` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.6068` n `113` status `ready` deltaP `28.4445` edge `0.1552` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.1824` n `113` status `ready` deltaP `22.3974` edge `0.0313` maxDD `-1.2451`
- `market_context_high->fx_4h` score `0.0778` n `123` status `ready` deltaP `8.6891` edge `0.0084` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0192` n `133` status `ready` deltaP `4.7341` edge `0.0018` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.395` n `133` status `ready` deltaP `4.5675` edge `-0.0019` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.4023` n `133` status `ready` deltaP `0.8318` edge `0.011` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.5229` n `123` status `ready` deltaP `1.7784` edge `0.044` maxDD `-1.165`
- `market_context_high->index_24h` score `-0.624` n `113` status `ready` deltaP `10.6087` edge `-0.0225` maxDD `-4.925`
- `market_context_high->index_1h` score `-0.655` n `133` status `ready` deltaP `-2.0362` edge `-0.0052` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.2683` n `123` status `ready` deltaP `3.811` edge `-0.017` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.3974` n `133` status `ready` deltaP `1.2775` edge `-0.0296` maxDD `-9.3126`
- `market_context_high->index_4h` score `-2.2301` n `123` status `ready` deltaP `-9.4004` edge `-0.0358` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.4151` n `133` status `ready` deltaP `-0.9916` edge `-0.0744` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-3.8719` n `133` status `ready` deltaP `-2.6552` edge `-0.0565` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.9281` n `113` status `ready` deltaP `-2.5934` edge `-0.1288` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-6.2402` n `123` status `ready` deltaP `-9.7561` edge `-0.231` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.5532` n `113` status `ready` deltaP `-18.9927` edge `-0.1546` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-7.1871` n `113` status `ready` deltaP `-5.2483` edge `-0.3289` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-8.9109` n `123` status `ready` deltaP `-8.5874` edge `-0.359` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
