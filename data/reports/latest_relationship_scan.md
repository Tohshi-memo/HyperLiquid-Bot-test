# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T00:52:26.704772+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4319`

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

- `news_risk_high->crypto_alt_4h` score `-0.4225` n `146` status `ready` deltaP `7.0776` edge `0.1623` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6048` n `146` status `ready` deltaP `2.7807` edge `0.0267` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6722` n `146` status `ready` deltaP `3.1437` edge `0.003` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.6965` n `146` status `ready` deltaP `-2.5223` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.4063` n `146` status `ready` deltaP `-6.621` edge `-0.011` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5392` n `146` status `ready` deltaP `-8.3914` edge `-0.0192` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6377` n `146` status `ready` deltaP `1.3699` edge `0.011` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.3514` n `146` status `ready` deltaP `-5.7378` edge `0.0044` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4462` n `146` status `ready` deltaP `-10.274` edge `0.0013` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.5504` n `146` status `ready` deltaP `-12.1628` edge `0.0383` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.6751` n `146` status `ready` deltaP `-22.124` edge `-0.0246` maxDD `-2.336`
- `news_risk_high->crypto_major_1h` score `-3.0246` n `146` status `ready` deltaP `-5.9101` edge `-0.0401` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8692` n `146` status `ready` deltaP `-14.5358` edge `0.0099` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.706` n `146` status `ready` deltaP `-12.5571` edge `-0.0713` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.2971` n `146` status `ready` deltaP `-9.4369` edge `-0.0599` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-9.0896` n `146` status `ready` deltaP `-16.9763` edge `-0.2861` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.3093` n `146` status `ready` deltaP `-14.6253` edge `0.1478` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.4007` n `146` status `ready` deltaP `2.1309` edge `0.0385` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.481` n `146` status `ready` deltaP `9.9778` edge `0.4271` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-14.6887` n `146` status `ready` deltaP `3.7494` edge `-0.2087` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
