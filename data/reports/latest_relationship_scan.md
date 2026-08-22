# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T06:17:23.503838+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14742`

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

- `market_context_high->unknown_1h` score `1.4568` n `133` status `ready` deltaP `8.3878` edge `0.0882` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.6104` n `133` status `ready` deltaP `20.938` edge `-0.0448` maxDD `-0.5133`
- `market_context_high->index_1h` score `0.1211` n `133` status `ready` deltaP `9.5583` edge `0.0049` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.1201` n `133` status `ready` deltaP `8.3624` edge `0.0099` maxDD `-0.3539`
- `market_context_high->equity_1h` score `-0.175` n `133` status `ready` deltaP `7.0134` edge `0.0378` maxDD `-5.2257`
- `market_context_high->fx_1h` score `-0.1868` n `133` status `ready` deltaP `1.1312` edge `0.0044` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.288` n `133` status `ready` deltaP `1.4306` edge `-0.0046` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.2954` n `133` status `ready` deltaP `6.3187` edge `-0.0184` maxDD `-1.5942`
- `market_context_high->commodity_1h` score `-0.6472` n `133` status `ready` deltaP `-3.9721` edge `0.0001` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.6712` n `133` status `ready` deltaP `-1.0086` edge `0.0057` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.6814` n `133` status `ready` deltaP `0.9445` edge `0.0099` maxDD `-2.618`
- `market_context_high->crypto_alt_1h` score `-0.7999` n `133` status `ready` deltaP `-0.0292` edge `0.0137` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.3754` n `133` status `ready` deltaP `-1.5499` edge `-0.0635` maxDD `-4.1996`
- `market_context_high->commodity_24h` score `-1.5294` n `105` status `ready` deltaP `-5.1339` edge `0.0901` maxDD `-4.666`
- `market_context_high->equity_4h` score `-1.83` n `133` status `ready` deltaP `-2.4299` edge `0.0621` maxDD `-16.1079`
- `market_context_high->crypto_alt_4h` score `-2.4226` n `133` status `ready` deltaP `4.0506` edge `-0.1019` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.4806` n `105` status `ready` deltaP `-6.9197` edge `0.0004` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.2387` n `105` status `ready` deltaP `-5.5953` edge `-0.0559` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-5.0879` n `105` status `ready` deltaP `-20.7143` edge `-0.1834` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.5815` n `133` status `ready` deltaP `-1.9542` edge `-0.35` maxDD `-3.1677`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
