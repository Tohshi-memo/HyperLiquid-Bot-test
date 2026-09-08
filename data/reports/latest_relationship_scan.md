# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T02:52:29.893567+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10385`

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

- `market_context_high->unknown_24h` score `1939.8508` n `241` status `ready` deltaP `18.0937` edge `161.5388` maxDD `-0.0819`
- `risk_on_high->unknown_24h` score `1910.5423` n `117` status `ready` deltaP `18.9236` edge `159.0857` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `1910.5423` n `117` status `ready` deltaP `18.9236` edge `159.0857` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `9.0262` n `117` status `ready` deltaP `24.0251` edge `0.615` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `9.0262` n `117` status `ready` deltaP `24.0251` edge `0.615` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.9408` n `117` status `ready` deltaP `31.5497` edge `0.3219` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.9408` n `117` status `ready` deltaP `31.5497` edge `0.3219` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.1845` n `117` status `ready` deltaP `21.1005` edge `0.9308` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.1845` n `117` status `ready` deltaP `21.1005` edge `0.9308` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.8999` n `117` status `ready` deltaP `25.8287` edge `0.322` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8999` n `117` status `ready` deltaP `25.8287` edge `0.322` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `3.9788` n `241` status `ready` deltaP `16.6803` edge `0.3031` maxDD `-3.9523`
- `market_context_high->equity_24h` score `1.4193` n `241` status `ready` deltaP `9.8958` edge `0.0523` maxDD `0.0`
- `risk_on_high->index_24h` score `1.1765` n `117` status `ready` deltaP `11.8456` edge `0.0233` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.1765` n `117` status `ready` deltaP `11.8456` edge `0.0233` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `0.9418` n `117` status `ready` deltaP `3.9473` edge `0.0874` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9418` n `117` status `ready` deltaP `3.9473` edge `0.0874` maxDD `-1.1521`
- `risk_on_high->equity_24h` score `0.7341` n `117` status `ready` deltaP `9.8958` edge `-0.0048` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.7341` n `117` status `ready` deltaP `9.8958` edge `-0.0048` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.4857` n `117` status `ready` deltaP `14.2229` edge `-0.0012` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
