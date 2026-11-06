# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T03:07:28.494824+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4314`

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

- `news_risk_high->crypto_alt_4h` score `-0.2752` n `146` status `ready` deltaP `6.9254` edge `0.1822` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6376` n `146` status `ready` deltaP `2.631` edge `0.0235` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6965` n `146` status `ready` deltaP `-2.5223` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7345` n `146` status `ready` deltaP `2.6946` edge `0.0008` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.4514` n `146` status `ready` deltaP `-7.382` edge `-0.0117` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5376` n `146` status `ready` deltaP `-8.2417` edge `-0.02` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6833` n `146` status `ready` deltaP `0.9132` edge `0.0082` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.456` n `146` status `ready` deltaP `-12.1628` edge `0.0504` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.4637` n `146` status `ready` deltaP `-6.1869` edge `-0.007` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4869` n `146` status `ready` deltaP `-10.7231` edge `0.0009` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.7802` n `146` status `ready` deltaP `-23.6811` edge `-0.0277` maxDD `-2.336`
- `news_risk_high->crypto_major_1h` score `-2.9899` n `146` status `ready` deltaP `-5.7604` edge `-0.0382` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.9214` n `146` status `ready` deltaP `-14.9924` edge `0.0086` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.7532` n `146` status `ready` deltaP `-12.8615` edge `-0.0732` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-5.9585` n `146` status `ready` deltaP `-9.2847` edge `-0.0327` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-9.1688` n `146` status `ready` deltaP `-16.9763` edge `-0.2927` maxDD `-16.6552`
- `news_risk_high->equity_4h` score `-9.5773` n `146` status `ready` deltaP `1.9787` edge `0.0248` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-9.6203` n `146` status `ready` deltaP `-15.3174` edge `0.1265` maxDD `-43.7525`
- `news_risk_high->equity_24h` score `-10.6662` n `146` status `ready` deltaP `9.9778` edge `0.495` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-13.5181` n `146` status `ready` deltaP `5.3065` edge `-0.069` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
