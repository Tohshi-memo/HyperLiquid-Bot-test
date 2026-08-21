# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T21:37:22.933667+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14774`

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

- `market_context_high->unknown_1h` score `1.2563` n `133` status `ready` deltaP `8.8369` edge `0.0685` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.3178` n `133` status `ready` deltaP `22.0051` edge `-0.0763` maxDD `-0.5133`
- `market_context_high->index_1h` score `0.2153` n `133` status `ready` deltaP `11.3547` edge `0.005` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.1486` n `133` status `ready` deltaP `8.9722` edge `0.0095` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1089` n `133` status `ready` deltaP `2.6282` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2077` n `133` status `ready` deltaP `6.714` edge `0.0356` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3254` n `133` status `ready` deltaP `0.8318` edge `-0.0054` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.4266` n `133` status `ready` deltaP `4.1846` edge `-0.021` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.5594` n `133` status `ready` deltaP `3.2311` edge `0.0103` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.6082` n `133` status `ready` deltaP `-0.2464` edge `0.0087` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6768` n `133` status `ready` deltaP `-4.5709` edge `0.0003` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.716` n `133` status `ready` deltaP `0.5696` edge `0.0167` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-0.9958` n `105` status `ready` deltaP `-0.0992` edge `0.101` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.2623` n `133` status `ready` deltaP `-1.5499` edge `-0.049` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.332` n `133` status `ready` deltaP `3.8981` edge `-0.01` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.8043` n `133` status `ready` deltaP `-1.5152` edge `0.0593` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.4818` n `105` status `ready` deltaP `-6.9197` edge `0.0003` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-3.9867` n `133` status `ready` deltaP `-0.1249` edge `-0.2293` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.2977` n `105` status `ready` deltaP `-6.9842` edge `-0.0542` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.827` n `105` status `ready` deltaP `-18.4574` edge `-0.165` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
