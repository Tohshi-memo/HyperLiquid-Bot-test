# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T18:07:32.189837+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11824`

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

- `news_risk_high->equity_4h` score `7.4087` n `32` status `ready` deltaP `40.2439` edge `0.3491` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `2.5397` n `32` status `ready` deltaP `17.5347` edge `0.3243` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.5397` n `32` status `ready` deltaP `17.5347` edge `0.3243` maxDD `-6.2481`
- `news_risk_high->index_4h` score `2.3476` n `32` status `ready` deltaP `25.4573` edge `0.0391` maxDD `-0.0546`
- `risk_on_high->commodity_4h` score `2.1758` n `32` status `ready` deltaP `14.5579` edge `0.1025` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.1758` n `32` status `ready` deltaP `14.5579` edge `0.1025` maxDD `-0.1258`
- `risk_on_high->commodity_24h` score `1.7465` n `32` status `ready` deltaP `16.1458` edge `0.0379` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `1.7465` n `32` status `ready` deltaP `16.1458` edge `0.0379` maxDD `0.0`
- `news_risk_high->equity_1h` score `1.743` n `36` status `ready` deltaP `8.7326` edge `0.1189` maxDD `-0.5496`
- `risk_on_high->fx_24h` score `1.6668` n `32` status `ready` deltaP `18.5764` edge `0.0335` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.6668` n `32` status `ready` deltaP `18.5764` edge `0.0335` maxDD `-0.1418`
- `risk_on_high->commodity_1h` score `1.1437` n `32` status `ready` deltaP `12.4626` edge `0.0355` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1437` n `32` status `ready` deltaP `12.4626` edge `0.0355` maxDD `-0.1957`
- `risk_on_high->equity_24h` score `1.0508` n `32` status `ready` deltaP `3.4722` edge `0.2895` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `1.0508` n `32` status `ready` deltaP `3.4722` edge `0.2895` maxDD `-11.2348`
- `risk_on_high->index_24h` score `1.0447` n `32` status `ready` deltaP `10.5903` edge `0.0469` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `1.0447` n `32` status `ready` deltaP `10.5903` edge `0.0469` maxDD `-0.4355`
- `risk_on_high->fx_4h` score `0.9231` n `32` status `ready` deltaP `10.5945` edge `0.0204` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9231` n `32` status `ready` deltaP `10.5945` edge `0.0204` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.7047` n `172` status `ready` deltaP `10.2701` edge `0.0541` maxDD `-2.1077`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
