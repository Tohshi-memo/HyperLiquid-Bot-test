# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T08:37:25.910754+00:00`
- Price records: `672`
- Market context records: `6069`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11112`

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

- `news_risk_high->fx_24h` score `8.1546` n `30` status `ready` deltaP `72.7431` edge `0.1946` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.434` n `30` status `ready` deltaP `45.9451` edge `0.0678` maxDD `-0.0345`
- `news_risk_high->crypto_alt_24h` score `3.525` n `30` status `ready` deltaP `29.4444` edge `0.1122` maxDD `-0.5131`
- `news_risk_high->fx_1h` score `2.4207` n `32` status `ready` deltaP `29.0419` edge `0.022` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.5521` n `206` status `ready` deltaP `9.0989` edge `0.1604` maxDD `-2.671`
- `news_risk_high->commodity_24h` score `1.3084` n `30` status `ready` deltaP `21.0417` edge `-0.0107` maxDD `-0.3101`
- `news_risk_high->crypto_major_1h` score `1.1879` n `32` status `ready` deltaP `13.8286` edge `0.1068` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6111` n `32` status `ready` deltaP `9.0756` edge `0.064` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0789` n `30` status `ready` deltaP `9.2361` edge `0.0357` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4306` n `206` status `ready` deltaP `3.1306` edge `0.0038` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.5462` n `206` status `ready` deltaP `0.1584` edge `-0.0009` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.7949` n `206` status `ready` deltaP `-2.5812` edge `-0.0044` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.7989` n `206` status `ready` deltaP `4.9997` edge `0.041` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.8056` n `206` status `ready` deltaP `4.555` edge `0.0416` maxDD `-9.3536`
- `news_risk_high->metal_1h` score `-0.8269` n `32` status `ready` deltaP `-2.6946` edge `-0.0383` maxDD `-1.6464`
- `market_context_high->index_4h` score `-0.9153` n `206` status `ready` deltaP `2.2629` edge `0.0209` maxDD `-1.9335`
- `market_context_high->equity_1h` score `-0.9953` n `206` status `ready` deltaP `1.0799` edge `0.0227` maxDD `-4.3608`
- `news_risk_high->index_1h` score `-1.0026` n `32` status `ready` deltaP `-8.1774` edge `-0.0177` maxDD `-1.1725`
- `market_context_high->metal_4h` score `-1.0367` n `206` status `ready` deltaP `4.0285` edge `0.0055` maxDD `-3.4996`
- `market_context_high->index_1h` score `-1.2595` n `206` status `ready` deltaP `-2.6859` edge `0.0028` maxDD `-1.1879`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
