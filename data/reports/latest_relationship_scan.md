# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T03:07:25.779805+00:00`
- Price records: `672`
- Market context records: `6349`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.1375` n `32` status `ready` deltaP `42.3611` edge `0.9938` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.1545` n `32` status `ready` deltaP `51.0417` edge `0.1726` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.4502` n `32` status `ready` deltaP `17.5347` edge `0.5316` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.1266` n `32` status `ready` deltaP `42.9116` edge `0.0624` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.6868` n `32` status `ready` deltaP `32.2917` edge `0.1125` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3883` n `32` status `ready` deltaP `28.7425` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5465` n `32` status `ready` deltaP `15.1759` edge `0.1438` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.933` n `32` status `ready` deltaP `11.7702` edge `0.0873` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.6763` n `196` status `ready` deltaP `14.012` edge `0.0426` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.1057` n `207` status `ready` deltaP `-7.182` edge `0.1575` maxDD `-3.7317`
- `market_context_high->index_4h` score `-0.0311` n `196` status `ready` deltaP `6.4118` edge `0.0223` maxDD `-0.4108`
- `market_context_high->commodity_24h` score `-0.6067` n `129` status `ready` deltaP `-4.7965` edge `0.1406` maxDD `-6.2457`
- `market_context_high->metal_1h` score `-0.6086` n `207` status `ready` deltaP `3.7114` edge `0.0023` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.6646` n `207` status `ready` deltaP `-2.3236` edge `-0.0014` maxDD `-2.1314`
- `news_risk_high->index_24h` score `-0.714` n `32` status `ready` deltaP `0.3472` edge `-0.0067` maxDD `-2.3058`
- `market_context_high->metal_24h` score `-0.7254` n `129` status `ready` deltaP `13.5214` edge `0.0737` maxDD `-11.8809`
- `market_context_high->fx_1h` score `-0.7324` n `207` status `ready` deltaP `-0.8469` edge `-0.002` maxDD `-0.9376`
- `news_risk_high->metal_1h` score `-0.7558` n `32` status `ready` deltaP `-3.2934` edge `-0.0252` maxDD `-1.6464`
- `news_risk_high->unknown_1h` score `-0.8115` n `32` status `ready` deltaP `5.3331` edge `-0.0687` maxDD `-0.7581`
- `market_context_high->index_1h` score `-1.0319` n `207` status `ready` deltaP `-2.555` edge `0.003` maxDD `-0.7564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
