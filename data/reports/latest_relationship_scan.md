# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T11:07:35.782998+00:00`
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

- `market_context_high->unknown_24h` score `36.7086` n `46` status `ready` deltaP `23.3469` edge `2.9077` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `7.9549` n `46` status `ready` deltaP `41.395` edge `0.4043` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `7.9186` n `46` status `ready` deltaP `36.5262` edge `0.4343` maxDD `-0.434`
- `market_context_high->unknown_4h` score `5.4981` n `88` status `ready` deltaP `1.0532` edge `0.5507` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1786` n `88` status `ready` deltaP `15.2162` edge `0.0814` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.2804` n `88` status `ready` deltaP `6.1309` edge `0.0241` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.229` n `88` status `ready` deltaP `16.1031` edge `0.008` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.1664` n `88` status `ready` deltaP `7.8321` edge `-0.0035` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4943` n `88` status `ready` deltaP `1.1296` edge `-0.0175` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5635` n `88` status `ready` deltaP `-1.9189` edge `-0.01` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6222` n `88` status `ready` deltaP `3.8249` edge `0.0182` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.9694` n `88` status `ready` deltaP `3.2567` edge `-0.007` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2707` n `88` status `ready` deltaP `-3.4703` edge `-0.0117` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.6515` n `88` status `ready` deltaP `4.5659` edge `-0.0886` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.902` n `88` status `ready` deltaP `-10.7262` edge `-0.0469` maxDD `-4.7021`
- `market_context_high->fx_24h` score `-2.0177` n `46` status `ready` deltaP `-7.5257` edge `0.0026` maxDD `-4.3126`
- `market_context_high->unknown_1h` score `-3.5166` n `88` status `ready` deltaP `1.5515` edge `-0.2587` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6931` n `88` status `ready` deltaP `-13.3982` edge `-0.0811` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-5.0083` n `46` status `ready` deltaP `-25.2038` edge `-0.1325` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.9796` n `88` status `ready` deltaP `-1.1918` edge `-0.3538` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
