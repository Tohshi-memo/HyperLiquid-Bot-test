# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T05:22:30.319939+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11734`

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

- `news_risk_high->unknown_24h` score `2019.2004` n `113` status `ready` deltaP `1.2153` edge `168.2586` maxDD `0.0`
- `market_context_high->unknown_1h` score `115.093` n `46` status `ready` deltaP `10.401` edge `9.5264` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `52.2849` n `44` status `ready` deltaP `30.1926` edge `4.1909` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.3986` n `44` status `ready` deltaP `14.9148` edge `2.3051` maxDD `-2.7051`
- `market_context_high->equity_24h` score `27.9364` n `44` status `ready` deltaP `36.0954` edge `2.1188` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8861` n `44` status `ready` deltaP `33.4912` edge `0.4427` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.8782` n `44` status `ready` deltaP `34.2171` edge `0.1189` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.2178` n `44` status `ready` deltaP `36.0033` edge `0.0352` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.8155` n `44` status `ready` deltaP `16.4495` edge `0.1626` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.1568` n `44` status `ready` deltaP `8.5505` edge `0.102` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.0593` n `113` status `ready` deltaP `18.8913` edge `0.1271` maxDD `-6.8481`
- `market_context_high->equity_1h` score `0.9207` n `46` status `ready` deltaP `10.7264` edge `0.0455` maxDD `-1.5564`
- `market_context_high->crypto_major_4h` score `0.867` n `44` status `ready` deltaP `6.9152` edge `0.1166` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.8283` n `46` status `ready` deltaP `12.6009` edge `0.0087` maxDD `-0.2275`
- `market_context_high->crypto_major_1h` score `0.6049` n `46` status `ready` deltaP `6.7496` edge `0.0912` maxDD `-4.8632`
- `news_risk_high->index_24h` score `0.5953` n `113` status `ready` deltaP `12.7551` edge `0.0341` maxDD `-2.2287`
- `market_context_high->crypto_alt_1h` score `0.2797` n `46` status `ready` deltaP `6.5283` edge `0.0687` maxDD `-5.7799`
- `market_context_high->fx_1h` score `0.2579` n `46` status `ready` deltaP `9.2879` edge `0.0068` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.1259` n `46` status `ready` deltaP `4.7904` edge `0.0104` maxDD `-0.2145`
- `news_risk_high->index_1h` score `-0.1898` n `142` status `ready` deltaP `1.5476` edge `0.003` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
