# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T08:22:25.879499+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4400`

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

- `news_risk_high->crypto_alt_4h` score `0.4403` n `146` status `ready` deltaP `9.1338` edge `0.2592` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4504` n `146` status `ready` deltaP `2.3316` edge `0.0495` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7168` n `146` status `ready` deltaP `-2.8217` edge `-0.003` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.822` n `146` status `ready` deltaP `1.9461` edge `-0.0015` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2931` n `146` status `ready` deltaP `-4.7986` edge `-0.0116` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.467` n `146` status `ready` deltaP `-7.622` edge `-0.0121` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.7375` n `146` status `ready` deltaP `10.2145` edge `0.1453` maxDD `-16.6552`
- `news_risk_high->index_24h` score `-1.7505` n `146` status `ready` deltaP `1.0298` edge `0.0529` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.7997` n `146` status `ready` deltaP `0.3842` edge `-0.0032` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.3485` n `146` status `ready` deltaP `-17.8534` edge `-0.0112` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.475` n `146` status `ready` deltaP `-10.1243` edge `-0.0021` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.5753` n `146` status `ready` deltaP `-5.4384` edge `-0.0263` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.0856` n `146` status `ready` deltaP `-7.2574` edge `-0.0362` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8908` n `146` status `ready` deltaP `-12.7799` edge `-0.0036` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.5418` n `146` status `ready` deltaP `-3.7943` edge `-0.0327` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.2761` n `146` status `ready` deltaP `-10.4202` edge `-0.0516` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-7.4272` n `146` status `ready` deltaP `18.8476` edge `0.6216` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-9.5606` n `146` status `ready` deltaP `16.417` edge `0.5442` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-10.8641` n `146` status `ready` deltaP `0.3842` edge `-0.0718` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.3351` n `146` status `ready` deltaP `-20.7834` edge `-0.0633` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
