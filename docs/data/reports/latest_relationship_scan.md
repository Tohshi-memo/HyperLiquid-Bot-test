# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T13:37:25.832034+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2590`

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

- `market_context_high->unknown_1h` score `10007.8674` n `126` status `ready` deltaP `0.8649` edge `834.003` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6084.7383` n `126` status `ready` deltaP `-0.7719` edge `507.0972` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2101` n `126` status `ready` deltaP `3.8019` edge `0.0142` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3334` n `126` status `ready` deltaP `2.2597` edge `0.0034` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.6402` n `126` status `ready` deltaP `9.9666` edge `0.0321` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4154` n `126` status `ready` deltaP `-9.1056` edge `-0.0013` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8693` n `126` status `ready` deltaP `-5.9645` edge `0.0017` maxDD `-1.794`
- `market_context_high->equity_1h` score `-1.9126` n `126` status `ready` deltaP `5.2395` edge `0.0116` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.2943` n `126` status `ready` deltaP `-8.3714` edge `-0.0222` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.5857` n `126` status `ready` deltaP `-5.4709` edge `-0.0157` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.8193` n `126` status `ready` deltaP `1.5112` edge `-0.0132` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.4917` n `126` status `ready` deltaP `-5.0922` edge `-0.0293` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-5.1174` n `126` status `ready` deltaP `-2.9375` edge `0.0564` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.4295` n `123` status `ready` deltaP `-13.0336` edge `-0.0068` maxDD `-6.7014`
- `market_context_high->commodity_4h` score `-6.9454` n `126` status `ready` deltaP `-19.4251` edge `-0.08` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.3357` n `123` status `ready` deltaP `9.1675` edge `0.1155` maxDD `-51.3676`
- `market_context_high->crypto_alt_4h` score `-8.642` n `126` status `ready` deltaP `-4.0046` edge `-0.0122` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-10.7515` n `123` status `ready` deltaP `18.551` edge `0.4584` maxDD `-145.1715`
- `market_context_high->crypto_alt_24h` score `-14.0255` n `123` status `ready` deltaP `7.5077` edge `0.1769` maxDD `-150.3411`
- `market_context_high->index_24h` score `-14.6094` n `123` status `ready` deltaP `-27.0664` edge `-0.1203` maxDD `-39.0031`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
