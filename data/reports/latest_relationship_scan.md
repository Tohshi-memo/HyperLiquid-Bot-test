# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T00:22:37.842360+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11245`

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

- `news_risk_high->unknown_1h` score `383.0844` n `82` status `ready` deltaP `-3.3044` edge `31.9879` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `24.8887` n `91` status `ready` deltaP `43.1166` edge `1.8096` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `24.8887` n `91` status `ready` deltaP `43.1166` edge `1.8096` maxDD `-0.8386`
- `news_risk_high->crypto_major_24h` score `22.5879` n `42` status `ready` deltaP `51.7609` edge `1.6273` maxDD `-5.8705`
- `market_context_high->crypto_alt_24h` score `21.9792` n `151` status `ready` deltaP `38.0151` edge `1.6609` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `13.4541` n `42` status `ready` deltaP `22.4206` edge `1.0205` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `10.7632` n `42` status `ready` deltaP `32.2173` edge `0.692` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.3303` n `91` status `ready` deltaP `36.9792` edge `0.531` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.3303` n `91` status `ready` deltaP `36.9792` edge `0.531` maxDD `0.0`
- `market_context_high->equity_24h` score `9.0411` n `151` status `ready` deltaP `36.9792` edge `0.5069` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.9108` n `91` status `ready` deltaP `43.7751` edge `0.4879` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9108` n `91` status `ready` deltaP `43.7751` edge `0.4879` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.0769` n `42` status `ready` deltaP `51.0417` edge `0.3328` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.8017` n `91` status `ready` deltaP `25.021` edge `1.2402` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.8017` n `91` status `ready` deltaP `25.021` edge `1.2402` maxDD `-24.5429`
- `news_risk_high->index_24h` score `7.796` n `42` status `ready` deltaP `50.0992` edge `0.325` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `6.7521` n `91` status `ready` deltaP `31.8966` edge `0.4359` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.7521` n `91` status `ready` deltaP `31.8966` edge `0.4359` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.3344` n `91` status `ready` deltaP `51.5644` edge `0.105` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.3344` n `91` status `ready` deltaP `51.5644` edge `0.105` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
