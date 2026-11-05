# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T22:52:26.739591+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4276`

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

- `news_risk_high->crypto_alt_4h` score `-0.3805` n `146` status `ready` deltaP `6.9997` edge `0.1682` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4598` n `146` status `ready` deltaP `3.2298` edge `0.0423` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.653` n `146` status `ready` deltaP `3.2934` edge `0.0036` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7043` n `146` status `ready` deltaP `-2.672` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.41` n `146` status `ready` deltaP `-6.7073` edge `-0.0109` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.501` n `146` status `ready` deltaP `-7.7926` edge `-0.0183` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6405` n `146` status `ready` deltaP `1.4513` edge `0.0101` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.3046` n `146` status `ready` deltaP `-5.4384` edge `0.0084` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4737` n `146` status `ready` deltaP `-10.5734` edge `0.001` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.589` n `146` status `ready` deltaP `-20.859` edge `-0.022` maxDD `-2.336`
- `news_risk_high->index_24h` score `-2.6642` n `146` status `ready` deltaP `-12.2504` edge `0.0243` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-2.8495` n `146` status `ready` deltaP `-5.461` edge `-0.0285` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8665` n `146` status `ready` deltaP `-14.4567` edge `0.0096` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.6857` n `146` status `ready` deltaP `-12.4833` edge `-0.0701` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.3413` n `146` status `ready` deltaP `-9.8104` edge `-0.0611` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-8.8816` n `146` status `ready` deltaP `-16.0561` edge `-0.2749` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.1451` n `146` status `ready` deltaP `-14.4928` edge `0.1606` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.4817` n `146` status `ready` deltaP `2.2135` edge `0.0312` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-12.4581` n `146` status `ready` deltaP `9.8989` edge `0.3462` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.4842` n `146` status `ready` deltaP `2.4466` edge `-0.302` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
