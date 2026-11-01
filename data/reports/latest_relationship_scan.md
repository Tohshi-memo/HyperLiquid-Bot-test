# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T12:22:25.906868+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6597`

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

- `market_context_high->unknown_24h` score `7031.7122` n `55` status `ready` deltaP `1.5625` edge `585.9656` maxDD `0.0`
- `market_context_high->unknown_4h` score `376.1809` n `55` status `ready` deltaP `5.194` edge `31.3181` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `64.2112` n `55` status `ready` deltaP `3.1628` edge `5.3409` maxDD `-0.2178`
- `news_risk_high->unknown_1h` score `42.806` n `128` status `ready` deltaP `-6.2406` edge `3.6374` maxDD `-0.9571`
- `market_context_high->equity_24h` score `21.2421` n `55` status `ready` deltaP `43.8415` edge `1.5015` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `12.8108` n `98` status `ready` deltaP `29.6379` edge `1.0056` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.9254` n `55` status `ready` deltaP `56.5972` edge `0.1998` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.5073` n `55` status `ready` deltaP `45.7892` edge `0.2681` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `5.8653` n `55` status `ready` deltaP `23.4451` edge `0.3619` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.4193` n `55` status `ready` deltaP `29.8254` edge `0.2864` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `4.4152` n `116` status `ready` deltaP `16.721` edge `0.3951` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `3.3575` n `55` status `ready` deltaP `31.5244` edge `0.0947` maxDD `-0.3387`
- `market_context_high->equity_4h` score `3.3402` n `55` status `ready` deltaP `5.4379` edge `0.3123` maxDD `-2.283`
- `market_context_high->crypto_major_24h` score `2.4369` n `55` status `ready` deltaP `10.8586` edge `0.3077` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.7649` n `55` status `ready` deltaP `-5.1673` edge `0.4125` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.5618` n `55` status `ready` deltaP `18.3508` edge `0.0503` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.4482` n `55` status `ready` deltaP `2.2782` edge `0.158` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.3748` n `55` status `ready` deltaP `8.0321` edge `0.122` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.3511` n `55` status `ready` deltaP `3.9249` edge `0.1535` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.8852` n `55` status `ready` deltaP `11.0261` edge `0.0251` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
