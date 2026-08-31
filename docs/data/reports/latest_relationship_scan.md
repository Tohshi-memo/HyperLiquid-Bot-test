# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T15:02:51.347884+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11688`

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

- `risk_on_high->crypto_alt_24h` score `13.3019` n `66` status `ready` deltaP `34.4697` edge `1.1617` maxDD `-18.3075`
- `risk_on_and_context->crypto_alt_24h` score `13.3019` n `66` status `ready` deltaP `34.4697` edge `1.1617` maxDD `-18.3075`
- `risk_on_high->unknown_4h` score `8.091` n `107` status `ready` deltaP `24.9459` edge `0.5696` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.091` n `107` status `ready` deltaP `24.9459` edge `0.5696` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.545` n `159` status `ready` deltaP `21.6425` edge `0.4705` maxDD `-2.5493`
- `market_context_high->crypto_alt_24h` score `4.3546` n `109` status `ready` deltaP `16.552` edge `0.6715` maxDD `-27.517`
- `risk_on_high->fx_24h` score `2.9672` n `66` status `ready` deltaP `59.5486` edge `0.0432` maxDD `-1.1157`
- `risk_on_and_context->fx_24h` score `2.9672` n `66` status `ready` deltaP `59.5486` edge `0.0432` maxDD `-1.1157`
- `risk_on_high->unknown_1h` score `2.449` n `107` status `ready` deltaP `6.8149` edge `0.2163` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.449` n `107` status `ready` deltaP `6.8149` edge `0.2163` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.2264` n `159` status `ready` deltaP `6.1566` edge `0.2075` maxDD `-2.041`
- `risk_on_high->crypto_major_24h` score `1.6196` n `66` status `ready` deltaP `20.2651` edge `0.5147` maxDD `-29.3725`
- `risk_on_and_context->crypto_major_24h` score `1.6196` n `66` status `ready` deltaP `20.2651` edge `0.5147` maxDD `-29.3725`
- `market_context_high->metal_24h` score `1.6119` n `109` status `ready` deltaP `27.5866` edge `0.185` maxDD `-5.6477`
- `news_risk_high->unknown_1h` score `1.5455` n `61` status `ready` deltaP `3.9192` edge `0.1373` maxDD `-1.1043`
- `market_context_high->fx_24h` score `1.3584` n `109` status `ready` deltaP `34.9309` edge `0.0276` maxDD `-1.782`
- `risk_on_high->commodity_24h` score `0.8066` n `66` status `ready` deltaP `9.7223` edge `0.1374` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.8066` n `66` status `ready` deltaP `9.7223` edge `0.1374` maxDD `-0.5706`
- `risk_on_high->metal_24h` score `0.7854` n `66` status `ready` deltaP `26.6414` edge `0.0695` maxDD `-5.0471`
- `risk_on_and_context->metal_24h` score `0.7854` n `66` status `ready` deltaP `26.6414` edge `0.0695` maxDD `-5.0471`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
