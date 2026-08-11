# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T03:52:27.891870+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11744`

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

- `market_context_high->unknown_24h` score `25.6749` n `140` status `ready` deltaP `-15.6624` edge `2.4894` maxDD `-9.6329`
- `market_context_high->fx_24h` score `0.9977` n `140` status `ready` deltaP `19.4414` edge `0.0343` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.9136` n `169` status `ready` deltaP `12.5242` edge `0.0641` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6545` n `181` status `ready` deltaP `9.0355` edge `0.0286` maxDD `-0.7439`
- `market_context_high->fx_4h` score `-0.2147` n `169` status `ready` deltaP `4.2077` edge `0.0044` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.2418` n `181` status `ready` deltaP `2.2751` edge `-0.001` maxDD `-0.613`
- `market_context_high->index_1h` score `-0.8281` n `181` status `ready` deltaP `-6.4473` edge `-0.0044` maxDD `-1.0359`
- `market_context_high->index_4h` score `-1.1023` n `169` status `ready` deltaP `-5.6992` edge `-0.0139` maxDD `-1.4875`
- `market_context_high->metal_1h` score `-1.2822` n `181` status `ready` deltaP `-5.017` edge `-0.0098` maxDD `-2.0884`
- `market_context_high->commodity_24h` score `-1.3074` n `140` status `ready` deltaP `9.3845` edge `0.1107` maxDD `-19.6032`
- `market_context_high->equity_1h` score `-1.4673` n `181` status `ready` deltaP `-6.2582` edge `-0.0187` maxDD `-6.8818`
- `market_context_high->metal_24h` score `-1.954` n `140` status `ready` deltaP `1.6659` edge `-0.0415` maxDD `-2.9283`
- `market_context_high->index_24h` score `-2.3665` n `140` status `ready` deltaP `-10.8997` edge `-0.0212` maxDD `-6.7627`
- `market_context_high->crypto_alt_1h` score `-2.681` n `181` status `ready` deltaP `-9.6904` edge `-0.0403` maxDD `-6.4812`
- `market_context_high->metal_4h` score `-3.1068` n `169` status `ready` deltaP `-7.0213` edge `-0.0357` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.4339` n `181` status `ready` deltaP `-7.5655` edge `-0.0453` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-4.2911` n `169` status `ready` deltaP `-15.1838` edge `-0.138` maxDD `-15.8728`
- `market_context_high->crypto_alt_4h` score `-6.4203` n `169` status `ready` deltaP `-10.6536` edge `-0.1292` maxDD `-20.1177`
- `market_context_high->crypto_major_24h` score `-6.7617` n `140` status `ready` deltaP `-13.6283` edge `-0.1989` maxDD `-33.5037`
- `market_context_high->crypto_alt_24h` score `-9.2778` n `140` status `ready` deltaP `-11.4038` edge `-0.2173` maxDD `-27.3857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
