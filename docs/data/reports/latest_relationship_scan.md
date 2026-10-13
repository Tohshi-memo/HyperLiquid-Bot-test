# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T00:37:32.455590+00:00`
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

- `risk_on_high->crypto_alt_4h` score `5.1201` n `48` status `ready` deltaP `20.7826` edge `0.3329` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.1201` n `48` status `ready` deltaP `20.7826` edge `0.3329` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `4.4242` n `32` status `ready` deltaP `30.087` edge `0.1681` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.4242` n `32` status `ready` deltaP `30.087` edge `0.1681` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `4.4183` n `100` status `ready` deltaP `15.8659` edge `0.4073` maxDD `-9.2574`
- `risk_on_high->crypto_major_4h` score `4.146` n `48` status `ready` deltaP `35.4167` edge `0.3807` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.146` n `48` status `ready` deltaP `35.4167` edge `0.3807` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `3.988` n `100` status `ready` deltaP `19.25` edge `0.3599` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.5719` n `102` status `ready` deltaP `12.296` edge `0.1441` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.5596` n `50` status `ready` deltaP `5.5509` edge `0.0701` maxDD `-2.5044`
- `risk_on_and_context->crypto_alt_1h` score `0.5596` n `50` status `ready` deltaP `5.5509` edge `0.0701` maxDD `-2.5044`
- `market_context_high->crypto_major_1h` score `0.4416` n `102` status `ready` deltaP `4.9548` edge `0.0999` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.2075` n `50` status `ready` deltaP `4.994` edge `0.0586` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.2075` n `50` status `ready` deltaP `4.994` edge `0.0586` maxDD `-3.2233`
- `market_context_high->unknown_4h` score `0.0891` n `100` status `ready` deltaP `-4.5366` edge `0.1023` maxDD `-1.8373`
- `market_context_high->index_1h` score `-0.0326` n `102` status `ready` deltaP `4.4427` edge `0.0023` maxDD `-0.5542`
- `market_context_high->metal_1h` score `-0.2065` n `102` status `ready` deltaP `5.1339` edge `0.0023` maxDD `-0.7068`
- `market_context_high->metal_4h` score `-0.342` n `100` status `ready` deltaP `8.6098` edge `0.0094` maxDD `-1.624`
- `market_context_high->fx_1h` score `-0.397` n `102` status `ready` deltaP `-1.7223` edge `-0.0014` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.431` n `50` status `ready` deltaP `1.2515` edge `-0.0006` maxDD `-0.7068`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
