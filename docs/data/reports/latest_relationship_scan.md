# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T21:22:39.683382+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9645`

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

- `market_context_high->unknown_1h` score `84.7723` n `47` status `ready` deltaP `10.116` edge `7.004` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `45.6101` n `47` status `ready` deltaP `30.4226` edge `3.6373` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.2632` n `47` status `ready` deltaP `24.782` edge `2.3947` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.1679` n `47` status `ready` deltaP `32.1587` edge `1.9185` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.9384` n `47` status `ready` deltaP `35.8045` edge `0.4358` maxDD `-0.3705`
- `news_risk_high->unknown_1h` score `5.7057` n `114` status `ready` deltaP `-4.0498` edge `0.5269` maxDD `-0.9543`
- `market_context_high->metal_24h` score `4.1092` n `47` status `ready` deltaP `34.8848` edge `0.1337` maxDD `-0.2401`
- `news_risk_high->crypto_alt_1h` score `3.3178` n `114` status `ready` deltaP `16.1572` edge `0.2178` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.9133` n `47` status `ready` deltaP `33.4166` edge `0.0354` maxDD `-0.2323`
- `news_risk_high->crypto_major_4h` score `2.7247` n `104` status `ready` deltaP `17.507` edge `0.3235` maxDD `-13.719`
- `news_risk_high->crypto_alt_4h` score `2.6476` n `104` status `ready` deltaP `8.9939` edge `0.4058` maxDD `-15.9436`
- `news_risk_high->crypto_major_1h` score `2.4937` n `114` status `ready` deltaP `16.798` edge `0.1435` maxDD `-1.8141`
- `market_context_high->equity_4h` score `2.3721` n `47` status `ready` deltaP `16.992` edge `0.1262` maxDD `-1.3444`
- `news_risk_high->commodity_24h` score `2.2983` n `80` status `ready` deltaP `23.5764` edge `0.09` maxDD `-1.7857`
- `news_risk_high->fx_4h` score `1.6278` n `104` status `ready` deltaP `23.6163` edge `0.0418` maxDD `-0.421`
- `news_risk_high->metal_1h` score `1.5212` n `114` status `ready` deltaP `19.511` edge `0.0252` maxDD `-0.6142`
- `news_risk_high->crypto_major_24h` score `1.33` n `80` status `ready` deltaP `-4.4444` edge `1.1044` maxDD `-63.6743`
- `market_context_high->index_1h` score `1.011` n `47` status `ready` deltaP `15.2089` edge `0.0107` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9546` n `47` status `ready` deltaP `11.7658` edge `0.0414` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.7663` n `80` status `ready` deltaP `22.9167` edge `0.0903` maxDD `-7.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
