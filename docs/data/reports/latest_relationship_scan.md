# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T16:07:28.542153+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10441`

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

- `risk_on_high->unknown_24h` score `332.9974` n `96` status `ready` deltaP `24.1319` edge `27.5889` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `332.9974` n `96` status `ready` deltaP `24.1319` edge `27.5889` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `20.9152` n `96` status `ready` deltaP `36.8056` edge `1.569` maxDD `-3.0481`
- `risk_on_and_context->crypto_major_24h` score `20.9152` n `96` status `ready` deltaP `36.8056` edge `1.569` maxDD `-3.0481`
- `risk_on_high->crypto_alt_24h` score `14.6709` n `96` status `ready` deltaP `32.2917` edge `1.0073` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `14.6709` n `96` status `ready` deltaP `32.2917` edge `1.0073` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.1024` n `208` status `ready` deltaP `24.5994` edge `0.5687` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.4507` n `117` status `ready` deltaP `29.2631` edge `0.2963` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.4507` n `117` status `ready` deltaP `29.2631` edge `0.2963` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.7593` n `117` status `ready` deltaP `25.6762` edge `0.3113` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.7593` n `117` status `ready` deltaP `25.6762` edge `0.3113` maxDD `-3.8693`
- `market_context_high->equity_24h` score `4.7129` n `208` status `ready` deltaP `17.3611` edge `0.277` maxDD `0.0`
- `risk_on_high->equity_24h` score `4.0457` n `96` status `ready` deltaP `17.3611` edge `0.2214` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.0457` n `96` status `ready` deltaP `17.3611` edge `0.2214` maxDD `0.0`
- `risk_on_high->index_24h` score `2.1632` n `96` status `ready` deltaP `18.75` edge `0.0595` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.1632` n `96` status `ready` deltaP `18.75` edge `0.0595` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.3955` n `208` status `ready` deltaP `13.2212` edge `0.0675` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.9813` n `117` status `ready` deltaP `4.5461` edge `0.0867` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9813` n `117` status `ready` deltaP `4.5461` edge `0.0867` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.6959` n `96` status `ready` deltaP `16.3195` edge `0.096` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
