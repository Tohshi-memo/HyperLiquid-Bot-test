# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T22:07:16.929349+00:00`
- Price records: `672`
- Market context records: `1781`
- Flow alert records: `7024`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8882`

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

- `market_context_high->metal_24h` score `7.0993` n `183` status `ready` deltaP `28.051` edge `0.6472` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `5.9528` n `30` status `ready` deltaP `27.2765` edge `0.3797` maxDD `-3.5713`
- `market_context_high->crypto_alt_4h` score `5.9244` n `194` status `ready` deltaP `21.7076` edge `0.5256` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.5388` n `194` status `ready` deltaP `22.935` edge `0.4659` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `3.6176` n `194` status `ready` deltaP `15.2973` edge `0.4266` maxDD `-11.1695`
- `market_context_high->index_24h` score `3.2789` n `183` status `ready` deltaP `16.5415` edge `0.2858` maxDD `-4.1604`
- `market_context_high->equity_4h` score `3.0695` n `194` status `ready` deltaP `16.6269` edge `0.2544` maxDD `-5.0894`
- `news_risk_high->commodity_1h` score `3.0659` n `30` status `ready` deltaP `23.8224` edge `0.1284` maxDD `-1.2043`
- `market_context_high->equity_24h` score `2.0954` n `183` status `ready` deltaP `16.1943` edge `0.5565` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.682` n `183` status `ready` deltaP `13.351` edge `0.5832` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.9451` n `194` status `ready` deltaP `12.4591` edge `0.1046` maxDD `-3.7119`
- `news_risk_high->fx_4h` score `0.8071` n `30` status `ready` deltaP `20.2643` edge `-0.0044` maxDD `-0.1774`
- `market_context_high->crypto_alt_1h` score `0.6251` n `197` status `ready` deltaP `7.8027` edge `0.1103` maxDD `-4.8183`
- `news_risk_high->unknown_4h` score `0.4608` n `30` status `ready` deltaP `10.5894` edge `0.0608` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `0.2265` n `197` status `ready` deltaP `4.9979` edge `0.0929` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0608` n `197` status `ready` deltaP `5.0427` edge `0.0523` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1416` n `197` status `ready` deltaP `4.4508` edge `0.0217` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.1745` n `194` status `ready` deltaP `13.3219` edge `0.158` maxDD `-12.5349`
- `news_risk_high->unknown_1h` score `-0.4248` n `30` status `ready` deltaP `17.1557` edge `-0.1216` maxDD `-2.1115`
- `market_context_high->fx_24h` score `-0.441` n `183` status `ready` deltaP `8.4386` edge `0.0119` maxDD `-1.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
