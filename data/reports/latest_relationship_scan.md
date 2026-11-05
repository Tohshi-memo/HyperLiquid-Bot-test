# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T13:22:42.437676+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3791`

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

- `news_risk_high->crypto_alt_4h` score `0.1201` n `146` status `ready` deltaP `7.7619` edge `0.2273` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4248` n `146` status `ready` deltaP `3.6789` edge `0.0438` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7323` n `146` status `ready` deltaP `-3.1211` edge `-0.003` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.743` n `146` status `ready` deltaP `2.8443` edge `-0.0009` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.4497` n `146` status `ready` deltaP `-7.4695` edge `-0.0109` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5688` n `146` status `ready` deltaP `-8.8405` edge `-0.02` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.7615` n `146` status `ready` deltaP `1.2989` edge `-0.0044` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2578` n `146` status `ready` deltaP `-15.9437` edge `-0.0123` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.3935` n `146` status `ready` deltaP `-9.6752` edge `0.0017` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.4677` n `146` status `ready` deltaP `-4.9893` edge `-0.0155` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.941` n `146` status `ready` deltaP `-12.3382` edge `-0.0106` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-3.0475` n `146` status `ready` deltaP `-5.7604` edge `-0.043` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.6907` n `146` status `ready` deltaP `-13.0847` edge `0.0151` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.6841` n `146` status `ready` deltaP `-12.1784` edge `-0.072` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.5883` n `146` status `ready` deltaP `-10.5726` edge `-0.0766` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-7.354` n `146` status `ready` deltaP `-9.5771` edge `-0.1908` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.3227` n `146` status `ready` deltaP `-16.4431` edge `0.1588` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.4549` n `146` status `ready` deltaP `2.2135` edge `-0.0499` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-14.2392` n `146` status `ready` deltaP `9.8198` edge `0.1983` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.6968` n `146` status `ready` deltaP `2.5281` edge `-0.3298` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
