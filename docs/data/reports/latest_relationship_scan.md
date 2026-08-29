# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T16:07:25.163649+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11276`

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

- `news_risk_high->unknown_24h` score `42.5111` n `62` status `ready` deltaP `8.7702` edge `3.5815` maxDD `-4.1232`
- `news_risk_high->crypto_alt_24h` score `19.182` n `62` status `ready` deltaP `30.3708` edge `1.7336` maxDD `-22.3391`
- `market_context_high->unknown_24h` score `9.3047` n `104` status `ready` deltaP `20.4327` edge `0.7124` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.3362` n `79` status `ready` deltaP `11.2689` edge `0.5119` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.5878` n `104` status `ready` deltaP `33.1998` edge `0.2629` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.6423` n `79` status `ready` deltaP `4.9629` edge `0.2228` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.5512` n `121` status `ready` deltaP `18.4036` edge `0.1331` maxDD `-0.7887`
- `news_risk_high->fx_4h` score `2.5184` n `79` status `ready` deltaP `36.3615` edge `0.0224` maxDD `-0.3953`
- `market_context_high->unknown_1h` score `0.9698` n `133` status `ready` deltaP `9.3029` edge `0.0669` maxDD `-1.5148`
- `news_risk_high->equity_24h` score `0.8578` n `62` status `ready` deltaP `17.6915` edge `0.2829` maxDD `-18.9364`
- `risk_on_high->metal_1h` score `0.7887` n `33` status `ready` deltaP `11.6903` edge `0.0092` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `0.7887` n `33` status `ready` deltaP `11.6903` edge `0.0092` maxDD `-0.0463`
- `risk_on_high->crypto_alt_1h` score `0.7588` n `33` status `ready` deltaP `14.2715` edge `0.0497` maxDD `-2.1381`
- `risk_on_and_context->crypto_alt_1h` score `0.7588` n `33` status `ready` deltaP `14.2715` edge `0.0497` maxDD `-2.1381`
- `news_risk_high->fx_1h` score `0.7425` n `79` status `ready` deltaP `14.2841` edge `0.0055` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.3966` n `79` status `ready` deltaP `11.7259` edge `0.0047` maxDD `-0.5618`
- `news_risk_high->metal_24h` score `0.3564` n `62` status `ready` deltaP `29.85` edge `-0.0013` maxDD `-7.827`
- `market_context_high->crypto_major_4h` score `0.3067` n `121` status `ready` deltaP `19.55` edge `0.2403` maxDD `-20.9394`
- `news_risk_high->index_24h` score `0.0951` n `62` status `ready` deltaP `13.6256` edge `0.0076` maxDD `-2.2325`
- `market_context_high->crypto_alt_4h` score `-0.0437` n `121` status `ready` deltaP `21.8366` edge `0.3354` maxDD `-31.4361`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
