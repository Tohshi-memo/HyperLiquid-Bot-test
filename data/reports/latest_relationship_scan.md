# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T02:52:28.887179+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7535`

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

- `market_context_high->unknown_24h` score `7479.1807` n `49` status `ready` deltaP `1.3889` edge `623.2558` maxDD `0.0`
- `market_context_high->unknown_4h` score `399.044` n `49` status `ready` deltaP `7.258` edge `33.2096` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `34.5944` n `54` status `ready` deltaP `4.3081` edge `2.8652` maxDD `-0.2178`
- `market_context_high->equity_24h` score `20.2878` n `49` status `ready` deltaP `42.5773` edge `1.4304` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.6956` n `94` status `ready` deltaP `33.3924` edge `1.0543` maxDD `-6.8493`
- `market_context_high->commodity_24h` score `6.5645` n `49` status `ready` deltaP `45.394` edge `0.2755` maxDD `-0.8203`
- `market_context_high->index_24h` score `6.2514` n `49` status `ready` deltaP `49.1319` edge `0.1934` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.1591` n `49` status `ready` deltaP `25.0778` edge `0.3755` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.3193` n `49` status `ready` deltaP `30.015` edge `0.2768` maxDD `-1.6901`
- `market_context_high->commodity_4h` score `3.8934` n `49` status `ready` deltaP `36.688` edge `0.0966` maxDD `-0.3387`
- `market_context_high->equity_4h` score `2.8952` n `49` status `ready` deltaP `1.9008` edge `0.2988` maxDD `-2.283`
- `market_context_high->equity_1h` score `2.3224` n `54` status `ready` deltaP `8.8102` edge `0.1873` maxDD `-1.5336`
- `news_risk_high->crypto_alt_4h` score `2.2858` n `126` status `ready` deltaP `9.3181` edge `0.267` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `1.7452` n `49` status `ready` deltaP `6.4059` edge `0.2487` maxDD `-3.0799`
- `market_context_high->crypto_major_1h` score `1.5779` n `54` status `ready` deltaP `6.9583` edge `0.136` maxDD `-1.4048`
- `market_context_high->crypto_alt_24h` score `1.5037` n `49` status `ready` deltaP `-7.8798` edge `0.3971` maxDD `-8.8096`
- `market_context_high->crypto_alt_1h` score `1.4995` n `54` status `ready` deltaP `4.0031` edge `0.1595` maxDD `-2.2314`
- `market_context_high->fx_1h` score `1.4499` n `54` status `ready` deltaP `19.4722` edge `0.0086` maxDD `-0.0736`
- `market_context_high->metal_4h` score `1.3441` n `49` status `ready` deltaP `16.5599` edge `0.0441` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.5068` n `54` status `ready` deltaP `7.7456` edge `0.0163` maxDD `-0.3895`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
