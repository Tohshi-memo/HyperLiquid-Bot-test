# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T01:37:33.948610+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11740`

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

- `market_context_high->unknown_4h` score `80.9194` n `88` status `ready` deltaP `7.525` edge `6.7379` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.8248` n `88` status `ready` deltaP `33.3017` edge `2.9192` maxDD `-16.7984`
- `market_context_high->crypto_alt_24h` score `7.2473` n `88` status `ready` deltaP `31.3762` edge `1.2294` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1257` n `88` status `ready` deltaP `31.8497` edge `0.3444` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.5228` n `38` status `ready` deltaP `18.1217` edge `0.244` maxDD `-3.6997`
- `market_context_high->metal_24h` score `2.7729` n `88` status `ready` deltaP `26.8624` edge `0.1073` maxDD `-1.4245`
- `news_risk_high->index_1h` score `1.3702` n `38` status `ready` deltaP `18.1217` edge `0.0235` maxDD `-0.4103`
- `news_risk_high->metal_1h` score `0.9987` n `38` status `ready` deltaP `15.041` edge `0.0084` maxDD `-0.3692`
- `news_risk_high->crypto_alt_1h` score `0.9546` n `38` status `ready` deltaP `22.0139` edge `0.0694` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6075` n `38` status `ready` deltaP `22.0139` edge `0.0363` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.236` n `38` status `ready` deltaP `-5.3262` edge `0.0381` maxDD `-0.2948`
- `market_context_high->metal_1h` score `-0.3641` n `88` status `ready` deltaP `3.797` edge `0.012` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3739` n `88` status `ready` deltaP `2.9872` edge `0.0004` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.6451` n `88` status `ready` deltaP `2.1896` edge `0.0133` maxDD `-4.182`
- `news_risk_high->fx_1h` score `-0.6819` n `38` status `ready` deltaP `-3.2304` edge `-0.0061` maxDD `-0.3348`
- `market_context_high->index_4h` score `-0.741` n `88` status `ready` deltaP `2.633` edge `-0.0148` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0493` n `88` status `ready` deltaP `-8.2539` edge `0.0036` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.1317` n `88` status `ready` deltaP `-2.1203` edge `0.0074` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.1902` n `88` status `ready` deltaP `-11.9624` edge `-0.0044` maxDD `-0.8088`
- `market_context_high->fx_24h` score `-1.4555` n `88` status `ready` deltaP `6.5972` edge `-0.0053` maxDD `-3.4642`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
