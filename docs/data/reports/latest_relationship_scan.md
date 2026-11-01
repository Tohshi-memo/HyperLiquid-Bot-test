# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T15:37:26.328681+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6615`

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

- `market_context_high->unknown_24h` score `7071.6967` n `55` status `ready` deltaP `1.3889` edge `589.2988` maxDD `0.0`
- `market_context_high->unknown_4h` score `379.8653` n `55` status `ready` deltaP `5.4989` edge `31.6231` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `74.6955` n `55` status `ready` deltaP `3.4622` edge `6.2126` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.0508` n `55` status `ready` deltaP `42.7999` edge `1.4925` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.0328` n `94` status `ready` deltaP `30.2674` edge `1.0199` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.721` n `55` status `ready` deltaP `54.6875` edge `0.1955` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.2978` n `55` status `ready` deltaP `44.4003` edge `0.2599` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.0939` n `55` status `ready` deltaP `23.9024` edge `0.3779` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.6731` n `55` status `ready` deltaP `31.1974` edge `0.2984` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.479` n `55` status `ready` deltaP `6.0477` edge `0.3198` maxDD `-2.283`
- `news_risk_high->crypto_alt_4h` score `3.3533` n `116` status `ready` deltaP `14.5921` edge `0.3208` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `3.298` n `55` status `ready` deltaP `30.9146` edge `0.0938` maxDD `-0.3387`
- `market_context_high->crypto_major_24h` score `2.3998` n `55` status `ready` deltaP `10.685` edge `0.3041` maxDD `-3.0799`
- `news_risk_high->unknown_1h` score `1.936` n `126` status `ready` deltaP `-7.8509` edge `0.2423` maxDD `-0.9571`
- `market_context_high->crypto_alt_24h` score `1.7817` n `55` status `ready` deltaP `-4.9937` edge `0.4135` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.6348` n `55` status `ready` deltaP `19.113` edge `0.0513` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.5417` n `55` status `ready` deltaP `3.1764` edge `0.1598` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.4084` n `55` status `ready` deltaP `8.1818` edge `0.1238` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.3907` n `55` status `ready` deltaP `4.0746` edge `0.1558` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.9367` n `55` status `ready` deltaP `11.6249` edge `0.0254` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
