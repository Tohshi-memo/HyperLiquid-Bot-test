# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T05:07:30.866794+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11742`

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

- `market_context_high->unknown_4h` score `78.9082` n `88` status `ready` deltaP `7.525` edge `6.5703` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.4858` n `88` status `ready` deltaP `32.2601` edge `2.8979` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `12.1202` n `40` status `ready` deltaP `34.8476` edge `0.8899` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.036` n `88` status `ready` deltaP `32.9387` edge `1.3201` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1737` n `88` status `ready` deltaP `31.8497` edge `0.3484` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.8774` n `47` status `ready` deltaP `20.544` edge `0.2574` maxDD `-3.6997`
- `market_context_high->metal_24h` score `3.5482` n `88` status `ready` deltaP `29.2929` edge `0.1557` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.1917` n `40` status `ready` deltaP `20.8841` edge `0.2755` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `2.9474` n `40` status `ready` deltaP `32.3476` edge `0.0676` maxDD `-1.0104`
- `news_risk_high->index_4h` score `2.6904` n `40` status `ready` deltaP `26.4939` edge `0.0912` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.5641` n `40` status `ready` deltaP `30.8841` edge `0.2867` maxDD `-10.1088`
- `news_risk_high->commodity_4h` score `2.0314` n `40` status `ready` deltaP `23.3232` edge `0.1303` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `1.6093` n `47` status `ready` deltaP `20.8434` edge `0.0206` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4369` n `47` status `ready` deltaP `18.7158` edge `0.0251` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.1578` n `47` status `ready` deltaP `23.2068` edge `0.0875` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.8225` n `47` status `ready` deltaP `21.5282` edge `0.0671` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.2099` n `47` status `ready` deltaP `-4.2075` edge `0.0346` maxDD `-0.3438`
- `market_context_high->commodity_1h` score `-0.4175` n `88` status `ready` deltaP `2.5381` edge `-0.0022` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.448` n `88` status `ready` deltaP `3.0485` edge `0.01` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.6572` n `88` status `ready` deltaP `1.7323` edge `0.0148` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
