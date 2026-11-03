# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T09:22:28.747482+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4448`

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

- `news_risk_high->crypto_alt_4h` score `0.2906` n `146` status `ready` deltaP `6.3899` edge `0.2583` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4612` n `146` status `ready` deltaP `1.8825` edge `0.0511` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6381` n `146` status `ready` deltaP `-1.3247` edge `-0.0029` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9191` n `146` status `ready` deltaP `1.0479` edge `-0.0036` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2338` n `146` status `ready` deltaP `-4.1998` edge `-0.008` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.2713` n `146` status `ready` deltaP `-3.9634` edge `-0.0114` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-2.0269` n `146` status `ready` deltaP `-2.6646` edge `-0.012` maxDD `-4.0745`
- `news_risk_high->metal_24h` score `-2.1478` n `145` status `ready` deltaP `9.011` edge `0.1131` maxDD `-16.1727`
- `news_risk_high->index_24h` score `-2.2842` n `145` status `ready` deltaP `-4.0876` edge `0.0186` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.4118` n `145` status `ready` deltaP `-17.6916` edge `-0.0204` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4547` n `146` status `ready` deltaP `-9.6752` edge `-0.0034` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.7054` n `146` status `ready` deltaP `-6.9354` edge `-0.033` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2834` n `146` status `ready` deltaP `-8.6047` edge `-0.0437` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.0589` n `146` status `ready` deltaP `-13.8469` edge `-0.0105` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.6261` n `146` status `ready` deltaP `-5.9284` edge `-0.0255` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-6.5326` n `145` status `ready` deltaP `18.3621` edge `0.7126` maxDD `-116.8025`
- `news_risk_high->crypto_major_4h` score `-6.8874` n `146` status `ready` deltaP `-13.6214` edge `-0.0812` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-10.77` n `145` status `ready` deltaP `13.501` edge `0.4217` maxDD `-99.0698`
- `news_risk_high->equity_4h` score `-11.2938` n `146` status `ready` deltaP `-0.6828` edge `-0.1005` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.9902` n `145` status `ready` deltaP `-24.3678` edge `-0.0968` maxDD `-43.5281`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
