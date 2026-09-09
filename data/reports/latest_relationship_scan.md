# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T13:52:35.419709+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10416`

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

- `risk_on_high->crypto_alt_24h` score `8.5295` n `117` status `ready` deltaP `20.7265` edge `0.5956` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `8.5295` n `117` status `ready` deltaP `20.7265` edge `0.5956` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.5104` n `117` status `ready` deltaP `31.8545` edge `0.284` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.5104` n `117` status `ready` deltaP `31.8545` edge `0.284` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `4.076` n `117` status `ready` deltaP `17.1074` edge `0.8153` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.076` n `117` status `ready` deltaP `17.1074` edge `0.8153` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `3.7062` n `117` status `ready` deltaP `22.3226` edge `0.2459` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `3.7062` n `117` status `ready` deltaP `22.3226` edge `0.2459` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `3.4821` n `241` status `ready` deltaP `13.3817` edge `0.2837` maxDD `-3.9523`
- `risk_on_high->index_24h` score `1.9762` n `117` status `ready` deltaP `21.047` edge `0.0286` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.9762` n `117` status `ready` deltaP `21.047` edge `0.0286` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.2547` n `241` status `ready` deltaP `16.1422` edge `0.0363` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.8171` n `117` status `ready` deltaP `3.3485` edge `0.081` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8171` n `117` status `ready` deltaP `3.3485` edge `0.081` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.6131` n `117` status `ready` deltaP `19.7383` edge `0.0626` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.6131` n `117` status `ready` deltaP `19.7383` edge `0.0626` maxDD `-0.9131`
- `risk_on_high->equity_1h` score `0.2112` n `117` status `ready` deltaP `12.5762` edge `-0.0131` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.2112` n `117` status `ready` deltaP `12.5762` edge `-0.0131` maxDD `-2.2516`
- `risk_on_high->metal_1h` score `0.2045` n `117` status `ready` deltaP `8.7812` edge `0.0007` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.2045` n `117` status `ready` deltaP `8.7812` edge `0.0007` maxDD `-0.3081`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
