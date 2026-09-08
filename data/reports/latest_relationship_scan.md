# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T01:22:33.413023+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10313`

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

- `market_context_high->unknown_24h` score `2897.9271` n `241` status `ready` deltaP `18.9618` edge `241.3727` maxDD `-0.0819`
- `risk_on_high->unknown_24h` score `2868.6185` n `117` status `ready` deltaP `19.7917` edge `238.9196` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `2868.6185` n `117` status `ready` deltaP `19.7917` edge `238.9196` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `9.3513` n `117` status `ready` deltaP `24.8932` edge `0.6363` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `9.3513` n `117` status `ready` deltaP `24.8932` edge `0.6363` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.9456` n `117` status `ready` deltaP `31.5497` edge `0.3223` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.9456` n `117` status `ready` deltaP `31.5497` edge `0.3223` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.2805` n `117` status `ready` deltaP `21.1005` edge `0.9431` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.2805` n `117` status `ready` deltaP `21.1005` edge `0.9431` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.8699` n `117` status `ready` deltaP `25.8287` edge `0.3195` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8699` n `117` status `ready` deltaP `25.8287` edge `0.3195` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `4.3038` n `241` status `ready` deltaP `17.5484` edge `0.3244` maxDD `-3.9523`
- `market_context_high->equity_24h` score `1.877` n `241` status `ready` deltaP `10.9375` edge `0.0835` maxDD `0.0`
- `risk_on_high->index_24h` score `1.3294` n `117` status `ready` deltaP `12.8873` edge `0.0291` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.3294` n `117` status `ready` deltaP `12.8873` edge `0.0291` maxDD `-0.0051`
- `risk_on_high->equity_24h` score `1.1918` n `117` status `ready` deltaP `10.9375` edge `0.0264` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.1918` n `117` status `ready` deltaP `10.9375` edge `0.0264` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `0.9286` n `117` status `ready` deltaP `3.9473` edge `0.0863` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9286` n `117` status `ready` deltaP `3.9473` edge `0.0863` maxDD `-1.1521`
- `market_context_high->index_24h` score `0.608` n `241` status `ready` deltaP `7.9825` edge `0.0368` maxDD `-0.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
