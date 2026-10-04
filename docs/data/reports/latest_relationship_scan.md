# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T06:22:31.650043+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5004`

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

- `market_context_high->unknown_4h` score `273.3166` n `55` status `ready` deltaP `7.0566` edge `22.7437` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `210.5535` n `67` status `ready` deltaP `1.2423` edge `17.5793` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `14.6717` n `46` status `ready` deltaP `32.6012` edge `1.1326` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `13.3459` n `46` status `ready` deltaP `39.0437` edge `0.9171` maxDD `-4.5519`
- `news_risk_high->equity_24h` score `11.3935` n `59` status `ready` deltaP `29.4421` edge `0.7632` maxDD `-0.1353`
- `news_risk_high->crypto_major_4h` score `11.0916` n `65` status `ready` deltaP `40.1736` edge `0.6768` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.5626` n `65` status `ready` deltaP `24.6646` edge `0.6002` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.1287` n `55` status `ready` deltaP `18.775` edge `0.4559` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.8514` n `59` status `ready` deltaP `33.1023` edge `0.1836` maxDD `0.0`
- `market_context_high->equity_24h` score `4.4194` n `46` status `ready` deltaP `10.1348` edge `0.4004` maxDD `-6.3081`
- `news_risk_high->equity_4h` score `3.9337` n `65` status `ready` deltaP `27.1318` edge `0.2082` maxDD `-2.9013`
- `market_context_high->crypto_alt_4h` score `3.2107` n `55` status `ready` deltaP `17.3919` edge `0.4246` maxDD `-7.6465`
- `news_risk_high->index_4h` score `3.1684` n `65` status `ready` deltaP `34.5052` edge `0.0602` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9963` n `65` status `ready` deltaP `13.3095` edge `0.1965` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.5714` n `67` status `ready` deltaP `15.8124` edge `0.1539` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.5524` n `65` status `ready` deltaP `21.8223` edge `0.1088` maxDD `-0.993`
- `market_context_high->crypto_alt_1h` score `2.1611` n `67` status `ready` deltaP `11.9291` edge `0.1752` maxDD `-3.6376`
- `market_context_high->fx_4h` score `2.1605` n `55` status `ready` deltaP `25.8204` edge `0.035` maxDD `-0.1673`
- `news_risk_high->index_1h` score `2.1082` n `65` status `ready` deltaP `25.9166` edge `0.0179` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.5175` n `65` status `ready` deltaP `4.719` edge `0.1469` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
