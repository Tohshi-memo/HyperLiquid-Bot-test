# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T21:07:19.900553+00:00`
- Price records: `672`
- Market context records: `2389`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `news_risk_high->crypto_alt_24h` score `21.6067` n `43` status `ready` deltaP `49.8627` edge `1.527` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.197` n `43` status `ready` deltaP `49.9313` edge `1.2275` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.3379` n `43` status `ready` deltaP `29.7925` edge `1.111` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.7842` n `43` status `ready` deltaP `19.7674` edge `0.9083` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.3609` n `43` status `ready` deltaP `28.1613` edge `0.5316` maxDD `-1.4744`
- `news_risk_high->index_24h` score `5.4481` n `43` status `ready` deltaP `13.6184` edge `0.4051` maxDD `-1.3507`
- `market_context_high->unknown_24h` score `5.2494` n `123` status `ready` deltaP `23.0564` edge `0.3249` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.8839` n `143` status `ready` deltaP `23.4437` edge `0.4317` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `3.6163` n `123` status `ready` deltaP `15.8537` edge `0.7472` maxDD `-25.1408`
- `news_risk_high->fx_24h` score `3.5815` n `43` status `ready` deltaP `37.924` edge `0.0641` maxDD `-0.1442`
- `market_context_high->crypto_alt_4h` score `3.5608` n `143` status `ready` deltaP `18.2` edge `0.4433` maxDD `-15.4319`
- `news_risk_high->commodity_4h` score `3.4716` n `43` status `ready` deltaP `31.3953` edge `0.3029` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.6888` n `143` status `ready` deltaP `15.7705` edge `0.1799` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.0649` n `43` status `ready` deltaP `26.3648` edge `0.0147` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.6557` n `43` status `ready` deltaP `14.9248` edge `0.1108` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.5817` n `146` status `ready` deltaP `13.7438` edge `0.1596` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.2884` n `123` status `ready` deltaP `10.1584` edge `0.0914` maxDD `-1.4737`
- `news_risk_high->unknown_1h` score `1.081` n `43` status `ready` deltaP `19.8475` edge `0.0047` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `0.9888` n `146` status `ready` deltaP `8.5411` edge `0.1442` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.9774` n `143` status `ready` deltaP `14.5851` edge `0.0668` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
