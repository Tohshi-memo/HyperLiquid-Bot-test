# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T12:37:34.032051+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9804`

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

- `market_context_high->crypto_alt_4h` score `8.2858` n `117` status `ready` deltaP `21.49` edge `0.6921` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `7.3014` n `117` status `ready` deltaP `25.3883` edge `0.5951` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.8747` n `54` status `ready` deltaP `23.7692` edge `0.4592` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.8747` n `54` status `ready` deltaP `23.7692` edge `0.4592` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.9145` n `48` status `ready` deltaP `31.8261` edge `0.2807` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9145` n `48` status `ready` deltaP `31.8261` edge `0.2807` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `5.2857` n `54` status `ready` deltaP `38.4937` edge `0.5063` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.2857` n `54` status `ready` deltaP `38.4937` edge `0.5063` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `3.3414` n `117` status `ready` deltaP `-3.467` edge `0.3662` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `2.228` n `117` status `ready` deltaP `15.5126` edge `0.189` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.6638` n `117` status `ready` deltaP `8.5061` edge `0.1625` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.068` n `117` status `ready` deltaP `12.2408` edge `0.0286` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.0749` n `54` status `ready` deltaP `3.9477` edge `0.0363` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.0749` n `54` status `ready` deltaP `3.9477` edge `0.0363` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.2651` n `117` status `ready` deltaP `1.9982` edge `0.0026` maxDD `-0.3742`
- `risk_on_high->crypto_alt_1h` score `-0.285` n `54` status `ready` deltaP `5.2562` edge `0.031` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.285` n `54` status `ready` deltaP `5.2562` edge `0.031` maxDD `-5.8734`
- `market_context_high->metal_1h` score `-0.4261` n `117` status `ready` deltaP `6.8159` edge `0.006` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.4884` n `117` status `ready` deltaP `1.975` edge `-0.001` maxDD `-1.3154`
- `risk_on_high->metal_1h` score `-0.4913` n `54` status `ready` deltaP `1.4028` edge `0.0008` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
