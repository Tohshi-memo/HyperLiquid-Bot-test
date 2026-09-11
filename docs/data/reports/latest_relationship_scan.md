# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T14:52:32.043476+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12479`

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

- `news_risk_high->unknown_1h` score `751.0865` n `59` status `ready` deltaP `-6.0591` edge `62.6731` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `23.1475` n `91` status `ready` deltaP `41.9013` edge `1.6726` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `23.1475` n `91` status `ready` deltaP `41.9013` edge `1.6726` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `20.7499` n `156` status `ready` deltaP `37.1394` edge `1.5643` maxDD `-3.9523`
- `risk_on_high->equity_24h` score `9.5216` n `91` status `ready` deltaP `36.8056` edge `0.5481` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.5216` n `91` status `ready` deltaP `36.8056` edge `0.5481` maxDD `0.0`
- `market_context_high->equity_24h` score `9.2672` n `156` status `ready` deltaP `36.8056` edge `0.5269` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.4515` n `91` status `ready` deltaP `41.1837` edge `0.4669` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.4515` n `91` status `ready` deltaP `41.1837` edge `0.4669` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `7.3368` n `91` status `ready` deltaP `25.021` edge `1.1806` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.3368` n `91` status `ready` deltaP `25.021` edge `1.1806` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `6.6284` n `91` status `ready` deltaP `30.8296` edge `0.4327` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.6284` n `91` status `ready` deltaP `30.8296` edge `0.4327` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.5674` n `91` status `ready` deltaP `51.9116` edge `0.1221` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.5674` n `91` status `ready` deltaP `51.9116` edge `0.1221` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.3689` n `156` status `ready` deltaP `43.6698` edge `0.1123` maxDD `-0.1483`
- `market_context_high->crypto_alt_4h` score `3.6845` n `156` status `ready` deltaP `23.7844` edge `0.319` maxDD `-7.6417`
- `risk_on_high->equity_4h` score `3.626` n `91` status `ready` deltaP `34.1078` edge `0.0841` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.626` n `91` status `ready` deltaP `34.1078` edge `0.0841` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.0979` n `156` status `ready` deltaP `27.2397` edge `0.0759` maxDD `-2.6138`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
