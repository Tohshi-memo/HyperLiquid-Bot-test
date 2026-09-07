# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T21:22:30.239810+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10273`

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

- `risk_on_high->unknown_24h` score `3224.5065` n `114` status `ready` deltaP `21.7014` edge `268.5642` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `3224.5065` n `114` status `ready` deltaP `21.7014` edge `268.5642` maxDD `0.0`
- `market_context_high->unknown_24h` score `1015.4912` n `229` status `ready` deltaP `20.828` edge `84.4906` maxDD `-0.0819`
- `risk_on_high->crypto_alt_24h` score `10.6356` n `114` status `ready` deltaP `28.2803` edge `0.7039` maxDD `-0.1572`
- `risk_on_and_context->crypto_alt_24h` score `10.6356` n `114` status `ready` deltaP `28.2803` edge `0.7039` maxDD `-0.1572`
- `risk_on_high->crypto_major_24h` score `10.2122` n `114` status `ready` deltaP `22.9898` edge `1.0401` maxDD `-20.3882`
- `risk_on_and_context->crypto_major_24h` score `10.2122` n `114` status `ready` deltaP `22.9898` edge `1.0401` maxDD `-20.3882`
- `market_context_high->crypto_alt_24h` score `6.238` n `229` status `ready` deltaP `22.1744` edge `0.4295` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.7764` n `117` status `ready` deltaP `30.635` edge `0.3143` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.7764` n `117` status `ready` deltaP `30.635` edge `0.3143` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.8807` n `117` status `ready` deltaP `25.8287` edge `0.3204` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8807` n `117` status `ready` deltaP `25.8287` edge `0.3204` maxDD `-3.8693`
- `market_context_high->equity_24h` score `3.1528` n `229` status `ready` deltaP `13.7153` edge `0.1713` maxDD `0.0`
- `risk_on_high->equity_24h` score `2.3356` n `114` status `ready` deltaP `13.7153` edge `0.1032` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.3356` n `114` status `ready` deltaP `13.7153` edge `0.1032` maxDD `0.0`
- `risk_on_high->index_24h` score `1.6974` n `114` status `ready` deltaP `15.5976` edge `0.0417` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.6974` n `114` status `ready` deltaP `15.5976` edge `0.0417` maxDD `-0.0051`
- `market_context_high->index_24h` score `0.9681` n `229` status `ready` deltaP `10.3689` edge `0.0509` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.9633` n `117` status `ready` deltaP `4.3964` edge `0.0862` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9633` n `117` status `ready` deltaP `4.3964` edge `0.0862` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
