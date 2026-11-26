# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T20:07:27.825168+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3132`

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

- `news_risk_high->unknown_1h` score `3218.2331` n `31` status `ready` deltaP `2.3807` edge `268.1878` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3202.2702` n `31` status `ready` deltaP `4.3962` edge `266.8322` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `29.532` n `31` status `ready` deltaP `38.7153` edge `2.2029` maxDD `0.0`
- `news_risk_high->equity_24h` score `26.9114` n `31` status `ready` deltaP `37.8472` edge `1.9903` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `23.3889` n `31` status `ready` deltaP `38.0208` edge `1.6956` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.0795` n `31` status `ready` deltaP `24.7787` edge `0.7618` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.9637` n `31` status `ready` deltaP `36.9198` edge `0.5489` maxDD `-2.178`
- `news_risk_high->metal_24h` score `6.7734` n `31` status `ready` deltaP `24.3952` edge `0.4293` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.5149` n `31` status `ready` deltaP `17.8452` edge `0.858` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.9048` n `31` status `ready` deltaP `41.3643` edge `0.1458` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.7385` n `31` status `ready` deltaP `39.2361` edge `0.1333` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.3668` n `31` status `ready` deltaP `19.3886` edge `0.17` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.1517` n `31` status `ready` deltaP `35.243` edge `0.0537` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6147` n `31` status `ready` deltaP `31.244` edge `0.0181` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.2904` n `31` status `ready` deltaP `8.2142` edge `0.285` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.064` n `31` status `ready` deltaP `11.2082` edge `0.2256` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4098` n `31` status `ready` deltaP `28.0857` edge `0.0214` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.843` n `31` status `ready` deltaP `14.4915` edge `0.0672` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.3095` n `31` status `ready` deltaP `10.8084` edge `0.0074` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4682` n `31` status `ready` deltaP `-2.9602` edge `0.0069` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
