# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T12:22:29.450544+00:00`
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

- `news_risk_high->unknown_1h` score `751.078` n `59` status `ready` deltaP `-5.9094` edge `62.6714` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `22.8319` n `91` status `ready` deltaP `41.9013` edge `1.6463` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `22.8319` n `91` status `ready` deltaP `41.9013` edge `1.6463` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `20.6835` n `158` status `ready` deltaP `37.2692` edge `1.5579` maxDD `-3.9523`
- `risk_on_high->equity_24h` score `9.3835` n `91` status `ready` deltaP `36.4583` edge `0.5389` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.3835` n `91` status `ready` deltaP `36.4583` edge `0.5389` maxDD `0.0`
- `market_context_high->equity_24h` score `9.3391` n `158` status `ready` deltaP `36.4583` edge `0.5352` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.6917` n `91` status `ready` deltaP `41.3361` edge `0.4859` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.6917` n `91` status `ready` deltaP `41.3361` edge `0.4859` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `7.4016` n `91` status `ready` deltaP `25.021` edge `1.1889` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.4016` n `91` status `ready` deltaP `25.021` edge `1.1889` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `7.0743` n `91` status `ready` deltaP `31.4393` edge `0.4658` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.0743` n `91` status `ready` deltaP `31.4393` edge `0.4658` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.595` n `91` status `ready` deltaP `51.9116` edge `0.1244` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.595` n `91` status `ready` deltaP `51.9116` edge `0.1244` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.4298` n `158` status `ready` deltaP `43.8159` edge `0.1164` maxDD `-0.1483`
- `market_context_high->crypto_alt_4h` score `4.0176` n `158` status `ready` deltaP `24.2127` edge `0.3439` maxDD `-7.6417`
- `risk_on_high->equity_4h` score `3.5602` n `91` status `ready` deltaP `34.2603` edge `0.0776` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.5602` n `91` status `ready` deltaP `34.2603` edge `0.0776` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.2833` n `158` status `ready` deltaP `27.5626` edge `0.0892` maxDD `-2.6138`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
