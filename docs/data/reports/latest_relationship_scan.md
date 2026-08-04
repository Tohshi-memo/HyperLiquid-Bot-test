# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T17:07:55.609190+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9839`

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

- `market_context_high->unknown_24h` score `28.3987` n `57` status `ready` deltaP `21.6831` edge `2.2263` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.3081` n `89` status `ready` deltaP `0.4778` edge `0.5387` maxDD `-3.6303`
- `market_context_high->crypto_alt_24h` score `3.5172` n `57` status `ready` deltaP `21.4455` edge `0.2237` maxDD `-2.2189`
- `market_context_high->commodity_24h` score `1.3428` n `57` status `ready` deltaP `23.4923` edge `0.2075` maxDD `-11.6902`
- `market_context_high->commodity_4h` score `1.2045` n `89` status `ready` deltaP `15.225` edge `0.0835` maxDD `-2.7703`
- `market_context_high->fx_1h` score `0.2009` n `90` status `ready` deltaP `8.2036` edge `-0.0031` maxDD `-0.7878`
- `market_context_high->commodity_1h` score `0.1838` n `90` status `ready` deltaP `5.0432` edge `0.0233` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.181` n `89` status `ready` deltaP `15.1343` edge `0.0083` maxDD `-1.8797`
- `market_context_high->index_1h` score `-0.5098` n `90` status `ready` deltaP `0.8916` edge `-0.0179` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5573` n `90` status `ready` deltaP `-1.9062` edge `-0.0093` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.6907` n `90` status `ready` deltaP `-1.8596` edge `-0.0051` maxDD `-3.0178`
- `market_context_high->fx_24h` score `-0.7002` n `57` status `ready` deltaP `4.6692` edge `0.0311` maxDD `-4.3126`
- `market_context_high->metal_4h` score `-0.7052` n `89` status `ready` deltaP `3.2047` edge `0.0117` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8367` n `89` status `ready` deltaP `4.6383` edge `0.0008` maxDD `-5.7857`
- `market_context_high->metal_24h` score `-1.3411` n `57` status `ready` deltaP `-15.1499` edge `0.0459` maxDD `-2.6802`
- `market_context_high->equity_1h` score `-1.697` n `90` status `ready` deltaP `4.6507` edge `-0.095` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.9622` n `89` status `ready` deltaP `-11.1931` edge `-0.0515` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-3.4439` n `90` status `ready` deltaP `-12.0093` edge `-0.0696` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4912` n `90` status `ready` deltaP `2.0492` edge `-0.2599` maxDD `-1.2421`
- `market_context_high->index_24h` score `-3.8316` n `57` status `ready` deltaP `-19.1612` edge `-0.144` maxDD `-7.8922`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
