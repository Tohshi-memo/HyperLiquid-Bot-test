# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T12:52:31.811356+00:00`
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

- `market_context_high->unknown_24h` score `36.4911` n `46` status `ready` deltaP `22.6525` edge `2.8942` maxDD `-0.0103`
- `market_context_high->commodity_24h` score `8.1046` n `46` status `ready` deltaP `37.7415` edge `0.4417` maxDD `-0.434`
- `market_context_high->crypto_alt_24h` score `7.5168` n `46` status `ready` deltaP `40.1797` edge `0.3759` maxDD `-0.3889`
- `market_context_high->unknown_4h` score `5.4799` n `88` status `ready` deltaP `0.9007` edge `0.5502` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.193` n `88` status `ready` deltaP `15.2162` edge `0.0826` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.2424` n `89` status `ready` deltaP `5.655` edge `0.0241` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.2408` n `88` status `ready` deltaP `16.2555` edge `0.0085` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.2009` n `89` status `ready` deltaP `8.2033` edge `-0.0031` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.462` n `89` status `ready` deltaP `1.6148` edge `-0.0166` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5457` n `89` status `ready` deltaP `-1.5323` edge `-0.0103` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6339` n `88` status `ready` deltaP `3.8249` edge `0.0167` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8837` n `88` status `ready` deltaP `4.0189` edge `-0.0011` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2021` n `89` status `ready` deltaP `-2.7333` edge `-0.0109` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.6218` n `89` status `ready` deltaP `4.8375` edge `-0.0866` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.902` n `88` status `ready` deltaP `-10.7262` edge `-0.0469` maxDD `-4.7021`
- `market_context_high->fx_24h` score `-2.1306` n `46` status `ready` deltaP `-8.7409` edge `0.0013` maxDD `-4.3126`
- `market_context_high->unknown_1h` score `-3.471` n `89` status `ready` deltaP `2.2119` edge `-0.2593` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6236` n `89` status `ready` deltaP `-12.9954` edge `-0.078` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-5.1441` n `46` status `ready` deltaP `-25.551` edge `-0.1415` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-7.1552` n `88` status `ready` deltaP `-2.2589` edge `-0.3692` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
