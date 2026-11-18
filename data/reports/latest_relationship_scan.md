# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T23:37:30.671949+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2262`

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

- `market_context_high->unknown_24h` score `1371.1827` n `98` status `ready` deltaP `5.2083` edge `114.2305` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.2734` n `98` status `ready` deltaP `39.594` edge `1.7648` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.3238` n `98` status `ready` deltaP `24.4402` edge `1.5012` maxDD `-13.3222`
- `market_context_high->metal_24h` score `-0.3253` n `98` status `ready` deltaP `15.3557` edge `0.193` maxDD `-15.7982`
- `market_context_high->metal_1h` score `-0.3535` n `98` status `ready` deltaP `1.1304` edge `0.0073` maxDD `-2.1461`
- `market_context_high->metal_4h` score `-0.58` n `98` status `ready` deltaP `11.7721` edge `0.0039` maxDD `-6.1238`
- `market_context_high->crypto_alt_4h` score `-0.7477` n `98` status `ready` deltaP `0.8773` edge `0.1793` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.9422` n `98` status `ready` deltaP `-3.2232` edge `-0.0006` maxDD `-1.2295`
- `market_context_high->crypto_major_4h` score `-1.0318` n `98` status `ready` deltaP `-1.9257` edge `0.2388` maxDD `-22.3259`
- `market_context_high->crypto_alt_1h` score `-1.2103` n `98` status `ready` deltaP `-1.9583` edge `0.0082` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.4286` n `98` status `ready` deltaP `-9.4953` edge `-0.0011` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-1.9894` n `98` status `ready` deltaP `0.11` edge `0.0202` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.5792` n `98` status `ready` deltaP `-9.1494` edge `-0.0196` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.8995` n `98` status `ready` deltaP `-15.523` edge `-0.0334` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.0759` n `98` status `ready` deltaP `0.7088` edge `-0.0433` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.5888` n `98` status `ready` deltaP `-25.1493` edge `-0.0105` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.748` n `98` status `ready` deltaP `-18.8138` edge `-0.006` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.47` n `98` status `ready` deltaP `-24.5146` edge `-0.113` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.0906` n `98` status `ready` deltaP `-16.2486` edge `-0.107` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.2337` n `98` status `ready` deltaP `-14.7337` edge `-0.2392` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
