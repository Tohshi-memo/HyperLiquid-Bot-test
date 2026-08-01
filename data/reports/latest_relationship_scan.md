# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T09:37:30.618599+00:00`
- Price records: `672`
- Market context records: `8608`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `4751.3343` n `64` status `ready` deltaP `34.6512` edge `395.7556` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.9469` n `35` status `ready` deltaP `50.6165` edge `1.2812` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `5.8085` n `64` status `ready` deltaP `20.2863` edge `0.4085` maxDD `-3.4427`
- `market_context_high->crypto_major_24h` score `3.7366` n `35` status `ready` deltaP `13.2904` edge `0.6675` maxDD `-17.8312`
- `market_context_high->fx_24h` score `3.5696` n `35` status `ready` deltaP `36.3308` edge `0.0891` maxDD `-0.3737`
- `news_risk_high->index_4h` score `2.2721` n `64` status `ready` deltaP `19.4849` edge `0.0785` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7358` n `64` status `ready` deltaP `16.1879` edge `0.0844` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.6324` n `62` status `ready` deltaP `12.0661` edge `0.1513` maxDD `-5.323`
- `news_risk_high->crypto_major_4h` score `1.1305` n `64` status `ready` deltaP `8.0408` edge `0.1689` maxDD `-3.5385`
- `market_context_high->metal_24h` score `0.55` n `35` status `ready` deltaP `6.358` edge `0.0814` maxDD `-1.9029`
- `news_risk_high->crypto_alt_4h` score `0.4701` n `64` status `ready` deltaP `11.6629` edge `0.1217` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4048` n `64` status `ready` deltaP `7.7378` edge `0.053` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.368` n `64` status `ready` deltaP `7.1399` edge `0.0508` maxDD `-2.0972`
- `market_context_high->index_24h` score `0.3097` n `35` status `ready` deltaP `17.6231` edge `0.0272` maxDD `-4.0651`
- `news_risk_high->fx_1h` score `0.1087` n `64` status `ready` deltaP `5.6591` edge `0.0043` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0509` n `64` status `ready` deltaP `11.6843` edge `0.0221` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.046` n `64` status `ready` deltaP `4.2998` edge `0.0089` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `0.0178` n `64` status `ready` deltaP `2.7136` edge `0.0318` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.1164` n `64` status `ready` deltaP `3.4847` edge `0.0074` maxDD `-0.5599`
- `market_context_high->fx_4h` score `-0.1174` n `62` status `ready` deltaP `8.5089` edge `0.0131` maxDD `-1.3685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
