# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T15:22:25.498267+00:00`
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

- `market_context_high->unknown_1h` score `1.2239` n `149` status `ready` deltaP `7.0068` edge `0.078` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.9033` n `145` status `ready` deltaP `18.524` edge `-0.0043` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.059` n `145` status `ready` deltaP `7.2487` edge `0.0095` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.036` n `149` status `ready` deltaP `6.5979` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0795` n `149` status `ready` deltaP `3.1648` edge `0.0046` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3128` n `149` status `ready` deltaP `5.1732` edge `0.0324` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.332` n `149` status `ready` deltaP `0.63` edge `-0.0049` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3545` n `145` status `ready` deltaP `7.3581` edge `-0.017` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.4517` n `145` status `ready` deltaP `5.0926` edge `0.0117` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.8309` n `145` status `ready` deltaP `-3.2695` edge `0.0003` maxDD `-2.4692`
- `market_context_high->fx_24h` score `-0.9999` n `133` status `ready` deltaP `3.044` edge `0.0125` maxDD `-2.2121`
- `market_context_high->commodity_1h` score `-1.1243` n `149` status `ready` deltaP `-8.3219` edge `-0.0029` maxDD `-1.1941`
- `market_context_high->equity_4h` score `-1.6887` n `145` status `ready` deltaP `-0.7874` edge `0.0694` maxDD `-16.1188`
- `market_context_high->crypto_alt_4h` score `-2.2159` n `145` status `ready` deltaP `4.4039` edge `-0.0672` maxDD `-7.0785`
- `market_context_high->commodity_24h` score `-2.371` n `133` status `ready` deltaP `-6.9836` edge `0.0323` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-2.3925` n `149` status `ready` deltaP `-1.935` edge `-0.037` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.4745` n `149` status `ready` deltaP `-4.7592` edge `-0.1101` maxDD `-7.8171`
- `market_context_high->index_24h` score `-4.5105` n `133` status `ready` deltaP `-8.9926` edge `-0.0376` maxDD `-21.1244`
- `market_context_high->crypto_major_4h` score `-5.4816` n `145` status `ready` deltaP `-0.2712` edge `-0.322` maxDD `-5.6395`
- `market_context_high->metal_24h` score `-5.5674` n `133` status `ready` deltaP `-26.0665` edge `-0.2092` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
