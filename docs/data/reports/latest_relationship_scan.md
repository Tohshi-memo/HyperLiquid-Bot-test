# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T23:22:27.750859+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `news_risk_high->unknown_1h` score `2.4511` n `31` status `ready` deltaP `28.7957` edge `0.0241` maxDD `-0.2787`
- `market_context_high->unknown_1h` score `1.6181` n `139` status `ready` deltaP `5.3796` edge `0.1217` maxDD `-0.4843`
- `news_risk_high->fx_1h` score `1.539` n `31` status `ready` deltaP `20.7504` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->commodity_1h` score `1.2309` n `31` status `ready` deltaP `27.3518` edge `-0.0062` maxDD `-0.4666`
- `market_context_high->unknown_4h` score `0.9898` n `139` status `ready` deltaP `19.3247` edge `-0.0075` maxDD `-0.4415`
- `news_risk_high->equity_1h` score `0.764` n `31` status `ready` deltaP `17.9737` edge `0.0063` maxDD `-0.9204`
- `market_context_high->fx_4h` score `0.1299` n `139` status `ready` deltaP `8.6693` edge `0.0091` maxDD `-0.3527`
- `market_context_high->index_1h` score `-0.0697` n `139` status `ready` deltaP `5.9945` edge `0.0042` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1059` n `139` status `ready` deltaP `2.672` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.34` n `139` status `ready` deltaP `4.56` edge `0.033` maxDD `-5.2257`
- `news_risk_high->metal_1h` score `-0.3626` n `31` status `ready` deltaP `-2.8105` edge `-0.0096` maxDD `-0.1184`
- `market_context_high->metal_4h` score `-0.3984` n `139` status `ready` deltaP `6.7786` edge `-0.0168` maxDD `-1.5942`
- `news_risk_high->crypto_major_1h` score `-0.4398` n `31` status `ready` deltaP `10.1072` edge `-0.036` maxDD `-5.0209`
- `market_context_high->metal_1h` score `-0.5119` n `139` status `ready` deltaP `0.601` edge `-0.0048` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.617` n `139` status `ready` deltaP `2.0793` edge `0.0106` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.9903` n `139` status `ready` deltaP `-6.08` edge `-0.0014` maxDD `-2.4692`
- `market_context_high->fx_24h` score `-0.9941` n `123` status `ready` deltaP `0.4361` edge `0.0088` maxDD `-2.1321`
- `market_context_high->commodity_1h` score `-1.1351` n `139` status `ready` deltaP `-8.6891` edge `-0.0026` maxDD `-1.1328`
- `news_risk_high->index_1h` score `-1.5515` n `31` status `ready` deltaP `-13.9173` edge `-0.0012` maxDD `-0.1583`
- `market_context_high->crypto_alt_4h` score `-1.5547` n `139` status `ready` deltaP `6.5034` edge `-0.0261` maxDD `-7.0785`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
