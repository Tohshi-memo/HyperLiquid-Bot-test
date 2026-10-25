# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T08:22:27.946925+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7912`

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

- `market_context_high->unknown_4h` score `42.008` n `105` status `ready` deltaP `0.045` edge `3.5339` maxDD `-1.016`
- `market_context_high->unknown_1h` score `12.7811` n `114` status `ready` deltaP `4.4831` edge `1.0841` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `3.723` n `41` status `ready` deltaP `20.0288` edge `0.4743` maxDD `-8.4413`
- `market_context_high->crypto_major_24h` score `1.5033` n `41` status `ready` deltaP `11.687` edge `0.1533` maxDD `-5.8084`
- `market_context_high->commodity_24h` score `0.8571` n `41` status `ready` deltaP `16.9038` edge `0.0881` maxDD `-3.6055`
- `market_context_high->fx_4h` score `-0.0354` n `105` status `ready` deltaP `6.9918` edge `0.0087` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0572` n `114` status `ready` deltaP `3.7005` edge `0.0029` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.5242` n `114` status `ready` deltaP `-0.3624` edge `0.0088` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.534` n `41` status `ready` deltaP `3.938` edge `0.006` maxDD `-1.0569`
- `market_context_high->metal_1h` score `-0.6203` n `114` status `ready` deltaP `4.7694` edge `-0.0043` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6534` n `114` status `ready` deltaP `-1.9908` edge `-0.0053` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.8575` n `105` status `ready` deltaP `-2.9167` edge `0.0324` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.4099` n `114` status `ready` deltaP `1.413` edge `-0.0321` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.7479` n `105` status `ready` deltaP `6.6521` edge `-0.019` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.042` n `105` status `ready` deltaP `-5.6185` edge `-0.0369` maxDD `-4.3282`
- `market_context_high->metal_24h` score `-2.7699` n `41` status `ready` deltaP `-6.0086` edge `-0.0213` maxDD `-6.5572`
- `market_context_high->crypto_alt_1h` score `-3.143` n `114` status `ready` deltaP `-2.2692` edge `-0.0594` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.7983` n `114` status `ready` deltaP `-0.3441` edge `-0.0869` maxDD `-12.1865`
- `market_context_high->index_24h` score `-5.7098` n `41` status `ready` deltaP `-24.5511` edge `-0.182` maxDD `-5.078`
- `market_context_high->crypto_major_4h` score `-5.9915` n `105` status `ready` deltaP `-10.2656` edge `-0.2` maxDD `-33.3092`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
