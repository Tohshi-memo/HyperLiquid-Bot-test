# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T04:07:28.531530+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `26.4312` n `139` status `ready` deltaP `-15.8834` edge `2.5539` maxDD `-9.6329`
- `market_context_high->commodity_4h` score `0.8676` n `169` status `ready` deltaP `12.0847` edge `0.0632` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6557` n `181` status `ready` deltaP `9.0355` edge `0.0287` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.635` n `139` status `ready` deltaP `19.2564` edge `0.0338` maxDD `-1.4613`
- `market_context_high->fx_4h` score `-0.2162` n `169` status `ready` deltaP `4.2077` edge `0.0042` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.2418` n `181` status `ready` deltaP `2.2751` edge `-0.001` maxDD `-0.613`
- `market_context_high->index_1h` score `-0.8281` n `181` status `ready` deltaP `-6.4473` edge `-0.0044` maxDD `-1.0359`
- `market_context_high->commodity_24h` score `-1.0796` n `139` status `ready` deltaP `9.7408` edge `0.1177` maxDD `-18.3508`
- `market_context_high->index_4h` score `-1.0953` n `169` status `ready` deltaP `-5.6992` edge `-0.013` maxDD `-1.4875`
- `market_context_high->metal_1h` score `-1.2476` n `181` status `ready` deltaP `-4.6139` edge `-0.0096` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-1.4665` n `181` status `ready` deltaP `-6.2582` edge `-0.0186` maxDD `-6.8818`
- `market_context_high->metal_24h` score `-2.0159` n `139` status `ready` deltaP `1.4912` edge `-0.0455` maxDD `-2.9283`
- `market_context_high->index_24h` score `-2.4149` n `139` status `ready` deltaP `-11.2594` edge `-0.025` maxDD `-6.7627`
- `market_context_high->crypto_alt_1h` score `-2.6332` n `181` status `ready` deltaP `-9.2874` edge `-0.039` maxDD `-6.4812`
- `market_context_high->metal_4h` score `-3.1092` n `169` status `ready` deltaP `-7.0213` edge `-0.0359` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.3896` n `181` status `ready` deltaP `-7.1625` edge `-0.0443` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-4.2692` n `169` status `ready` deltaP `-15.1838` edge `-0.1352` maxDD `-15.8728`
- `market_context_high->crypto_alt_4h` score `-6.366` n `169` status `ready` deltaP `-10.2141` edge `-0.1276` maxDD `-20.1177`
- `market_context_high->crypto_major_24h` score `-6.7949` n `139` status `ready` deltaP `-13.8459` edge `-0.2017` maxDD `-33.5037`
- `market_context_high->crypto_alt_24h` score `-9.1947` n `139` status `ready` deltaP `-10.9208` edge `-0.2136` maxDD `-27.3857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
