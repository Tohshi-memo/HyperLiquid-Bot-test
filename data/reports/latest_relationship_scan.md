# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T10:37:25.778157+00:00`
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

- `market_context_high->unknown_24h` score `36.7988` n `46` status `ready` deltaP `23.6942` edge `2.9129` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `8.0846` n `46` status `ready` deltaP `41.7422` edge `0.4128` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `7.9186` n `46` status `ready` deltaP `36.5262` edge `0.4343` maxDD `-0.434`
- `market_context_high->unknown_4h` score `5.5281` n `88` status `ready` deltaP `1.0532` edge `0.5532` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.181` n `88` status `ready` deltaP `15.2162` edge `0.0816` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.2433` n `88` status `ready` deltaP `5.8315` edge `0.023` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.2369` n `88` status `ready` deltaP `16.2555` edge `0.008` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.1412` n `88` status `ready` deltaP `7.5327` edge `-0.0036` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4849` n `88` status `ready` deltaP `1.2793` edge `-0.0173` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5533` n `88` status `ready` deltaP `-1.7692` edge `-0.0097` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6214` n `88` status `ready` deltaP `3.8249` edge `0.0183` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.9434` n `88` status `ready` deltaP `3.5615` edge `-0.0057` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2371` n `88` status `ready` deltaP `-3.1709` edge `-0.0109` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.6125` n `88` status `ready` deltaP `4.8653` edge `-0.0856` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.8933` n `88` status `ready` deltaP `-10.5737` edge `-0.0468` maxDD `-4.7021`
- `market_context_high->fx_24h` score `-1.984` n `46` status `ready` deltaP `-7.1784` edge `0.0031` maxDD `-4.3126`
- `market_context_high->unknown_1h` score `-3.4878` n `88` status `ready` deltaP `1.8509` edge `-0.2583` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6487` n `88` status `ready` deltaP `-13.0988` edge `-0.0794` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.9963` n `46` status `ready` deltaP `-25.2038` edge `-0.1315` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.9061` n `88` status `ready` deltaP `-0.887` edge `-0.3464` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
