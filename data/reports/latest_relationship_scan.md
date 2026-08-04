# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T07:22:51.677654+00:00`
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

- `market_context_high->unknown_24h` score `37.3627` n `46` status `ready` deltaP `25.7775` edge `2.946` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `8.8832` n `46` status `ready` deltaP `43.9991` edge `0.4643` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `7.9961` n `46` status `ready` deltaP `36.6998` edge `0.4396` maxDD `-0.434`
- `market_context_high->unknown_4h` score `5.8199` n `88` status `ready` deltaP `2.1203` edge `0.5704` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1786` n `88` status `ready` deltaP `15.2162` edge `0.0814` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.3279` n `88` status `ready` deltaP `17.7799` edge `0.0095` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2673` n `88` status `ready` deltaP `5.9812` edge `0.024` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.17` n `88` status `ready` deltaP `7.8321` edge `-0.0032` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4577` n `88` status `ready` deltaP `1.7284` edge `-0.0168` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5105` n `88` status `ready` deltaP `-1.1704` edge `-0.0082` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.522` n `88` status `ready` deltaP `5.1968` edge `0.0219` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.9647` n `88` status `ready` deltaP `3.2567` edge `-0.0064` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2383` n `88` status `ready` deltaP `-3.3206` edge `-0.01` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5424` n `88` status `ready` deltaP `5.6138` edge `-0.0816` maxDD `-10.619`
- `market_context_high->fx_24h` score `-1.7518` n `46` status `ready` deltaP `-4.9215` edge `0.0074` maxDD `-4.3126`
- `market_context_high->index_4h` score `-1.816` n `88` status `ready` deltaP `-9.5067` edge `-0.044` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.3416` n `88` status `ready` deltaP `3.0485` edge `-0.2541` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5792` n `88` status `ready` deltaP `-12.5` edge `-0.0776` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.8583` n `46` status `ready` deltaP `-23.9885` edge `-0.1281` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.523` n `88` status `ready` deltaP `1.0947` edge `-0.3105` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
