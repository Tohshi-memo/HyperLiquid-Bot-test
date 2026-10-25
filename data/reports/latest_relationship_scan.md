# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T12:07:28.805721+00:00`
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

- `market_context_high->unknown_4h` score `39.0099` n `113` status `ready` deltaP `-0.2914` edge `3.2863` maxDD `-1.016`
- `market_context_high->unknown_1h` score `3.6169` n `113` status `ready` deltaP `4.0207` edge `0.3235` maxDD `-1.5781`
- `market_context_high->commodity_24h` score `0.7106` n `54` status `ready` deltaP `16.2616` edge `0.0736` maxDD `-3.6055`
- `market_context_high->fx_4h` score `0.0475` n `113` status `ready` deltaP `8.221` edge `0.009` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0653` n `113` status `ready` deltaP `3.5597` edge `0.0028` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.5326` n `113` status `ready` deltaP `-0.4822` edge `0.0089` maxDD `-1.0053`
- `market_context_high->crypto_major_24h` score `-0.5691` n `54` status `ready` deltaP `0.8681` edge `0.0238` maxDD `-4.5369`
- `market_context_high->index_1h` score `-0.6441` n `113` status `ready` deltaP `-1.7368` edge `-0.0058` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.6491` n `113` status `ready` deltaP `4.4844` edge `-0.0048` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.9154` n `113` status `ready` deltaP `-3.61` edge `0.0296` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.4002` n `113` status `ready` deltaP `1.8997` edge `-0.0341` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.86` n `113` status `ready` deltaP `5.071` edge `-0.0178` maxDD `-5.3474`
- `market_context_high->fx_24h` score `-2.0862` n `54` status `ready` deltaP `-3.588` edge `0.0073` maxDD `-1.2451`
- `market_context_high->index_4h` score `-2.1696` n `113` status `ready` deltaP `-8.0725` edge `-0.0369` maxDD `-4.3282`
- `market_context_high->index_24h` score `-2.5888` n `54` status `ready` deltaP `-8.2755` edge `-0.1485` maxDD `-4.925`
- `market_context_high->crypto_alt_1h` score `-3.1618` n `113` status `ready` deltaP `-2.3091` edge `-0.0607` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.6286` n `54` status `ready` deltaP `-10.706` edge `0.0049` maxDD `-7.2058`
- `market_context_high->equity_1h` score `-3.8404` n `113` status `ready` deltaP `-0.2398` edge `-0.0911` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-4.1936` n `54` status `ready` deltaP `3.588` edge `-0.0783` maxDD `-31.9942`
- `market_context_high->crypto_major_4h` score `-10.04` n `113` status `ready` deltaP `-12.7428` edge `-0.2519` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
