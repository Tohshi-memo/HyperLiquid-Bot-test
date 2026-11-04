# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T03:07:27.336816+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.6274` n `146` status `ready` deltaP `8.9814` edge `0.2842` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.2524` n `146` status `ready` deltaP `3.5292` edge `0.0669` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6576` n `146` status `ready` deltaP `-1.7738` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7142` n `146` status `ready` deltaP `2.8443` edge `0.0015` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.1863` n `146` status `ready` deltaP `-3.601` edge `-0.0059` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.3356` n `146` status `ready` deltaP `12.2979` edge `0.1649` maxDD `-16.6552`
- `news_risk_high->fx_4h` score `-1.4654` n `146` status `ready` deltaP `-7.622` edge `-0.0119` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.6956` n `146` status `ready` deltaP `2.0715` edge `0.053` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.8221` n `146` status `ready` deltaP `-0.2255` edge `-0.002` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2722` n `146` status `ready` deltaP `-16.9854` edge `-0.0072` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.4349` n `146` status `ready` deltaP `-5.2887` edge `-0.0093` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4666` n `146` status `ready` deltaP `-10.274` edge `-0.0004` maxDD `-3.2657`
- `news_risk_high->crypto_major_1h` score `-2.8854` n `146` status `ready` deltaP `-6.3592` edge `-0.0255` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.9053` n `146` status `ready` deltaP `-12.9323` edge `-0.0038` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.376` n `146` status `ready` deltaP `-3.6418` edge `-0.0199` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-6.1709` n `146` status `ready` deltaP `21.7989` edge `0.763` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.2335` n `146` status `ready` deltaP `-10.8775` edge `-0.045` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.3239` n `146` status `ready` deltaP `19.0212` edge `0.6299` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-10.7591` n `146` status `ready` deltaP `-0.0731` edge `-0.06` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.3031` n `146` status `ready` deltaP `-20.2626` edge `-0.0641` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
