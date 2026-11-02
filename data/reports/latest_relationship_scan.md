# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T12:52:30.430191+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.1478` n `143` status `ready` deltaP `5.845` edge `0.2306` maxDD `-13.0493`
- `news_risk_high->fx_1h` score `-0.5424` n `146` status `ready` deltaP `0.4717` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->crypto_alt_1h` score `-0.5501` n `146` status `ready` deltaP `1.134` edge `0.0447` maxDD `-5.8225`
- `news_risk_high->crypto_alt_24h` score `-0.7348` n `121` status `ready` deltaP `16.4213` edge `0.5853` maxDD `-54.1189`
- `news_risk_high->metal_24h` score `-0.843` n `121` status `ready` deltaP `12.9348` edge `0.1313` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0844` n `146` status `ready` deltaP `-0.5988` edge `-0.0064` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.1405` n `143` status `ready` deltaP `-1.4796` edge `-0.0112` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2806` n `146` status `ready` deltaP `-4.9483` edge `-0.009` maxDD `-3.1082`
- `news_risk_high->fx_24h` score `-2.0962` n `121` status `ready` deltaP `-14.4413` edge `-0.0016` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2297` n `143` status `ready` deltaP `-4.6446` edge `-0.0248` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3769` n `146` status `ready` deltaP `-8.4776` edge `-0.0049` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.7738` n `121` status `ready` deltaP `-8.7193` edge `-0.0133` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.9183` n `146` status `ready` deltaP `-7.5342` edge `-0.0563` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.3446` n `146` status `ready` deltaP `-8.7544` edge `-0.0478` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.0463` n `143` status `ready` deltaP `-12.8646` edge `-0.016` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.5732` n `143` status `ready` deltaP `-4.7416` edge `-0.029` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-5.3717` n `121` status `ready` deltaP `7.428` edge `0.2713` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.2532` n `143` status `ready` deltaP `-14.4881` edge `-0.1059` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-8.3082` n `143` status `ready` deltaP `-3.488` edge `-0.2058` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-11.6687` n `121` status `ready` deltaP `-26.0618` edge `-0.1525` maxDD `-29.3582`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
