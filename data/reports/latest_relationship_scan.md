# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T10:07:29.850483+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12406`

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

- `news_risk_high->unknown_1h` score `750.9161` n `59` status `ready` deltaP `-6.3585` edge `62.6609` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `22.2221` n `91` status `ready` deltaP `40.3388` edge `1.6059` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `22.2221` n `91` status `ready` deltaP `40.3388` edge `1.6059` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `19.6554` n `167` status `ready` deltaP `36.2525` edge `1.479` maxDD `-3.9523`
- `market_context_high->equity_24h` score `9.1997` n `167` status `ready` deltaP `34.8958` edge `0.534` maxDD `0.0`
- `risk_on_high->equity_24h` score `8.9513` n `91` status `ready` deltaP `34.8958` edge `0.5133` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.9513` n `91` status `ready` deltaP `34.8958` edge `0.5133` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.7985` n `91` status `ready` deltaP `41.3361` edge `0.4948` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.7985` n `91` status `ready` deltaP `41.3361` edge `0.4948` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.3635` n `91` status `ready` deltaP `31.4393` edge `0.4899` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.3635` n `91` status `ready` deltaP `31.4393` edge `0.4899` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.3376` n `91` status `ready` deltaP `25.021` edge `1.1807` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.3376` n `91` status `ready` deltaP `25.021` edge `1.1807` maxDD `-24.5429`
- `risk_on_high->index_24h` score `5.4713` n `91` status `ready` deltaP `50.6964` edge `0.1222` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.4713` n `91` status `ready` deltaP `50.6964` edge `0.1222` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.3637` n `167` status `ready` deltaP `43.2147` edge `0.1149` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.4938` n `91` status `ready` deltaP `33.9554` edge `0.0741` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.4938` n `91` status `ready` deltaP `33.9554` edge `0.0741` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.441` n `167` status `ready` deltaP `27.9739` edge `0.0996` maxDD `-2.6138`
- `risk_on_high->equity_1h` score `1.6393` n `91` status `ready` deltaP `21.4829` edge `0.0212` maxDD `-0.2246`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
