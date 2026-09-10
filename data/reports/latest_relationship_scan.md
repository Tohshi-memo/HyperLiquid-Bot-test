# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T10:52:30.151982+00:00`
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

- `risk_on_high->crypto_alt_24h` score `16.5607` n `91` status `ready` deltaP `33.7416` edge `1.1781` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `16.5607` n `91` status `ready` deltaP `33.7416` edge `1.1781` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `11.972` n `201` status `ready` deltaP `25.3058` edge `0.9117` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.9147` n `91` status `ready` deltaP `39.9642` edge `0.4303` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.9147` n `91` status `ready` deltaP `39.9642` edge `0.4303` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `6.1302` n `91` status `ready` deltaP `29.7625` edge `0.3983` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.1302` n `91` status `ready` deltaP `29.7625` edge `0.3983` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `5.5241` n `91` status `ready` deltaP `22.5905` edge `0.9644` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.5241` n `91` status `ready` deltaP `22.5905` edge `0.9644` maxDD `-24.5429`
- `risk_on_high->index_24h` score `3.3061` n `91` status `ready` deltaP `34.5505` edge `0.0494` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.3061` n `91` status `ready` deltaP `34.5505` edge `0.0494` maxDD `-0.0051`
- `market_context_high->equity_24h` score `3.0864` n `201` status `ready` deltaP `18.75` edge `0.1322` maxDD `0.0`
- `market_context_high->index_24h` score `2.4343` n `201` status `ready` deltaP `28.892` edge `0.0496` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.043` n `91` status `ready` deltaP `26.6383` edge `0.002` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `2.043` n `91` status `ready` deltaP `26.6383` edge `0.002` maxDD `-0.0802`
- `market_context_high->commodity_24h` score `1.8611` n `201` status `ready` deltaP `18.452` edge `0.046` maxDD `-0.1139`
- `risk_on_high->commodity_24h` score `1.8449` n `91` status `ready` deltaP `18.1185` edge `0.0423` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.8449` n `91` status `ready` deltaP `18.1185` edge `0.0423` maxDD `-0.0811`
- `risk_on_high->equity_24h` score `1.4808` n `91` status `ready` deltaP `18.75` edge `-0.0016` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.4808` n `91` status `ready` deltaP `18.75` edge `-0.0016` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
