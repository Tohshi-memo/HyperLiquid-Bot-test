# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T02:29:24.286243+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4812`

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

- `news_risk_high->crypto_alt_24h` score `0.0698` n `126` status `ready` deltaP `21.9246` edge `0.8133` maxDD `-65.3749`
- `news_risk_high->crypto_alt_4h` score `0.0094` n `146` status `ready` deltaP `4.1033` edge `0.2375` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.497` n `146` status `ready` deltaP `1.2837` edge `0.0505` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5712` n `146` status `ready` deltaP `-0.1271` edge `-0.0023` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8625` n `126` status `ready` deltaP `12.5744` edge `0.1312` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.961` n `146` status `ready` deltaP `0.5988` edge `-0.0041` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2301` n `146` status `ready` deltaP `-3.2012` edge `-0.0112` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.325` n `146` status `ready` deltaP `-5.5471` edge `-0.0107` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.1208` n `146` status `ready` deltaP `-3.8841` edge `-0.0159` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.1787` n `126` status `ready` deltaP `-3.125` edge `0.0257` maxDD `-7.402`
- `news_risk_high->equity_24h` score `-2.2819` n `126` status `ready` deltaP `17.0635` edge `0.6032` maxDD `-67.0937`
- `news_risk_high->commodity_1h` score `-2.3349` n `146` status `ready` deltaP `-8.4776` edge `-0.0014` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.5449` n `126` status `ready` deltaP `-20.6102` edge `-0.018` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6929` n `146` status `ready` deltaP `-6.7857` edge `-0.0324` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2523` n `146` status `ready` deltaP `-8.3053` edge `-0.0431` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8132` n `146` status `ready` deltaP `-12.1701` edge `-0.0012` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.9093` n `146` status `ready` deltaP `-7.7577` edge `-0.0369` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.1228` n `146` status `ready` deltaP `-14.6885` edge `-0.0937` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-9.026` n `126` status `ready` deltaP `-14.0625` edge `0.0226` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-11.3563` n `126` status `ready` deltaP `-25.62` edge `-0.0867` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
