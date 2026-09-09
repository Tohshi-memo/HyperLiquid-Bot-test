# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T20:07:29.157456+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10070`

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

- `risk_on_high->crypto_alt_24h` score `11.4194` n `117` status `ready` deltaP `24.7196` edge `0.8098` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `11.4194` n `117` status `ready` deltaP `24.7196` edge `0.8098` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `6.3719` n `241` status `ready` deltaP `17.3748` edge `0.4979` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `5.9869` n `117` status `ready` deltaP `33.8363` edge `0.3105` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.9869` n `117` status `ready` deltaP `33.8363` edge `0.3105` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.9815` n `117` status `ready` deltaP `20.406` edge `1.0376` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.9815` n `117` status `ready` deltaP `20.406` edge `1.0376` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.1741` n `117` status `ready` deltaP `24.1518` edge `0.2727` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.1741` n `117` status `ready` deltaP `24.1518` edge `0.2727` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.4756` n `117` status `ready` deltaP `25.0401` edge `0.0436` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.4756` n `117` status `ready` deltaP `25.0401` edge `0.0436` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.7542` n `241` status `ready` deltaP `20.1353` edge `0.0513` maxDD `-0.1483`
- `market_context_high->equity_24h` score `1.3022` n `241` status `ready` deltaP `8.5069` edge `0.0518` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.0245` n `117` status `ready` deltaP `4.2467` edge `0.0923` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0245` n `117` status `ready` deltaP `4.2467` edge `0.0923` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.7629` n `117` status `ready` deltaP `19.7383` edge `0.0818` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.7629` n `117` status `ready` deltaP `19.7383` edge `0.0818` maxDD `-0.9131`
- `risk_on_high->equity_24h` score `0.617` n `117` status `ready` deltaP `8.5069` edge `-0.0053` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.617` n `117` status `ready` deltaP `8.5069` edge `-0.0053` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.3682` n `117` status `ready` deltaP `13.7738` edge `-0.008` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
