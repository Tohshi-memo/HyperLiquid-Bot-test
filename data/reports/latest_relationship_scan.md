# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T10:52:20.095803+00:00`
- Price records: `672`
- Market context records: `2237`
- Flow alert records: `8334`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9203`

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

- `news_risk_high->crypto_alt_24h` score `25.442` n `35` status `ready` deltaP `55.744` edge `1.8074` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.0339` n `35` status `ready` deltaP `45.9276` edge `0.9906` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.3901` n `35` status `ready` deltaP `36.8998` edge `0.9013` maxDD `-2.1831`
- `market_context_high->crypto_alt_4h` score `12.9203` n `131` status `ready` deltaP `36.5586` edge `0.9266` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7183` n `131` status `ready` deltaP `42.2129` edge `0.7481` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `9.1586` n `35` status `ready` deltaP `36.6468` edge `0.5415` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `7.8552` n `35` status `ready` deltaP `20.496` edge `0.9285` maxDD `-3.3119`
- `market_context_high->unknown_4h` score `6.1702` n `131` status `ready` deltaP `24.5043` edge `0.3962` maxDD `-1.6306`
- `market_context_high->unknown_24h` score `5.4515` n `125` status `ready` deltaP `26.3611` edge `0.5439` maxDD `-17.8948`
- `market_context_high->equity_4h` score `4.438` n `131` status `ready` deltaP `24.3705` edge `0.2485` maxDD `-1.2911`
- `news_risk_high->commodity_4h` score `3.9568` n `43` status `ready` deltaP `33.377` edge `0.3519` maxDD `-3.0367`
- `market_context_high->index_4h` score `3.8494` n `131` status `ready` deltaP `29.0973` edge `0.1665` maxDD `-0.5091`
- `market_context_high->crypto_major_24h` score `3.3659` n `125` status `ready` deltaP `16.0389` edge `0.8983` maxDD `-39.8963`
- `news_risk_high->fx_24h` score `3.1607` n `35` status `ready` deltaP `32.619` edge `0.0644` maxDD `-0.1442`
- `market_context_high->crypto_major_1h` score `2.9074` n `143` status `ready` deltaP `15.7343` edge `0.1851` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `2.7735` n `143` status `ready` deltaP `15.7343` edge `0.2126` maxDD `-4.9097`
- `news_risk_high->commodity_24h` score `2.5867` n `35` status `ready` deltaP `0.3075` edge `0.2952` maxDD `-3.202`
- `market_context_high->index_24h` score `2.5353` n `125` status `ready` deltaP `10.8583` edge `0.2132` maxDD `-2.6117`
- `news_risk_high->fx_4h` score `2.1512` n `43` status `ready` deltaP `27.2794` edge `0.0158` maxDD `-0.1382`
- `news_risk_high->index_24h` score `1.9661` n `35` status `ready` deltaP `10.744` edge `0.1341` maxDD `-1.3507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
