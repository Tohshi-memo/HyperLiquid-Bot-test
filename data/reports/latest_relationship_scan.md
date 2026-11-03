# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T09:07:28.991808+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.2867` n `146` status `ready` deltaP `6.3899` edge `0.2578` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4394` n `146` status `ready` deltaP `2.0322` edge `0.0529` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6381` n `146` status `ready` deltaP `-1.3247` edge `-0.0029` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9047` n `146` status `ready` deltaP `1.1976` edge `-0.0034` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2354` n `146` status `ready` deltaP `-4.1998` edge `-0.0082` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.2713` n `146` status `ready` deltaP `-3.9634` edge `-0.0114` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-2.0269` n `146` status `ready` deltaP `-2.6646` edge `-0.012` maxDD `-4.0745`
- `news_risk_high->metal_24h` score `-2.0389` n `144` status `ready` deltaP `9.2014` edge `0.1143` maxDD `-15.6442`
- `news_risk_high->index_24h` score `-2.2769` n `144` status `ready` deltaP `-3.993` edge `0.0189` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.4021` n `144` status `ready` deltaP `-17.5347` edge `-0.0202` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4391` n `146` status `ready` deltaP `-9.5255` edge `-0.0031` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6898` n `146` status `ready` deltaP `-6.7857` edge `-0.032` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2582` n `146` status `ready` deltaP `-8.455` edge `-0.0426` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.0335` n `146` status `ready` deltaP `-13.6945` edge `-0.0094` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.6479` n `146` status `ready` deltaP `-6.0809` edge `-0.0263` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-6.2631` n `144` status `ready` deltaP `18.5764` edge `0.7163` maxDD `-114.7819`
- `news_risk_high->crypto_major_4h` score `-6.8994` n `146` status `ready` deltaP `-13.6214` edge `-0.0822` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-10.0837` n `144` status `ready` deltaP `13.7153` edge `0.4303` maxDD `-95.2969`
- `news_risk_high->equity_4h` score `-11.2962` n `146` status `ready` deltaP `-0.6828` edge `-0.1007` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.9538` n `144` status `ready` deltaP `-24.3055` edge `-0.0972` maxDD `-43.2863`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
