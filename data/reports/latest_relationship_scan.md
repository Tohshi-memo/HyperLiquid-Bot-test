# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T02:22:29.239667+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9858`

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

- `market_context_high->unknown_1h` score `72.1769` n `47` status `ready` deltaP `10.8645` edge `5.9494` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `36.4921` n `46` status `ready` deltaP `23.7772` edge `2.8981` maxDD `-0.5817`
- `market_context_high->equity_24h` score `21.1871` n `46` status `ready` deltaP `21.173` edge `1.6345` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `20.7696` n `46` status `ready` deltaP `18.75` edge `1.6058` maxDD `0.0`
- `market_context_high->index_24h` score `7.1152` n `46` status `ready` deltaP `30.2008` edge `0.4003` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.9815` n `103` status `ready` deltaP `14.6889` edge `0.417` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.6212` n `103` status `ready` deltaP `17.5853` edge `0.3256` maxDD `-2.619`
- `news_risk_high->crypto_major_24h` score `4.1924` n `102` status `ready` deltaP `-3.2475` edge `1.2278` maxDD `-59.876`
- `news_risk_high->crypto_alt_1h` score `2.6193` n `103` status `ready` deltaP `13.7565` edge `0.1756` maxDD `-1.5895`
- `news_risk_high->commodity_24h` score `2.4951` n `102` status `ready` deltaP `23.8664` edge `0.1667` maxDD `-2.431`
- `market_context_high->index_4h` score `2.4734` n `47` status `ready` deltaP `29.1483` edge `0.0272` maxDD `-0.2323`
- `market_context_high->metal_24h` score `2.118` n `46` status `ready` deltaP `24.1773` edge `0.0387` maxDD `-0.2042`
- `news_risk_high->crypto_major_1h` score `2.1056` n `103` status `ready` deltaP `16.1517` edge `0.1113` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.5856` n `103` status `ready` deltaP `23.224` edge `0.0409` maxDD `-0.421`
- `market_context_high->equity_4h` score `1.4667` n `47` status `ready` deltaP `11.8091` edge `0.0853` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.2019` n `102` status `ready` deltaP `29.3403` edge `0.1216` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.8049` n `47` status `ready` deltaP `12.9634` edge `0.0085` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6625` n `103` status `ready` deltaP `15.502` edge `0.0112` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.6178` n `47` status `ready` deltaP `9.0712` edge `0.0313` maxDD `-1.5564`
- `news_risk_high->metal_4h` score `0.3282` n `103` status `ready` deltaP `14.27` edge `0.0427` maxDD `-1.9941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
