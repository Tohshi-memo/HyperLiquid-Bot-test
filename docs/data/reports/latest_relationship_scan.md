# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T11:07:27.806769+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5108`

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

- `market_context_high->unknown_4h` score `40.2591` n `113` status `ready` deltaP `-0.2914` edge `3.3904` maxDD `-1.016`
- `market_context_high->unknown_1h` score `3.6673` n `113` status `ready` deltaP `4.0207` edge `0.3277` maxDD `-1.5781`
- `market_context_high->commodity_24h` score `0.929` n `50` status `ready` deltaP `19.3958` edge `0.0807` maxDD `-3.6055`
- `market_context_high->fx_4h` score `0.0487` n `113` status `ready` deltaP `8.221` edge `0.0091` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0498` n `113` status `ready` deltaP `3.8591` edge `0.0028` maxDD `-0.1258`
- `market_context_high->crypto_major_24h` score `-0.3881` n `50` status `ready` deltaP `-0.1667` edge `0.0539` maxDD `-4.5369`
- `market_context_high->commodity_1h` score `-0.5457` n `113` status `ready` deltaP `-0.6319` edge `0.0088` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.5952` n `113` status `ready` deltaP `5.0832` edge `-0.0043` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.616` n `113` status `ready` deltaP `-1.2877` edge `-0.0052` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.9075` n `113` status `ready` deltaP `-3.4576` edge `0.0296` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.33` n `113` status `ready` deltaP `2.3488` edge `-0.0281` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.8198` n `113` status `ready` deltaP `5.5283` edge `-0.0175` maxDD `-5.3474`
- `market_context_high->fx_24h` score `-1.9279` n `50` status `ready` deltaP `-3.3403` edge `0.0062` maxDD `-1.2338`
- `market_context_high->index_4h` score `-2.1483` n `113` status `ready` deltaP `-7.7676` edge `-0.0362` maxDD `-4.3282`
- `market_context_high->crypto_alt_24h` score `-2.1978` n `50` status `ready` deltaP `7.7361` edge `0.0625` maxDD `-26.334`
- `market_context_high->crypto_alt_1h` score `-3.0454` n `113` status `ready` deltaP `-2.0097` edge `-0.053` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.4206` n `50` status `ready` deltaP `-9.5208` edge `-0.0035` maxDD `-7.1131`
- `market_context_high->equity_1h` score `-3.7301` n `113` status `ready` deltaP `0.359` edge `-0.0859` maxDD `-12.1865`
- `market_context_high->index_24h` score `-4.3575` n `50` status `ready` deltaP `-11.7292` edge `-0.1567` maxDD `-4.925`
- `market_context_high->crypto_major_4h` score `-10.0148` n `113` status `ready` deltaP `-12.7428` edge `-0.2498` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
