# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T21:07:26.624177+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7757`

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

- `market_context_high->unknown_24h` score `3180.4205` n `94` status `ready` deltaP `-10.2726` edge `265.1465` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `111.3063` n `94` status `ready` deltaP `0.6325` edge `9.2846` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `77.6824` n `108` status `ready` deltaP `-5.1951` edge `6.5368` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `19.2076` n `78` status `ready` deltaP `45.3526` edge `1.3034` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.7582` n `94` status `ready` deltaP `24.6196` edge `1.0081` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.4159` n `108` status `ready` deltaP `20.2744` edge `0.4548` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.9356` n `94` status `ready` deltaP `43.8312` edge `0.1374` maxDD `-0.1315`
- `market_context_high->metal_4h` score `1.6228` n `94` status `ready` deltaP `20.0733` edge `0.0439` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.8998` n `94` status `ready` deltaP `12.7341` edge `0.0191` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.8265` n `108` status `ready` deltaP `8.8767` edge `0.1051` maxDD `-3.9659`
- `market_context_high->equity_4h` score `0.6065` n `94` status `ready` deltaP `3.4931` edge `0.1938` maxDD `-4.48`
- `market_context_high->equity_1h` score `0.5076` n `94` status `ready` deltaP `7.4468` edge `0.103` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.4811` n `94` status `ready` deltaP `14.7574` edge `0.0608` maxDD `-0.8002`
- `market_context_high->crypto_major_1h` score `0.3788` n `94` status `ready` deltaP `9.5745` edge `0.0875` maxDD `-5.2213`
- `market_context_high->fx_4h` score `0.285` n `94` status `ready` deltaP `9.2631` edge `0.0011` maxDD `-0.1285`
- `market_context_high->fx_1h` score `0.2324` n `94` status `ready` deltaP `8.5425` edge `-0.0004` maxDD `-0.1407`
- `market_context_high->metal_24h` score `-0.1919` n `94` status `ready` deltaP `10.3945` edge `0.1708` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-0.321` n `94` status `ready` deltaP `15.1888` edge `0.1316` maxDD `-14.5879`
- `market_context_high->commodity_1h` score `-0.3747` n `94` status `ready` deltaP `-1.5766` edge `0.0139` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.3764` n `94` status `ready` deltaP `3.3571` edge `0.0021` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
