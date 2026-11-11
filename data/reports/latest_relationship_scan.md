# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T00:22:28.863856+00:00`
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

- `market_context_high->unknown_4h` score `80.5187` n `88` status `ready` deltaP `7.525` edge `6.7045` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.2316` n `88` status `ready` deltaP `33.6489` edge `2.9521` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `7.0661` n `88` status `ready` deltaP `30.6818` edge `1.2108` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1269` n `88` status `ready` deltaP `31.8497` edge `0.3445` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.308` n `36` status `ready` deltaP `17.1158` edge `0.2331` maxDD `-3.7228`
- `market_context_high->metal_24h` score `2.5223` n `88` status `ready` deltaP `25.9943` edge `0.0922` maxDD `-1.4245`
- `news_risk_high->index_1h` score `1.2705` n `36` status `ready` deltaP `17.1158` edge `0.0219` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.8298` n `36` status `ready` deltaP `20.7086` edge `0.0621` maxDD `-6.1688`
- `news_risk_high->metal_1h` score `0.7986` n `36` status `ready` deltaP `13.2901` edge `0.0034` maxDD `-0.3692`
- `news_risk_high->crypto_major_1h` score `0.4905` n `36` status `ready` deltaP `20.5589` edge `0.031` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.3147` n `36` status `ready` deltaP `-5.3227` edge `0.0416` maxDD `-0.2537`
- `market_context_high->metal_1h` score `-0.3437` n `88` status `ready` deltaP `3.9467` edge `0.0127` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3653` n `88` status `ready` deltaP `3.1369` edge `0.0005` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.6193` n `88` status `ready` deltaP `2.342` edge `0.0156` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.6585` n `88` status `ready` deltaP `3.3952` edge `-0.0093` maxDD `-2.4871`
- `news_risk_high->fx_1h` score `-0.7045` n `36` status `ready` deltaP `-3.676` edge `-0.0052` maxDD `-0.3199`
- `market_context_high->index_1h` score `-0.9924` n `88` status `ready` deltaP `-7.5054` edge `0.0059` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0798` n `88` status `ready` deltaP `-1.5105` edge `0.01` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2081` n `88` status `ready` deltaP `-12.2618` edge `-0.0047` maxDD `-0.8088`
- `market_context_high->fx_24h` score `-1.5513` n `88` status `ready` deltaP `5.7292` edge `-0.0075` maxDD `-3.4642`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
