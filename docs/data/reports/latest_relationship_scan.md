# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T23:22:24.139715+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10828`

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

- `market_context_high->equity_4h` score `2.1799` n `96` status `ready` deltaP `11.6107` edge `0.1931` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.7265` n `96` status `ready` deltaP `14.2528` edge `0.079` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9198` n `96` status `ready` deltaP `15.7622` edge `0.0103` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.4386` n `96` status `ready` deltaP `12.754` edge `0.0091` maxDD `-1.273`
- `market_context_high->index_4h` score `0.287` n `96` status `ready` deltaP `9.7815` edge `0.0242` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.1942` n `96` status `ready` deltaP `6.4236` edge `0.1654` maxDD `-4.666`
- `market_context_high->fx_4h` score `0.0344` n `96` status `ready` deltaP `7.4949` edge `0.0047` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.1412` n `96` status `ready` deltaP `3.4244` edge `0.0041` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.1665` n `96` status `ready` deltaP `17.7083` edge `-0.0813` maxDD `-1.0505`
- `market_context_high->unknown_1h` score `-0.2171` n `96` status `ready` deltaP `5.6138` edge `-0.0328` maxDD `-0.4843`
- `market_context_high->fx_1h` score `-0.3206` n `96` status `ready` deltaP `-1.1727` edge `0.0026` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.6781` n `96` status `ready` deltaP `-1.2449` edge `0.0064` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8329` n `96` status `ready` deltaP `-0.1684` edge `-0.0255` maxDD `-2.413`
- `market_context_high->commodity_1h` score `-0.8954` n `96` status `ready` deltaP `-7.8905` edge `-0.0056` maxDD `-1.1941`
- `market_context_high->crypto_major_1h` score `-0.9631` n `96` status `ready` deltaP `0.8857` edge `-0.0449` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-2.049` n `96` status `ready` deltaP `3.2012` edge `-0.0651` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.2795` n `96` status `ready` deltaP `5.3607` edge `-0.1236` maxDD `-3.1677`
- `market_context_high->crypto_major_24h` score `-3.2293` n `96` status `ready` deltaP `2.9514` edge `-0.168` maxDD `-4.9964`
- `market_context_high->fx_24h` score `-3.2473` n `96` status `ready` deltaP `-16.3194` edge `-0.0035` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-3.3806` n `96` status `ready` deltaP `-10.9375` edge `-0.0297` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
