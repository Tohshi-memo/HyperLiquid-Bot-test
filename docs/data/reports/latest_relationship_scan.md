# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T15:07:40.388767+00:00`
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

- `market_context_high->unknown_24h` score `7038.2215` n `55` status `ready` deltaP `1.3889` edge `586.5092` maxDD `0.0`
- `market_context_high->unknown_4h` score `379.7081` n `55` status `ready` deltaP `5.4989` edge `31.61` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `74.7567` n `55` status `ready` deltaP `3.6119` edge `6.2167` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.0232` n `55` status `ready` deltaP `42.7999` edge `1.4902` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.0677` n `96` status `ready` deltaP `30.2083` edge `1.0232` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.7234` n `55` status `ready` deltaP `54.6875` edge `0.1957` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.3388` n `55` status `ready` deltaP `44.7475` edge `0.261` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.0661` n `55` status `ready` deltaP `23.75` edge `0.3766` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.6537` n `55` status `ready` deltaP `31.0449` edge `0.2978` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `3.4844` n `116` status `ready` deltaP `15.3017` edge `0.327` maxDD `-7.4246`
- `market_context_high->equity_4h` score `3.4682` n `55` status `ready` deltaP `6.0477` edge `0.3189` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.326` n `55` status `ready` deltaP `31.2195` edge `0.0941` maxDD `-0.3387`
- `market_context_high->crypto_major_24h` score `2.392` n `55` status `ready` deltaP `10.685` edge `0.3031` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.7324` n `55` status `ready` deltaP `-5.3409` edge `0.4095` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.608` n `55` status `ready` deltaP `18.8082` edge `0.0511` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.5261` n `55` status `ready` deltaP `3.0267` edge `0.1595` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.382` n `55` status `ready` deltaP `7.8824` edge `0.1236` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.3559` n `55` status `ready` deltaP `3.7752` edge `0.1549` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.9367` n `55` status `ready` deltaP `11.6249` edge `0.0254` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5708` n `55` status `ready` deltaP `13.7861` edge `-0.0003` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
