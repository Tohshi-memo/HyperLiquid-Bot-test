# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T03:22:32.377614+00:00`
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

- `market_context_high->unknown_24h` score `12.4324` n `90` status `ready` deltaP `4.4445` edge `1.0107` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `3.8982` n `109` status `ready` deltaP `-1.6503` edge `0.4354` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2432` n `109` status `ready` deltaP `14.209` edge `0.0935` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.7721` n `90` status `ready` deltaP `2.0139` edge `0.2024` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.7352` n `90` status `ready` deltaP `23.8542` edge `0.0558` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4107` n `109` status `ready` deltaP `7.7597` edge `0.0241` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.032` n `109` status `ready` deltaP `5.9825` edge `-0.0022` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1407` n `109` status `ready` deltaP `9.0093` edge `0.0079` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5674` n `109` status `ready` deltaP `-2.159` edge `-0.0089` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7432` n `109` status `ready` deltaP `-3.3566` edge `-0.0195` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.9712` n `109` status `ready` deltaP `0.8028` edge `-0.0064` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.2901` n `90` status `ready` deltaP `0.5555` edge `-0.0248` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.4378` n `109` status `ready` deltaP `-4.6888` edge `-0.0175` maxDD `-3.0178`
- `market_context_high->index_24h` score `-1.6393` n `90` status `ready` deltaP `-4.8264` edge `0.0415` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.8471` n `109` status `ready` deltaP `1.1194` edge `-0.0907` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1635` n `109` status `ready` deltaP `-13.43` edge `-0.0624` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.1649` n `109` status `ready` deltaP `0.9272` edge `-0.0476` maxDD `-5.7857`
- `market_context_high->unknown_1h` score `-3.2561` n `109` status `ready` deltaP `2.1823` edge `-0.2412` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.2767` n `109` status `ready` deltaP `-11.299` edge `-0.0604` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.1435` n `90` status `ready` deltaP `9.6181` edge `-0.0303` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
