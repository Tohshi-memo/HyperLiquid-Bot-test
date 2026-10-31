# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T19:07:27.268296+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7645`

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

- `market_context_high->unknown_24h` score `2958.0067` n `98` status `ready` deltaP `-9.5344` edge `246.6071` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `91.8196` n `98` status `ready` deltaP `0.7839` edge `7.6597` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `77.7088` n `108` status `ready` deltaP `-5.1951` edge `6.539` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `19.4125` n `70` status `ready` deltaP `45.754` edge `1.3178` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.8366` n `98` status `ready` deltaP `25.7051` edge `1.0074` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.1215` n `108` status `ready` deltaP `19.0549` edge `0.4384` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.8639` n `98` status `ready` deltaP `43.3107` edge `0.1349` maxDD `-0.1315`
- `market_context_high->metal_4h` score `1.6328` n `98` status `ready` deltaP `20.2432` edge `0.0436` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.8231` n `98` status `ready` deltaP `11.8508` edge `0.0186` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.7341` n `108` status `ready` deltaP `8.2779` edge `0.1014` maxDD `-3.9659`
- `market_context_high->equity_4h` score `0.6927` n `98` status `ready` deltaP `5.3602` edge `0.1924` maxDD `-4.48`
- `market_context_high->equity_1h` score `0.4498` n `98` status `ready` deltaP `6.8435` edge `0.0996` maxDD `-2.3383`
- `market_context_high->fx_4h` score `0.3138` n `98` status `ready` deltaP `9.6534` edge `0.0009` maxDD `-0.1285`
- `market_context_high->crypto_major_1h` score `0.3008` n `98` status `ready` deltaP `8.5849` edge `0.0841` maxDD `-5.2213`
- `market_context_high->fx_1h` score `0.2941` n `98` status `ready` deltaP `9.7` edge `-0.0002` maxDD `-0.1407`
- `market_context_high->commodity_4h` score `0.2256` n `98` status `ready` deltaP `13.088` edge `0.0579` maxDD `-0.9648`
- `market_context_high->metal_24h` score `-0.0387` n `98` status `ready` deltaP `12.3051` edge `0.1777` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-0.2037` n `98` status `ready` deltaP `16.0341` edge `0.141` maxDD `-14.5879`
- `market_context_high->commodity_1h` score `-0.3345` n `98` status `ready` deltaP `-0.7882` edge `0.0138` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.3446` n `98` status `ready` deltaP `3.7547` edge `0.0021` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
