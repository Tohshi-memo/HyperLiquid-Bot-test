# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T13:22:28.583124+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4861`

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

- `news_risk_high->crypto_alt_4h` score `-0.0403` n `145` status `ready` deltaP `5.1871` edge `0.2239` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5493` n `146` status `ready` deltaP `1.134` edge `0.0448` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5587` n `146` status `ready` deltaP `0.1723` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8932` n `123` status `ready` deltaP `11.9538` edge `0.1314` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0724` n `146` status `ready` deltaP `-0.4491` edge `-0.0064` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.1321` n `145` status `ready` deltaP `-1.332` edge `-0.0111` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2829` n `146` status `ready` deltaP `-4.9483` edge `-0.0093` maxDD `-3.1082`
- `news_risk_high->crypto_alt_24h` score `-1.5863` n `123` status `ready` deltaP `15.5065` edge `0.5531` maxDD `-59.1213`
- `news_risk_high->fx_24h` score `-2.0439` n `123` status `ready` deltaP `-13.9016` edge `0.0015` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2477` n `145` status `ready` deltaP `-5.0053` edge `-0.0247` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3781` n `146` status `ready` deltaP `-8.4776` edge `-0.005` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.6906` n `123` status `ready` deltaP `-7.7787` edge `-0.0089` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.9183` n `146` status `ready` deltaP `-7.5342` edge `-0.0563` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.3482` n `146` status `ready` deltaP `-8.7544` edge `-0.0481` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.9471` n `145` status `ready` deltaP `-11.9386` edge `-0.0139` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.6042` n `145` status `ready` deltaP `-5.1293` edge `-0.029` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-5.2732` n `123` status `ready` deltaP `8.0327` edge `0.2799` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.3403` n `145` status `ready` deltaP `-14.8276` edge `-0.1109` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-11.8667` n `123` status `ready` deltaP `-26.2365` edge `-0.1554` maxDD `-30.353`
- `news_risk_high->crypto_major_24h` score `-12.0497` n `123` status `ready` deltaP `-22.2391` edge `-0.1913` maxDD `-41.8332`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
