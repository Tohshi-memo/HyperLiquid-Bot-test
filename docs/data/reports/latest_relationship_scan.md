# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T05:07:27.610157+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.7446` n `146` status `ready` deltaP `9.2863` edge `0.2972` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.3217` n `146` status `ready` deltaP `2.9304` edge `0.062` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6677` n `146` status `ready` deltaP `-1.9235` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7345` n `146` status `ready` deltaP `2.6946` edge `0.0008` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2229` n `146` status `ready` deltaP `-4.1998` edge `-0.0066` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.3188` n `146` status `ready` deltaP `12.2979` edge `0.1663` maxDD `-16.6552`
- `news_risk_high->fx_4h` score `-1.4638` n `146` status `ready` deltaP `-7.622` edge `-0.0117` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.6549` n `146` status `ready` deltaP `2.4187` edge `0.0559` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.7206` n `146` status `ready` deltaP `0.8415` edge `0.0039` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.3313` n `146` status `ready` deltaP `-17.8534` edge `-0.009` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.4287` n `146` status `ready` deltaP `-4.9893` edge `-0.0105` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4342` n `146` status `ready` deltaP `-9.8249` edge `-0.0007` maxDD `-3.2657`
- `news_risk_high->crypto_major_1h` score `-2.9777` n `146` status `ready` deltaP `-6.8083` edge `-0.0302` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.788` n `146` status `ready` deltaP `-12.1701` edge `0.0009` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.3178` n `146` status `ready` deltaP `-3.1845` edge `-0.0181` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-5.9987` n `146` status `ready` deltaP `-10.2677` edge `-0.0295` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-6.4753` n `146` status `ready` deltaP `21.1045` edge `0.7286` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-8.4381` n `146` status `ready` deltaP `18.6739` edge `0.6227` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-10.2729` n `146` status `ready` deltaP `0.994` edge `-0.0266` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.3038` n `146` status `ready` deltaP `-20.4362` edge `-0.063` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
