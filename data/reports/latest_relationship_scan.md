# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T18:18:58.900327+00:00`
- Price records: `672`
- Market context records: `3099`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6921`

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

- `market_context_high->crypto_alt_24h` score `16.5998` n `82` status `ready` deltaP `14.3546` edge `2.5601` maxDD `-33.5432`
- `market_context_high->commodity_24h` score `15.195` n `82` status `ready` deltaP `45.1008` edge `1.0084` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `14.9124` n `82` status `ready` deltaP `22.8447` edge `1.1392` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.8983` n `82` status `ready` deltaP `32.7363` edge `0.9262` maxDD `-14.8998`
- `market_context_high->equity_24h` score `7.5789` n `82` status `ready` deltaP `18.5933` edge `1.3684` maxDD `-35.9896`
- `market_context_high->commodity_4h` score `3.0545` n `117` status `ready` deltaP `18.2015` edge `0.179` maxDD `-1.9973`
- `market_context_high->unknown_4h` score `0.5138` n `117` status `ready` deltaP `5.9582` edge `0.0793` maxDD `-3.7631`
- `market_context_high->commodity_1h` score `-0.0853` n `120` status `ready` deltaP `1.2375` edge `0.0269` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4776` n `120` status `ready` deltaP `4.2964` edge `0.0164` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.6566` n `82` status `ready` deltaP `3.3664` edge `-0.0044` maxDD `-0.4876`
- `market_context_high->fx_1h` score `-0.6831` n `120` status `ready` deltaP `-7.2006` edge `-0.0023` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.8177` n `120` status `ready` deltaP `3.2285` edge `0.0866` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.3331` n `120` status `ready` deltaP `-3.0339` edge `-0.0021` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3592` n `117` status `ready` deltaP `-12.8232` edge `-0.0044` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.3871` n `117` status `ready` deltaP `10.3464` edge `0.0441` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-2.2732` n `120` status `ready` deltaP `-1.4471` edge `0.0465` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.424` n `120` status `ready` deltaP `-7.4751` edge `-0.0128` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.641` n `120` status `ready` deltaP `3.3084` edge `-0.0577` maxDD `-12.7554`
- `market_context_high->crypto_alt_4h` score `-3.8143` n `117` status `ready` deltaP `12.8947` edge `0.2295` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-4.1445` n `117` status `ready` deltaP `5.3107` edge `-0.0388` maxDD `-36.5699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
