# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T11:22:35.938880+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4288`

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

- `news_risk_high->crypto_alt_4h` score `0.2992` n `146` status `ready` deltaP `6.3899` edge `0.2594` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4963` n `146` status `ready` deltaP `1.4334` edge `0.0496` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6381` n `146` status `ready` deltaP `-1.3247` edge `-0.0029` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9143` n `146` status `ready` deltaP `1.0479` edge `-0.0032` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2331` n `146` status `ready` deltaP `-4.1998` edge `-0.0079` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.2839` n `146` status `ready` deltaP `-4.1159` edge `-0.012` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-2.0261` n `146` status `ready` deltaP `-2.6646` edge `-0.0119` maxDD `-4.0745`
- `news_risk_high->metal_24h` score `-2.043` n `146` status `ready` deltaP `10.0409` edge `0.121` maxDD `-16.6552`
- `news_risk_high->index_24h` score `-2.1641` n `146` status `ready` deltaP `-2.9632` edge `0.0265` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.3779` n `146` status `ready` deltaP `-17.159` edge `-0.0196` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.481` n `146` status `ready` deltaP `-9.8249` edge `-0.0046` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.7108` n `146` status `ready` deltaP `-7.0851` edge `-0.0327` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.3181` n `146` status `ready` deltaP `-9.0538` edge `-0.0436` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.2273` n `146` status `ready` deltaP `-15.0664` edge `-0.0164` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.4614` n `146` status `ready` deltaP `-4.7089` edge `-0.0199` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-6.3144` n `146` status `ready` deltaP `19.3684` edge `0.7608` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.8466` n `146` status `ready` deltaP `-13.6214` edge `-0.0778` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-10.3291` n `146` status `ready` deltaP `14.5073` edge `0.4977` maxDD `-102.7472`
- `news_risk_high->equity_4h` score `-11.2878` n `146` status `ready` deltaP `-0.6828` edge `-0.1` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.9319` n `146` status `ready` deltaP `-23.9084` edge `-0.0922` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
