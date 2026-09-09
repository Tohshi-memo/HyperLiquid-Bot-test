# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T23:52:26.644138+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9978`

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

- `risk_on_high->crypto_alt_24h` score `13.7253` n `117` status `ready` deltaP `27.3237` edge `0.9846` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.7253` n `117` status `ready` deltaP `27.3237` edge `0.9846` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `8.6779` n `241` status `ready` deltaP `19.9789` edge `0.6727` maxDD `-3.9523`
- `risk_on_high->crypto_major_24h` score `7.5217` n `117` status `ready` deltaP `23.0102` edge `1.2177` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.5217` n `117` status `ready` deltaP `23.0102` edge `1.2177` maxDD `-24.5429`
- `risk_on_high->crypto_alt_4h` score `6.9038` n `117` status `ready` deltaP `35.818` edge `0.3737` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `6.9038` n `117` status `ready` deltaP `35.818` edge `0.3737` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.8521` n `117` status `ready` deltaP `25.9811` edge `0.317` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8521` n `117` status `ready` deltaP `25.9811` edge `0.317` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.7776` n `117` status `ready` deltaP `27.6442` edge `0.0514` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.7776` n `117` status `ready` deltaP `27.6442` edge `0.0514` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.0877` n `241` status `ready` deltaP `11.1111` edge `0.0999` maxDD `0.0`
- `market_context_high->index_24h` score `2.0561` n `241` status `ready` deltaP `22.7394` edge `0.0591` maxDD `-0.1483`
- `risk_on_high->equity_24h` score `1.4025` n `117` status `ready` deltaP `11.1111` edge `0.0428` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.4025` n `117` status `ready` deltaP `11.1111` edge `0.0428` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.202` n `117` status `ready` deltaP `4.6958` edge `0.1041` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.202` n `117` status `ready` deltaP `4.6958` edge `0.1041` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.8175` n `117` status `ready` deltaP `19.7383` edge `0.0888` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.8175` n `117` status `ready` deltaP `19.7383` edge `0.0888` maxDD `-0.9131`
- `risk_on_high->equity_1h` score `0.4796` n `117` status `ready` deltaP `14.672` edge `-0.0047` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
