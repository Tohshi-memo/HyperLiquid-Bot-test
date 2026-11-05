# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T07:07:32.032715+00:00`
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

- `news_risk_high->crypto_alt_4h` score `-0.5541` n `146` status `ready` deltaP `5.4753` edge `0.1561` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6671` n `146` status `ready` deltaP `1.5831` edge `0.0267` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7253` n `146` status `ready` deltaP `-2.9714` edge `-0.0031` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7298` n `146` status `ready` deltaP `2.994` edge `-0.0008` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.5251` n `146` status `ready` deltaP `-8.2417` edge `-0.0184` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.6055` n `146` status `ready` deltaP `-10.061` edge `-0.0136` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.7569` n `146` status `ready` deltaP `1.2989` edge `-0.0038` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1107` n `146` status `ready` deltaP `-7.28` edge `0.0093` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4335` n `146` status `ready` deltaP `-18.6638` edge `-0.0167` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5706` n `146` status `ready` deltaP `-6.0372` edge `-0.0217` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.8702` n `146` status `ready` deltaP `-12.1628` edge `-0.0027` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.0957` n `146` status `ready` deltaP `-9.4262` edge `0.0403` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.4168` n `146` status `ready` deltaP `-7.7065` edge `-0.0608` maxDD `-9.4709`
- `news_risk_high->metal_4h` score `-5.486` n `146` status `ready` deltaP `-10.1967` edge `-0.0687` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-6.3382` n `146` status `ready` deltaP `-5.3846` edge `-0.1341` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.6731` n `146` status `ready` deltaP `-12.4019` edge `-0.1548` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-10.3894` n `146` status `ready` deltaP `-20.1616` edge `0.0947` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.8181` n `146` status `ready` deltaP `0.6891` edge `-0.07` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.779` n `146` status `ready` deltaP `9.9778` edge `0.2356` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-14.2129` n `146` status `ready` deltaP `6.3446` edge `-0.165` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
