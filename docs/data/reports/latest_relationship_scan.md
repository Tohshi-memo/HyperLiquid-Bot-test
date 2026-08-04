# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T09:07:27.911129+00:00`
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

- `market_context_high->unknown_24h` score `37.0861` n `46` status `ready` deltaP `24.7358` edge `2.9299` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `8.408` n `46` status `ready` deltaP `42.7839` edge `0.4328` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `7.9534` n `46` status `ready` deltaP `36.5262` edge `0.4372` maxDD `-0.434`
- `market_context_high->unknown_4h` score `5.6363` n `88` status `ready` deltaP `1.2056` edge `0.5612` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1992` n `88` status `ready` deltaP `15.3687` edge `0.0821` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.2646` n `88` status `ready` deltaP `16.7129` edge `0.0085` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2133` n `88` status `ready` deltaP `5.5321` edge `0.0225` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1688` n `88` status `ready` deltaP `7.8321` edge `-0.0033` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4577` n `88` status `ready` deltaP `1.7284` edge `-0.0168` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5409` n `88` status `ready` deltaP `-1.6195` edge `-0.0091` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6009` n `88` status `ready` deltaP `4.1297` edge `0.0189` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.9482` n `88` status `ready` deltaP `3.4091` edge `-0.0053` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2551` n `88` status `ready` deltaP `-3.3206` edge `-0.0114` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5642` n `88` status `ready` deltaP `5.3144` edge `-0.0824` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.8712` n `88` status `ready` deltaP `-10.2689` edge `-0.046` maxDD `-4.7021`
- `market_context_high->fx_24h` score `-1.879` n `46` status `ready` deltaP `-6.1368` edge `0.0049` maxDD `-4.3126`
- `market_context_high->unknown_1h` score `-3.4196` n `88` status `ready` deltaP `2.5994` edge `-0.2576` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5972` n `88` status `ready` deltaP `-12.6497` edge `-0.0781` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.953` n `46` status `ready` deltaP `-24.8566` edge `-0.1302` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.7064` n `88` status `ready` deltaP `0.0277` edge `-0.3269` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
