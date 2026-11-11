# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T06:07:26.444055+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11724`

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

- `market_context_high->unknown_4h` score `78.5998` n `88` status `ready` deltaP `7.525` edge `6.5446` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.3976` n `88` status `ready` deltaP `32.0864` edge `2.8917` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `12.6553` n `44` status `ready` deltaP `36.2112` edge `0.9254` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.3007` n `88` status `ready` deltaP `33.6332` edge `1.3494` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1857` n `88` status `ready` deltaP `31.8497` edge `0.3494` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.9806` n `47` status `ready` deltaP `20.544` edge `0.266` maxDD `-3.6997`
- `market_context_high->metal_24h` score `3.7741` n `88` status `ready` deltaP `29.9874` edge `0.1699` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.5444` n `44` status `ready` deltaP `22.173` edge `0.2963` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `3.2883` n `44` status `ready` deltaP `33.9385` edge `0.0854` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `3.2579` n `44` status `ready` deltaP `25.5959` edge `0.1262` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.9222` n `44` status `ready` deltaP `28.3121` edge `0.0984` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.4721` n `44` status `ready` deltaP `29.1435` edge `0.2865` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.6273` n `47` status `ready` deltaP `20.8434` edge `0.0221` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4573` n `47` status `ready` deltaP `18.7158` edge `0.0268` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.2498` n `47` status `ready` deltaP `23.6559` edge `0.0963` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.8685` n `47` status `ready` deltaP `21.6779` edge `0.072` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.1811` n `47` status `ready` deltaP `-3.9081` edge `0.0363` maxDD `-0.3438`
- `market_context_high->commodity_1h` score `-0.3887` n `88` status `ready` deltaP `2.8375` edge `-0.0005` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.43` n `88` status `ready` deltaP `3.0485` edge `0.0115` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.6447` n `88` status `ready` deltaP `1.7323` edge `0.0164` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
