# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T21:22:28.121617+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10146`

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

- `risk_on_high->crypto_alt_24h` score `12.0996` n `117` status `ready` deltaP `25.5876` edge `0.8607` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `12.0996` n `117` status `ready` deltaP `25.5876` edge `0.8607` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `7.0522` n `241` status `ready` deltaP `18.2428` edge `0.5488` maxDD `-3.9523`
- `risk_on_high->crypto_major_24h` score `6.4572` n `117` status `ready` deltaP `21.2741` edge `1.0928` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.4572` n `117` status `ready` deltaP `21.2741` edge `1.0928` maxDD `-24.5429`
- `risk_on_high->crypto_alt_4h` score `6.1531` n `117` status `ready` deltaP `34.2936` edge `0.3213` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `6.1531` n `117` status `ready` deltaP `34.2936` edge `0.3213` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.2849` n `117` status `ready` deltaP `24.4567` edge `0.2799` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.2849` n `117` status `ready` deltaP `24.4567` edge `0.2799` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.5787` n `117` status `ready` deltaP `25.9081` edge `0.0464` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.5787` n `117` status `ready` deltaP `25.9081` edge `0.0464` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.8572` n `241` status `ready` deltaP `21.0033` edge `0.0541` maxDD `-0.1483`
- `market_context_high->equity_24h` score `1.5672` n `241` status `ready` deltaP `9.375` edge `0.0681` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.0281` n `117` status `ready` deltaP `4.097` edge `0.0936` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0281` n `117` status `ready` deltaP `4.097` edge `0.0936` maxDD `-1.1521`
- `risk_on_high->equity_24h` score `0.882` n `117` status `ready` deltaP `9.375` edge `0.011` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.882` n `117` status `ready` deltaP `9.375` edge `0.011` maxDD `0.0`
- `risk_on_high->metal_24h` score `0.7808` n `117` status `ready` deltaP `19.7383` edge `0.0841` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.7808` n `117` status `ready` deltaP `19.7383` edge `0.0841` maxDD `-0.9131`
- `risk_on_high->equity_1h` score `0.4401` n `117` status `ready` deltaP `14.3726` edge `-0.006` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
