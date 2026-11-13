# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T19:22:34.795471+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10554`

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

- `market_context_high->unknown_24h` score `370.3208` n `75` status `ready` deltaP `2.8889` edge `30.8549` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `34.0086` n `53` status `ready` deltaP `33.1467` edge `2.6837` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.7749` n `75` status `ready` deltaP `27.6875` edge `2.1175` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `17.233` n `75` status `ready` deltaP `48.2778` edge `1.3657` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.4357` n `53` status `ready` deltaP `42.0434` edge `1.767` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.985` n `53` status `ready` deltaP `34.7158` edge `0.797` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.7305` n `53` status `ready` deltaP `37.3264` edge `0.2287` maxDD `0.0`
- `market_context_high->index_24h` score `4.9291` n `75` status `ready` deltaP `26.4306` edge `0.2437` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.8168` n `53` status `ready` deltaP `45.634` edge `0.1348` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.2481` n `53` status `ready` deltaP `24.4431` edge `0.2214` maxDD `-0.4279`
- `market_context_high->metal_24h` score `3.9972` n `75` status `ready` deltaP `40.2917` edge `0.333` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.3647` n `53` status `ready` deltaP `17.2664` edge `0.2283` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.2525` n `53` status `ready` deltaP `29.6077` edge `0.099` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.1947` n `53` status `ready` deltaP `19.6762` edge `0.2838` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2242` n `53` status `ready` deltaP `26.0394` edge `0.0372` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.02` n `53` status `ready` deltaP `20.2888` edge `0.0767` maxDD `-0.8235`
- `news_risk_high->crypto_alt_24h` score `1.9956` n `53` status `ready` deltaP `15.1205` edge `0.6056` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `1.8085` n `53` status `ready` deltaP `26.1936` edge `0.2211` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1855` n `53` status `ready` deltaP `16.1281` edge `0.0214` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.5894` n `53` status `ready` deltaP `16.6958` edge `0.0622` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
