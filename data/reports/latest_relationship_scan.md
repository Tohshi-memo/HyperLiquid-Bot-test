# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T21:37:21.074746+00:00`
- Price records: `672`
- Market context records: `2599`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `market_context_high->unknown_24h` score `7.788` n `136` status `ready` deltaP `17.9432` edge `0.5622` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.4359` n `146` status `ready` deltaP `25.3488` edge `0.5519` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.7082` n `146` status `ready` deltaP `15.6783` edge `0.3855` maxDD `-10.1468`
- `market_context_high->crypto_alt_24h` score `1.474` n `136` status `ready` deltaP `3.5948` edge `0.7367` maxDD `-39.0265`
- `market_context_high->crypto_alt_1h` score `1.4456` n `146` status `ready` deltaP `11.73` edge `0.161` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.9378` n `136` status `ready` deltaP `9.5282` edge `0.1127` maxDD `-2.5127`
- `market_context_high->unknown_4h` score `0.8779` n `146` status `ready` deltaP `7.6846` edge `0.1269` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.8276` n `146` status `ready` deltaP `9.3122` edge `0.1263` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.194` n `146` status `ready` deltaP `8.8227` edge `0.0415` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0988` n `146` status `ready` deltaP `4.3905` edge `0.0119` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.3217` n `146` status `ready` deltaP `2.3993` edge `0.0235` maxDD `-2.6375`
- `market_context_high->equity_24h` score `-0.3493` n `136` status `ready` deltaP `14.2361` edge `-0.057` maxDD `-2.3615`
- `market_context_high->commodity_1h` score `-0.4422` n `146` status `ready` deltaP `5.2026` edge `0.0163` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.5709` n `146` status `ready` deltaP `1.7103` edge `0.0158` maxDD `-2.9823`
- `market_context_high->metal_4h` score `-0.634` n `146` status `ready` deltaP `4.5021` edge `0.0559` maxDD `-4.7664`
- `market_context_high->fx_1h` score `-0.6521` n `146` status `ready` deltaP `-0.6849` edge `0.0037` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.7713` n `146` status `ready` deltaP `0.0718` edge `0.0191` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.9144` n `146` status `ready` deltaP `-0.378` edge `0.0121` maxDD `-0.8621`
- `market_context_high->fx_24h` score `-0.9553` n `136` status `ready` deltaP `3.0229` edge `-0.0004` maxDD `-1.6157`
- `market_context_high->commodity_4h` score `-1.1457` n `146` status `ready` deltaP `2.5768` edge `0.0302` maxDD `-10.2078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
