# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T15:37:45.553952+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4372`

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

- `news_risk_high->crypto_alt_4h` score `0.2251` n `146` status `ready` deltaP `6.3899` edge `0.2499` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4651` n `146` status `ready` deltaP `1.7328` edge `0.0516` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6716` n `146` status `ready` deltaP `-1.9235` edge `-0.0032` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8831` n `146` status `ready` deltaP `1.3473` edge `-0.0026` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.1887` n `146` status `ready` deltaP `-3.4513` edge `-0.0072` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.3963` n `146` status `ready` deltaP `-6.0976` edge `-0.0132` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.733` n `146` status `ready` deltaP `11.9506` edge `0.1341` maxDD `-16.6552`
- `news_risk_high->index_24h` score `-1.8889` n `146` status `ready` deltaP `-0.0119` edge `0.0421` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.0144` n `146` status `ready` deltaP `-2.6646` edge `-0.0104` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.3106` n `146` status `ready` deltaP `-16.4645` edge `-0.0156` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.481` n `146` status `ready` deltaP `-10.1243` edge `-0.0026` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6851` n `146` status `ready` deltaP `-6.9354` edge `-0.0304` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2522` n `146` status `ready` deltaP `-8.455` edge `-0.0421` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.2159` n `146` status `ready` deltaP `-15.5238` edge `-0.0124` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.46` n `146` status `ready` deltaP `-4.5565` edge `-0.0208` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.7858` n `146` status `ready` deltaP `22.3198` edge `0.8089` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.8766` n `146` status `ready` deltaP `-13.6214` edge `-0.0803` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.5078` n `146` status `ready` deltaP `17.4587` edge `0.6298` maxDD `-102.7472`
- `news_risk_high->equity_4h` score `-11.2314` n `146` status `ready` deltaP `-0.6828` edge `-0.0953` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.4282` n `146` status `ready` deltaP `-20.957` edge `-0.0699` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
