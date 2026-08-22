# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T04:22:24.983974+00:00`
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

- `market_context_high->unknown_1h` score `1.3402` n `133` status `ready` deltaP `9.4357` edge `0.0715` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.7558` n `133` status `ready` deltaP `22.0051` edge `-0.0398` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1628` n `133` status `ready` deltaP `9.1246` edge `0.0103` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1281` n `133` status `ready` deltaP `9.708` edge `0.0048` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1626` n `133` status `ready` deltaP `1.5803` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.1836` n `133` status `ready` deltaP `7.1631` edge `0.0357` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3075` n `133` status `ready` deltaP `1.1312` edge `-0.0051` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3633` n `133` status `ready` deltaP `5.2517` edge `-0.02` maxDD `-1.5942`
- `market_context_high->commodity_4h` score `-0.5844` n `133` status `ready` deltaP `0.2109` edge `0.0087` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6269` n `133` status `ready` deltaP `-3.6727` edge `0.0007` maxDD `-1.1941`
- `market_context_high->index_4h` score `-0.6925` n `133` status `ready` deltaP `0.792` edge `0.0095` maxDD `-2.618`
- `market_context_high->crypto_alt_1h` score `-1.1203` n `133` status `ready` deltaP `-0.1789` edge `-0.012` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-1.3763` n `105` status `ready` deltaP `-3.745` edge `0.0936` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.4815` n `133` status `ready` deltaP `-1.4002` edge `-0.0781` maxDD `-4.1996`
- `market_context_high->equity_4h` score `-1.8794` n `133` status `ready` deltaP `-2.7348` edge `0.0578` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.3587` n `105` status `ready` deltaP `-5.5308` edge `0.0013` maxDD `-2.2121`
- `market_context_high->crypto_alt_4h` score `-2.4892` n `133` status `ready` deltaP `3.5932` edge `-0.1044` maxDD `-5.4926`
- `market_context_high->index_24h` score `-4.3105` n `105` status `ready` deltaP `-6.8105` edge `-0.057` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-5.0899` n `105` status `ready` deltaP `-20.8879` edge `-0.1825` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.3215` n `133` status `ready` deltaP `-1.3444` edge `-0.3324` maxDD `-3.1677`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
