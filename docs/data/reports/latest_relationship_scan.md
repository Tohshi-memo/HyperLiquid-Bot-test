# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T15:37:28.056938+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11760`

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

- `market_context_high->unknown_4h` score `72.7062` n `88` status `ready` deltaP `8.1347` edge `6.0494` maxDD `-0.9161`
- `market_context_high->equity_24h` score `29.6002` n `88` status `ready` deltaP `25.4892` edge `2.5359` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.6168` n `53` status `ready` deltaP `35.0207` edge `0.8468` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `9.2889` n `88` status `ready` deltaP `39.3624` edge `1.4379` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.3209` n `88` status `ready` deltaP `25.5997` edge `0.319` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.3609` n `88` status `ready` deltaP `31.2026` edge `0.2107` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.871` n `53` status `ready` deltaP `20.2859` edge `0.3361` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `3.679` n `53` status `ready` deltaP `37.0974` edge `0.0969` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.5994` n `53` status `ready` deltaP `18.3143` edge `0.2491` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `2.7938` n `53` status `ready` deltaP `24.7297` edge `0.0933` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.3509` n `53` status `ready` deltaP `21.9656` edge `0.0931` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.9177` n `53` status `ready` deltaP `23.2972` edge `0.2544` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.7748` n `53` status `ready` deltaP `21.8478` edge `0.0277` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3593` n `53` status `ready` deltaP `17.6251` edge `0.0259` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7722` n `53` status `ready` deltaP `19.091` edge `0.0769` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.7601` n `53` status `ready` deltaP `18.0431` edge `0.0751` maxDD `-6.1688`
- `market_context_high->metal_1h` score `-0.2274` n `88` status `ready` deltaP `4.6952` edge `0.0174` maxDD `-1.4122`
- `news_risk_high->commodity_1h` score `-0.293` n `53` status `ready` deltaP `-3.5476` edge `0.0327` maxDD `-0.3438`
- `market_context_high->crypto_major_24h` score `-0.3289` n `88` status `ready` deltaP `17.5663` edge `1.018` maxDD `-80.6681`
- `market_context_high->commodity_1h` score `-0.5282` n `88` status `ready` deltaP `1.1908` edge `-0.0074` maxDD `-1.7935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
