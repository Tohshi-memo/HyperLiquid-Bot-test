# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T20:07:41.502949+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4026`

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

- `news_risk_high->crypto_alt_4h` score `0.1911` n `146` status `ready` deltaP `8.6765` edge `0.2303` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.3818` n `146` status `ready` deltaP `3.5292` edge `0.0503` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6327` n `146` status `ready` deltaP `-1.3247` edge `-0.0022` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7885` n `146` status `ready` deltaP `2.3952` edge `-0.0017` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.3811` n `146` status `ready` deltaP `-6.1459` edge `-0.0139` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4284` n `146` status `ready` deltaP `-7.1646` edge `-0.0102` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.894` n `146` status `ready` deltaP `-0.378` edge `-0.0102` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2125` n `146` status `ready` deltaP `-8.3279` edge `0.0078` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.2687` n `146` status `ready` deltaP `-5.9345` edge `0.0329` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.4566` n `146` status `ready` deltaP `-18.8368` edge `-0.0185` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5464` n `146` status `ready` deltaP `-6.0372` edge `-0.0186` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1685` n `146` status `ready` deltaP `-6.6586` edge `-0.0471` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.232` n `146` status `ready` deltaP `-10.036` edge `0.033` maxDD `-9.5011`
- `news_risk_high->metal_24h` score `-3.8477` n `146` status `ready` deltaP `2.2278` edge `0.0227` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-4.8717` n `146` status `ready` deltaP `-5.6235` edge `-0.048` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0871` n `146` status `ready` deltaP `-11.1824` edge `-0.1141` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-9.3313` n `146` status `ready` deltaP `13.957` edge `0.4101` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-10.9233` n `146` status `ready` deltaP `0.0793` edge `-0.0747` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.5327` n `146` status `ready` deltaP `11.8809` edge `0.4101` maxDD `-102.3626`
- `news_risk_high->commodity_24h` score `-11.9729` n `146` status `ready` deltaP `-20.6807` edge `-0.0338` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
