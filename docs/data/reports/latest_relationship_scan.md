# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T08:37:27.563074+00:00`
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

- `market_context_high->unknown_1h` score `1.3669` n `133` status `ready` deltaP `7.9387` edge `0.0837` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.5099` n `133` status `ready` deltaP `20.1758` edge `-0.0481` maxDD `-0.5133`
- `market_context_high->index_1h` score `0.1452` n `133` status `ready` deltaP `10.0074` edge `0.005` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.1034` n `133` status `ready` deltaP `8.0575` edge `0.0098` maxDD `-0.3539`
- `market_context_high->equity_1h` score `-0.1734` n `133` status `ready` deltaP `7.0134` edge `0.038` maxDD `-5.2257`
- `market_context_high->fx_1h` score `-0.1782` n `133` status `ready` deltaP `1.2809` edge `0.0045` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2203` n `133` status `ready` deltaP `7.5382` edge `-0.0169` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.2802` n `133` status `ready` deltaP `1.5803` edge `-0.0046` maxDD `-0.6822`
- `market_context_high->commodity_1h` score `-0.6386` n `133` status `ready` deltaP `-3.6727` edge `-0.0008` maxDD `-1.1941`
- `market_context_high->index_4h` score `-0.645` n `133` status `ready` deltaP `1.5542` edge `0.0105` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.7123` n `133` status `ready` deltaP `-1.6184` edge `0.0045` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8335` n `133` status `ready` deltaP `-0.1789` edge `0.0119` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.4408` n `133` status `ready` deltaP `-2.4481` edge `-0.0659` maxDD `-4.1996`
- `market_context_high->commodity_24h` score `-1.5812` n `107` status `ready` deltaP `-5.1207` edge `0.0857` maxDD `-4.666`
- `market_context_high->equity_4h` score `-1.73` n `133` status `ready` deltaP `-1.3628` edge `0.0678` maxDD `-16.1079`
- `market_context_high->crypto_alt_4h` score `-1.7903` n `133` status `ready` deltaP `4.9652` edge `-0.0553` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.4797` n `107` status `ready` deltaP `-7.0581` edge `0.0014` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.1942` n `107` status `ready` deltaP `-4.9406` edge `-0.0526` maxDD `-18.8413`
- `market_context_high->metal_24h` score `-5.0902` n `107` status `ready` deltaP `-20.3401` edge `-0.1862` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.3007` n `133` status `ready` deltaP `-1.9542` edge `-0.3266` maxDD `-3.1677`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
