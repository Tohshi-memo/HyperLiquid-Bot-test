# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T20:52:33.330317+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->fx_24h` score `0.9669` n `145` status `ready` deltaP `20.4064` edge `0.0253` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.9187` n `178` status `ready` deltaP `12.363` edge `0.0656` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6414` n `186` status `ready` deltaP `8.8275` edge `0.0289` maxDD `-0.7439`
- `market_context_high->fx_1h` score `-0.115` n `186` status `ready` deltaP `4.5329` edge `0.0002` maxDD `-0.613`
- `market_context_high->fx_4h` score `-0.1508` n `178` status `ready` deltaP `6.0615` edge `0.007` maxDD `-0.4647`
- `market_context_high->equity_24h` score `-0.2419` n `145` status `ready` deltaP `1.3745` edge `0.3299` maxDD `-21.0709`
- `market_context_high->index_24h` score `-0.5882` n `145` status `ready` deltaP `1.2191` edge `0.096` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.6088` n `186` status `ready` deltaP `-4.1031` edge `-0.0028` maxDD `-0.832`
- `market_context_high->metal_24h` score `-0.7866` n `145` status `ready` deltaP `2.5482` edge `0.0499` maxDD `-2.9283`
- `market_context_high->index_4h` score `-0.854` n `178` status `ready` deltaP `-3.0796` edge `-0.0099` maxDD `-1.3245`
- `market_context_high->equity_1h` score `-1.0228` n `186` status `ready` deltaP `-3.1904` edge `-0.0062` maxDD `-5.9591`
- `market_context_high->metal_1h` score `-1.2155` n `186` status `ready` deltaP `-4.3477` edge `-0.0087` maxDD `-2.0884`
- `market_context_high->crypto_alt_1h` score `-2.7021` n `186` status `ready` deltaP `-9.5744` edge `-0.0416` maxDD `-6.5795`
- `market_context_high->crypto_major_24h` score `-2.7021` n `145` status `ready` deltaP `-1.8825` edge `-0.0646` maxDD `-15.8753`
- `market_context_high->metal_4h` score `-3.0263` n `178` status `ready` deltaP `-6.2551` edge `-0.0341` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.4462` n `178` status `ready` deltaP `-12.1164` edge `-0.0975` maxDD `-12.0832`
- `market_context_high->crypto_major_1h` score `-3.674` n `186` status `ready` deltaP `-9.6227` edge `-0.0516` maxDD `-11.9002`
- `market_context_high->crypto_alt_24h` score `-5.456` n `145` status `ready` deltaP `-12.8226` edge `-0.1637` maxDD `-10.1055`
- `market_context_high->crypto_alt_4h` score `-6.0965` n `178` status `ready` deltaP `-12.0119` edge `-0.1344` maxDD `-16.8181`
- `market_context_high->commodity_24h` score `-7.8898` n `145` status `ready` deltaP `-3.5833` edge `-0.147` maxDD `-50.5832`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
