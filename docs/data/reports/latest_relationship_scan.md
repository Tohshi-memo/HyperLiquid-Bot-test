# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T19:07:29.912135+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10225`

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

- `risk_on_high->unknown_24h` score `167.3497` n `108` status `ready` deltaP `22.3958` edge `13.7965` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `167.3497` n `108` status `ready` deltaP `22.3958` edge `13.7965` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `13.7495` n `108` status `ready` deltaP `27.0834` edge `1.2073` maxDD `-14.3652`
- `risk_on_and_context->crypto_major_24h` score `13.7495` n `108` status `ready` deltaP `27.0834` edge `1.2073` maxDD `-14.3652`
- `risk_on_high->crypto_alt_24h` score `11.8388` n `108` status `ready` deltaP `29.7453` edge `0.7944` maxDD `-0.1572`
- `risk_on_and_context->crypto_alt_24h` score `11.8388` n `108` status `ready` deltaP `29.7453` edge `0.7944` maxDD `-0.1572`
- `market_context_high->crypto_alt_24h` score `6.9925` n `220` status `ready` deltaP `23.4154` edge `0.4841` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.7726` n `117` status `ready` deltaP `30.4826` edge `0.315` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.7726` n `117` status `ready` deltaP `30.4826` edge `0.315` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.0561` n `117` status `ready` deltaP `26.8957` edge `0.3279` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.0561` n `117` status `ready` deltaP `26.8957` edge `0.3279` maxDD `-3.8693`
- `market_context_high->equity_24h` score `3.8478` n `220` status `ready` deltaP `15.2778` edge `0.2188` maxDD `0.0`
- `risk_on_high->equity_24h` score `3.0378` n `108` status `ready` deltaP `15.2778` edge `0.1513` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.0378` n `108` status `ready` deltaP `15.2778` edge `0.1513` maxDD `0.0`
- `risk_on_high->index_24h` score `1.9007` n `108` status `ready` deltaP `17.0139` edge `0.0492` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.9007` n `108` status `ready` deltaP `17.0139` edge `0.0492` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.1585` n `220` status `ready` deltaP `11.6099` edge `0.0585` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `1.0088` n `117` status `ready` deltaP `4.6958` edge `0.088` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0088` n `117` status `ready` deltaP `4.6958` edge `0.088` maxDD `-1.1521`
- `risk_on_high->equity_1h` score `0.5133` n `117` status `ready` deltaP `14.3726` edge `0.0001` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
