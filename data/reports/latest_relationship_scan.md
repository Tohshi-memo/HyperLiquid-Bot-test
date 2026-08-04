# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T13:22:28.958852+00:00`
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

- `market_context_high->unknown_24h` score `36.4563` n `46` status `ready` deltaP `22.6525` edge `2.8913` maxDD `-0.0103`
- `market_context_high->commodity_24h` score `8.1804` n `46` status `ready` deltaP `38.0887` edge `0.4457` maxDD `-0.434`
- `market_context_high->crypto_alt_24h` score `7.3895` n `46` status `ready` deltaP `39.8325` edge `0.3676` maxDD `-0.3889`
- `market_context_high->unknown_4h` score `5.4447` n `88` status `ready` deltaP `0.5959` edge `0.5493` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.211` n `88` status `ready` deltaP `15.2162` edge `0.0841` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.2735` n `89` status `ready` deltaP `5.9544` edge `0.0247` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.2511` n `88` status `ready` deltaP `16.408` edge `0.0088` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.2129` n `89` status `ready` deltaP `8.353` edge `-0.0031` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4815` n `89` status `ready` deltaP `1.3154` edge `-0.0171` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5644` n `89` status `ready` deltaP `-1.8317` edge `-0.0107` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6433` n `88` status `ready` deltaP `3.8249` edge `0.0155` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8546` n `88` status `ready` deltaP `4.3237` edge `0.0006` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2189` n `89` status `ready` deltaP `-2.7333` edge `-0.0123` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.6701` n `89` status `ready` deltaP `4.8375` edge `-0.0928` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.9059` n `88` status `ready` deltaP `-10.7262` edge `-0.0474` maxDD `-4.7021`
- `market_context_high->fx_24h` score `-2.1619` n `46` status `ready` deltaP `-9.0882` edge `0.001` maxDD `-4.3126`
- `market_context_high->unknown_1h` score `-3.4578` n `89` status `ready` deltaP `2.3616` edge `-0.2592` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6512` n `89` status `ready` deltaP `-13.1451` edge `-0.0793` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-5.2223` n `46` status `ready` deltaP `-25.8982` edge `-0.1457` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-7.2077` n `88` status `ready` deltaP `-2.5638` edge `-0.3739` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
