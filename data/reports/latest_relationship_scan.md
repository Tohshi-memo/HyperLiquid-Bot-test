# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T02:07:28.323604+00:00`
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

- `market_context_high->unknown_4h` score `80.8882` n `88` status `ready` deltaP `7.525` edge `6.7353` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.743` n `88` status `ready` deltaP `32.9545` edge `2.9147` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `8.6472` n `31` status `ready` deltaP `30.6452` edge `0.6285` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `7.3535` n `88` status `ready` deltaP `31.7235` edge `1.2407` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1281` n `88` status `ready` deltaP `31.8497` edge `0.3446` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.8135` n `40` status `ready` deltaP `19.4012` edge `0.2597` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `3.0479` n `31` status `ready` deltaP `19.5957` edge `0.1487` maxDD `-0.3611`
- `market_context_high->metal_24h` score `2.8763` n `88` status `ready` deltaP `27.2096` edge `0.1136` maxDD `-1.4245`
- `news_risk_high->index_1h` score `1.487` n `40` status `ready` deltaP `19.4012` edge `0.0247` maxDD `-0.4103`
- `news_risk_high->crypto_alt_4h` score `1.3548` n `31` status `ready` deltaP `25.9736` edge `0.1644` maxDD `-10.1088`
- `news_risk_high->crypto_major_4h` score `1.3397` n `31` status `ready` deltaP `15.9913` edge `0.2139` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `1.2591` n `40` status `ready` deltaP `16.7515` edge `0.0187` maxDD `-0.3692`
- `news_risk_high->metal_4h` score `1.1853` n `31` status `ready` deltaP `27.4194` edge `0.0068` maxDD `-1.0104`
- `news_risk_high->index_4h` score `1.1661` n `31` status `ready` deltaP `20.8398` edge `0.0542` maxDD `-0.8235`
- `news_risk_high->crypto_alt_1h` score `1.0406` n `40` status `ready` deltaP `23.2934` edge `0.0719` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7544` n `40` status `ready` deltaP `23.2934` edge `0.0466` maxDD `-7.0808`
- `market_context_high->metal_1h` score `-0.3653` n `88` status `ready` deltaP `3.797` edge `0.0119` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.377` n `88` status `ready` deltaP `2.9872` edge `0.0` maxDD `-1.7935`
- `news_risk_high->commodity_1h` score `-0.3881` n `40` status `ready` deltaP `-7.6946` edge `0.035` maxDD `-0.3438`
- `market_context_high->commodity_4h` score `-0.6624` n `88` status `ready` deltaP `2.0371` edge `0.0121` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
