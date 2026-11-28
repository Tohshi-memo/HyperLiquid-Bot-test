# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T21:22:36.299679+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7484`

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

- `market_context_high->fx_1h` score `0.8015` n `72` status `ready` deltaP `13.0988` edge `0.0016` maxDD `-0.1042`
- `market_context_high->fx_4h` score `0.662` n `65` status `ready` deltaP `12.7439` edge `0.0098` maxDD `-0.1673`
- `market_context_high->metal_1h` score `0.2546` n `72` status `ready` deltaP `7.3935` edge `0.0042` maxDD `-0.2485`
- `market_context_high->commodity_1h` score `-0.0194` n `72` status `ready` deltaP `3.5263` edge `0.0086` maxDD `-0.4347`
- `market_context_high->equity_1h` score `-0.2072` n `72` status `ready` deltaP `6.2375` edge `-0.0079` maxDD `-2.1532`
- `market_context_high->index_1h` score `-0.455` n `72` status `ready` deltaP `-0.8982` edge `-0.003` maxDD `-0.2813`
- `market_context_high->metal_4h` score `-0.4831` n `65` status `ready` deltaP `0.2979` edge `0.0083` maxDD `-0.4441`
- `market_context_high->crypto_major_1h` score `-1.2142` n `72` status `ready` deltaP `-4.4661` edge `0.0016` maxDD `-7.5329`
- `market_context_high->equity_4h` score `-3.9572` n `65` status `ready` deltaP `-20.7692` edge `-0.1652` maxDD `-6.9605`
- `market_context_high->commodity_4h` score `-4.2421` n `65` status `ready` deltaP `-26.3415` edge `-0.0201` maxDD `-2.9572`
- `market_context_high->crypto_alt_1h` score `-4.3994` n `72` status `ready` deltaP `-9.506` edge `-0.1079` maxDD `-11.9607`
- `market_context_high->index_4h` score `-4.5652` n `65` status `ready` deltaP `-27.3804` edge `-0.0231` maxDD `-0.984`
- `market_context_high->crypto_major_4h` score `-9.5769` n `65` status `ready` deltaP `-11.4564` edge `-0.2712` maxDD `-22.7068`
- `market_context_high->crypto_alt_4h` score `-20.1` n `65` status `ready` deltaP `-34.8101` edge `-0.6965` maxDD `-49.048`
- `market_context_high->unknown_4h` score `-670.4685` n `65` status `ready` deltaP `4.4066` edge `-55.8968` maxDD `-0.063`
- `market_context_high->unknown_1h` score `-1324.8967` n `72` status `ready` deltaP `1.4388` edge `-110.406` maxDD `-0.2652`
- `news_risk_high->unknown_4h` score `3087.3812` n `28` status `thin_sample` deltaP `5.9451` edge `275.6194` maxDD `0.0`
- `news_risk_high->unknown_1h` score `3030.0691` n `28` status `thin_sample` deltaP `8.3832` edge `270.486` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `26.0737` n `28` status `thin_sample` deltaP `41.1458` edge `2.0537` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.4352` n `28` status `thin_sample` deltaP `39.2361` edge `1.563` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
