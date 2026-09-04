# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T19:22:33.671360+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10794`

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

- `risk_on_high->unknown_4h` score `19.6032` n `133` status `ready` deltaP `7.4741` edge `1.6456` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.6032` n `133` status `ready` deltaP `7.4741` edge `1.6456` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.5126` n `133` status `ready` deltaP `-1.9518` edge `1.0301` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.5126` n `133` status `ready` deltaP `-1.9518` edge `1.0301` maxDD `-1.95`
- `market_context_high->unknown_4h` score `10.284` n `212` status `ready` deltaP `9.2758` edge `0.8647` maxDD `-2.563`
- `market_context_high->unknown_1h` score `8.734` n `217` status `ready` deltaP `-1.0059` edge `0.7976` maxDD `-2.0446`
- `news_risk_high->crypto_alt_24h` score `3.7026` n `46` status `ready` deltaP `18.9765` edge `0.209` maxDD `-0.8236`
- `news_risk_high->crypto_major_4h` score `2.1865` n `46` status `ready` deltaP `9.4247` edge `0.1677` maxDD `-1.5324`
- `news_risk_high->commodity_24h` score `2.1067` n `46` status `ready` deltaP `12.9076` edge `0.1067` maxDD `-0.042`
- `news_risk_high->equity_1h` score `1.6722` n `46` status `ready` deltaP `16.1286` edge `0.0709` maxDD `-0.7924`
- `news_risk_high->metal_4h` score `1.5961` n `46` status `ready` deltaP `16.7086` edge `0.0479` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.5472` n `46` status `ready` deltaP `11.0286` edge `0.0755` maxDD `-0.2737`
- `news_risk_high->index_1h` score `1.1469` n `46` status `ready` deltaP `14.6967` edge `0.011` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `0.7197` n `46` status `ready` deltaP `9.2229` edge `0.0178` maxDD `-0.2118`
- `news_risk_high->fx_4h` score `0.3067` n `46` status `ready` deltaP `10.558` edge `0.0004` maxDD `-0.9514`
- `news_risk_high->crypto_alt_1h` score `0.1711` n `46` status `ready` deltaP `3.9053` edge `0.0185` maxDD `-1.0885`
- `news_risk_high->commodity_1h` score `0.1682` n `46` status `ready` deltaP `8.3312` edge `0.0031` maxDD `-0.9036`
- `risk_on_high->metal_1h` score `0.0922` n `133` status `ready` deltaP `12.2631` edge `0.0013` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0922` n `133` status `ready` deltaP `12.2631` edge `0.0013` maxDD `-1.699`
- `news_risk_high->crypto_major_1h` score `0.0562` n `46` status `ready` deltaP `-0.5207` edge `0.0399` maxDD `-1.0047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
