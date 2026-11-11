# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T03:07:28.213244+00:00`
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

- `market_context_high->unknown_4h` score `80.6218` n `88` status `ready` deltaP `7.525` edge `6.7131` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.6185` n `88` status `ready` deltaP `32.4337` edge `2.9078` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `10.3395` n `35` status `ready` deltaP `32.7047` edge `0.7558` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `7.5514` n `88` status `ready` deltaP `32.2443` edge `1.2626` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1365` n `88` status `ready` deltaP `31.8497` edge `0.3453` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.6688` n `44` status `ready` deltaP `19.4066` edge `0.2476` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `3.1507` n `35` status `ready` deltaP `22.4564` edge `0.1382` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.0806` n `88` status `ready` deltaP `27.904` edge `0.126` maxDD `-1.4245`
- `news_risk_high->index_4h` score `2.2266` n `35` status `ready` deltaP `23.6368` edge `0.0716` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8037` n `35` status `ready` deltaP `26.9555` edge `0.2154` maxDD `-10.1088`
- `news_risk_high->crypto_major_4h` score `1.5247` n `35` status `ready` deltaP `18.0793` edge `0.2237` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `1.5019` n `35` status `ready` deltaP `29.8476` edge `0.0312` maxDD `-1.0104`
- `news_risk_high->metal_1h` score `1.4644` n `44` status `ready` deltaP `19.2569` edge `0.0191` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2995` n `44` status `ready` deltaP `17.2836` edge `0.0232` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.8665` n `44` status `ready` deltaP `21.3255` edge `0.0627` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.4824` n `44` status `ready` deltaP `19.2025` edge `0.039` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.1429` n `44` status `ready` deltaP `-3.2934` edge `0.0371` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.4156` n `88` status `ready` deltaP `3.3479` edge `0.0107` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4253` n `88` status `ready` deltaP `2.3884` edge `-0.0022` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.6901` n `88` status `ready` deltaP `1.5798` edge `0.0116` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
