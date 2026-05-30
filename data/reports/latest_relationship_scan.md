# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T11:52:20.133296+00:00`
- Price records: `672`
- Market context records: `2346`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9176`

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

- `news_risk_high->crypto_alt_24h` score `21.2089` n `43` status `ready` deltaP `50.0363` edge `1.4927` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.9655` n `43` status `ready` deltaP `44.723` edge `1.1596` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.5771` n `43` status `ready` deltaP `29.7925` edge `1.0476` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.9526` n `43` status `ready` deltaP `19.7674` edge `0.839` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `10.0948` n `139` status `ready` deltaP `19.7842` edge `1.0986` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.6305` n `43` status `ready` deltaP `27.6405` edge `0.4742` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `6.9571` n `139` status `ready` deltaP `24.378` edge `0.4584` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `6.6008` n `157` status `ready` deltaP `22.5843` edge `0.6674` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `6.5325` n `157` status `ready` deltaP `25.3768` edge `0.5562` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `5.5148` n `157` status `ready` deltaP `22.0998` edge `0.3732` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.7287` n `43` status `ready` deltaP `12.5767` edge `0.3521` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.016` n `43` status `ready` deltaP `34.1392` edge `0.3544` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.409` n `43` status `ready` deltaP `36.1879` edge `0.0613` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.0087` n `139` status `ready` deltaP `14.0824` edge `0.2086` maxDD `-1.4737`
- `market_context_high->equity_24h` score `2.251` n `139` status `ready` deltaP `19.8879` edge `0.2077` maxDD `-6.8828`
- `market_context_high->index_4h` score `2.0493` n `157` status `ready` deltaP `20.1229` edge `0.1192` maxDD `-2.2732`
- `news_risk_high->fx_4h` score `2.0295` n `43` status `ready` deltaP `25.9075` edge `0.0148` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `1.6732` n `165` status `ready` deltaP `12.446` edge `0.1752` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.5324` n `165` status `ready` deltaP `12.7527` edge `0.1621` maxDD `-4.2199`
- `market_context_high->equity_4h` score `1.1293` n `157` status `ready` deltaP `11.0037` edge `0.1612` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
