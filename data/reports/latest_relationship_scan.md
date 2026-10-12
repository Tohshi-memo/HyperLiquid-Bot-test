# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T21:52:29.304387+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8942`

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

- `risk_on_high->crypto_alt_4h` score `4.9147` n `48` status `ready` deltaP `20.6301` edge `0.3168` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.9147` n `48` status `ready` deltaP `20.6301` edge `0.3168` maxDD `-1.9151`
- `market_context_high->crypto_alt_4h` score `4.2129` n `100` status `ready` deltaP `15.7134` edge `0.3912` maxDD `-9.2574`
- `risk_on_high->crypto_major_4h` score `3.993` n `48` status `ready` deltaP `35.2643` edge `0.3621` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.993` n `48` status `ready` deltaP `35.2643` edge `0.3621` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `3.7526` n `100` status `ready` deltaP `19.0976` edge `0.3413` maxDD `-7.4722`
- `market_context_high->crypto_major_24h` score `2.3651` n `73` status `ready` deltaP `15.5394` edge `0.9466` maxDD `-49.7579`
- `market_context_high->crypto_alt_1h` score `1.7528` n `100` status `ready` deltaP `12.9521` edge `0.1548` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `1.1313` n `48` status `ready` deltaP `7.2854` edge `0.1054` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.1313` n `48` status `ready` deltaP `7.2854` edge `0.1054` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.7807` n `100` status `ready` deltaP `5.0958` edge `0.1074` maxDD `-3.4384`
- `market_context_high->unknown_4h` score `0.6523` n `100` status `ready` deltaP `-4.2317` edge `0.1472` maxDD `-1.8373`
- `risk_on_high->crypto_major_1h` score `0.4958` n `48` status `ready` deltaP `6.2625` edge `0.0871` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4958` n `48` status `ready` deltaP `6.2625` edge `0.0871` maxDD `-3.2233`
- `market_context_high->index_1h` score `0.0515` n `100` status `ready` deltaP `5.3514` edge `0.004` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1465` n `100` status `ready` deltaP `5.9521` edge `0.0042` maxDD `-0.4868`
- `market_context_high->metal_4h` score `-0.2277` n `100` status `ready` deltaP `9.8293` edge `0.0108` maxDD `-1.624`
- `risk_on_high->metal_1h` score `-0.3291` n `48` status `ready` deltaP `3.1188` edge `0.0037` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.3291` n `48` status `ready` deltaP `3.1188` edge `0.0037` maxDD `-0.4868`
- `market_context_high->fx_1h` score `-0.3432` n `100` status `ready` deltaP `-0.7027` edge `-0.0013` maxDD `-0.3742`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
