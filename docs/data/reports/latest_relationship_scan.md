# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T07:52:32.483333+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3930`

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

- `news_risk_high->crypto_alt_4h` score `-0.4563` n `146` status `ready` deltaP `5.9326` edge `0.1656` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6546` n `146` status `ready` deltaP `1.7328` edge `0.0273` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7004` n `146` status `ready` deltaP `-2.5223` edge `-0.0029` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7705` n `146` status `ready` deltaP `2.5449` edge `-0.0012` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.5259` n `146` status `ready` deltaP `-8.2417` edge `-0.0185` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5778` n `146` status `ready` deltaP `-9.6037` edge `-0.0131` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.7276` n `146` status `ready` deltaP `1.7562` edge `-0.0031` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1478` n `146` status `ready` deltaP `-7.5794` edge `0.0082` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4296` n `146` status `ready` deltaP `-18.6638` edge `-0.0162` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5994` n `146` status `ready` deltaP `-6.3366` edge `-0.0234` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.8804` n `146` status `ready` deltaP `-12.1628` edge `-0.004` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.155` n `146` status `ready` deltaP `-9.8835` edge `0.0384` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.4036` n `146` status `ready` deltaP `-7.5568` edge `-0.0607` maxDD `-9.4709`
- `news_risk_high->metal_4h` score `-5.4812` n `146` status `ready` deltaP `-10.1967` edge `-0.0683` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-6.4722` n `146` status `ready` deltaP `-5.9037` edge `-0.1418` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.5357` n `146` status `ready` deltaP `-11.9446` edge `-0.1464` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-10.2862` n `146` status `ready` deltaP `-20.1616` edge `0.1033` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.7371` n `146` status `ready` deltaP `1.1464` edge `-0.0663` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.8126` n `146` status `ready` deltaP `9.9778` edge `0.2328` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-14.3764` n `146` status `ready` deltaP `5.8255` edge `-0.1825` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
