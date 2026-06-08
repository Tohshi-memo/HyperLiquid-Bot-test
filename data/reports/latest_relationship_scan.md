# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T19:07:27.577775+00:00`
- Price records: `672`
- Market context records: `3308`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13151`

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

- `risk_on_high->crypto_major_4h` score `15.8201` n `32` status `ready` deltaP `29.7256` edge `1.2324` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8201` n `32` status `ready` deltaP `29.7256` edge `1.2324` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `14.567` n `124` status `ready` deltaP `20.4021` edge `2.7157` maxDD `-70.3986`
- `market_context_high->index_24h` score `10.3183` n `124` status `ready` deltaP `32.146` edge `0.901` maxDD `-16.1026`
- `market_context_high->equity_24h` score `8.3446` n `124` status `ready` deltaP `23.7063` edge `1.7534` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.3829` n `32` status `ready` deltaP `9.9848` edge `0.7331` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.3829` n `32` status `ready` deltaP `9.9848` edge `0.7331` maxDD `-11.7537`
- `market_context_high->commodity_24h` score `7.3728` n `124` status `ready` deltaP `32.2581` edge `0.588` maxDD `-9.7587`
- `risk_on_high->equity_4h` score `3.5632` n `32` status `ready` deltaP `13.7957` edge `0.4783` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5632` n `32` status `ready` deltaP `13.7957` edge `0.4783` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.3566` n `124` status `ready` deltaP `21.2926` edge `2.2301` maxDD `-152.2601`
- `risk_on_high->crypto_major_1h` score `2.0837` n `32` status `ready` deltaP `7.3166` edge `0.3253` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.0837` n `32` status `ready` deltaP `7.3166` edge `0.3253` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `2.0535` n `184` status `ready` deltaP `19.0416` edge `0.14` maxDD `-3.9989`
- `risk_on_high->index_4h` score `1.0798` n `32` status `ready` deltaP `0.8384` edge `0.1916` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.0798` n `32` status `ready` deltaP `0.8384` edge `0.1916` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.2837` n `32` status `ready` deltaP `6.3997` edge `0.0622` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2837` n `32` status `ready` deltaP `6.3997` edge `0.0622` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.247` n `32` status `ready` deltaP `0.5988` edge `0.1714` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.247` n `32` status `ready` deltaP `0.5988` edge `0.1714` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
