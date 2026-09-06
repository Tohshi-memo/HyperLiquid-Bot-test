# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T23:52:29.012475+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10545`

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

- `risk_on_high->unknown_24h` score `326.4245` n `107` status `ready` deltaP `26.7361` edge `27.0238` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `326.4245` n `107` status `ready` deltaP `26.7361` edge `27.0238` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `19.4021` n `107` status `ready` deltaP `33.9499` edge `1.4422` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `19.4021` n `107` status `ready` deltaP `33.9499` edge `1.4422` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `13.6216` n `107` status `ready` deltaP `30.0347` edge `0.9349` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.6216` n `107` status `ready` deltaP `30.0347` edge `0.9349` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.7662` n `196` status `ready` deltaP `23.9123` edge `0.6286` maxDD `-2.5998`
- `market_context_high->unknown_1h` score `7.9754` n `250` status `ready` deltaP `-4.6096` edge `0.7678` maxDD `-2.4626`
- `market_context_high->equity_24h` score `6.7096` n `196` status `ready` deltaP `23.0903` edge `0.4052` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `6.3764` n `123` status `ready` deltaP `29.8781` edge `0.3378` maxDD `-0.116`
- `risk_on_and_context->crypto_alt_4h` score `6.3764` n `123` status `ready` deltaP `29.8781` edge `0.3378` maxDD `-0.116`
- `risk_on_high->equity_24h` score `5.8708` n `107` status `ready` deltaP `23.0903` edge `0.3353` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.8708` n `107` status `ready` deltaP `23.0903` edge `0.3353` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.2246` n `123` status `ready` deltaP `23.8821` edge `0.2787` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.2246` n `123` status `ready` deltaP `23.8821` edge `0.2787` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.7707` n `107` status `ready` deltaP `23.238` edge `0.0802` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.7707` n `107` status `ready` deltaP `23.238` edge `0.0802` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.6957` n `196` status `ready` deltaP `21.9601` edge `0.0955` maxDD `-0.0472`
- `risk_on_high->crypto_alt_1h` score `0.7914` n `131` status `ready` deltaP `4.0328` edge `0.0743` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.7914` n `131` status `ready` deltaP `4.0328` edge `0.0743` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
