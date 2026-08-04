# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T09:22:24.025048+00:00`
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

- `market_context_high->unknown_24h` score `37.0362` n `46` status `ready` deltaP `24.5622` edge `2.9269` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `8.3521` n `46` status `ready` deltaP `42.6102` edge `0.4293` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `7.9462` n `46` status `ready` deltaP `36.5262` edge `0.4366` maxDD `-0.434`
- `market_context_high->unknown_4h` score `5.6195` n `88` status `ready` deltaP `1.2056` edge `0.5598` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.198` n `88` status `ready` deltaP `15.3687` edge `0.082` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.2551` n `88` status `ready` deltaP `16.5604` edge `0.0083` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2097` n `88` status `ready` deltaP `5.5321` edge `0.0222` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1556` n `88` status `ready` deltaP `7.6824` edge `-0.0034` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4569` n `88` status `ready` deltaP `1.7284` edge `-0.0167` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5417` n `88` status `ready` deltaP `-1.6195` edge `-0.0092` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6104` n `88` status `ready` deltaP `3.9773` edge `0.0187` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.9348` n `88` status `ready` deltaP `3.5615` edge `-0.0046` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2395` n `88` status `ready` deltaP `-3.1709` edge `-0.0111` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5588` n `88` status `ready` deltaP `5.3144` edge `-0.0817` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.8799` n `88` status `ready` deltaP `-10.4213` edge `-0.0461` maxDD `-4.7021`
- `market_context_high->fx_24h` score `-1.8965` n `46` status `ready` deltaP `-6.3104` edge `0.0046` maxDD `-4.3126`
- `market_context_high->unknown_1h` score `-3.4327` n `88` status `ready` deltaP `2.4497` edge `-0.2577` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5984` n `88` status `ready` deltaP `-12.6497` edge `-0.0782` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.9704` n `46` status `ready` deltaP `-25.0302` edge `-0.1305` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.7268` n `88` status `ready` deltaP `-0.1248` edge `-0.3285` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
