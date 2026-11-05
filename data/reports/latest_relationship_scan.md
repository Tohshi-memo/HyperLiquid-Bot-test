# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T05:52:31.132024+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3908`

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

- `news_risk_high->crypto_alt_4h` score `-0.5731` n `146` status `ready` deltaP `5.1704` edge `0.1557` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5845` n `146` status `ready` deltaP `2.1819` edge `0.0333` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6891` n `146` status `ready` deltaP `3.4431` edge `-0.0004` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7261` n `146` status `ready` deltaP `-2.9714` edge `-0.0032` maxDD `-0.6065`
- `news_risk_high->metal_1h` score `-1.515` n `146` status `ready` deltaP `-8.092` edge `-0.0181` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.6237` n `146` status `ready` deltaP `-10.3659` edge `-0.0139` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8003` n `146` status `ready` deltaP `0.6891` edge `-0.0053` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1514` n `146` status `ready` deltaP `-7.7291` edge `0.0089` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4367` n `146` status `ready` deltaP `-18.6638` edge `-0.0171` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.516` n `146` status `ready` deltaP `-5.5881` edge `-0.0177` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.8499` n `146` status `ready` deltaP `-12.1628` edge `-0.0001` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.1103` n `146` status `ready` deltaP `-9.5786` edge `0.0401` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.3388` n `146` status `ready` deltaP `-7.2574` edge `-0.0573` maxDD `-9.4709`
- `news_risk_high->metal_4h` score `-5.4848` n `146` status `ready` deltaP `-10.1967` edge `-0.0686` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-6.119` n `146` status `ready` deltaP `-4.5196` edge `-0.1216` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.6949` n `146` status `ready` deltaP `-12.5543` edge `-0.1556` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-10.5886` n `146` status `ready` deltaP `-20.1616` edge `0.0781` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.8831` n `146` status `ready` deltaP `0.5367` edge `-0.0744` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.7106` n `146` status `ready` deltaP `9.9778` edge `0.2413` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-13.8419` n `146` status `ready` deltaP `7.2096` edge `-0.1232` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
