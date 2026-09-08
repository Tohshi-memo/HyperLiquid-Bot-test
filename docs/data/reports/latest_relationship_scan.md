# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T00:22:25.246200+00:00`
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

- `market_context_high->unknown_24h` score `3548.4009` n `241` status `ready` deltaP `19.1354` edge `295.5777` maxDD `-0.0819`
- `risk_on_high->unknown_24h` score `3519.0312` n `117` status `ready` deltaP `19.9653` edge `293.1195` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `3519.0312` n `117` status `ready` deltaP `19.9653` edge `293.1195` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `9.5129` n `117` status `ready` deltaP `25.414` edge `0.6463` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `9.5129` n `117` status `ready` deltaP `25.414` edge `0.6463` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.9322` n `117` status `ready` deltaP `31.3972` edge `0.3222` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.9322` n `117` status `ready` deltaP `31.3972` edge `0.3222` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.3335` n `117` status `ready` deltaP `21.1005` edge `0.9499` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.3335` n `117` status `ready` deltaP `21.1005` edge `0.9499` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.8833` n `117` status `ready` deltaP `25.9811` edge `0.3196` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8833` n `117` status `ready` deltaP `25.9811` edge `0.3196` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `4.4788` n `241` status `ready` deltaP `18.0692` edge `0.3347` maxDD `-3.8873`
- `market_context_high->equity_24h` score `2.1582` n `241` status `ready` deltaP `11.6319` edge `0.1023` maxDD `0.0`
- `risk_on_high->equity_24h` score `1.4718` n `117` status `ready` deltaP `11.6319` edge `0.0451` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.4718` n `117` status `ready` deltaP `11.6319` edge `0.0451` maxDD `0.0`
- `risk_on_high->index_24h` score `1.4258` n `117` status `ready` deltaP `13.5817` edge `0.0325` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.4258` n `117` status `ready` deltaP `13.5817` edge `0.0325` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `1.0197` n `117` status `ready` deltaP `4.5461` edge `0.0899` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0197` n `117` status `ready` deltaP `4.5461` edge `0.0899` maxDD `-1.1521`
- `market_context_high->index_24h` score `0.7043` n `241` status `ready` deltaP `8.6769` edge `0.0402` maxDD `-0.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
