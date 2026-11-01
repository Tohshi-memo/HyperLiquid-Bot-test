# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T14:22:26.738592+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6613`

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

- `market_context_high->unknown_24h` score `7031.3539` n `55` status `ready` deltaP `1.3889` edge `585.9369` maxDD `0.0`
- `market_context_high->unknown_4h` score `379.5819` n `55` status `ready` deltaP `5.3464` edge `31.6005` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `74.8563` n `55` status `ready` deltaP `3.7616` edge `6.224` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.0738` n `55` status `ready` deltaP `43.1471` edge `1.4921` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.1162` n `98` status `ready` deltaP `30.4847` edge `1.0254` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.7759` n `55` status `ready` deltaP `55.2083` edge `0.1966` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.4128` n `55` status `ready` deltaP `45.2683` edge `0.2637` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.0085` n `55` status `ready` deltaP `23.75` edge `0.3718` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.5945` n `55` status `ready` deltaP `30.7401` edge `0.2949` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `3.7496` n `116` status `ready` deltaP `15.3017` edge `0.3491` maxDD `-7.4246`
- `market_context_high->equity_4h` score `3.4198` n `55` status `ready` deltaP `5.7428` edge `0.3169` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.3673` n `55` status `ready` deltaP `31.6768` edge `0.0945` maxDD `-0.3387`
- `market_context_high->crypto_major_24h` score `2.4045` n `55` status `ready` deltaP `10.685` edge `0.3047` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.7239` n `55` status `ready` deltaP `-5.3409` edge `0.4084` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.569` n `55` status `ready` deltaP `18.3508` edge `0.0509` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.4937` n `55` status `ready` deltaP `2.7273` edge `0.1588` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.3532` n `55` status `ready` deltaP `7.7327` edge `0.1222` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.29` n `55` status `ready` deltaP `3.4758` edge `0.1514` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.9367` n `55` status `ready` deltaP `11.6249` edge `0.0254` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.6248` n `128` status `ready` deltaP `8.561` edge `0.0904` maxDD `-3.9659`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
