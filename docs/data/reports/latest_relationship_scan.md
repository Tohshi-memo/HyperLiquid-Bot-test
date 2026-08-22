# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T22:22:24.802843+00:00`
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

- `market_context_high->unknown_1h` score `1.6345` n `142` status `ready` deltaP `6.0787` edge `0.1184` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.816` n `142` status `ready` deltaP `18.6319` edge `-0.0123` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1439` n `142` status `ready` deltaP `8.923` edge `0.0092` maxDD `-0.3527`
- `market_context_high->index_1h` score `-0.0261` n `142` status `ready` deltaP `6.7871` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1364` n `142` status `ready` deltaP `2.0853` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3105` n `142` status `ready` deltaP `5.1573` edge `0.0328` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.3535` n `142` status `ready` deltaP `7.3557` edge `-0.0169` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.5694` n `142` status `ready` deltaP `-0.0885` edge `-0.005` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.5831` n `142` status `ready` deltaP `2.6859` edge `0.0109` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.9343` n `142` status `ready` deltaP `-5.1528` edge `-0.0004` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.0719` n `142` status `ready` deltaP `-7.5188` edge `-0.0023` maxDD `-1.1328`
- `market_context_high->fx_24h` score `-1.1067` n `126` status `ready` deltaP `0.124` edge `0.0094` maxDD `-2.1693`
- `market_context_high->crypto_alt_1h` score `-1.5203` n `142` status `ready` deltaP `-2.0894` edge `-0.0315` maxDD `-7.9582`
- `market_context_high->equity_4h` score `-1.6999` n `142` status `ready` deltaP `-0.6312` edge `0.0679` maxDD `-16.1967`
- `market_context_high->crypto_alt_4h` score `-1.9511` n `142` status `ready` deltaP `4.9683` edge `-0.0489` maxDD `-7.0785`
- `market_context_high->commodity_24h` score `-2.1371` n `126` status `ready` deltaP `-6.1756` edge `0.0464` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-2.3355` n `142` status `ready` deltaP `-5.7771` edge `-0.1132` maxDD `-7.8171`
- `market_context_high->metal_24h` score `-5.3999` n `126` status `ready` deltaP `-23.7599` edge `-0.2031` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.5036` n `142` status `ready` deltaP `1.1637` edge `-0.3334` maxDD `-5.6395`
- `market_context_high->index_24h` score `-6.8811` n `126` status `ready` deltaP `-7.5149` edge `-0.0426` maxDD `-21.1244`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
