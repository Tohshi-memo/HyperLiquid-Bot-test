# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T23:37:27.081501+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11328`

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

- `news_risk_high->unknown_1h` score `1658.536` n `35` status `ready` deltaP `-3.4089` edge `138.2576` maxDD `-0.8832`
- `risk_on_high->crypto_alt_24h` score `20.2412` n `91` status `ready` deltaP `36.1722` edge `1.4686` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.2412` n `91` status `ready` deltaP `36.1722` edge `1.4686` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `15.6525` n `201` status `ready` deltaP `27.7364` edge `1.2022` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.9567` n `91` status `ready` deltaP `42.0983` edge `0.5029` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9567` n `91` status `ready` deltaP `42.0983` edge `0.5029` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.6417` n `91` status `ready` deltaP `32.2015` edge `0.508` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.6417` n `91` status `ready` deltaP `32.2015` edge `0.508` maxDD `-3.8693`
- `market_context_high->equity_24h` score `7.5675` n `201` status `ready` deltaP `27.6042` edge `0.4466` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.2175` n `91` status `ready` deltaP `25.021` edge `1.1653` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2175` n `91` status `ready` deltaP `25.021` edge `1.1653` maxDD `-24.5429`
- `risk_on_high->equity_24h` score `5.9715` n `91` status `ready` deltaP `27.6042` edge `0.3136` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.9715` n `91` status `ready` deltaP `27.6042` edge `0.3136` maxDD `0.0`
- `risk_on_high->index_24h` score `4.5628` n `91` status `ready` deltaP `43.4047` edge `0.0951` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.5628` n `91` status `ready` deltaP `43.4047` edge `0.0951` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.6911` n `201` status `ready` deltaP `37.7462` edge `0.0953` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.4134` n `91` status `ready` deltaP `32.1261` edge `0.0796` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.4134` n `91` status `ready` deltaP `32.1261` edge `0.0796` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.2889` n `201` status `ready` deltaP `25.2867` edge `0.1077` maxDD `-2.843`
- `risk_on_high->equity_1h` score `1.619` n `91` status `ready` deltaP `21.0338` edge `0.0225` maxDD `-0.2246`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
