# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T08:37:30.303101+00:00`
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

- `news_risk_high->crypto_alt_4h` score `-0.3866` n `146` status `ready` deltaP `6.2375` edge `0.1725` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6398` n `146` status `ready` deltaP `1.8825` edge `0.0282` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7082` n `146` status `ready` deltaP `-2.672` edge `-0.0029` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7837` n `146` status `ready` deltaP `2.3952` edge `-0.0013` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.5345` n `146` status `ready` deltaP `-8.3914` edge `-0.0186` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5509` n `146` status `ready` deltaP `-9.1463` edge `-0.0127` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.7189` n `146` status `ready` deltaP `1.9086` edge `-0.003` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1802` n `146` status `ready` deltaP `-7.8788` edge `0.0075` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4167` n `146` status `ready` deltaP `-18.4908` edge `-0.0157` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5947` n `146` status `ready` deltaP `-6.3366` edge `-0.0228` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.8858` n `146` status `ready` deltaP `-12.1628` edge `-0.0047` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.212` n `146` status `ready` deltaP `-10.3408` edge `0.0367` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.3892` n `146` status `ready` deltaP `-7.4071` edge `-0.0605` maxDD `-9.4709`
- `news_risk_high->metal_4h` score `-5.4812` n `146` status `ready` deltaP `-10.1967` edge `-0.0683` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-6.6049` n `146` status `ready` deltaP `-6.4227` edge `-0.1494` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.4479` n `146` status `ready` deltaP `-11.7921` edge `-0.1401` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-10.1331` n `146` status `ready` deltaP `-19.6426` edge `0.1126` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.7105` n `146` status `ready` deltaP `1.2989` edge `-0.0651` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.8282` n `146` status `ready` deltaP `9.9778` edge `0.2315` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-14.5469` n `146` status `ready` deltaP `5.3065` edge `-0.2009` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
