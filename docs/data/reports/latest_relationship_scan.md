# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T04:07:29.009277+00:00`
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

- `market_context_high->unknown_24h` score `1171.6285` n `241` status `ready` deltaP `17.3993` edge `97.5249` maxDD `-0.0819`
- `risk_on_high->unknown_24h` score `1142.3199` n `117` status `ready` deltaP `18.2292` edge `95.0718` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `1142.3199` n `117` status `ready` deltaP `18.2292` edge `95.0718` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `8.8356` n `117` status `ready` deltaP `23.1571` edge `0.6049` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `8.8356` n `117` status `ready` deltaP `23.1571` edge `0.6049` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.9528` n `117` status `ready` deltaP `31.5497` edge `0.3229` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.9528` n `117` status `ready` deltaP `31.5497` edge `0.3229` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.1393` n `117` status `ready` deltaP `21.1005` edge `0.925` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.1393` n `117` status `ready` deltaP `21.1005` edge `0.925` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.9459` n `117` status `ready` deltaP `26.1335` edge `0.3238` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.9459` n `117` status `ready` deltaP `26.1335` edge `0.3238` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `3.7881` n `241` status `ready` deltaP `15.8123` edge `0.293` maxDD `-3.9523`
- `risk_on_high->index_24h` score `1.0398` n `117` status `ready` deltaP `10.9776` edge `0.0177` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.0398` n `117` status `ready` deltaP `10.9776` edge `0.0177` maxDD `-0.0051`
- `market_context_high->equity_24h` score `1.0294` n `241` status `ready` deltaP `9.0278` edge `0.0256` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.0173` n `117` status `ready` deltaP `4.2467` edge `0.0917` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0173` n `117` status `ready` deltaP `4.2467` edge `0.0917` maxDD `-1.1521`
- `risk_on_high->equity_1h` score `0.5132` n `117` status `ready` deltaP `14.5223` edge `-0.0009` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.5132` n `117` status `ready` deltaP `14.5223` edge `-0.0009` maxDD `-2.2516`
- `risk_on_high->crypto_major_1h` score `0.3752` n `117` status `ready` deltaP `4.7828` edge `0.0721` maxDD `-3.1509`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
