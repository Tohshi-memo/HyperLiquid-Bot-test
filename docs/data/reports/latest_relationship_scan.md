# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T15:52:17.437575+00:00`
- Price records: `672`
- Market context records: `1027`
- Flow alert records: `4864`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8635`

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

- `market_context_high->crypto_major_24h` score `13.9827` n `187` status `ready` deltaP `32.7412` edge `1.0058` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.4475` n `187` status `ready` deltaP `11.2391` edge `0.4191` maxDD `-9.5387`
- `market_context_high->equity_24h` score `2.47` n `187` status `ready` deltaP `10.0908` edge `0.2561` maxDD `-5.0699`
- `market_context_high->index_24h` score `1.865` n `187` status `ready` deltaP `9.399` edge `0.2023` maxDD `-2.7633`
- `market_context_high->fx_1h` score `-0.1021` n `187` status `ready` deltaP `4.7816` edge `0.0006` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.5436` n `187` status `ready` deltaP `3.4791` edge `0.0095` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.5642` n `187` status `ready` deltaP `0.7413` edge `0.0237` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.6639` n `187` status `ready` deltaP `1.208` edge `0.0174` maxDD `-3.7959`
- `market_context_high->crypto_major_1h` score `-0.9474` n `187` status `ready` deltaP `5.2091` edge `-0.0153` maxDD `-9.2715`
- `market_context_high->fx_4h` score `-0.9744` n `187` status `ready` deltaP `2.3314` edge `0.0029` maxDD `-1.6381`
- `market_context_high->index_4h` score `-1.3658` n `187` status `ready` deltaP `0.0187` edge `0.0337` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.447` n `187` status `ready` deltaP `1.698` edge `0.0833` maxDD `-10.5498`
- `market_context_high->metal_24h` score `-1.5737` n `187` status `ready` deltaP `-7.0266` edge `0.346` maxDD `-26.4236`
- `market_context_high->crypto_alt_1h` score `-1.611` n `187` status `ready` deltaP `-0.4371` edge `-0.0146` maxDD `-6.0054`
- `market_context_high->metal_1h` score `-1.6461` n `187` status `ready` deltaP `0.9959` edge `-0.0389` maxDD `-8.3025`
- `market_context_high->crypto_alt_4h` score `-2.757` n `187` status `ready` deltaP `0.6839` edge `0.0435` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-2.9233` n `187` status `ready` deltaP `7.379` edge `0.0778` maxDD `-22.648`
- `market_context_high->fx_24h` score `-3.2083` n `187` status `ready` deltaP `2.4312` edge `-0.0199` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.5248` n `187` status `ready` deltaP `-4.2553` edge `0.0514` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.9724` n `187` status `ready` deltaP `-1.3923` edge `-0.1561` maxDD `-20.8458`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
