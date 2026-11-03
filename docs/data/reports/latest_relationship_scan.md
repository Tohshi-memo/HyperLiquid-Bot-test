# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T17:08:11.680069+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4374`

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

- `news_risk_high->crypto_alt_4h` score `0.2481` n `146` status `ready` deltaP `6.8472` edge `0.2498` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4488` n `146` status `ready` deltaP `2.0322` edge `0.0517` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.688` n `146` status `ready` deltaP `-2.2229` edge `-0.0033` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8975` n `146` status `ready` deltaP `1.1976` edge `-0.0028` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.17` n `146` status `ready` deltaP `-3.1519` edge `-0.0068` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4398` n `146` status `ready` deltaP `-6.8598` edge `-0.0137` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.6778` n `146` status `ready` deltaP `11.9506` edge `0.1387` maxDD `-16.6552`
- `news_risk_high->index_24h` score `-1.8075` n `146` status `ready` deltaP `1.0298` edge `0.0456` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.065` n `146` status `ready` deltaP `-3.4268` edge `-0.0118` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2934` n `146` status `ready` deltaP `-16.4645` edge `-0.0134` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.5361` n `146` status `ready` deltaP `-10.7231` edge `-0.0032` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6812` n `146` status `ready` deltaP `-6.9354` edge `-0.0299` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2331` n `146` status `ready` deltaP `-8.3053` edge `-0.0415` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.0961` n `146` status `ready` deltaP `-14.7616` edge `-0.0075` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.4538` n `146` status `ready` deltaP `-4.404` edge `-0.0213` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.7591` n `146` status `ready` deltaP `22.667` edge `0.81` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.9284` n `146` status `ready` deltaP `-13.7738` edge `-0.0836` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.1328` n `146` status `ready` deltaP `18.5003` edge `0.6493` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.4376` n `146` status `ready` deltaP `-1.445` edge `-0.1074` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2393` n `146` status `ready` deltaP `-19.9153` edge `-0.0611` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
