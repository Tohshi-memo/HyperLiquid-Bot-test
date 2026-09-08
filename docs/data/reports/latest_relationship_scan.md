# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T00:07:28.452956+00:00`
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

- `risk_on_high->unknown_24h` score `3680.8332` n `117` status `ready` deltaP `19.9653` edge `306.603` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `3680.8332` n `117` status `ready` deltaP `19.9653` edge `306.603` maxDD `0.0`
- `market_context_high->unknown_24h` score `3355.8427` n `240` status `ready` deltaP `19.132` edge `279.5312` maxDD `-0.0819`
- `risk_on_high->crypto_alt_24h` score `9.5177` n `117` status `ready` deltaP `25.414` edge `0.6467` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `9.5177` n `117` status `ready` deltaP `25.414` edge `0.6467` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.9286` n `117` status `ready` deltaP `31.3972` edge `0.3219` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.9286` n `117` status `ready` deltaP `31.3972` edge `0.3219` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.3359` n `117` status `ready` deltaP `21.1005` edge `0.9502` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.3359` n `117` status `ready` deltaP `21.1005` edge `0.9502` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.8675` n `117` status `ready` deltaP `25.8287` edge `0.3193` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8675` n `117` status `ready` deltaP `25.8287` edge `0.3193` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `4.7399` n `240` status `ready` deltaP `18.4375` edge `0.3431` maxDD `-3.349`
- `market_context_high->equity_24h` score `2.2332` n `240` status `ready` deltaP `11.8056` edge `0.1074` maxDD `0.0`
- `risk_on_high->equity_24h` score `1.5348` n `117` status `ready` deltaP `11.8056` edge `0.0492` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.5348` n `117` status `ready` deltaP `11.8056` edge `0.0492` maxDD `0.0`
- `risk_on_high->index_24h` score `1.4481` n `117` status `ready` deltaP `13.7553` edge `0.0332` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.4481` n `117` status `ready` deltaP `13.7553` edge `0.0332` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `1.04` n `117` status `ready` deltaP `4.6958` edge `0.0906` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.04` n `117` status `ready` deltaP `4.6958` edge `0.0906` maxDD `-1.1521`
- `market_context_high->index_24h` score `0.7253` n `240` status `ready` deltaP `8.8194` edge `0.041` maxDD `-0.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
