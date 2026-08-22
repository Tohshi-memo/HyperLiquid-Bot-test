# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T18:52:32.023630+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14866`

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

- `market_context_high->unknown_1h` score `1.5347` n `149` status `ready` deltaP `6.7074` edge `0.1059` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.9591` n `149` status `ready` deltaP `18.7418` edge `-0.0011` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1073` n `149` status `ready` deltaP `8.2071` edge `0.0093` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.0204` n `149` status `ready` deltaP `6.8973` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1114` n `149` status `ready` deltaP `2.566` edge `0.0045` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2935` n `149` status `ready` deltaP `8.1498` edge `-0.0172` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.3206` n `149` status `ready` deltaP `5.0235` edge `0.0324` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3561` n `149` status `ready` deltaP `0.1809` edge `-0.005` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.5293` n `149` status `ready` deltaP `3.6299` edge `0.0115` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.8604` n `149` status `ready` deltaP `-3.7762` edge `-0.0001` maxDD `-2.4692`
- `market_context_high->fx_24h` score `-1.1191` n `133` status `ready` deltaP `0.9607` edge `0.0111` maxDD `-2.2121`
- `market_context_high->commodity_1h` score `-1.1375` n `149` status `ready` deltaP `-8.6213` edge `-0.0026` maxDD `-1.1941`
- `market_context_high->equity_4h` score `-1.676` n `149` status `ready` deltaP `-0.5177` edge `0.0702` maxDD `-16.1967`
- `market_context_high->commodity_24h` score `-2.1345` n `133` status `ready` deltaP `-4.553` edge `0.0358` maxDD `-4.666`
- `market_context_high->crypto_alt_4h` score `-2.5229` n `149` status `ready` deltaP `2.8462` edge `-0.0824` maxDD `-7.0785`
- `market_context_high->crypto_alt_1h` score `-2.534` n `149` status `ready` deltaP `-2.6835` edge `-0.0438` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.6352` n `149` status `ready` deltaP `-5.5077` edge `-0.1185` maxDD `-7.8171`
- `market_context_high->index_24h` score `-4.3662` n `133` status `ready` deltaP `-6.562` edge `-0.0353` maxDD `-21.1244`
- `market_context_high->metal_24h` score `-5.4067` n `133` status `ready` deltaP `-23.636` edge `-0.2048` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.6832` n `149` status `ready` deltaP `-0.5412` edge `-0.337` maxDD `-5.6395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
