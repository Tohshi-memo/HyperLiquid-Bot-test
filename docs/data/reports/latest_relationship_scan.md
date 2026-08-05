# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T23:22:25.672225+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11685`

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

- `market_context_high->unknown_24h` score `12.7576` n `90` status `ready` deltaP `4.4445` edge `1.0378` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `2.9234` n `109` status `ready` deltaP `-1.9551` edge `0.3562` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2022` n `109` status `ready` deltaP `14.0566` edge `0.0911` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8844` n `90` status `ready` deltaP `2.0139` edge `0.2168` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.8263` n `90` status `ready` deltaP `24.7223` edge `0.0617` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4275` n `109` status `ready` deltaP `7.7597` edge `0.0255` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.056` n `109` status `ready` deltaP `6.2819` edge `-0.0022` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1035` n `109` status `ready` deltaP `9.6191` edge `0.0086` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.4918` n `109` status `ready` deltaP `-1.1111` edge `-0.0062` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7461` n `109` status `ready` deltaP `3.2418` edge `0.0062` maxDD `-3.211`
- `market_context_high->index_1h` score `-0.7837` n `109` status `ready` deltaP `-3.9554` edge `-0.0207` maxDD `-1.6054`
- `market_context_high->crypto_alt_24h` score `-1.3096` n `90` status `ready` deltaP `0.5555` edge `-0.0273` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.493` n `109` status `ready` deltaP `-4.6888` edge `-0.0221` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.8853` n `109` status `ready` deltaP `0.5206` edge `-0.0916` maxDD `-10.619`
- `market_context_high->index_24h` score `-2.059` n `90` status `ready` deltaP `-7.6042` edge `0.0062` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.1825` n `109` status `ready` deltaP `-13.7349` edge `-0.0628` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.2531` n `109` status `ready` deltaP `0.4699` edge `-0.0519` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-3.308` n `109` status `ready` deltaP `-10.9996` edge `-0.065` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.5177` n `109` status `ready` deltaP `1.8829` edge `-0.261` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0863` n `90` status `ready` deltaP `10.3125` edge `-0.0276` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
