# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T01:07:32.378051+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11041`

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

- `market_context_high->unknown_1h` score `83.858` n `47` status `ready` deltaP `9.3675` edge `6.9328` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.4377` n `47` status `ready` deltaP `30.4226` edge `3.7896` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.2004` n `47` status `ready` deltaP `24.782` edge `2.4728` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.8874` n `47` status `ready` deltaP `34.7628` edge `1.9611` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `10.1735` n `114` status `ready` deltaP `-0.4123` edge `0.8728` maxDD `-0.7809`
- `market_context_high->index_24h` score `8.2055` n `47` status `ready` deltaP `38.4087` edge `0.4407` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.4555` n `47` status `ready` deltaP `37.4889` edge `0.1452` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.3599` n `65` status `ready` deltaP `31.3221` edge `0.106` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.9523` n `47` status `ready` deltaP `33.8739` edge `0.0356` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.7261` n `114` status `ready` deltaP `14.7022` edge `0.1801` maxDD `-1.7416`
- `market_context_high->equity_4h` score `2.4443` n `47` status `ready` deltaP `17.1445` edge `0.1312` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `1.9232` n `114` status `ready` deltaP `15.343` edge `0.1139` maxDD `-2.4737`
- `news_risk_high->metal_1h` score `1.2235` n `114` status `ready` deltaP `16.601` edge `0.0198` maxDD `-0.6142`
- `market_context_high->index_1h` score `0.92` n `47` status `ready` deltaP `14.161` edge `0.0101` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8587` n `47` status `ready` deltaP `10.8676` edge `0.0394` maxDD `-1.5564`
- `news_risk_high->fx_4h` score `0.5894` n `102` status `ready` deltaP `13.3071` edge `0.024` maxDD `-0.421`
- `market_context_high->crypto_alt_4h` score `0.3545` n `47` status `ready` deltaP `7.0965` edge `0.049` maxDD `-3.3417`
- `market_context_high->fx_1h` score `0.2422` n `47` status `ready` deltaP `7.5646` edge `0.0054` maxDD `-0.1854`
- `news_risk_high->equity_1h` score `0.1295` n `114` status `ready` deltaP `4.5593` edge `0.0384` maxDD `-2.6402`
- `market_context_high->metal_1h` score `-0.0419` n `47` status `ready` deltaP `2.3793` edge `0.0104` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
