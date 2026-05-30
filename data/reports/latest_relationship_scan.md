# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T12:07:18.625578+00:00`
- Price records: `672`
- Market context records: `2347`
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

- `news_risk_high->crypto_alt_24h` score `21.2473` n `43` status `ready` deltaP `50.0363` edge `1.4959` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `17.007` n `43` status `ready` deltaP `44.8966` edge `1.1619` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.6035` n `43` status `ready` deltaP `29.7925` edge `1.0498` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.9898` n `43` status `ready` deltaP `19.7674` edge `0.8421` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `9.982` n `139` status `ready` deltaP `19.7842` edge `1.0892` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.6617` n `43` status `ready` deltaP `27.6405` edge `0.4768` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `6.8587` n `139` status `ready` deltaP `24.378` edge `0.4502` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `6.59` n `156` status `ready` deltaP `22.4047` edge `0.6677` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `6.5404` n `156` status `ready` deltaP `25.2502` edge `0.5577` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `5.5896` n `156` status `ready` deltaP `22.4047` edge `0.3774` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.7575` n `43` status `ready` deltaP `12.5767` edge `0.3545` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.016` n `43` status `ready` deltaP `34.1392` edge `0.3544` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.409` n `43` status `ready` deltaP `36.1879` edge `0.0613` maxDD `-0.1442`
- `market_context_high->index_24h` score `2.9211` n `139` status `ready` deltaP `14.0824` edge `0.2013` maxDD `-1.4737`
- `market_context_high->equity_24h` score `2.1706` n `139` status `ready` deltaP `19.8879` edge `0.201` maxDD `-6.8828`
- `market_context_high->index_4h` score `2.0437` n `156` status `ready` deltaP `20.0086` edge `0.1195` maxDD `-2.2732`
- `news_risk_high->fx_4h` score `2.0295` n `43` status `ready` deltaP `25.9075` edge `0.0148` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `1.6654` n `164` status `ready` deltaP `12.228` edge `0.176` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.5665` n `164` status `ready` deltaP `12.9984` edge `0.1633` maxDD `-4.2199`
- `market_context_high->equity_4h` score `1.1277` n `156` status `ready` deltaP `10.8935` edge `0.1618` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
