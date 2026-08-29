# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T16:37:25.361673+00:00`
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

- `news_risk_high->unknown_24h` score `40.4117` n `63` status `ready` deltaP `9.0774` edge `3.4045` maxDD `-4.1232`
- `news_risk_high->crypto_alt_24h` score `18.7931` n `63` status `ready` deltaP `30.7292` edge `1.6988` maxDD `-22.3391`
- `market_context_high->unknown_24h` score `9.6503` n `104` status `ready` deltaP `20.4327` edge `0.7412` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.2971` n `78` status `ready` deltaP `10.9444` edge `0.5108` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6191` n `104` status `ready` deltaP `33.547` edge `0.2632` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.6937` n `78` status `ready` deltaP `4.8404` edge `0.2279` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.5652` n `123` status `ready` deltaP `18.6992` edge `0.1323` maxDD `-0.7887`
- `news_risk_high->fx_4h` score `1.6369` n `78` status `ready` deltaP `36.3743` edge `0.0223` maxDD `-0.3953`
- `risk_on_high->metal_1h` score `0.9549` n `35` status `ready` deltaP `13.7682` edge `0.0092` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `0.9549` n `35` status `ready` deltaP `13.7682` edge `0.0092` maxDD `-0.0463`
- `risk_on_high->crypto_alt_1h` score `0.8883` n `35` status `ready` deltaP `16.1762` edge `0.0536` maxDD `-2.1381`
- `risk_on_and_context->crypto_alt_1h` score `0.8883` n `35` status `ready` deltaP `16.1762` edge `0.0536` maxDD `-2.1381`
- `market_context_high->unknown_1h` score `0.8479` n `135` status `ready` deltaP `8.5441` edge `0.0618` maxDD `-1.5148`
- `news_risk_high->equity_24h` score `0.8397` n `63` status `ready` deltaP `18.2292` edge `0.277` maxDD `-18.9364`
- `news_risk_high->fx_1h` score `0.7118` n `78` status `ready` deltaP `13.9145` edge `0.0054` maxDD `-0.108`
- `market_context_high->crypto_major_4h` score `0.4751` n `123` status `ready` deltaP `20.0203` edge `0.2512` maxDD `-20.9394`
- `news_risk_high->commodity_1h` score `0.3682` n `78` status `ready` deltaP `11.2391` edge `0.0043` maxDD `-0.5618`
- `news_risk_high->metal_24h` score `0.1523` n `63` status `ready` deltaP `27.381` edge `-0.002` maxDD `-7.8811`
- `market_context_high->crypto_alt_4h` score `0.1007` n `123` status `ready` deltaP `22.3069` edge `0.3443` maxDD `-31.4361`
- `news_risk_high->index_24h` score `0.0422` n `63` status `ready` deltaP `12.6984` edge `0.007` maxDD `-2.2325`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
