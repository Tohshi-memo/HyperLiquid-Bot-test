# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T00:22:33.134753+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.41` n `146` status `ready` deltaP `8.3716` edge `0.2604` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4036` n `146` status `ready` deltaP `2.4813` edge `0.0545` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7113` n `146` status `ready` deltaP `-2.672` edge `-0.0033` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8688` n `146` status `ready` deltaP `1.497` edge `-0.0024` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.1669` n `146` status `ready` deltaP `-3.1519` edge `-0.0064` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.4136` n `146` status `ready` deltaP `12.2979` edge `0.1584` maxDD `-16.6552`
- `news_risk_high->fx_4h` score `-1.4693` n `146` status `ready` deltaP `-7.622` edge `-0.0124` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.7425` n `146` status `ready` deltaP `1.7243` edge `0.0493` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.9583` n `146` status `ready` deltaP `-1.7499` edge `-0.0093` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2318` n `146` status `ready` deltaP `-16.4645` edge `-0.0055` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.5589` n `146` status `ready` deltaP `-11.0225` edge `-0.0031` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6937` n `146` status `ready` deltaP `-6.9354` edge `-0.0315` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1456` n `146` status `ready` deltaP `-7.7065` edge `-0.0382` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.0823` n `146` status `ready` deltaP `-14.3043` edge `-0.0094` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.308` n `146` status `ready` deltaP `-3.0321` edge `-0.0183` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.9894` n `146` status `ready` deltaP `21.9726` edge `0.7851` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.6753` n `146` status `ready` deltaP `-11.9446` edge `-0.0747` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.3366` n `146` status `ready` deltaP `18.8476` edge `0.63` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.4524` n `146` status `ready` deltaP `-1.7499` edge `-0.1066` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2609` n `146` status `ready` deltaP `-19.9153` edge `-0.0629` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
