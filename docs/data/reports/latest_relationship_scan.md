# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T06:07:25.681483+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6341`

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

- `market_context_high->unknown_24h` score `6586.4292` n `58` status `ready` deltaP `3.3106` edge `548.8545` maxDD `-0.2646`
- `market_context_high->unknown_4h` score `344.0598` n `58` status `ready` deltaP `5.4405` edge `28.6397` maxDD `-0.0124`
- `news_risk_high->unknown_1h` score `80.2516` n `108` status `ready` deltaP `-5.1951` edge `6.7509` maxDD `-0.9571`
- `market_context_high->unknown_1h` score `35.7072` n `58` status `ready` deltaP `2.9786` edge `2.9668` maxDD `-0.2178`
- `market_context_high->equity_24h` score `20.3949` n `58` status `ready` deltaP `42.0617` edge `1.4511` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.3229` n `98` status `ready` deltaP `31.374` edge `1.0367` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.6342` n `58` status `ready` deltaP `55.5915` edge `0.1959` maxDD `-0.0926`
- `market_context_high->commodity_24h` score `5.8078` n `58` status `ready` deltaP `42.1575` edge `0.2465` maxDD `-1.8188`
- `news_risk_high->crypto_alt_4h` score `5.0351` n `108` status `ready` deltaP `19.0549` edge `0.4312` maxDD `-7.4246`
- `market_context_high->crypto_alt_4h` score `4.7048` n `58` status `ready` deltaP `19.917` edge `0.3067` maxDD `-2.4596`
- `market_context_high->crypto_major_4h` score `4.5936` n `58` status `ready` deltaP `26.7188` edge `0.245` maxDD `-1.8929`
- `market_context_high->commodity_4h` score `3.0724` n `58` status `ready` deltaP `29.7203` edge `0.0913` maxDD `-0.3387`
- `market_context_high->equity_4h` score `2.9474` n `58` status `ready` deltaP `3.648` edge `0.2915` maxDD `-2.283`
- `market_context_high->crypto_major_24h` score `2.2515` n `58` status `ready` deltaP `9.3031` edge `0.2943` maxDD `-3.0799`
- `market_context_high->metal_4h` score `1.6904` n `58` status `ready` deltaP `20.1377` edge `0.0491` maxDD `-0.7323`
- `market_context_high->crypto_alt_24h` score `1.6589` n `58` status `ready` deltaP `-6.0644` edge `0.4049` maxDD `-8.8096`
- `market_context_high->crypto_major_1h` score `1.1555` n `58` status `ready` deltaP `6.8966` edge `0.114` maxDD `-2.4284`
- `market_context_high->metal_1h` score `1.0235` n `58` status `ready` deltaP `12.74` edge `0.0252` maxDD `-0.3209`
- `market_context_high->crypto_alt_1h` score `0.7352` n `58` status `ready` deltaP `1.497` edge `0.138` maxDD `-2.9372`
- `market_context_high->equity_1h` score `0.7332` n `58` status `ready` deltaP `-0.2994` edge `0.1485` maxDD `-1.5336`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
