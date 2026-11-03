# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T01:52:27.376400+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4836`

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

- `news_risk_high->crypto_alt_4h` score `0.0001` n `146` status `ready` deltaP `4.1033` edge `0.2363` maxDD `-14.0916`
- `news_risk_high->crypto_alt_24h` score `-0.0887` n `126` status `ready` deltaP `21.5774` edge `0.7953` maxDD `-65.3749`
- `news_risk_high->crypto_alt_1h` score `-0.4963` n `146` status `ready` deltaP `1.2837` edge `0.0506` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5883` n `146` status `ready` deltaP `-0.4265` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8664` n `126` status `ready` deltaP `12.5744` edge `0.1307` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9598` n `146` status `ready` deltaP `0.5988` edge `-0.004` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2403` n `146` status `ready` deltaP `-3.3537` edge `-0.0115` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.325` n `146` status `ready` deltaP `-5.5471` edge `-0.0107` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.1026` n `146` status `ready` deltaP `-3.5792` edge `-0.0156` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.2124` n `126` status `ready` deltaP `-3.4723` edge `0.0237` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.348` n `146` status `ready` deltaP `-8.6273` edge `-0.0015` maxDD `-3.2657`
- `news_risk_high->equity_24h` score `-2.4341` n `126` status `ready` deltaP `16.7163` edge `0.586` maxDD `-67.0937`
- `news_risk_high->fx_24h` score `-2.5457` n `126` status `ready` deltaP `-20.6102` edge `-0.0181` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6688` n `146` status `ready` deltaP `-6.4863` edge `-0.0313` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2499` n `146` status `ready` deltaP `-8.3053` edge `-0.0429` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8132` n `146` status `ready` deltaP `-12.1701` edge `-0.0012` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.9057` n `146` status `ready` deltaP `-7.7577` edge `-0.0366` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.1132` n `146` status `ready` deltaP `-14.6885` edge `-0.0929` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-9.205` n `126` status `ready` deltaP `-14.4097` edge `0.01` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-11.4345` n `126` status `ready` deltaP `-25.9672` edge `-0.0909` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
