# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T04:07:25.651388+00:00`
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

- `market_context_high->unknown_1h` score `1.3666` n `133` status `ready` deltaP `9.5854` edge `0.0727` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.7908` n `133` status `ready` deltaP `22.1575` edge `-0.0379` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1715` n `133` status `ready` deltaP `9.277` edge `0.0104` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1273` n `133` status `ready` deltaP `9.708` edge `0.0047` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1549` n `133` status `ready` deltaP `1.73` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.1921` n `133` status `ready` deltaP `7.0134` edge `0.0356` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3083` n `133` status `ready` deltaP `1.1312` edge `-0.0052` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3641` n `133` status `ready` deltaP `5.2517` edge `-0.0201` maxDD `-1.5942`
- `market_context_high->commodity_4h` score `-0.5742` n `133` status `ready` deltaP `0.3633` edge `0.009` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6269` n `133` status `ready` deltaP `-3.6727` edge `0.0007` maxDD `-1.1941`
- `market_context_high->index_4h` score `-0.6925` n `133` status `ready` deltaP `0.792` edge `0.0095` maxDD `-2.618`
- `market_context_high->crypto_alt_1h` score `-1.1143` n `133` status `ready` deltaP `-0.1789` edge `-0.0115` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-1.36` n `105` status `ready` deltaP `-3.5714` edge `0.0938` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.4822` n `133` status `ready` deltaP `-1.4002` edge `-0.0782` maxDD `-4.1996`
- `market_context_high->equity_4h` score `-1.8794` n `133` status `ready` deltaP `-2.7348` edge `0.0578` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.3424` n `105` status `ready` deltaP `-5.3572` edge `0.0015` maxDD `-2.2121`
- `market_context_high->crypto_alt_4h` score `-2.422` n `133` status `ready` deltaP `3.5932` edge `-0.0988` maxDD `-5.4926`
- `market_context_high->index_24h` score `-4.3195` n `105` status `ready` deltaP `-6.9842` edge `-0.057` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-5.0883` n `105` status `ready` deltaP `-20.8879` edge `-0.1823` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.2385` n `133` status `ready` deltaP `-1.192` edge `-0.3265` maxDD `-3.1677`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
