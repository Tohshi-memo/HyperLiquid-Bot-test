# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T07:37:29.974104+00:00`
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

- `market_context_high->crypto_major_24h` score `2.2217` n `96` status `ready` deltaP `7.6389` edge `0.255` maxDD `-4.9964`
- `market_context_high->equity_4h` score `1.8277` n `96` status `ready` deltaP `10.2388` edge `0.1729` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.6306` n `96` status `ready` deltaP `13.8037` edge `0.074` maxDD `-0.4112`
- `market_context_high->metal_4h` score `1.3614` n `96` status `ready` deltaP `19.3089` edge `0.0423` maxDD `-1.273`
- `market_context_high->commodity_24h` score `1.1418` n `96` status `ready` deltaP `14.2361` edge `0.2348` maxDD `-4.666`
- `market_context_high->crypto_major_4h` score `1.0889` n `96` status `ready` deltaP `11.9156` edge `0.1134` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.8899` n `96` status `ready` deltaP `15.4628` edge `0.0098` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.2492` n `96` status `ready` deltaP `8.6078` edge `-0.0139` maxDD `-0.4843`
- `market_context_high->metal_1h` score `0.1799` n `96` status `ready` deltaP `6.2687` edge `0.0119` maxDD `-0.4291`
- `market_context_high->crypto_alt_4h` score `0.1734` n `96` status `ready` deltaP `9.7561` edge `0.0764` maxDD `-5.4926`
- `market_context_high->index_4h` score `0.1055` n `96` status `ready` deltaP `7.6473` edge `0.0233` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.0589` n `96` status `ready` deltaP `7.9522` edge `0.0048` maxDD `-0.3539`
- `market_context_high->unknown_24h` score `-0.1914` n `96` status `ready` deltaP `14.7569` edge `-0.0637` maxDD `-1.0505`
- `market_context_high->fx_1h` score `-0.3284` n `96` status `ready` deltaP `-1.3224` edge `0.0026` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.3892` n `96` status `ready` deltaP `2.8318` edge `0.0157` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.4268` n `96` status `ready` deltaP `2.0771` edge `0.0116` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.5347` n `96` status `ready` deltaP `1.3466` edge `0.0075` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8791` n `96` status `ready` deltaP `-7.5911` edge `-0.0055` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.1957` n `96` status `ready` deltaP `-3.6458` edge `0.0736` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-4.24` n `96` status `ready` deltaP `-25.1736` edge `-0.0272` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
