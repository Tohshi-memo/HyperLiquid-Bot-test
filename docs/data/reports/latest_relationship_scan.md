# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T14:22:33.563538+00:00`
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

- `market_context_high->unknown_24h` score `36.4131` n `46` status `ready` deltaP `22.6525` edge `2.8877` maxDD `-0.0103`
- `market_context_high->commodity_24h` score `8.3524` n `46` status `ready` deltaP `38.7832` edge `0.4554` maxDD `-0.434`
- `market_context_high->crypto_alt_24h` score `7.2525` n `46` status `ready` deltaP `39.4852` edge `0.3585` maxDD `-0.3889`
- `market_context_high->unknown_4h` score `5.1751` n `89` status `ready` deltaP `-0.2844` edge `0.5327` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.0199` n `89` status `ready` deltaP `14.4628` edge `0.0732` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.2915` n `89` status `ready` deltaP `5.9544` edge `0.0262` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.2134` n `89` status `ready` deltaP `15.7441` edge `0.0084` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.1997` n `89` status `ready` deltaP `8.2033` edge `-0.0032` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.5057` n `89` status `ready` deltaP `1.016` edge `-0.0182` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5753` n `89` status `ready` deltaP `-1.9814` edge `-0.0111` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.599` n `89` status `ready` deltaP `4.2718` edge `0.0182` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8753` n `89` status `ready` deltaP `4.181` edge `-0.0011` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.1674` n `89` status `ready` deltaP `-2.2842` edge `-0.011` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.7356` n `89` status `ready` deltaP `4.5381` edge `-0.0992` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.856` n `89` status `ready` deltaP `-10.1261` edge `-0.045` maxDD `-4.7021`
- `market_context_high->fx_24h` score `-2.2295` n `46` status `ready` deltaP `-9.7826` edge `0.0` maxDD `-4.3126`
- `market_context_high->unknown_1h` score `-3.4075` n `89` status `ready` deltaP `2.8107` edge `-0.258` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5805` n `89` status `ready` deltaP `-12.696` edge `-0.0764` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-5.3672` n `46` status `ready` deltaP `-26.4191` edge `-0.1543` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-7.1404` n `89` status `ready` deltaP `-2.2437` edge `-0.3674` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
