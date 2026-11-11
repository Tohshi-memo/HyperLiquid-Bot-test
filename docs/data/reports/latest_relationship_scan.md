# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T15:07:27.770856+00:00`
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

- `market_context_high->unknown_4h` score `73.3782` n `88` status `ready` deltaP `8.1347` edge `6.1054` maxDD `-0.9161`
- `market_context_high->equity_24h` score `30.012` n `88` status `ready` deltaP `25.8364` edge `2.5679` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.7048` n `53` status `ready` deltaP `35.3255` edge `0.8521` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `9.3393` n `88` status `ready` deltaP `39.536` edge `1.4432` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.3859` n `88` status `ready` deltaP `25.9469` edge `0.3221` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.3393` n `88` status `ready` deltaP `31.2026` edge `0.2089` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.8397` n `53` status `ready` deltaP `20.1335` edge `0.3345` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6642` n `53` status `ready` deltaP `18.464` edge `0.2535` maxDD `-3.6997`
- `news_risk_high->metal_4h` score `3.6366` n `53` status `ready` deltaP `36.7925` edge `0.0954` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `2.8722` n `53` status `ready` deltaP `25.0345` edge `0.0978` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.3533` n `53` status `ready` deltaP `21.9656` edge `0.0933` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.9357` n `53` status `ready` deltaP `23.4497` edge `0.2557` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.7473` n `53` status `ready` deltaP `21.5484` edge `0.0274` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3748` n `53` status `ready` deltaP `17.7748` edge `0.0262` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7379` n `53` status `ready` deltaP `18.9413` edge `0.0735` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.7258` n `53` status `ready` deltaP `17.8934` edge `0.0717` maxDD `-6.1688`
- `market_context_high->metal_1h` score `-0.255` n `88` status `ready` deltaP `4.3958` edge `0.0171` maxDD `-1.4122`
- `market_context_high->crypto_major_24h` score `-0.2586` n `88` status `ready` deltaP `17.7399` edge `1.0227` maxDD `-80.6681`
- `news_risk_high->commodity_1h` score `-0.287` n `53` status `ready` deltaP `-3.5476` edge `0.0332` maxDD `-0.3438`
- `market_context_high->commodity_1h` score `-0.5243` n `88` status `ready` deltaP `1.1908` edge `-0.0069` maxDD `-1.7935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
