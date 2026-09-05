# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T02:22:31.711076+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10456`

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

- `risk_on_high->unknown_4h` score `19.6783` n `133` status `ready` deltaP `8.0838` edge `1.6478` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.6783` n `133` status `ready` deltaP `8.0838` edge `1.6478` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `9.1808` n `217` status `ready` deltaP `8.5204` edge `0.7778` maxDD `-2.563`
- `news_risk_high->crypto_alt_24h` score `6.9817` n `38` status `ready` deltaP `24.4608` edge `0.4457` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `4.0243` n `38` status `ready` deltaP `23.4101` edge `0.1835` maxDD `-0.0034`
- `news_risk_high->crypto_major_4h` score `3.576` n `38` status `ready` deltaP `16.1746` edge `0.2327` maxDD `-1.0693`
- `news_risk_high->metal_4h` score `2.2336` n `38` status `ready` deltaP `22.6573` edge `0.0572` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.925` n `38` status `ready` deltaP `12.2111` edge `0.0991` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.6497` n `38` status `ready` deltaP `14.0167` edge `0.0831` maxDD `-0.7924`
- `news_risk_high->index_1h` score `1.288` n `38` status `ready` deltaP `16.1756` edge `0.0129` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `1.2308` n `38` status `ready` deltaP `14.7416` edge `0.0236` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `1.1829` n `38` status `ready` deltaP `5.9486` edge `0.0772` maxDD `-0.4628`
- `news_risk_high->crypto_alt_4h` score `1.0528` n `38` status `ready` deltaP `8.0552` edge `0.0669` maxDD `-1.296`
- `news_risk_high->crypto_alt_1h` score `0.8926` n `38` status `ready` deltaP `8.2178` edge `0.0461` maxDD `-0.7867`
- `risk_on_high->metal_1h` score `0.121` n `133` status `ready` deltaP `12.8619` edge `0.001` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.121` n `133` status `ready` deltaP `12.8619` edge `0.001` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `0.0513` n `38` status `ready` deltaP `7.1699` edge `0.0034` maxDD `-0.9036`
- `news_risk_high->fx_24h` score `0.0293` n `38` status `ready` deltaP `10.8004` edge `0.0362` maxDD `-3.1274`
- `risk_on_high->index_1h` score `-0.1964` n `133` status `ready` deltaP `3.3936` edge `-0.0033` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1964` n `133` status `ready` deltaP `3.3936` edge `-0.0033` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
