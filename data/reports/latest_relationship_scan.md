# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T09:37:30.656560+00:00`
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

- `market_context_high->unknown_24h` score `36.9887` n `46` status `ready` deltaP `24.3886` edge `2.9241` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `8.2974` n `46` status `ready` deltaP `42.4366` edge `0.4259` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `7.939` n `46` status `ready` deltaP `36.5262` edge `0.436` maxDD `-0.434`
- `market_context_high->unknown_4h` score `5.6039` n `88` status `ready` deltaP `1.2056` edge `0.5585` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1992` n `88` status `ready` deltaP `15.3687` edge `0.0821` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.2464` n `88` status `ready` deltaP `16.408` edge `0.0082` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2109` n `88` status `ready` deltaP `5.5321` edge `0.0223` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1424` n `88` status `ready` deltaP `7.5327` edge `-0.0035` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4569` n `88` status `ready` deltaP `1.7284` edge `-0.0167` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5432` n `88` status `ready` deltaP `-1.6195` edge `-0.0094` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6112` n `88` status `ready` deltaP `3.9773` edge `0.0186` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.9324` n `88` status `ready` deltaP `3.5615` edge `-0.0043` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2228` n `88` status `ready` deltaP `-3.0212` edge `-0.0107` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5588` n `88` status `ready` deltaP `5.3144` edge `-0.0817` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.8799` n `88` status `ready` deltaP `-10.4213` edge `-0.0461` maxDD `-4.7021`
- `market_context_high->fx_24h` score `-1.914` n `46` status `ready` deltaP `-6.484` edge `0.0043` maxDD `-4.3126`
- `market_context_high->unknown_1h` score `-3.4327` n `88` status `ready` deltaP `2.4497` edge `-0.2577` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5996` n `88` status `ready` deltaP `-12.6497` edge `-0.0783` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.9879` n `46` status `ready` deltaP `-25.2038` edge `-0.1308` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.7449` n `88` status `ready` deltaP `-0.2772` edge `-0.3298` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
