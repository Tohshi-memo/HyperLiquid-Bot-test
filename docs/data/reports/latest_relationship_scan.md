# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T23:22:19.865504+00:00`
- Price records: `672`
- Market context records: `2400`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9202`

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

- `news_risk_high->crypto_alt_24h` score `21.0533` n `43` status `ready` deltaP `48.3002` edge `1.4913` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.2227` n `43` status `ready` deltaP `49.7577` edge `1.2308` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.3487` n `43` status `ready` deltaP `29.7925` edge `1.1119` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.4799` n `43` status `ready` deltaP `19.5938` edge `0.8841` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.2973` n `43` status `ready` deltaP `28.1613` edge `0.5263` maxDD `-1.4744`
- `news_risk_high->index_24h` score `5.4594` n `43` status `ready` deltaP `13.4448` edge `0.4072` maxDD `-1.3507`
- `market_context_high->unknown_24h` score `5.2647` n `116` status `ready` deltaP `22.4677` edge `0.3301` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.8073` n `139` status `ready` deltaP `23.5819` edge `0.4244` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.5983` n `43` status `ready` deltaP `37.924` edge `0.0655` maxDD `-0.1442`
- `market_context_high->crypto_alt_4h` score `3.5233` n `139` status `ready` deltaP `18.0164` edge `0.4414` maxDD `-15.4319`
- `news_risk_high->commodity_4h` score `3.2545` n `43` status `ready` deltaP `30.1758` edge `0.2832` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `2.9775` n `116` status `ready` deltaP `13.6195` edge `0.6802` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.4153` n `139` status `ready` deltaP `13.1756` edge `0.1744` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.1012` n `43` status `ready` deltaP `26.6697` edge `0.0157` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7093` n `43` status `ready` deltaP `15.5346` edge `0.1112` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.2448` n `139` status `ready` deltaP `12.5027` edge `0.1398` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.2` n `116` status `ready` deltaP `8.5129` edge `0.095` maxDD `-1.4737`
- `news_risk_high->unknown_1h` score `1.1074` n `43` status `ready` deltaP `19.9972` edge `0.0059` maxDD `-1.7548`
- `market_context_high->index_4h` score `0.8249` n `139` status `ready` deltaP `13.8631` edge `0.0589` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `0.7263` n `139` status `ready` deltaP `7.8243` edge `0.1271` maxDD `-6.1656`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
