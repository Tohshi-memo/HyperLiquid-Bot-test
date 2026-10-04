# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T23:07:28.293177+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5036`

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

- `market_context_high->unknown_1h` score `97.4828` n `97` status `ready` deltaP `-0.1605` edge `8.1661` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `82.5482` n `97` status `ready` deltaP `2.7564` edge `6.8918` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.012` n `65` status `ready` deltaP `34.8382` edge `0.6224` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `7.7243` n `46` status `ready` deltaP `27.4985` edge `0.5256` maxDD `-4.5519`
- `news_risk_high->crypto_alt_4h` score `7.1233` n `65` status `ready` deltaP `22.6829` edge `0.5768` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `6.9732` n `46` status `ready` deltaP `21.0598` edge `0.568` maxDD `-8.1838`
- `news_risk_high->equity_24h` score `5.693` n `65` status `ready` deltaP `18.499` edge `0.3611` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.3454` n `97` status `ready` deltaP `18.8192` edge `0.307` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.6817` n `65` status `ready` deltaP `26.0417` edge `0.1332` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.3655` n `65` status `ready` deltaP `23.3208` edge `0.186` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.0956` n `65` status `ready` deltaP `33.8954` edge `0.0582` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.6883` n `65` status `ready` deltaP `11.064` edge `0.1858` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.3643` n `65` status `ready` deltaP `21.0601` edge `0.0982` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1405` n `65` status `ready` deltaP `26.3657` edge `0.0176` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `1.9498` n `97` status `ready` deltaP `13.9824` edge `0.1143` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.5522` n `65` status `ready` deltaP `5.3178` edge `0.1458` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.4358` n `97` status `ready` deltaP `25.2782` edge `0.0268` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3739` n `46` status `ready` deltaP `25.536` edge `0.1077` maxDD `-1.8102`
- `market_context_high->crypto_alt_4h` score `1.2365` n `97` status `ready` deltaP `4.5386` edge `0.2517` maxDD `-7.6465`
- `market_context_high->fx_1h` score `0.9252` n `97` status `ready` deltaP `14.5672` edge `0.0064` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
