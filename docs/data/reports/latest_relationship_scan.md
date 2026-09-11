# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T03:52:32.621957+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11398`

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

- `news_risk_high->unknown_1h` score `923.0085` n `52` status `ready` deltaP `-9.7881` edge `77.0248` maxDD `-1.7068`
- `news_risk_high->unknown_4h` score `652.9196` n `40` status `ready` deltaP `-25.6707` edge `54.6461` maxDD `-2.1996`
- `risk_on_high->crypto_alt_24h` score `20.8227` n `91` status `ready` deltaP `36.3458` edge `1.5159` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.8227` n `91` status `ready` deltaP `36.3458` edge `1.5159` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `17.5157` n `190` status `ready` deltaP `32.3666` edge `1.3266` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.9585` n `91` status `ready` deltaP `41.641` edge `0.5061` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9585` n `91` status `ready` deltaP `41.641` edge `0.5061` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.4564` n `190` status `ready` deltaP `30.5556` edge `0.501` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.8007` n `91` status `ready` deltaP `32.6588` edge `0.5182` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.8007` n `91` status `ready` deltaP `32.6588` edge `0.5182` maxDD `-3.8693`
- `risk_on_high->equity_24h` score `7.3176` n `91` status `ready` deltaP `30.5556` edge `0.4061` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `7.3176` n `91` status `ready` deltaP `30.5556` edge `0.4061` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.29` n `91` status `ready` deltaP `25.021` edge `1.1746` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.29` n `91` status `ready` deltaP `25.021` edge `1.1746` maxDD `-24.5429`
- `risk_on_high->index_24h` score `4.9645` n `91` status `ready` deltaP `46.3561` edge `0.1089` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.9645` n `91` status `ready` deltaP `46.3561` edge `0.1089` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.9949` n `190` status `ready` deltaP `40.1791` edge `0.1044` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.6594` n `91` status `ready` deltaP `33.9554` edge `0.0879` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.6594` n `91` status `ready` deltaP `33.9554` edge `0.0879` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.5148` n `190` status `ready` deltaP `27.3909` edge `0.1125` maxDD `-2.843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
