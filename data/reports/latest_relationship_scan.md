# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T15:52:32.872421+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.2196` n `146` status `ready` deltaP `6.3899` edge `0.2492` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4659` n `146` status `ready` deltaP `1.7328` edge `0.0515` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6716` n `146` status `ready` deltaP `-1.9235` edge `-0.0032` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8963` n `146` status `ready` deltaP `1.1976` edge `-0.0027` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.1887` n `146` status `ready` deltaP `-3.4513` edge `-0.0072` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.3963` n `146` status `ready` deltaP `-6.0976` edge `-0.0132` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.727` n `146` status `ready` deltaP `11.9506` edge `0.1346` maxDD `-16.6552`
- `news_risk_high->index_24h` score `-1.8752` n `146` status `ready` deltaP `0.1618` edge `0.0427` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.0247` n `146` status `ready` deltaP `-2.817` edge `-0.0107` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.3075` n `146` status `ready` deltaP `-16.4645` edge `-0.0152` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4954` n `146` status `ready` deltaP `-10.274` edge `-0.0028` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6867` n `146` status `ready` deltaP `-6.9354` edge `-0.0306` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2534` n `146` status `ready` deltaP `-8.455` edge `-0.0422` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.2027` n `146` status `ready` deltaP `-15.5238` edge `-0.0113` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.477` n `146` status `ready` deltaP `-4.7089` edge `-0.0212` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.772` n `146` status `ready` deltaP `22.4934` edge `0.8095` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.8934` n `146` status `ready` deltaP `-13.6214` edge `-0.0817` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.3942` n `146` status `ready` deltaP `17.6323` edge `0.6333` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.2614` n `146` status `ready` deltaP `-0.6828` edge `-0.0978` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.3927` n `146` status `ready` deltaP `-20.7834` edge `-0.0681` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
