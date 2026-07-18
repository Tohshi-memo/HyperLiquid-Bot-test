# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T15:22:26.575945+00:00`
- Price records: `672`
- Market context records: `7153`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11762`

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

- `market_context_high->fx_4h` score `0.3395` n `153` status `ready` deltaP `12.7641` edge `0.0132` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.2034` n `161` status `ready` deltaP `3.8652` edge `0.0024` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.4859` n `161` status `ready` deltaP `-1.2153` edge `0.0318` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.5726` n `161` status `ready` deltaP `0.4156` edge `0.0277` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.5911` n `161` status `ready` deltaP `4.1646` edge `0.0375` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.7023` n `161` status `ready` deltaP `-1.7183` edge `-0.0165` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7435` n `161` status `ready` deltaP `1.3519` edge `-0.0045` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.5253` n `161` status `ready` deltaP `-6.2735` edge `-0.005` maxDD `-2.0897`
- `market_context_high->unknown_4h` score `-1.8581` n `153` status `ready` deltaP `-6.1712` edge `0.0141` maxDD `-5.8938`
- `market_context_high->commodity_4h` score `-2.0442` n `153` status `ready` deltaP `-4.3529` edge `-0.0378` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.9251` n `153` status `ready` deltaP `-10.2244` edge `-0.012` maxDD `-5.2551`
- `market_context_high->equity_1h` score `-3.4911` n `161` status `ready` deltaP `-0.0846` edge `-0.0411` maxDD `-15.2742`
- `market_context_high->index_4h` score `-3.9299` n `153` status `ready` deltaP `-2.0076` edge `-0.0442` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.5036` n `133` status `ready` deltaP `-13.4581` edge `-0.1547` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.9609` n `133` status `ready` deltaP `-15.7046` edge `-0.026` maxDD `-3.9503`
- `market_context_high->crypto_major_4h` score `-4.9887` n `153` status `ready` deltaP `1.9368` edge `0.0067` maxDD `-25.1605`
- `market_context_high->crypto_alt_4h` score `-5.5456` n `153` status `ready` deltaP `-3.4025` edge `-0.0329` maxDD `-24.5243`
- `market_context_high->unknown_24h` score `-10.1016` n `133` status `ready` deltaP `-32.7029` edge `-0.1091` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-14.6406` n `153` status `ready` deltaP `-4.2962` edge `-0.2244` maxDD `-66.0271`
- `market_context_high->metal_24h` score `-14.7164` n `133` status `ready` deltaP `-31.776` edge `-0.1964` maxDD `-40.7836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
