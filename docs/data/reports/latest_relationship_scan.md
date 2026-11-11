# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T17:07:24.136044+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11730`

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

- `market_context_high->unknown_4h` score `72.6287` n `88` status `ready` deltaP `8.592` edge `6.0399` maxDD `-0.9161`
- `market_context_high->equity_24h` score `27.8368` n `88` status `ready` deltaP `24.4476` edge `2.3959` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.3472` n `53` status `ready` deltaP `34.4109` edge `0.8284` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.6318` n `88` status `ready` deltaP `38.3207` edge `1.3606` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.0648` n `88` status `ready` deltaP `24.558` edge `0.3046` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.3897` n `88` status `ready` deltaP `31.2026` edge `0.2131` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `3.8086` n `53` status `ready` deltaP `38.012` edge `0.1016` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.5783` n `53` status `ready` deltaP `19.3713` edge `0.3178` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.4099` n `53` status `ready` deltaP `17.8652` edge `0.2363` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `2.5814` n `53` status `ready` deltaP `23.815` edge `0.0817` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.3011` n `53` status `ready` deltaP `21.5083` edge `0.092` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.8659` n `53` status `ready` deltaP `22.746` edge `0.0293` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.7071` n `53` status `ready` deltaP `22.3826` edge `0.2335` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3125` n `53` status `ready` deltaP `17.176` edge `0.025` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.688` n `53` status `ready` deltaP `18.4922` edge `0.0701` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.6774` n `53` status `ready` deltaP `17.4443` edge `0.0685` maxDD `-6.1688`
- `market_context_high->metal_1h` score `-0.1364` n `88` status `ready` deltaP `5.5934` edge `0.019` maxDD `-1.4122`
- `news_risk_high->commodity_1h` score `-0.3949` n `53` status `ready` deltaP `-3.847` edge `0.0262` maxDD `-0.3438`
- `market_context_high->fx_24h` score `-0.5632` n `88` status `ready` deltaP `13.7153` edge `0.0216` maxDD `-3.4642`
- `market_context_high->commodity_1h` score `-0.5944` n `88` status `ready` deltaP `0.8914` edge `-0.0139` maxDD `-1.7935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
