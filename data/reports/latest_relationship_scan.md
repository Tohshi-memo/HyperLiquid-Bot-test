# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T05:37:27.932025+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9688`

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

- `market_context_high->unknown_4h` score `74.0555` n `145` status `ready` deltaP `3.3674` edge `6.1824` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `17.2271` n `145` status `ready` deltaP `0.8724` edge `1.4787` maxDD `-1.5807`
- `market_context_high->index_24h` score `0.5196` n `121` status `ready` deltaP `21.3473` edge `0.0251` maxDD `-2.7307`
- `market_context_high->fx_4h` score `0.4671` n `145` status `ready` deltaP `13.361` edge `0.0097` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.4312` n `145` status `ready` deltaP `10.2674` edge `0.0033` maxDD `-0.1986`
- `market_context_high->metal_24h` score `0.1485` n `121` status `ready` deltaP `21.5234` edge `0.1281` maxDD `-6.204`
- `market_context_high->metal_1h` score `0.0479` n `145` status `ready` deltaP `10.5616` edge `0.0104` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `0.0353` n `145` status `ready` deltaP `5.1456` edge `0.0187` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.2205` n `121` status `ready` deltaP `15.6695` edge `0.0245` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.4528` n `145` status `ready` deltaP `6.414` edge `0.0424` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.6044` n `145` status `ready` deltaP `5.2581` edge `0.0273` maxDD `-7.8544`
- `market_context_high->index_1h` score `-0.6414` n `145` status `ready` deltaP `-0.9168` edge `-0.0024` maxDD `-1.8971`
- `market_context_high->metal_4h` score `-0.7541` n `145` status `ready` deltaP `9.9485` edge `0.0012` maxDD `-4.8031`
- `market_context_high->equity_1h` score `-1.6829` n `145` status `ready` deltaP `2.0772` edge `-0.002` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.9055` n `145` status `ready` deltaP `-0.3552` edge `0.0025` maxDD `-12.8878`
- `market_context_high->equity_24h` score `-3.128` n `121` status `ready` deltaP `-0.5672` edge `-0.0558` maxDD `-19.3152`
- `market_context_high->index_4h` score `-3.3986` n `145` status `ready` deltaP `-6.1817` edge `-0.0268` maxDD `-6.5496`
- `market_context_high->crypto_major_24h` score `-3.9329` n `121` status `ready` deltaP `1.8592` edge `-0.0309` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.0759` n `145` status `ready` deltaP `0.8747` edge `-0.071` maxDD `-29.2576`
- `market_context_high->equity_4h` score `-6.2348` n `145` status `ready` deltaP `0.5477` edge `-0.1519` maxDD `-42.0866`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
