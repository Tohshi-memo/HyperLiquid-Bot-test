# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T12:17:06.661447+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9833`

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

- `market_context_high->unknown_24h` score `36.5271` n `46` status `ready` deltaP `22.6525` edge `2.8972` maxDD `-0.0103`
- `market_context_high->commodity_24h` score `8.0348` n `46` status `ready` deltaP `37.3943` edge `0.4382` maxDD `-0.434`
- `market_context_high->crypto_alt_24h` score `7.6538` n `46` status `ready` deltaP `40.5269` edge `0.385` maxDD `-0.3889`
- `market_context_high->unknown_4h` score `5.4957` n `88` status `ready` deltaP `1.0532` edge `0.5505` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1846` n `88` status `ready` deltaP `15.2162` edge `0.0819` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.2483` n `89` status `ready` deltaP `5.8047` edge `0.0236` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.24` n `88` status `ready` deltaP `16.2555` edge `0.0084` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.1757` n `89` status `ready` deltaP `7.9039` edge `-0.0032` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4613` n `89` status `ready` deltaP `1.6148` edge `-0.0165` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5309` n `89` status `ready` deltaP `-1.3826` edge `-0.0094` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6253` n `88` status `ready` deltaP `3.8249` edge `0.0178` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.9136` n `88` status `ready` deltaP `3.714` edge `-0.0029` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.1794` n `89` status `ready` deltaP `-2.5836` edge `-0.01` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5984` n `89` status `ready` deltaP `4.9872` edge `-0.0846` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.9013` n `88` status `ready` deltaP `-10.7262` edge `-0.0468` maxDD `-4.7021`
- `market_context_high->fx_24h` score `-2.098` n `46` status `ready` deltaP `-8.3937` edge `0.0017` maxDD `-4.3126`
- `market_context_high->unknown_1h` score `-3.5033` n `89` status `ready` deltaP `1.9125` edge `-0.26` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5985` n `89` status `ready` deltaP `-12.8457` edge `-0.0769` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-5.0647` n `46` status `ready` deltaP `-25.2038` edge `-0.1372` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-7.1051` n `88` status `ready` deltaP `-1.954` edge `-0.3648` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
