# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T00:22:30.544836+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3815`

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

- `news_risk_high->crypto_alt_4h` score `-0.211` n `146` status `ready` deltaP `7.3046` edge `0.1879` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4668` n `146` status `ready` deltaP `2.7807` edge `0.0444` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.716` n `146` status `ready` deltaP `-2.8217` edge `-0.0029` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8041` n `146` status `ready` deltaP `2.2455` edge `-0.002` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.4441` n `146` status `ready` deltaP `-7.1938` edge `-0.015` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5699` n `146` status `ready` deltaP `-9.4512` edge `-0.0131` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.9618` n `146` status `ready` deltaP `-1.2926` edge `-0.0128` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1754` n `146` status `ready` deltaP `-7.8788` edge `0.0079` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4566` n `146` status `ready` deltaP `-18.8368` edge `-0.0185` maxDD `-2.336`
- `news_risk_high->index_24h` score `-2.4914` n `146` status `ready` deltaP `-8.7026` edge `0.0228` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.5752` n `146` status `ready` deltaP `-6.1869` edge `-0.0213` maxDD `-16.4088`
- `news_risk_high->commodity_4h` score `-3.22` n `146` status `ready` deltaP `-10.036` edge `0.034` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.2597` n `146` status `ready` deltaP `-7.1077` edge `-0.0517` maxDD `-9.4709`
- `news_risk_high->metal_24h` score `-4.737` n `146` status `ready` deltaP `-0.7134` edge `-0.0318` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-5.0489` n `146` status `ready` deltaP `-7.1479` edge `-0.0526` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.5339` n `146` status `ready` deltaP `-12.4019` edge `-0.1432` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-11.006` n `146` status `ready` deltaP `11.0158` edge `0.215` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-11.2244` n `146` status `ready` deltaP `-0.8353` edge `-0.0937` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-11.4077` n `146` status `ready` deltaP `-20.6807` edge `0.0133` maxDD `-43.7525`
- `news_risk_high->equity_24h` score `-12.1075` n `146` status `ready` deltaP `11.8809` edge `0.3622` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
