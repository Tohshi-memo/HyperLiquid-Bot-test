# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T10:52:32.087815+00:00`
- Price records: `672`
- Market context records: `7557`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14475`

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

- `risk_on_high->crypto_major_24h` score `7.6196` n `31` status `ready` deltaP `21.9646` edge `0.5662` maxDD `-4.8796`
- `risk_on_and_context->crypto_major_24h` score `7.6196` n `31` status `ready` deltaP `21.9646` edge `0.5662` maxDD `-4.8796`
- `risk_on_high->crypto_major_4h` score `6.7253` n `31` status `ready` deltaP `41.0848` edge `0.3058` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.7253` n `31` status `ready` deltaP `41.0848` edge `0.3058` maxDD `-0.8742`
- `risk_on_high->unknown_4h` score `4.7047` n `31` status `ready` deltaP `12.1558` edge `0.354` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.7047` n `31` status `ready` deltaP `12.1558` edge `0.354` maxDD `-0.4384`
- `risk_on_high->crypto_alt_24h` score `4.3057` n `31` status `ready` deltaP `20.4189` edge `0.2844` maxDD `-3.6039`
- `risk_on_and_context->crypto_alt_24h` score `4.3057` n `31` status `ready` deltaP `20.4189` edge `0.2844` maxDD `-3.6039`
- `risk_on_high->crypto_alt_4h` score `3.6971` n `31` status `ready` deltaP `28.9438` edge `0.1395` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `3.6971` n `31` status `ready` deltaP `28.9438` edge `0.1395` maxDD `-0.9492`
- `risk_on_high->crypto_major_1h` score `3.0293` n `31` status `ready` deltaP `26.9703` edge `0.0926` maxDD `-0.5971`
- `risk_on_and_context->crypto_major_1h` score `3.0293` n `31` status `ready` deltaP `26.9703` edge `0.0926` maxDD `-0.5971`
- `risk_on_high->equity_24h` score `1.9727` n `30` status `ready` deltaP `14.9477` edge `0.2539` maxDD `-5.7178`
- `risk_on_and_context->equity_24h` score `1.9727` n `30` status `ready` deltaP `14.9477` edge `0.2539` maxDD `-5.7178`
- `risk_on_high->unknown_24h` score `1.0874` n `31` status `ready` deltaP `8.9885` edge `0.0529` maxDD `-0.4433`
- `risk_on_and_context->unknown_24h` score `1.0874` n `31` status `ready` deltaP `8.9885` edge `0.0529` maxDD `-0.4433`
- `risk_on_high->equity_1h` score `0.8171` n `31` status `ready` deltaP `11.8183` edge `0.0595` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.8171` n `31` status `ready` deltaP `11.8183` edge `0.0595` maxDD `-1.3497`
- `risk_on_high->fx_24h` score `0.6653` n `30` status `ready` deltaP `17.6423` edge `0.0133` maxDD `-1.3162`
- `risk_on_and_context->fx_24h` score `0.6653` n `30` status `ready` deltaP `17.6423` edge `0.0133` maxDD `-1.3162`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
