# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T20:22:26.771522+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10173`

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

- `risk_on_high->unknown_24h` score `670.5373` n `110` status `ready` deltaP `22.3958` edge `55.7288` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `670.5373` n `110` status `ready` deltaP `22.3958` edge `55.7288` maxDD `0.0`
- `market_context_high->unknown_24h` score `61.5731` n `225` status `ready` deltaP `21.5069` edge `4.9929` maxDD `-0.0819`
- `risk_on_high->crypto_major_24h` score `12.5678` n `110` status `ready` deltaP `25.6692` edge `1.1471` maxDD `-16.006`
- `risk_on_and_context->crypto_major_24h` score `12.5678` n `110` status `ready` deltaP `25.6692` edge `1.1471` maxDD `-16.006`
- `risk_on_high->crypto_alt_24h` score `11.3737` n `110` status `ready` deltaP `28.911` edge `0.7612` maxDD `-0.1572`
- `risk_on_and_context->crypto_alt_24h` score `11.3737` n `110` status `ready` deltaP `28.911` edge `0.7612` maxDD `-0.1572`
- `market_context_high->crypto_alt_24h` score `6.5848` n `225` status `ready` deltaP `22.7292` edge `0.4547` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.7512` n `117` status `ready` deltaP `30.635` edge `0.3122` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.7512` n `117` status `ready` deltaP `30.635` edge `0.3122` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.9353` n `117` status `ready` deltaP `26.286` edge `0.3219` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.9353` n `117` status `ready` deltaP `26.286` edge `0.3219` maxDD `-3.8693`
- `market_context_high->equity_24h` score `3.4652` n `225` status `ready` deltaP `14.4097` edge `0.1927` maxDD `0.0`
- `risk_on_high->equity_24h` score `2.6804` n `110` status `ready` deltaP `14.4097` edge `0.1273` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.6804` n `110` status `ready` deltaP `14.4097` edge `0.1273` maxDD `0.0`
- `risk_on_high->index_24h` score `1.7897` n `110` status `ready` deltaP `16.1963` edge `0.0454` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.7897` n `110` status `ready` deltaP `16.1963` edge `0.0454` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.0544` n `225` status `ready` deltaP `10.9236` edge `0.0544` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.9441` n `117` status `ready` deltaP `4.2467` edge `0.0856` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9441` n `117` status `ready` deltaP `4.2467` edge `0.0856` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
