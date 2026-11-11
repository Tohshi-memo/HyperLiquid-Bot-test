# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T05:52:27.718963+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11756`

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

- `market_context_high->unknown_4h` score `78.6226` n `88` status `ready` deltaP `7.525` edge `6.5465` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.4462` n `88` status `ready` deltaP `32.2601` edge `2.8946` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `12.4715` n `43` status `ready` deltaP `35.8941` edge `0.9122` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.2425` n `88` status `ready` deltaP `33.4596` edge `1.3431` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1857` n `88` status `ready` deltaP `31.8497` edge `0.3494` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.9578` n `47` status `ready` deltaP `20.544` edge `0.2641` maxDD `-3.6997`
- `market_context_high->metal_24h` score `3.7206` n `88` status `ready` deltaP `29.8137` edge `0.1666` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.358` n `43` status `ready` deltaP `21.3273` edge `0.2864` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.2204` n `43` status `ready` deltaP `25.0674` edge `0.1266` maxDD `-0.3611`
- `news_risk_high->metal_4h` score `3.2167` n `43` status `ready` deltaP `33.5685` edge `0.0819` maxDD `-1.0104`
- `news_risk_high->index_4h` score `2.8668` n `43` status `ready` deltaP `27.8892` edge `0.0966` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.4246` n `43` status `ready` deltaP `28.4564` edge `0.285` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.6177` n `47` status `ready` deltaP `20.8434` edge `0.0213` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4525` n `47` status `ready` deltaP `18.7158` edge `0.0264` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.2233` n `47` status `ready` deltaP `23.5062` edge `0.0939` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.8583` n `47` status `ready` deltaP `21.6779` edge `0.0707` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.1827` n `47` status `ready` deltaP `-3.9081` edge `0.0361` maxDD `-0.3438`
- `market_context_high->commodity_1h` score `-0.3903` n `88` status `ready` deltaP `2.8375` edge `-0.0007` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.4396` n `88` status `ready` deltaP `3.0485` edge `0.0107` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.6486` n `88` status `ready` deltaP `1.7323` edge `0.0159` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
