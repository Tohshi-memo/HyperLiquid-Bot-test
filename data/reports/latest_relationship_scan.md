# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T01:22:30.781528+00:00`
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

- `risk_on_high->crypto_alt_24h` score `13.8121` n `113` status `ready` deltaP `28.2141` edge `0.9859` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.8121` n `113` status `ready` deltaP `28.2141` edge `0.9859` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `8.8755` n `235` status `ready` deltaP `20.724` edge `0.6842` maxDD `-3.9523`
- `risk_on_high->crypto_major_24h` score `7.1635` n `113` status `ready` deltaP `23.0534` edge `1.1715` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.1635` n `113` status `ready` deltaP `23.0534` edge `1.1715` maxDD `-24.5429`
- `risk_on_high->crypto_alt_4h` score `7.0801` n `113` status `ready` deltaP `36.5813` edge `0.3833` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.0801` n `113` status `ready` deltaP `36.5813` edge `0.3833` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.9822` n `113` status `ready` deltaP `26.9021` edge `0.3217` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.9822` n `113` status `ready` deltaP `26.9021` edge `0.3217` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.8572` n `113` status `ready` deltaP `28.5951` edge `0.0517` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.8572` n `113` status `ready` deltaP `28.5951` edge `0.0517` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.2358` n `235` status `ready` deltaP `12.1528` edge `0.1053` maxDD `0.0`
- `market_context_high->index_24h` score `2.1434` n `235` status `ready` deltaP `23.5904` edge `0.0607` maxDD `-0.1483`
- `risk_on_high->equity_24h` score `1.421` n `113` status `ready` deltaP `12.1528` edge `0.0374` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.421` n `113` status `ready` deltaP `12.1528` edge `0.0374` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.1818` n `113` status `ready` deltaP `4.7878` edge `0.1018` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.1818` n `113` status `ready` deltaP `4.7878` edge `0.1018` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.6111` n `113` status `ready` deltaP `18.6793` edge `0.0694` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.6111` n `113` status `ready` deltaP `18.6793` edge `0.0694` maxDD `-0.9131`
- `risk_on_high->equity_1h` score `0.5269` n `113` status `ready` deltaP `15.0681` edge `-0.0034` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
