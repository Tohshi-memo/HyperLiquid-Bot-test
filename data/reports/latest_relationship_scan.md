# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T06:22:32.373840+00:00`
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

- `market_context_high->unknown_4h` score `78.5566` n `88` status `ready` deltaP `7.525` edge `6.541` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.3321` n `88` status `ready` deltaP `31.9128` edge `2.8874` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `12.8211` n `45` status `ready` deltaP `36.5143` edge `0.9372` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.3549` n `88` status `ready` deltaP `33.8068` edge `1.3552` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1833` n `88` status `ready` deltaP `31.8497` edge `0.3492` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `4.0447` n `48` status `ready` deltaP `21.1203` edge `0.2675` maxDD `-3.6997`
- `market_context_high->metal_24h` score `3.8252` n `88` status `ready` deltaP `30.161` edge `0.173` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.7591` n `45` status `ready` deltaP `22.981` edge `0.3088` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `3.3742` n `45` status `ready` deltaP `34.292` edge `0.0902` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `3.2705` n `45` status `ready` deltaP `25.9485` edge `0.1249` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.9738` n `45` status `ready` deltaP `28.7161` edge `0.1` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.5163` n `45` status `ready` deltaP `29.8001` edge `0.2878` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.6914` n `48` status `ready` deltaP `21.4197` edge `0.0236` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5046` n `48` status `ready` deltaP `19.3363` edge `0.0266` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.1019` n `48` status `ready` deltaP `22.3428` edge `0.0861` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7978` n `48` status `ready` deltaP `20.4092` edge `0.0714` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.1779` n `48` status `ready` deltaP `-2.8443` edge `0.0376` maxDD `-0.3438`
- `market_context_high->commodity_1h` score `-0.3895` n `88` status `ready` deltaP `2.8375` edge `-0.0006` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.4192` n `88` status `ready` deltaP `3.0485` edge `0.0124` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.6535` n `88` status `ready` deltaP `1.5798` edge `0.0163` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
