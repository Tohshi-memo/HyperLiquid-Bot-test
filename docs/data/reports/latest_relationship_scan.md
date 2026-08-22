# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T19:22:27.115431+00:00`
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

- `market_context_high->unknown_1h` score `1.4976` n `149` status `ready` deltaP `6.408` edge `0.1048` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.9087` n `149` status `ready` deltaP `18.7418` edge `-0.0053` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1073` n `149` status `ready` deltaP `8.2071` edge `0.0093` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.0126` n `149` status `ready` deltaP `7.047` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.12` n `149` status `ready` deltaP `2.4163` edge `0.0044` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.3179` n `149` status `ready` deltaP `7.845` edge `-0.0172` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.3198` n `149` status `ready` deltaP `5.0235` edge `0.0325` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3398` n `149` status `ready` deltaP `0.4803` edge `-0.0049` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.5372` n `149` status `ready` deltaP `3.4774` edge `0.0115` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.8778` n `149` status `ready` deltaP `-4.081` edge `-0.0003` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.1212` n `149` status `ready` deltaP `-8.3219` edge `-0.0025` maxDD `-1.1941`
- `market_context_high->fx_24h` score `-1.1388` n `133` status `ready` deltaP `0.6135` edge `0.0109` maxDD `-2.2121`
- `market_context_high->equity_4h` score `-1.6776` n `149` status `ready` deltaP `-0.5177` edge `0.07` maxDD `-16.1967`
- `market_context_high->commodity_24h` score `-2.1032` n `133` status `ready` deltaP `-4.2058` edge `0.0361` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-2.4957` n `149` status `ready` deltaP `-2.3841` edge `-0.0426` maxDD `-7.9582`
- `market_context_high->crypto_alt_4h` score `-2.5929` n `149` status `ready` deltaP `2.5413` edge `-0.0862` maxDD `-7.0785`
- `market_context_high->crypto_major_1h` score `-3.6136` n `149` status `ready` deltaP `-5.358` edge `-0.1177` maxDD `-7.8171`
- `market_context_high->index_24h` score `-4.3466` n `133` status `ready` deltaP `-6.2148` edge `-0.0351` maxDD `-21.1244`
- `market_context_high->metal_24h` score `-5.384` n `133` status `ready` deltaP `-23.2887` edge `-0.2042` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.7518` n `149` status `ready` deltaP `-0.6937` edge `-0.3417` maxDD `-5.6395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
