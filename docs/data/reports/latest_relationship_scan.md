# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T06:52:26.797991+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3926`

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

- `news_risk_high->crypto_alt_4h` score `-0.5699` n `146` status `ready` deltaP `5.3229` edge `0.1551` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6476` n `146` status `ready` deltaP `1.7328` edge `0.0282` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.7154` n `146` status `ready` deltaP `3.1437` edge `-0.0006` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7339` n `146` status `ready` deltaP `-3.1211` edge `-0.0032` maxDD `-0.6065`
- `news_risk_high->metal_1h` score `-1.5166` n `146` status `ready` deltaP `-8.092` edge `-0.0183` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.615` n `146` status `ready` deltaP `-10.2134` edge `-0.0138` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.7664` n `146` status `ready` deltaP `1.1464` edge `-0.004` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.125` n `146` status `ready` deltaP `-7.4297` edge `0.0091` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4343` n `146` status `ready` deltaP `-18.6638` edge `-0.0168` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5511` n `146` status `ready` deltaP `-5.8875` edge `-0.0202` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.8663` n `146` status `ready` deltaP `-12.1628` edge `-0.0022` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.0945` n `146` status `ready` deltaP `-9.4262` edge `0.0404` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.3916` n `146` status `ready` deltaP `-7.5568` edge `-0.0597` maxDD `-9.4709`
- `news_risk_high->metal_4h` score `-5.4872` n `146` status `ready` deltaP `-10.1967` edge `-0.0688` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-6.2932` n `146` status `ready` deltaP `-5.2116` edge `-0.1315` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.6925` n `146` status `ready` deltaP `-12.5543` edge `-0.1554` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-10.4278` n `146` status `ready` deltaP `-20.1616` edge `0.0915` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.8363` n `146` status `ready` deltaP `0.5367` edge `-0.0705` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.7634` n `146` status `ready` deltaP `9.9778` edge `0.2369` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-14.1438` n `146` status `ready` deltaP `6.5176` edge `-0.1573` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
