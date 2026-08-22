# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T14:52:28.201622+00:00`
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

- `market_context_high->unknown_1h` score `1.0067` n `149` status `ready` deltaP `6.8571` edge `0.0609` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.6969` n `145` status `ready` deltaP `18.524` edge `-0.0215` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.059` n `145` status `ready` deltaP `7.2487` edge `0.0095` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.036` n `149` status `ready` deltaP `6.5979` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0639` n `149` status `ready` deltaP `3.4642` edge `0.0046` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3299` n `149` status `ready` deltaP `4.8738` edge `0.0322` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3398` n `149` status `ready` deltaP `0.4803` edge `-0.0049` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3411` n `145` status `ready` deltaP `7.5105` edge `-0.0169` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.4596` n `145` status `ready` deltaP `4.9401` edge `0.0117` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.8499` n `145` status `ready` deltaP `-3.5744` edge `-0.0001` maxDD `-2.4692`
- `market_context_high->fx_24h` score `-1.0071` n `132` status `ready` deltaP `2.9356` edge `0.0123` maxDD `-2.2121`
- `market_context_high->commodity_1h` score `-1.1321` n `149` status `ready` deltaP `-8.4716` edge `-0.0029` maxDD `-1.1941`
- `market_context_high->equity_4h` score `-1.6982` n `145` status `ready` deltaP `-0.9399` edge `0.0692` maxDD `-16.1188`
- `market_context_high->crypto_alt_4h` score `-2.257` n `145` status `ready` deltaP `4.0991` edge `-0.0686` maxDD `-7.0785`
- `market_context_high->commodity_24h` score `-2.3314` n `132` status `ready` deltaP `-6.8182` edge `0.0345` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-2.4381` n `149` status `ready` deltaP `-2.2344` edge `-0.0388` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.5261` n `149` status `ready` deltaP `-5.0586` edge `-0.1124` maxDD `-7.8171`
- `market_context_high->index_24h` score `-4.5169` n `132` status `ready` deltaP `-9.0436` edge `-0.0385` maxDD `-21.0907`
- `market_context_high->crypto_major_4h` score `-5.5204` n `145` status `ready` deltaP `-0.5761` edge `-0.3232` maxDD `-5.6395`
- `market_context_high->metal_24h` score `-5.5686` n `132` status `ready` deltaP `-26.089` edge `-0.2092` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
