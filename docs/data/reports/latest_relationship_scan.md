# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T22:07:19.366420+00:00`
- Price records: `672`
- Market context records: `2394`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9201`

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

- `news_risk_high->crypto_alt_24h` score `21.3567` n `43` status `ready` deltaP `49.1682` edge `1.5108` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.2222` n `43` status `ready` deltaP `49.9313` edge `1.2296` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.3475` n `43` status `ready` deltaP `29.7925` edge `1.1118` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.6774` n `43` status `ready` deltaP `19.7674` edge `0.8994` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.3693` n `43` status `ready` deltaP `28.1613` edge `0.5323` maxDD `-1.4744`
- `news_risk_high->index_24h` score `5.4685` n `43` status `ready` deltaP `13.6184` edge `0.4068` maxDD `-1.3507`
- `market_context_high->unknown_24h` score `5.288` n `119` status `ready` deltaP `22.7285` edge `0.3303` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.7915` n `142` status `ready` deltaP `23.4434` edge `0.424` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.5875` n `43` status `ready` deltaP `37.924` edge `0.0646` maxDD `-0.1442`
- `market_context_high->crypto_alt_4h` score `3.5089` n `142` status `ready` deltaP `18.1209` edge `0.4395` maxDD `-15.4319`
- `news_risk_high->commodity_4h` score `3.358` n `43` status `ready` deltaP `30.7855` edge `0.2924` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `3.2704` n `119` status `ready` deltaP `14.7059` edge `0.7105` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.4867` n `142` status `ready` deltaP `13.8591` edge `0.1758` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.0709` n `43` status `ready` deltaP `26.3648` edge `0.0152` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.6935` n `43` status `ready` deltaP `15.3822` edge `0.1109` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.5133` n `142` status `ready` deltaP `12.9481` edge `0.1592` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.2324` n `119` status `ready` deltaP `9.3385` edge `0.0922` maxDD `-1.4737`
- `news_risk_high->unknown_1h` score `1.0654` n `43` status `ready` deltaP `19.6978` edge `0.0044` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `0.9757` n `142` status `ready` deltaP `8.107` edge `0.146` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.8681` n `142` status `ready` deltaP `13.9986` edge `0.0616` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
