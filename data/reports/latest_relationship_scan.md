# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T22:07:35.277924+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4542`

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

- `news_risk_high->crypto_alt_4h` score `0.2261` n `146` status `ready` deltaP `5.7802` edge `0.2541` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4955` n `146` status `ready` deltaP `1.4334` edge `0.0497` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6132` n `146` status `ready` deltaP `-0.8756` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.889` n `126` status `ready` deltaP `12.5744` edge `0.1278` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.949` n `146` status `ready` deltaP `0.7485` edge `-0.0041` maxDD `-1.3981`
- `news_risk_high->crypto_alt_24h` score `-1.0174` n `126` status `ready` deltaP `18.9732` edge `0.6936` maxDD `-65.3749`
- `news_risk_high->fx_4h` score `-1.2688` n `146` status `ready` deltaP `-3.811` edge `-0.0121` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.307` n `146` status `ready` deltaP `-5.2477` edge `-0.0104` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.108` n `146` status `ready` deltaP `-3.5792` edge `-0.0163` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3109` n `146` status `ready` deltaP `-8.3279` edge `-0.0004` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.4022` n `126` status `ready` deltaP `-5.382` edge `0.0121` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.405` n `126` status `ready` deltaP `-18.7004` edge `-0.0128` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6275` n `146` status `ready` deltaP `-5.8875` edge `-0.03` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2391` n `146` status `ready` deltaP `-8.1556` edge `-0.043` maxDD `-9.4709`
- `news_risk_high->equity_24h` score `-3.4673` n `126` status `ready` deltaP `14.1121` edge `0.4709` maxDD `-67.0937`
- `news_risk_high->commodity_4h` score `-3.705` n `146` status `ready` deltaP `-11.103` edge `0.0007` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.7865` n `146` status `ready` deltaP `-6.5382` edge `-0.0348` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.8016` n `146` status `ready` deltaP `-13.1641` edge `-0.0771` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-10.2857` n `126` status `ready` deltaP `-17.0139` edge `-0.0627` maxDD `-43.1482`
- `news_risk_high->equity_4h` score `-11.4654` n `146` status `ready` deltaP `-1.5975` edge `-0.1087` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
