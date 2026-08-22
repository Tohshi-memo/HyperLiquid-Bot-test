# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T16:22:24.964083+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14818`

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

- `market_context_high->unknown_1h` score `1.5275` n `149` status `ready` deltaP `6.8571` edge `0.1043` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.8771` n `146` status `ready` deltaP `18.466` edge `-0.0061` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0825` n `146` status `ready` deltaP `7.6846` edge `0.0096` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.0445` n `149` status `ready` deltaP `6.4482` edge `0.0044` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1036` n `149` status `ready` deltaP `2.7157` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3198` n `149` status `ready` deltaP `5.0235` edge `0.0325` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.3364` n `146` status `ready` deltaP `7.599` edge `-0.0171` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.3639` n `149` status `ready` deltaP `0.0312` edge `-0.005` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.4465` n `146` status `ready` deltaP `5.1767` edge `0.0118` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.8178` n `146` status `ready` deltaP `-3.0613` edge `0.0006` maxDD `-2.4692`
- `market_context_high->fx_24h` score `-1.0399` n `133` status `ready` deltaP `2.3496` edge `0.012` maxDD `-2.2121`
- `market_context_high->commodity_1h` score `-1.1399` n `149` status `ready` deltaP `-8.6213` edge `-0.0029` maxDD `-1.1941`
- `market_context_high->equity_4h` score `-1.6741` n `146` status `ready` deltaP `-0.5367` edge `0.0696` maxDD `-16.1188`
- `market_context_high->crypto_alt_4h` score `-2.2711` n `146` status `ready` deltaP `4.0887` edge `-0.0697` maxDD `-7.0785`
- `market_context_high->commodity_24h` score `-2.3046` n `133` status `ready` deltaP `-6.2891` edge `0.0332` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-2.4213` n `149` status `ready` deltaP `-2.0847` edge `-0.0384` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.4865` n `149` status `ready` deltaP `-4.7592` edge `-0.1111` maxDD `-7.8171`
- `market_context_high->index_24h` score `-4.4674` n `133` status `ready` deltaP `-8.2981` edge `-0.0367` maxDD `-21.1244`
- `market_context_high->crypto_major_4h` score `-5.4964` n `146` status `ready` deltaP `-0.0961` edge `-0.3244` maxDD `-5.6395`
- `market_context_high->metal_24h` score `-5.5235` n `133` status `ready` deltaP `-25.3721` edge `-0.2082` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
