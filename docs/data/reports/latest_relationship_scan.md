# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T16:37:35.969085+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4102`

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

- `news_risk_high->crypto_alt_4h` score `0.5686` n `146` status `ready` deltaP `8.6765` edge `0.2787` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.1066` n `146` status `ready` deltaP `4.5771` edge `0.0786` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6495` n `146` status `ready` deltaP `3.4431` edge `0.0029` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7136` n `146` status `ready` deltaP `-2.8217` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.4632` n `146` status `ready` deltaP `-7.7744` edge `-0.0106` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5703` n `146` status `ready` deltaP `-8.9902` edge `-0.0192` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6934` n `146` status `ready` deltaP `1.6037` edge `0.0023` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.1184` n `146` status `ready` deltaP `-4.0911` edge `0.0233` maxDD `-16.4088`
- `news_risk_high->fx_24h` score `-2.3064` n `146` status `ready` deltaP `-16.6381` edge `-0.0139` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4042` n `146` status `ready` deltaP `-9.8249` edge `0.0018` maxDD `-3.2657`
- `news_risk_high->crypto_major_1h` score `-2.5557` n `146` status `ready` deltaP `-4.4131` edge `-0.011` maxDD `-9.4709`
- `news_risk_high->index_24h` score `-2.9059` n `146` status `ready` deltaP `-12.3382` edge `-0.0061` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.6979` n `146` status `ready` deltaP `-13.0847` edge `0.0145` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.7571` n `146` status `ready` deltaP `-12.9406` edge `-0.073` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-5.8358` n `146` status `ready` deltaP `-9.5056` edge `-0.021` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-7.9498` n `146` status `ready` deltaP `-11.8341` edge `-0.2254` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-8.8585` n `146` status `ready` deltaP `-14.3598` edge `0.1836` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.5855` n `146` status `ready` deltaP `2.6708` edge `0.0195` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-14.0772` n `146` status `ready` deltaP `9.8198` edge `0.2118` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-16.0464` n `146` status `ready` deltaP `1.8337` edge `-0.37` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
