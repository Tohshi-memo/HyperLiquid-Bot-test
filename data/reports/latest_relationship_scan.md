# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T21:07:27.861263+00:00`
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

- `risk_on_high->unknown_24h` score `2610.664` n `113` status `ready` deltaP `21.875` edge `217.4095` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `2610.664` n `113` status `ready` deltaP `21.875` edge `217.4095` maxDD `0.0`
- `market_context_high->unknown_24h` score `783.5519` n `228` status `ready` deltaP `20.9978` edge `65.1612` maxDD `-0.0819`
- `risk_on_high->crypto_major_24h` score `10.8285` n `113` status `ready` deltaP `23.6419` edge `1.0674` maxDD `-19.1445`
- `risk_on_and_context->crypto_major_24h` score `10.8285` n `113` status `ready` deltaP `23.6419` edge `1.0674` maxDD `-19.1445`
- `risk_on_high->crypto_alt_24h` score `10.8247` n `113` status `ready` deltaP `28.4384` edge `0.7186` maxDD `-0.1572`
- `risk_on_and_context->crypto_alt_24h` score `10.8247` n `113` status `ready` deltaP `28.4384` edge `0.7186` maxDD `-0.1572`
- `market_context_high->crypto_alt_24h` score `6.3271` n `228` status `ready` deltaP `22.3136` edge `0.436` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.7716` n `117` status `ready` deltaP `30.635` edge `0.3139` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.7716` n `117` status `ready` deltaP `30.635` edge `0.3139` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.8977` n `117` status `ready` deltaP `25.9811` edge `0.3208` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8977` n `117` status `ready` deltaP `25.9811` edge `0.3208` maxDD `-3.8693`
- `market_context_high->equity_24h` score `3.2303` n `228` status `ready` deltaP `13.8889` edge `0.1766` maxDD `0.0`
- `risk_on_high->equity_24h` score `2.4191` n `113` status `ready` deltaP `13.8889` edge `0.109` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.4191` n `113` status `ready` deltaP `13.8889` edge `0.109` maxDD `0.0`
- `risk_on_high->index_24h` score `1.7203` n `113` status `ready` deltaP `15.7479` edge `0.0426` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.7203` n `113` status `ready` deltaP `15.7479` edge `0.0426` maxDD `-0.0051`
- `market_context_high->index_24h` score `0.99` n `228` status `ready` deltaP `10.5081` edge `0.0518` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.9681` n `117` status `ready` deltaP `4.3964` edge `0.0866` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9681` n `117` status `ready` deltaP `4.3964` edge `0.0866` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
