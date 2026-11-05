# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T04:07:25.415132+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3836`

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

- `news_risk_high->crypto_alt_4h` score `-0.4873` n `146` status `ready` deltaP `6.0851` edge `0.1606` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6905` n `146` status `ready` deltaP `1.4334` edge `0.0247` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7339` n `146` status `ready` deltaP `-3.1211` edge `-0.0032` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7801` n `146` status `ready` deltaP `2.5449` edge `-0.002` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.5524` n `146` status `ready` deltaP `-8.6908` edge `-0.0189` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5976` n `146` status `ready` deltaP `-9.9085` edge `-0.0136` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8365` n `146` status `ready` deltaP `0.2318` edge `-0.0069` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.131` n `146` status `ready` deltaP `-7.5794` edge `0.0096` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4367` n `146` status `ready` deltaP `-18.6638` edge `-0.0171` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6111` n `146` status `ready` deltaP `-6.3366` edge `-0.0249` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.7652` n `146` status `ready` deltaP `-11.2978` edge `0.005` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.1295` n `146` status `ready` deltaP `-9.5786` edge `0.0385` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.4599` n `146` status `ready` deltaP `-7.8562` edge `-0.0634` maxDD `-9.4709`
- `news_risk_high->metal_4h` score `-5.3842` n `146` status `ready` deltaP `-9.4345` edge `-0.0653` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-5.7006` n `146` status `ready` deltaP `-3.3085` edge `-0.0948` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.7408` n `146` status `ready` deltaP `-12.8592` edge `-0.1574` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-10.8454` n `146` status `ready` deltaP `-20.1616` edge `0.0567` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.9141` n `146` status `ready` deltaP `0.6891` edge `-0.078` maxDD `-52.2214`
- `news_risk_high->crypto_alt_24h` score `-13.1705` n `146` status `ready` deltaP `8.4207` edge `-0.0452` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-13.4009` n `146` status `ready` deltaP `10.3238` edge `0.2648` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
