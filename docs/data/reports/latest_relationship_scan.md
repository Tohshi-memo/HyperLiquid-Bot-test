# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T15:34:32.881277+00:00`
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

- `market_context_high->unknown_1h` score `1.2047` n `149` status `ready` deltaP `6.8571` edge `0.0774` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.8997` n `145` status `ready` deltaP `18.524` edge `-0.0046` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0598` n `145` status `ready` deltaP `7.2487` edge `0.0096` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.036` n `149` status `ready` deltaP `6.5979` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0873` n `149` status `ready` deltaP `3.0151` edge `0.0046` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.312` n `149` status `ready` deltaP `5.1732` edge `0.0325` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3398` n `149` status `ready` deltaP `0.4803` edge `-0.0049` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3545` n `145` status `ready` deltaP `7.3581` edge `-0.017` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.4438` n `145` status `ready` deltaP `5.245` edge `0.0117` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.8214` n `145` status `ready` deltaP `-3.1171` edge `0.0005` maxDD `-2.4692`
- `market_context_high->fx_24h` score `-1.0105` n `133` status `ready` deltaP `2.8704` edge `0.0123` maxDD `-2.2121`
- `market_context_high->commodity_1h` score `-1.1243` n `149` status `ready` deltaP `-8.3219` edge `-0.0029` maxDD `-1.1941`
- `market_context_high->equity_4h` score `-1.68` n `145` status `ready` deltaP `-0.635` edge `0.0695` maxDD `-16.1188`
- `market_context_high->crypto_alt_4h` score `-2.1941` n `145` status `ready` deltaP `4.5564` edge `-0.0664` maxDD `-7.0785`
- `market_context_high->commodity_24h` score `-2.3535` n `133` status `ready` deltaP `-6.81` edge `0.0326` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-2.3746` n `149` status `ready` deltaP `-1.7853` edge `-0.0365` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.4733` n `149` status `ready` deltaP `-4.7592` edge `-0.11` maxDD `-7.8171`
- `market_context_high->index_24h` score `-4.4999` n `133` status `ready` deltaP `-8.819` edge `-0.0374` maxDD `-21.1244`
- `market_context_high->crypto_major_4h` score `-5.4622` n `145` status `ready` deltaP `-0.1188` edge `-0.3214` maxDD `-5.6395`
- `market_context_high->metal_24h` score `-5.5568` n `133` status `ready` deltaP `-25.8929` edge `-0.209` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
