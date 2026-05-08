# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T08:22:16.818152+00:00`
- Price records: `629`
- Market context records: `736`
- Flow alert records: `2078`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1009`

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

- `market_context_high->crypto_major_24h` score `12.4244` n `146` status `ready` deltaP `29.6795` edge `0.8709` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5378` n `146` status `ready` deltaP `7.7579` edge `0.4979` maxDD `-0.0508`
- `market_context_high->index_24h` score `-0.0217` n `146` status `ready` deltaP `0.8403` edge `0.1921` maxDD `-5.9609`
- `market_context_high->fx_4h` score `-0.3173` n `152` status `ready` deltaP `5.679` edge `0.0086` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.4169` n `156` status `ready` deltaP `3.0998` edge `0.0024` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.563` n `156` status `ready` deltaP `1.7001` edge `0.0392` maxDD `-3.7959`
- `market_context_high->equity_24h` score `-0.7352` n `146` status `ready` deltaP `-0.839` edge `0.2048` maxDD `-10.5047`
- `market_context_high->index_1h` score `-0.9042` n `156` status `ready` deltaP `0.991` edge `0.0034` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.0861` n `156` status `ready` deltaP `-0.9414` edge `-0.0032` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.1143` n `156` status `ready` deltaP `5.2113` edge `-0.0053` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.5093` n `156` status `ready` deltaP `3.7795` edge `-0.0195` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-1.5897` n `152` status `ready` deltaP `17.2083` edge `0.1234` maxDD `-22.648`
- `market_context_high->unknown_1h` score `-1.6436` n `156` status `ready` deltaP `-5.2051` edge `-0.0251` maxDD `-3.5069`
- `market_context_high->index_4h` score `-1.8348` n `152` status `ready` deltaP `1.2553` edge `-0.009` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.1732` n `152` status `ready` deltaP `2.037` edge `0.0623` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.7401` n `152` status `ready` deltaP `-1.7004` edge `-0.0018` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.1812` n `156` status `ready` deltaP `-4.0759` edge `-0.042` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6185` n `152` status `ready` deltaP `-5.3615` edge `0.0843` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.9088` n `152` status `ready` deltaP `4.5881` edge `-0.1685` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.3166` n `146` status `ready` deltaP `-14.9002` edge `-0.0651` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
