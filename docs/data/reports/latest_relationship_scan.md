# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T03:52:27.523087+00:00`
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

- `news_risk_high->crypto_alt_24h` score `0.6013` n `126` status `ready` deltaP `22.9663` edge `0.8745` maxDD `-65.3749`
- `news_risk_high->crypto_alt_4h` score `0.1012` n `146` status `ready` deltaP `4.7131` edge `0.2452` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4526` n `146` status `ready` deltaP `1.7328` edge `0.0532` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5704` n `146` status `ready` deltaP `-0.1271` edge `-0.0022` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.819` n `126` status `ready` deltaP `13.0953` edge `0.1333` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9454` n `146` status `ready` deltaP `0.7485` edge `-0.0038` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2262` n `146` status `ready` deltaP `-3.2012` edge `-0.0107` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2915` n `146` status `ready` deltaP `-5.098` edge `-0.0094` maxDD `-3.1082`
- `news_risk_high->equity_24h` score `-1.7254` n `126` status `ready` deltaP `18.1051` edge `0.6676` maxDD `-67.0937`
- `news_risk_high->index_24h` score `-2.0676` n `126` status `ready` deltaP `-2.0834` edge `0.033` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.1579` n `146` status `ready` deltaP `-4.4938` edge `-0.0166` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3744` n `146` status `ready` deltaP `-8.9267` edge `-0.0017` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.5018` n `126` status `ready` deltaP `-19.9157` edge `-0.0171` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.7093` n `146` status `ready` deltaP `-6.9354` edge `-0.0335` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1923` n `146` status `ready` deltaP `-7.8562` edge `-0.0411` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8012` n `146` status `ready` deltaP `-12.1701` edge `-0.0002` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.9165` n `146` status `ready` deltaP `-7.7577` edge `-0.0375` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.1276` n `146` status `ready` deltaP `-14.6885` edge `-0.0941` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-8.4015` n `126` status `ready` deltaP `-13.0208` edge `0.0677` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-11.1796` n `126` status `ready` deltaP `-24.9256` edge `-0.0766` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
