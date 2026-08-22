# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T15:07:21.261056+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14802`

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

- `market_context_high->unknown_1h` score `1.1087` n `149` status `ready` deltaP `6.8571` edge `0.0694` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.8001` n `145` status `ready` deltaP `18.524` edge `-0.0129` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.059` n `145` status `ready` deltaP `7.2487` edge `0.0095` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.036` n `149` status `ready` deltaP `6.5979` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0717` n `149` status `ready` deltaP `3.3145` edge `0.0046` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3213` n `149` status `ready` deltaP `5.0235` edge `0.0323` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3398` n `149` status `ready` deltaP `0.4803` edge `-0.0049` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3533` n `145` status `ready` deltaP `7.3581` edge `-0.0169` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.4517` n `145` status `ready` deltaP `5.0926` edge `0.0117` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.8404` n `145` status `ready` deltaP `-3.422` edge `0.0001` maxDD `-2.4692`
- `market_context_high->fx_24h` score `-1.0169` n `132` status `ready` deltaP `2.762` edge `0.0122` maxDD `-2.2121`
- `market_context_high->commodity_1h` score `-1.1243` n `149` status `ready` deltaP `-8.3219` edge `-0.0029` maxDD `-1.1941`
- `market_context_high->equity_4h` score `-1.6974` n `145` status `ready` deltaP `-0.9399` edge `0.0693` maxDD `-16.1188`
- `market_context_high->crypto_alt_4h` score `-2.2377` n `145` status `ready` deltaP `4.2515` edge `-0.068` maxDD `-7.0785`
- `market_context_high->commodity_24h` score `-2.3163` n `132` status `ready` deltaP `-6.6446` edge `0.0346` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-2.4201` n `149` status `ready` deltaP `-2.0847` edge `-0.0383` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.5045` n `149` status `ready` deltaP `-4.9089` edge `-0.1116` maxDD `-7.8171`
- `market_context_high->index_24h` score `-4.5071` n `132` status `ready` deltaP `-8.87` edge `-0.0384` maxDD `-21.0907`
- `market_context_high->crypto_major_4h` score `-5.501` n `145` status `ready` deltaP `-0.4237` edge `-0.3226` maxDD `-5.6395`
- `market_context_high->metal_24h` score `-5.5588` n `132` status `ready` deltaP `-25.9154` edge `-0.2091` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
