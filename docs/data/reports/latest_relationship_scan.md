# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T03:52:23.908690+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4411`

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

- `news_risk_high->crypto_alt_4h` score `0.6952` n `146` status `ready` deltaP `8.9814` edge `0.2929` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.2414` n `146` status `ready` deltaP `3.5292` edge `0.0683` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6412` n `146` status `ready` deltaP `-1.4744` edge `-0.0023` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7273` n `146` status `ready` deltaP `2.6946` edge `0.0014` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.1848` n `146` status `ready` deltaP `-3.601` edge `-0.0057` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.3248` n `146` status `ready` deltaP `12.2979` edge `0.1658` maxDD `-16.6552`
- `news_risk_high->fx_4h` score `-1.4654` n `146` status `ready` deltaP `-7.622` edge `-0.0119` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.687` n `146` status `ready` deltaP `2.0715` edge `0.0541` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.7844` n `146` status `ready` deltaP `0.0793` edge `0.0008` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.3047` n `146` status `ready` deltaP `-17.5062` edge `-0.0079` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.4131` n `146` status `ready` deltaP `-5.139` edge `-0.0075` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4702` n `146` status `ready` deltaP `-10.274` edge `-0.0007` maxDD `-3.2657`
- `news_risk_high->crypto_major_1h` score `-2.8746` n `146` status `ready` deltaP `-6.3592` edge `-0.0246` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8424` n `146` status `ready` deltaP `-12.475` edge `-0.0016` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.3676` n `146` status `ready` deltaP `-3.6418` edge `-0.0192` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.1267` n `146` status `ready` deltaP `-10.8775` edge `-0.0361` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-6.2746` n `146` status `ready` deltaP `21.7989` edge `0.7497` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-8.3467` n `146` status `ready` deltaP `19.0212` edge `0.628` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-10.5367` n `146` status `ready` deltaP `0.2318` edge `-0.0435` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2995` n `146` status `ready` deltaP `-20.2626` edge `-0.0638` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
