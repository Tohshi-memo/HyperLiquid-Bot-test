# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T07:01:52.861857+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11762`

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

- `market_context_high->crypto_major_24h` score `2.1735` n `96` status `ready` deltaP `7.2916` edge `0.2533` maxDD `-4.9964`
- `market_context_high->equity_4h` score `1.8229` n `96` status `ready` deltaP `10.2388` edge `0.1725` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.6606` n `96` status `ready` deltaP `13.8037` edge `0.0765` maxDD `-0.4112`
- `market_context_high->metal_4h` score `1.3298` n `96` status `ready` deltaP `19.004` edge `0.0417` maxDD `-1.273`
- `market_context_high->commodity_24h` score `1.1715` n `96` status `ready` deltaP `14.5833` edge `0.2363` maxDD `-4.666`
- `market_context_high->crypto_major_4h` score `1.0709` n `96` status `ready` deltaP `11.9156` edge `0.1119` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.9067` n `96` status `ready` deltaP `15.6125` edge `0.0102` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.2624` n `96` status `ready` deltaP `8.7575` edge `-0.0138` maxDD `-0.4843`
- `market_context_high->metal_1h` score `0.1799` n `96` status `ready` deltaP `6.2687` edge `0.0119` maxDD `-0.4291`
- `market_context_high->crypto_alt_4h` score `0.1734` n `96` status `ready` deltaP `9.7561` edge `0.0764` maxDD `-5.4926`
- `market_context_high->index_4h` score `0.1055` n `96` status `ready` deltaP `7.6473` edge `0.0233` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.0677` n `96` status `ready` deltaP `8.1046` edge `0.0049` maxDD `-0.3539`
- `market_context_high->unknown_24h` score `-0.2336` n `96` status `ready` deltaP `14.4097` edge `-0.0649` maxDD `-1.0505`
- `market_context_high->fx_1h` score `-0.3206` n `96` status `ready` deltaP `-1.1727` edge `0.0026` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.3884` n `96` status `ready` deltaP `2.8318` edge `0.0158` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.4073` n `96` status `ready` deltaP `2.3765` edge `0.0121` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.5347` n `96` status `ready` deltaP `1.3466` edge `0.0075` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8814` n `96` status `ready` deltaP `-7.5911` edge `-0.0058` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.2019` n `96` status `ready` deltaP `-3.6458` edge `0.0728` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-4.2611` n `96` status `ready` deltaP `-25.3472` edge `-0.0278` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
