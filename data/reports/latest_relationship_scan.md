# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T06:52:30.638628+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4278`

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

- `news_risk_high->crypto_alt_4h` score `-0.0259` n `143` status `ready` deltaP `8.3735` edge `0.2045` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4983` n `143` status `ready` deltaP `3.3437` edge `0.0366` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6799` n `143` status `ready` deltaP `3.2431` edge `0.0017` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.6856` n `143` status `ready` deltaP `-2.3428` edge `-0.0022` maxDD `-0.6065`
- `news_risk_high->metal_1h` score `-1.4151` n `143` status `ready` deltaP `-7.2443` edge `-0.0168` maxDD `-2.6391`
- `news_risk_high->fx_4h` score `-1.4993` n `143` status `ready` deltaP `-8.2136` edge `-0.0123` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.5521` n `143` status `ready` deltaP `1.6949` edge `0.0069` maxDD `-4.0411`
- `news_risk_high->index_24h` score `-2.1078` n `143` status `ready` deltaP `-11.3582` edge `0.0699` maxDD `-6.8197`
- `news_risk_high->equity_1h` score `-2.3503` n `143` status `ready` deltaP `-5.2469` edge `0.0006` maxDD `-16.3557`
- `news_risk_high->commodity_1h` score `-2.5265` n `143` status `ready` deltaP `-11.1878` edge `0.0007` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.7384` n `143` status `ready` deltaP `-25.0974` edge `-0.0283` maxDD `-2.1034`
- `news_risk_high->crypto_major_1h` score `-2.7986` n `143` status `ready` deltaP `-5.3495` edge `-0.025` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.168` n `143` status `ready` deltaP `-17.07` edge `0.0019` maxDD `-9.5011`
- `news_risk_high->crypto_major_4h` score `-4.7177` n `143` status `ready` deltaP `-7.9962` edge `0.0042` maxDD `-20.5224`
- `news_risk_high->metal_4h` score `-5.4194` n `143` status `ready` deltaP `-12.1216` edge `-0.0698` maxDD `-8.7473`
- `news_risk_high->equity_24h` score `-7.6743` n `143` status `ready` deltaP `11.1417` edge `0.6264` maxDD `-94.5494`
- `news_risk_high->metal_24h` score `-8.5206` n `143` status `ready` deltaP `-15.8842` edge `-0.2838` maxDD `-14.6285`
- `news_risk_high->equity_4h` score `-9.1531` n `143` status `ready` deltaP `2.1522` edge `0.0164` maxDD `-49.8136`
- `news_risk_high->commodity_24h` score `-10.3349` n `143` status `ready` deltaP `-17.56` edge `0.0819` maxDD `-43.7525`
- `news_risk_high->crypto_alt_24h` score `-12.2297` n `143` status `ready` deltaP `6.9676` edge `0.0851` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
