# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T07:22:23.694445+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6477`

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

- `market_context_high->unknown_24h` score `7033.1766` n `55` status `ready` deltaP `4.6875` edge `586.0668` maxDD `0.0`
- `market_context_high->unknown_4h` score `372.9279` n `55` status `ready` deltaP `5.3464` edge `31.046` maxDD `-0.0124`
- `news_risk_high->unknown_1h` score `75.1712` n `109` status `ready` deltaP `-5.0252` edge `6.3264` maxDD `-0.9571`
- `market_context_high->unknown_1h` score `48.9005` n `55` status `ready` deltaP `2.4143` edge `4.07` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.7402` n `55` status `ready` deltaP `46.2721` edge `1.5268` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.1347` n `98` status `ready` deltaP `30.506` edge `1.0268` maxDD `-6.8493`
- `market_context_high->index_24h` score `7.2944` n `55` status `ready` deltaP `60.0694` edge `0.2074` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.744` n `55` status `ready` deltaP `46.4836` edge `0.2832` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `5.7667` n `55` status `ready` deltaP `23.2927` edge `0.3547` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.4645` n `55` status `ready` deltaP `30.4352` edge `0.2861` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `4.8517` n `108` status `ready` deltaP `18.2927` edge `0.421` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `3.3889` n `55` status `ready` deltaP `31.6768` edge `0.0963` maxDD `-0.3387`
- `market_context_high->equity_4h` score `3.3552` n `55` status `ready` deltaP `5.8952` edge `0.3105` maxDD `-2.283`
- `market_context_high->crypto_major_24h` score `2.6178` n `55` status `ready` deltaP `11.7267` edge `0.3251` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.9621` n `55` status `ready` deltaP `-4.2992` edge `0.432` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.5632` n `55` status `ready` deltaP `18.5033` edge `0.0494` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.4434` n `55` status `ready` deltaP `2.1285` edge `0.1586` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.4144` n `55` status `ready` deltaP `8.1818` edge `0.1243` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.3751` n `55` status `ready` deltaP `4.0746` edge `0.1545` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.8612` n `55` status `ready` deltaP `10.7267` edge `0.0251` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
