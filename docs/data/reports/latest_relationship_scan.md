# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T02:22:34.443863+00:00`
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

- `market_context_high->unknown_24h` score `2253.7638` n `241` status `ready` deltaP `18.4409` edge `187.6959` maxDD `-0.0819`
- `risk_on_high->unknown_24h` score `2224.4553` n `117` status `ready` deltaP `19.2708` edge `185.2428` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `2224.4553` n `117` status `ready` deltaP `19.2708` edge `185.2428` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `9.0665` n `117` status `ready` deltaP `24.1987` edge `0.6172` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `9.0665` n `117` status `ready` deltaP `24.1987` edge `0.6172` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.942` n `117` status `ready` deltaP `31.5497` edge `0.322` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.942` n `117` status `ready` deltaP `31.5497` edge `0.322` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.19` n `117` status `ready` deltaP `21.1005` edge `0.9315` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.19` n `117` status `ready` deltaP `21.1005` edge `0.9315` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.8891` n `117` status `ready` deltaP `25.8287` edge `0.3211` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8891` n `117` status `ready` deltaP `25.8287` edge `0.3211` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `4.0191` n `241` status `ready` deltaP `16.8539` edge `0.3053` maxDD `-3.9523`
- `market_context_high->equity_24h` score `1.561` n `241` status `ready` deltaP `10.2431` edge `0.0618` maxDD `0.0`
- `risk_on_high->index_24h` score `1.2259` n `117` status `ready` deltaP `12.1928` edge `0.0251` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.2259` n `117` status `ready` deltaP `12.1928` edge `0.0251` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `0.8794` n `117` status `ready` deltaP `3.6479` edge `0.0842` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8794` n `117` status `ready` deltaP `3.6479` edge `0.0842` maxDD `-1.1521`
- `risk_on_high->equity_24h` score `0.8758` n `117` status `ready` deltaP `10.2431` edge `0.0047` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.8758` n `117` status `ready` deltaP `10.2431` edge `0.0047` maxDD `0.0`
- `market_context_high->index_24h` score `0.5044` n `241` status `ready` deltaP `7.288` edge `0.0328` maxDD `-0.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
