# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T02:22:28.051249+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9338`

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

- `risk_on_high->crypto_alt_4h` score `5.3241` n `48` status `ready` deltaP `20.7826` edge `0.3499` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.3241` n `48` status `ready` deltaP `20.7826` edge `0.3499` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.0494` n `39` status `ready` deltaP `30.087` edge `0.2202` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.0494` n `39` status `ready` deltaP `30.087` edge `0.2202` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `4.6223` n `100` status `ready` deltaP `15.8659` edge `0.4243` maxDD `-9.2574`
- `risk_on_high->crypto_major_4h` score `4.2506` n `48` status `ready` deltaP `35.4167` edge `0.3941` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.2506` n `48` status `ready` deltaP `35.4167` edge `0.3941` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `4.1488` n `100` status `ready` deltaP `19.25` edge `0.3733` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.4838` n `109` status `ready` deltaP `12.1052` edge `0.1497` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.0346` n `109` status `ready` deltaP `5.7559` edge `0.1284` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.2419` n `109` status `ready` deltaP `0.9752` edge `0.0005` maxDD `-0.3742`
- `market_context_high->metal_4h` score `-0.342` n `100` status `ready` deltaP `8.6098` edge `0.0094` maxDD `-1.624`
- `market_context_high->index_1h` score `-0.3939` n `109` status `ready` deltaP `1.193` edge `-0.0023` maxDD `-1.1587`
- `market_context_high->unknown_4h` score `-0.4045` n `100` status `ready` deltaP `-4.8415` edge `0.0632` maxDD `-1.8373`
- `risk_on_high->crypto_major_1h` score `-0.4495` n `52` status `ready` deltaP `2.5449` edge `0.0178` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4495` n `52` status `ready` deltaP `2.5449` edge `0.0178` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.5001` n `109` status `ready` deltaP `3.3799` edge `0.0003` maxDD `-0.9556`
- `risk_on_high->fx_1h` score `-0.6025` n `52` status `ready` deltaP `-1.2301` edge `-0.004` maxDD `-0.3742`
- `risk_on_and_context->fx_1h` score `-0.6025` n `52` status `ready` deltaP `-1.2301` edge `-0.004` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.6344` n `52` status `ready` deltaP `-0.7485` edge `-0.0032` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
