# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T15:22:26.527753+00:00`
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

- `market_context_high->unknown_24h` score `371.5044` n `75` status `ready` deltaP `4.7986` edge `30.9408` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `32.6438` n `53` status `ready` deltaP `31.2369` edge `2.5827` maxDD `-3.6503`
- `market_context_high->equity_24h` score `24.4101` n `75` status `ready` deltaP `25.7777` edge `2.0165` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `18.0063` n `75` status `ready` deltaP `50.5348` edge `1.4151` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.2165` n `53` status `ready` deltaP `42.0434` edge `1.7389` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.1711` n `53` status `ready` deltaP `33.4963` edge `0.7373` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.5889` n `53` status `ready` deltaP `36.1111` edge `0.225` maxDD `0.0`
- `market_context_high->index_24h` score `4.7159` n `75` status `ready` deltaP `25.0417` edge `0.2352` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.6058` n `53` status `ready` deltaP `43.9571` edge `0.1284` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.035` n `53` status `ready` deltaP `23.0542` edge `0.2129` maxDD `-0.4279`
- `market_context_high->metal_24h` score `3.8374` n `75` status `ready` deltaP `38.2084` edge `0.3264` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.3959` n `53` status `ready` deltaP `17.4161` edge `0.2299` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9253` n `53` status `ready` deltaP `27.1687` edge `0.088` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.8475` n `53` status `ready` deltaP `18.4567` edge `0.263` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `2.4983` n `53` status `ready` deltaP `17.3775` edge `0.655` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.1199` n `53` status `ready` deltaP `24.9915` edge `0.0355` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9026` n `53` status `ready` deltaP `19.5266` edge `0.072` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.7121` n `53` status `ready` deltaP `25.5838` edge `0.2128` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2119` n `53` status `ready` deltaP `16.4275` edge `0.0216` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6018` n `53` status `ready` deltaP `16.8455` edge `0.0628` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
