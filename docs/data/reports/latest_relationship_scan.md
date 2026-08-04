# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T10:52:31.575554+00:00`
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

- `market_context_high->unknown_24h` score `36.7513` n `46` status `ready` deltaP `23.5205` edge `2.9101` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `8.0228` n `46` status `ready` deltaP `41.5686` edge `0.4088` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `7.9174` n `46` status `ready` deltaP `36.5262` edge `0.4342` maxDD `-0.434`
- `market_context_high->unknown_4h` score `5.5113` n `88` status `ready` deltaP `1.0532` edge `0.5518` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1786` n `88` status `ready` deltaP `15.2162` edge `0.0814` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.2625` n `88` status `ready` deltaP `5.9812` edge `0.0236` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.2369` n `88` status `ready` deltaP `16.2555` edge `0.008` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.1544` n `88` status `ready` deltaP `7.6824` edge `-0.0035` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4935` n `88` status `ready` deltaP `1.1296` edge `-0.0174` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5549` n `88` status `ready` deltaP `-1.7692` edge `-0.0099` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6222` n `88` status `ready` deltaP `3.8249` edge `0.0182` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.9583` n `88` status `ready` deltaP `3.4091` edge `-0.0066` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2551` n `88` status `ready` deltaP `-3.3206` edge `-0.0114` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.6312` n `88` status `ready` deltaP `4.7156` edge `-0.087` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.902` n `88` status `ready` deltaP `-10.7262` edge `-0.0469` maxDD `-4.7021`
- `market_context_high->fx_24h` score `-2.0003` n `46` status `ready` deltaP `-7.352` edge `0.0029` maxDD `-4.3126`
- `market_context_high->unknown_1h` score `-3.5034` n `88` status `ready` deltaP `1.7012` edge `-0.2586` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6715` n `88` status `ready` deltaP `-13.2485` edge `-0.0803` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-5.0023` n `46` status `ready` deltaP `-25.2038` edge `-0.132` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.946` n `88` status `ready` deltaP `-1.0394` edge `-0.3505` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
