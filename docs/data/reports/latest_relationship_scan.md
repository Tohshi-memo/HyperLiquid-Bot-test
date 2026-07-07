# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T15:37:30.395453+00:00`
- Price records: `672`
- Market context records: `5994`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11120`

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

- `news_risk_high->fx_24h` score `7.5371` n `30` status `ready` deltaP `68.9236` edge `0.1686` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.2977` n `30` status `ready` deltaP `32.8473` edge `0.1597` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.1409` n `30` status `ready` deltaP `42.8963` edge `0.0637` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2298` n `30` status `ready` deltaP `26.7764` edge `0.0212` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.1217` n `227` status `ready` deltaP `7.4729` edge `0.1531` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.7483` n `30` status `ready` deltaP `9.7405` edge `0.0777` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1639` n `30` status `ready` deltaP `5.1697` edge `0.0327` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1031` n `30` status `ready` deltaP `9.2361` edge `0.0388` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.4024` n `30` status `ready` deltaP `1.6866` edge `-0.0262` maxDD `-1.2643`
- `market_context_high->equity_24h` score `-0.4036` n `200` status `ready` deltaP `22.4931` edge `0.3532` maxDD `-31.2762`
- `market_context_high->equity_1h` score `-0.4323` n `227` status `ready` deltaP `3.5434` edge `0.0338` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.5147` n `227` status `ready` deltaP `2.0978` edge `-0.0001` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.5767` n `227` status `ready` deltaP `-0.3614` edge `0.0023` maxDD `-0.8358`
- `market_context_high->fx_1h` score `-0.7611` n `227` status `ready` deltaP `-1.623` edge `-0.0017` maxDD `-0.7392`
- `news_risk_high->index_1h` score `-1.0088` n `30` status `ready` deltaP `-8.9521` edge `-0.0182` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.0586` n `227` status `ready` deltaP `-0.1881` edge `0.0001` maxDD `-3.4322`
- `market_context_high->crypto_major_1h` score `-1.1463` n `227` status `ready` deltaP `2.3543` edge `0.0141` maxDD `-9.807`
- `market_context_high->index_1h` score `-1.1666` n `227` status `ready` deltaP `-1.375` edge `0.0033` maxDD `-1.3078`
- `market_context_high->index_4h` score `-1.2012` n `227` status `ready` deltaP `-0.1014` edge `0.0154` maxDD `-3.165`
- `market_context_high->crypto_alt_1h` score `-1.2203` n `227` status `ready` deltaP `1.3664` edge `0.0097` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
