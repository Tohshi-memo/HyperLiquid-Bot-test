# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T14:37:33.398351+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3795`

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

- `news_risk_high->crypto_alt_4h` score `0.2916` n `146` status `ready` deltaP `8.5241` edge `0.2442` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.3842` n `146` status `ready` deltaP `3.8286` edge `0.048` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6973` n `146` status `ready` deltaP `-2.5223` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.737` n `146` status `ready` deltaP `2.8443` edge `-0.0004` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.4427` n `146` status `ready` deltaP `-7.4695` edge `-0.01` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5913` n `146` status `ready` deltaP `-9.1399` edge `-0.0209` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.7395` n `146` status `ready` deltaP `1.6037` edge `-0.0036` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2178` n `146` status `ready` deltaP `-15.2492` edge `-0.0118` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.3827` n `146` status `ready` deltaP `-4.3905` edge `-0.0086` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.3923` n `146` status `ready` deltaP `-9.6752` edge `0.0018` maxDD `-3.2657`
- `news_risk_high->crypto_major_1h` score `-2.9312` n `146` status `ready` deltaP `-5.1616` edge `-0.0373` maxDD `-9.4709`
- `news_risk_high->index_24h` score `-2.9449` n `146` status `ready` deltaP `-12.3382` edge `-0.0111` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.6907` n `146` status `ready` deltaP `-13.0847` edge `0.0151` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.7411` n `146` status `ready` deltaP `-12.6357` edge `-0.0737` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.3185` n `146` status `ready` deltaP `-9.8104` edge `-0.0592` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-7.6011` n `146` status `ready` deltaP `-10.4452` edge `-0.2056` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.1201` n `146` status `ready` deltaP `-15.5751` edge `0.1699` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.2659` n `146` status `ready` deltaP `2.6708` edge `-0.0372` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-14.3616` n `146` status `ready` deltaP `9.8198` edge `0.1881` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-16.0535` n `146` status `ready` deltaP `1.8337` edge `-0.3709` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
