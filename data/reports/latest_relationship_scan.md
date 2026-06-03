# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T16:07:30.162993+00:00`
- Price records: `672`
- Market context records: `2779`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `3.6867` n `140` status `ready` deltaP `7.6488` edge `0.3027` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `3.4198` n `140` status `ready` deltaP `4.5387` edge `0.6464` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.8842` n `142` status `ready` deltaP `6.0331` edge `0.1388` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.3449` n `140` status `ready` deltaP `10.6051` edge `0.2829` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.1823` n `142` status `ready` deltaP `11.9289` edge `0.028` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0877` n `142` status `ready` deltaP `3.732` edge `0.0409` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.121` n `142` status `ready` deltaP `3.7489` edge `0.0089` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5874` n `142` status `ready` deltaP `-1.1364` edge `0.003` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6343` n `142` status `ready` deltaP `-0.2825` edge `-0.0041` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.6443` n `142` status `ready` deltaP `0.4322` edge `-0.0009` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.7085` n `142` status `ready` deltaP `5.0962` edge `0.0512` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.9233` n `142` status `ready` deltaP `3.926` edge `0.0424` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.0777` n `142` status `ready` deltaP `-3.4979` edge `0.0168` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.1215` n `142` status `ready` deltaP `-3.4481` edge `0.0074` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3784` n `140` status `ready` deltaP `-1.002` edge `-0.021` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.4333` n `142` status `ready` deltaP `13.8805` edge `0.2221` maxDD `-28.7261`
- `market_context_high->commodity_4h` score `-1.5627` n `142` status `ready` deltaP `0.161` edge `-0.0094` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-1.6671` n `142` status `ready` deltaP `0.5904` edge `-0.0049` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.2672` n `142` status `ready` deltaP `-1.5329` edge `-0.0254` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.5749` n `142` status `ready` deltaP `5.1249` edge `0.1263` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
