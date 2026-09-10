# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T11:07:28.663347+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11908`

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

- `risk_on_high->crypto_alt_24h` score `16.7174` n `91` status `ready` deltaP `33.9152` edge `1.19` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `16.7174` n `91` status `ready` deltaP `33.9152` edge `1.19` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `12.1287` n `201` status `ready` deltaP `25.4794` edge `0.9236` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.9749` n `91` status `ready` deltaP `40.1166` edge `0.4343` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.9749` n `91` status `ready` deltaP `40.1166` edge `0.4343` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `6.2204` n `91` status `ready` deltaP `29.9149` edge `0.4048` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.2204` n `91` status `ready` deltaP `29.9149` edge `0.4048` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `5.6283` n `91` status `ready` deltaP `22.7641` edge `0.9766` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.6283` n `91` status `ready` deltaP `22.7641` edge `0.9766` maxDD `-24.5429`
- `risk_on_high->index_24h` score `3.3296` n `91` status `ready` deltaP `34.7241` edge `0.0502` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.3296` n `91` status `ready` deltaP `34.7241` edge `0.0502` maxDD `-0.0051`
- `market_context_high->equity_24h` score `3.1663` n `201` status `ready` deltaP `18.9236` edge `0.1377` maxDD `0.0`
- `market_context_high->index_24h` score `2.4578` n `201` status `ready` deltaP `29.0656` edge `0.0504` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.0816` n `91` status `ready` deltaP `26.7907` edge `0.0042` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `2.0816` n `91` status `ready` deltaP `26.7907` edge `0.0042` maxDD `-0.0802`
- `market_context_high->commodity_24h` score `1.8364` n `201` status `ready` deltaP `18.2784` edge `0.0451` maxDD `-0.1139`
- `risk_on_high->commodity_24h` score `1.8202` n `91` status `ready` deltaP `17.9449` edge `0.0414` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.8202` n `91` status `ready` deltaP `17.9449` edge `0.0414` maxDD `-0.0811`
- `risk_on_high->equity_24h` score `1.5607` n `91` status `ready` deltaP `18.9236` edge `0.0039` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.5607` n `91` status `ready` deltaP `18.9236` edge `0.0039` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
