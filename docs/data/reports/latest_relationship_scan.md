# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T14:37:28.888763+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14802`

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

- `market_context_high->unknown_1h` score `0.888` n `149` status `ready` deltaP `6.5577` edge `0.053` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.6105` n `145` status `ready` deltaP `18.524` edge `-0.0287` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0582` n `145` status `ready` deltaP `7.2487` edge `0.0094` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.0437` n `149` status `ready` deltaP `6.4482` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0717` n `149` status `ready` deltaP `3.3145` edge `0.0046` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.3277` n `145` status `ready` deltaP `7.663` edge `-0.0168` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.3393` n `149` status `ready` deltaP `4.7241` edge `0.032` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3398` n `149` status `ready` deltaP `0.4803` edge `-0.0049` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.4596` n `145` status `ready` deltaP `4.9401` edge `0.0117` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.8602` n `145` status `ready` deltaP `-3.7269` edge `-0.0004` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.1243` n `149` status `ready` deltaP `-8.3219` edge `-0.0029` maxDD `-1.1941`
- `market_context_high->fx_24h` score `-1.5773` n `131` status `ready` deltaP `2.6466` edge `0.0119` maxDD `-2.2121`
- `market_context_high->equity_4h` score `-1.7061` n `145` status `ready` deltaP `-1.0923` edge `0.0692` maxDD `-16.1188`
- `market_context_high->crypto_alt_4h` score `-2.2119` n `145` status `ready` deltaP `4.4838` edge `-0.0674` maxDD `-7.0785`
- `market_context_high->commodity_24h` score `-2.2796` n `131` status `ready` deltaP `-6.4713` edge `0.0365` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-2.4813` n `149` status `ready` deltaP `-2.3841` edge `-0.0414` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.5716` n `149` status `ready` deltaP `-5.2083` edge `-0.1152` maxDD `-7.8171`
- `market_context_high->index_24h` score `-4.5471` n `131` status `ready` deltaP `-9.5062` edge `-0.0395` maxDD `-21.0736`
- `market_context_high->crypto_major_4h` score `-5.4668` n `145` status `ready` deltaP `-0.1914` edge `-0.3213` maxDD `-5.6395`
- `market_context_high->metal_24h` score `-5.5612` n `131` status `ready` deltaP `-25.9329` edge `-0.2093` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
