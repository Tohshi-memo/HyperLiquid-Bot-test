# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T19:07:34.277007+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->equity_24h` score `1.412` n `140` status `ready` deltaP `4.0529` edge `0.4207` maxDD `-21.0709`
- `market_context_high->commodity_4h` score `0.881` n `176` status `ready` deltaP `12.0566` edge `0.0645` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.8048` n `140` status `ready` deltaP `19.5197` edge `0.0177` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.7105` n `183` status `ready` deltaP `9.5858` edge `0.0296` maxDD `-0.7439`
- `market_context_high->fx_1h` score `-0.1228` n `183` status `ready` deltaP `4.383` edge `0.0002` maxDD `-0.613`
- `market_context_high->fx_4h` score `-0.1747` n `176` status `ready` deltaP `5.7927` edge `0.0068` maxDD `-0.4647`
- `market_context_high->index_24h` score `-0.2578` n `140` status `ready` deltaP `3.7744` edge `0.1065` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.6102` n `183` status `ready` deltaP `-4.0231` edge `-0.0037` maxDD `-0.8168`
- `market_context_high->metal_24h` score `-0.7672` n `140` status `ready` deltaP `1.7108` edge `0.0571` maxDD `-2.9283`
- `market_context_high->index_4h` score `-0.7995` n `176` status `ready` deltaP `-2.0926` edge `-0.0103` maxDD `-1.26`
- `market_context_high->metal_1h` score `-0.8394` n `183` status `ready` deltaP `-5.026` edge `-0.0105` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-1.0355` n `183` status `ready` deltaP `-3.4014` edge `-0.0152` maxDD `-5.2573`
- `market_context_high->crypto_alt_1h` score `-1.8117` n `183` status `ready` deltaP `-10.3408` edge `-0.0443` maxDD `-6.5229`
- `market_context_high->metal_4h` score `-2.003` n `176` status `ready` deltaP `-6.7212` edge `-0.0356` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.2585` n `176` status `ready` deltaP `-11.3775` edge `-0.1024` maxDD `-10.1608`
- `market_context_high->crypto_major_24h` score `-3.3247` n `140` status `ready` deltaP `0.5497` edge `-0.0313` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-3.8683` n `183` status `ready` deltaP `-10.5657` edge `-0.0615` maxDD `-11.9002`
- `market_context_high->crypto_alt_24h` score `-4.0367` n `140` status `ready` deltaP `-10.978` edge `-0.1189` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-6.0649` n `176` status `ready` deltaP `-11.7932` edge `-0.1354` maxDD `-16.6446`
- `market_context_high->commodity_24h` score `-8.6267` n `140` status `ready` deltaP `-5.3751` edge `-0.1986` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
