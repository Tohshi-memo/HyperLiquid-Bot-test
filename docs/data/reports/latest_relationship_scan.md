# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T12:37:24.660214+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11488`

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

- `market_context_high->unknown_4h` score `76.3038` n `88` status `ready` deltaP `8.1347` edge `6.3492` maxDD `-0.9161`
- `market_context_high->equity_24h` score `31.4708` n `88` status `ready` deltaP `27.5726` edge `2.6779` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.9936` n `52` status `ready` deltaP `36.1749` edge `0.8705` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `9.175` n `88` status `ready` deltaP `38.1471` edge `1.4314` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.646` n `88` status `ready` deltaP `27.683` edge `0.3322` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.2349` n `88` status `ready` deltaP `31.2026` edge `0.2002` maxDD `-1.4245`
- `news_risk_high->equity_1h` score `3.5886` n `53` status `ready` deltaP `18.0149` edge `0.2502` maxDD `-3.6997`
- `news_risk_high->metal_4h` score `3.489` n `52` status `ready` deltaP `35.4714` edge `0.0919` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.2151` n `52` status `ready` deltaP `18.7617` edge `0.2916` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.1931` n `52` status `ready` deltaP `26.196` edge `0.1168` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.3278` n `52` status `ready` deltaP `21.6463` edge `0.0933` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.697` n `53` status `ready` deltaP `21.0993` edge `0.0262` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.6417` n `52` status `ready` deltaP `22.7603` edge `0.2226` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3161` n `53` status `ready` deltaP `17.176` edge `0.0253` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6813` n `53` status `ready` deltaP `18.3425` edge `0.063` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6388` n `53` status `ready` deltaP `18.9413` edge `0.0608` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.1791` n `53` status `ready` deltaP `-2.6494` edge `0.0362` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.3053` n `88` status `ready` deltaP `3.9467` edge `0.0159` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4542` n `88` status `ready` deltaP `2.089` edge `-0.0039` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.7124` n `88` status `ready` deltaP `2.3281` edge `-0.0091` maxDD `-2.4871`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
