# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T18:22:32.318799+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4030`

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

- `news_risk_high->crypto_alt_4h` score `0.0023` n `146` status `ready` deltaP `7.7619` edge `0.2122` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5198` n `146` status `ready` deltaP `2.4813` edge `0.0396` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6249` n `146` status `ready` deltaP `-1.175` edge `-0.0022` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8556` n `146` status `ready` deltaP `1.6467` edge `-0.0023` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.422` n `146` status `ready` deltaP `-7.0122` edge `-0.0104` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.4293` n `146` status `ready` deltaP `-6.8944` edge `-0.0151` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.8632` n `146` status `ready` deltaP `0.0793` edge `-0.0093` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1705` n `146` status `ready` deltaP `-8.0285` edge `0.0093` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.1768` n `146` status `ready` deltaP `-4.7234` edge `0.0366` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.446` n `146` status `ready` deltaP `-18.6638` edge `-0.0183` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6079` n `146` status `ready` deltaP `-6.636` edge `-0.0225` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.3232` n `146` status `ready` deltaP `-7.5568` edge `-0.054` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.3364` n `146` status `ready` deltaP `-10.036` edge `0.0243` maxDD `-9.5011`
- `news_risk_high->metal_24h` score `-3.4928` n `146` status `ready` deltaP `3.4389` edge `0.0442` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-4.8439` n `146` status `ready` deltaP `-5.4711` edge `-0.0467` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.2621` n `146` status `ready` deltaP `-11.9446` edge `-0.1236` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-9.0827` n `146` status `ready` deltaP `14.8221` edge `0.4362` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-10.9399` n `146` status `ready` deltaP `0.2318` edge `-0.0771` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.4187` n `146` status `ready` deltaP `11.8809` edge `0.4196` maxDD `-102.3626`
- `news_risk_high->commodity_24h` score `-12.1505` n `146` status `ready` deltaP `-20.6807` edge `-0.0486` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
