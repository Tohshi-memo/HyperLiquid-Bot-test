# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T10:07:30.020205+00:00`
- Price records: `672`
- Market context records: `5970`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11220`

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

- `news_risk_high->fx_24h` score `7.1604` n `30` status `ready` deltaP `65.625` edge `0.1592` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.0388` n `30` status `ready` deltaP `36.6667` edge `0.196` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.8856` n `30` status `ready` deltaP `40.3049` edge `0.0597` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1603` n `30` status `ready` deltaP `26.0279` edge `0.0204` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4633` n `235` status `ready` deltaP `9.1931` edge `0.1701` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8442` n `30` status `ready` deltaP `10.3393` edge `0.086` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2107` n `30` status `ready` deltaP `5.4691` edge `0.0367` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.0701` n `30` status `ready` deltaP `8.0208` edge `0.0247` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.3798` n `30` status `ready` deltaP `1.986` edge `-0.0253` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4336` n `243` status `ready` deltaP `3.6088` edge `0.0332` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.4773` n `243` status `ready` deltaP `2.5622` edge `0.0016` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.5064` n `243` status `ready` deltaP `-1.5149` edge `0.0009` maxDD `-1.4578`
- `market_context_high->fx_1h` score `-0.6873` n `243` status `ready` deltaP `-0.8033` edge `-0.0008` maxDD `-0.756`
- `market_context_high->index_1h` score `-0.6908` n `243` status `ready` deltaP `-0.2433` edge `0.0044` maxDD `-1.3078`
- `market_context_high->equity_24h` score `-0.9437` n `214` status `ready` deltaP `20.9616` edge `0.3059` maxDD `-31.2762`
- `market_context_high->index_4h` score `-1.0935` n `235` status `ready` deltaP `1.2351` edge `0.0203` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.1085` n `30` status `ready` deltaP `-10.4491` edge `-0.021` maxDD `-1.1161`
- `market_context_high->crypto_major_1h` score `-1.1362` n `243` status `ready` deltaP `1.7385` edge `0.0195` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.17` n `243` status `ready` deltaP `1.4773` edge `0.0154` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.4142` n `235` status `ready` deltaP `-0.9555` edge `-0.0036` maxDD `-6.3734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
