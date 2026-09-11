# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T09:52:32.447401+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12398`

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

- `news_risk_high->unknown_1h` score `750.8525` n `59` status `ready` deltaP `-6.5082` edge `62.6566` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `22.1686` n `91` status `ready` deltaP `40.1652` edge `1.6026` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `22.1686` n `91` status `ready` deltaP `40.1652` edge `1.6026` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `19.562` n `168` status `ready` deltaP `36.1359` edge `1.472` maxDD `-3.9523`
- `market_context_high->equity_24h` score `9.1834` n `168` status `ready` deltaP `34.7222` edge `0.5338` maxDD `0.0`
- `risk_on_high->equity_24h` score `8.9026` n `91` status `ready` deltaP `34.7222` edge `0.5104` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.9026` n `91` status `ready` deltaP `34.7222` edge `0.5104` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.8153` n `91` status `ready` deltaP `41.3361` edge `0.4962` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.8153` n `91` status `ready` deltaP `41.3361` edge `0.4962` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.3935` n `91` status `ready` deltaP `31.4393` edge `0.4924` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.3935` n `91` status `ready` deltaP `31.4393` edge `0.4924` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.3329` n `91` status `ready` deltaP `25.021` edge `1.1801` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.3329` n `91` status `ready` deltaP `25.021` edge `1.1801` maxDD `-24.5429`
- `risk_on_high->index_24h` score `5.4551` n `91` status `ready` deltaP `50.5227` edge `0.122` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.4551` n `91` status `ready` deltaP `50.5227` edge `0.122` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.3526` n `168` status `ready` deltaP `43.1051` edge `0.1147` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.4926` n `91` status `ready` deltaP `33.9554` edge `0.074` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.4926` n `91` status `ready` deltaP `33.9554` edge `0.074` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.471` n `168` status `ready` deltaP `28.0488` edge `0.1016` maxDD `-2.6138`
- `risk_on_high->equity_1h` score `1.6381` n `91` status `ready` deltaP `21.4829` edge `0.0211` maxDD `-0.2246`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
