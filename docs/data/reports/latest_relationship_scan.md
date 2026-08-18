# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T07:52:26.807642+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11633`

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

- `market_context_high->crypto_major_24h` score `2.1682` n `77` status `ready` deltaP `5.5752` edge `0.2643` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.2178` n `77` status `ready` deltaP `14.333` edge `0.2439` maxDD `-4.666`
- `market_context_high->equity_1h` score `0.9284` n `97` status `ready` deltaP `8.5762` edge `0.0506` maxDD `-0.4329`
- `market_context_high->crypto_major_4h` score `0.7028` n `96` status `ready` deltaP `9.3242` edge `0.0985` maxDD `-3.1677`
- `market_context_high->metal_4h` score `0.6947` n `96` status `ready` deltaP `14.126` edge `0.0213` maxDD `-1.273`
- `market_context_high->index_1h` score `0.5835` n `97` status `ready` deltaP `12.0532` edge `0.007` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5148` n `97` status `ready` deltaP `9.3108` edge `0.0035` maxDD `-0.4807`
- `market_context_high->crypto_alt_4h` score `0.4319` n `96` status `ready` deltaP `11.4583` edge `0.1107` maxDD `-5.5373`
- `market_context_high->unknown_24h` score `0.0898` n `77` status `ready` deltaP `14.7449` edge `-0.072` maxDD `-0.1719`
- `market_context_high->metal_1h` score `-0.1013` n `97` status `ready` deltaP `3.4585` edge `0.0072` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.2151` n `96` status `ready` deltaP `3.379` edge `0.0004` maxDD `-0.3734`
- `market_context_high->crypto_alt_1h` score `-0.3065` n `97` status `ready` deltaP `2.8597` edge `0.0218` maxDD `-2.413`
- `market_context_high->equity_4h` score `-0.3271` n `96` status `ready` deltaP `0.9146` edge `0.0571` maxDD `-2.5696`
- `market_context_high->commodity_4h` score `-0.3364` n `96` status `ready` deltaP `4.3954` edge `0.0126` maxDD `-2.4692`
- `market_context_high->fx_1h` score `-0.4611` n `97` status `ready` deltaP `-3.5913` edge `0.001` maxDD `-0.2273`
- `market_context_high->crypto_major_1h` score `-0.4873` n `97` status `ready` deltaP `1.23` edge `0.0138` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.6577` n `96` status `ready` deltaP `0.0` edge `0.0086` maxDD `-0.4063`
- `market_context_high->commodity_1h` score `-0.9104` n `97` status `ready` deltaP `-7.2829` edge `-0.0069` maxDD `-1.5684`
- `market_context_high->metal_24h` score `-1.1328` n `77` status `ready` deltaP `-2.7414` edge `0.0383` maxDD `-4.887`
- `market_context_high->index_24h` score `-3.2654` n `77` status `ready` deltaP `-10.3693` edge `-0.1472` maxDD `-7.8515`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
