# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T19:37:30.036440+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `market_context_high->unknown_1h` score `1.4808` n `149` status `ready` deltaP `6.2583` edge `0.1044` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.8871` n `149` status `ready` deltaP `18.7418` edge `-0.0071` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0986` n `149` status `ready` deltaP `8.0547` edge `0.0092` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.0126` n `149` status `ready` deltaP `7.047` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1277` n `149` status `ready` deltaP `2.2666` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3198` n `149` status `ready` deltaP `5.0235` edge `0.0325` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.3313` n `149` status `ready` deltaP `7.6925` edge `-0.0173` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.3398` n `149` status `ready` deltaP `0.4803` edge `-0.0049` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.5372` n `149` status `ready` deltaP `3.4774` edge `0.0115` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.8865` n `149` status `ready` deltaP `-4.2335` edge `-0.0004` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.1212` n `149` status `ready` deltaP `-8.3219` edge `-0.0025` maxDD `-1.1941`
- `market_context_high->fx_24h` score `-1.1486` n `133` status `ready` deltaP `0.4399` edge `0.0108` maxDD `-2.2121`
- `market_context_high->equity_4h` score `-1.6792` n `149` status `ready` deltaP `-0.5177` edge `0.0698` maxDD `-16.1967`
- `market_context_high->commodity_24h` score `-2.102` n `133` status `ready` deltaP `-4.2058` edge `0.0362` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-2.4801` n `149` status `ready` deltaP `-2.2344` edge `-0.0423` maxDD `-7.9582`
- `market_context_high->crypto_alt_4h` score `-2.6291` n `149` status `ready` deltaP `2.3889` edge `-0.0882` maxDD `-7.0785`
- `market_context_high->crypto_major_1h` score `-3.6136` n `149` status `ready` deltaP `-5.358` edge `-0.1177` maxDD `-7.8171`
- `market_context_high->index_24h` score `-4.336` n `133` status `ready` deltaP `-6.0412` edge `-0.0349` maxDD `-21.1244`
- `market_context_high->metal_24h` score `-5.3726` n `133` status `ready` deltaP `-23.1151` edge `-0.2039` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.794` n `149` status `ready` deltaP `-0.8461` edge `-0.3442` maxDD `-5.6395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
