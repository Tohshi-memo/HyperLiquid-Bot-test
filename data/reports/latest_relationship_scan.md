# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T23:37:21.632939+00:00`
- Price records: `672`
- Market context records: `2401`
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

- `news_risk_high->crypto_alt_24h` score `20.9686` n `43` status `ready` deltaP `48.1266` edge `1.4854` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.1992` n `43` status `ready` deltaP `49.5841` edge `1.23` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.3391` n `43` status `ready` deltaP `29.7925` edge `1.1111` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.4` n `43` status `ready` deltaP `19.4202` edge `0.8786` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.2733` n `43` status `ready` deltaP `28.1613` edge `0.5243` maxDD `-1.4744`
- `news_risk_high->index_24h` score `5.4443` n `43` status `ready` deltaP `13.2712` edge `0.4071` maxDD `-1.3507`
- `market_context_high->unknown_24h` score `5.2407` n `116` status `ready` deltaP `22.4677` edge `0.3281` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.8085` n `139` status `ready` deltaP `23.5819` edge `0.4245` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.5995` n `43` status `ready` deltaP `37.924` edge `0.0656` maxDD `-0.1442`
- `market_context_high->crypto_alt_4h` score `3.5245` n `139` status `ready` deltaP `18.0164` edge `0.4415` maxDD `-15.4319`
- `news_risk_high->commodity_4h` score `3.2553` n `43` status `ready` deltaP `30.1758` edge `0.2833` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `2.9256` n `116` status `ready` deltaP `13.4459` edge `0.6747` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.3947` n `139` status `ready` deltaP `13.0232` edge `0.1737` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.1134` n `43` status `ready` deltaP `26.8221` edge `0.0157` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.6887` n `43` status `ready` deltaP `15.3822` edge `0.1105` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.2197` n `139` status `ready` deltaP `12.353` edge `0.1387` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.1849` n `116` status `ready` deltaP `8.3393` edge `0.0949` maxDD `-1.4737`
- `news_risk_high->unknown_1h` score `1.105` n `43` status `ready` deltaP `19.9972` edge `0.0057` maxDD `-1.7548`
- `market_context_high->index_4h` score `0.8297` n `139` status `ready` deltaP `13.8631` edge `0.0593` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `0.7215` n `139` status `ready` deltaP `7.8243` edge `0.1267` maxDD `-6.1656`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
