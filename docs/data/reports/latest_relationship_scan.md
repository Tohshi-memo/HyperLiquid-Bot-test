# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T04:22:16.072131+00:00`
- Price records: `672`
- Market context records: `2422`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `news_risk_high->crypto_alt_24h` score `19.8271` n `43` status `ready` deltaP `45.3488` edge `1.4088` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.5928` n `43` status `ready` deltaP `50.7994` edge `1.2547` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.0595` n `43` status `ready` deltaP `29.7925` edge `1.0878` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.4611` n `43` status `ready` deltaP `18.3785` edge `0.8073` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.8009` n `43` status `ready` deltaP `26.4252` edge `0.4965` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.844` n `102` status `ready` deltaP `24.2137` edge `0.3584` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.1338` n `43` status `ready` deltaP `10.3198` edge `0.4009` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.6228` n `125` status `ready` deltaP `22.6098` edge `0.5024` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.5979` n `125` status `ready` deltaP `21.5793` edge `0.4203` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.521` n `43` status `ready` deltaP `36.8823` edge `0.066` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.233` n `43` status `ready` deltaP `29.566` edge `0.2845` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.7297` n `125` status `ready` deltaP `14.0012` edge `0.1951` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `2.6586` n `102` status `ready` deltaP `11.3562` edge `0.6544` maxDD `-25.1408`
- `market_context_high->index_24h` score `2.4995` n `102` status `ready` deltaP `13.6029` edge `0.1433` maxDD `-0.3888`
- `news_risk_high->fx_4h` score `2.1122` n `43` status `ready` deltaP `26.8221` edge `0.0156` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7219` n `43` status `ready` deltaP `15.9919` edge `0.1092` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.2311` n `125` status `ready` deltaP `11.5066` edge `0.1453` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.0905` n `43` status `ready` deltaP `20.2966` edge `0.0025` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0146` n `125` status `ready` deltaP `8.6527` edge `0.1456` maxDD `-6.1656`
- `news_risk_high->commodity_1h` score `0.5709` n `43` status `ready` deltaP `9.5669` edge `0.0774` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
