# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T11:22:29.377088+00:00`
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

- `market_context_high->unknown_24h` score `36.6671` n `46` status `ready` deltaP `23.1733` edge `2.9054` maxDD `-0.0103`
- `market_context_high->commodity_24h` score `7.9373` n `46` status `ready` deltaP `36.6998` edge `0.4347` maxDD `-0.434`
- `market_context_high->crypto_alt_24h` score `7.899` n `46` status `ready` deltaP `41.2214` edge `0.4008` maxDD `-0.3889`
- `market_context_high->unknown_4h` score `5.4945` n `88` status `ready` deltaP `1.0532` edge `0.5504` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1798` n `88` status `ready` deltaP `15.2162` edge `0.0815` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.229` n `88` status `ready` deltaP `16.1031` edge `0.008` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.1968` n `89` status `ready` deltaP `5.655` edge `0.0203` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.123` n `89` status `ready` deltaP `7.3051` edge `-0.0036` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4605` n `89` status `ready` deltaP `1.6148` edge `-0.0164` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5231` n `89` status `ready` deltaP `-1.3826` edge `-0.0084` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6222` n `88` status `ready` deltaP `3.8249` edge `0.0182` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.9812` n `88` status `ready` deltaP `3.1042` edge `-0.0075` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2129` n `89` status `ready` deltaP `-2.883` edge `-0.0108` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5914` n `89` status `ready` deltaP `4.9872` edge `-0.0837` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.9028` n `88` status `ready` deltaP `-10.7262` edge `-0.047` maxDD `-4.7021`
- `market_context_high->fx_24h` score `-2.034` n `46` status `ready` deltaP `-7.6993` edge `0.0024` maxDD `-4.3126`
- `market_context_high->unknown_1h` score `-3.4949` n `89` status `ready` deltaP `2.0622` edge `-0.2603` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5769` n `89` status `ready` deltaP `-12.696` edge `-0.0761` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-5.0167` n `46` status `ready` deltaP `-25.2038` edge `-0.1332` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-7.0156` n `88` status `ready` deltaP `-1.3443` edge `-0.3574` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
