# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T14:07:19.975628+00:00`
- Price records: `672`
- Market context records: `1945`
- Flow alert records: `7494`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7547`

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

- `market_context_high->crypto_alt_4h` score `7.1011` n `230` status `ready` deltaP `22.0692` edge `0.5591` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.4965` n `230` status `ready` deltaP `25.647` edge `0.495` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.5405` n `230` status `ready` deltaP `14.1605` edge `0.3197` maxDD `-9.8581`
- `market_context_high->equity_4h` score `1.9498` n `230` status `ready` deltaP `13.6695` edge `0.1808` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `0.7715` n `199` status `ready` deltaP `15.0504` edge `0.496` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.6699` n `233` status `ready` deltaP `7.5808` edge `0.1039` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.5065` n `233` status `ready` deltaP `6.8824` edge `0.1077` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.2162` n `199` status `ready` deltaP `11.9871` edge `0.1807` maxDD `-12.7414`
- `market_context_high->index_24h` score `0.1417` n `199` status `ready` deltaP `4.1922` edge `0.1067` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.1213` n `230` status `ready` deltaP `8.3866` edge `0.0631` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.2171` n `233` status `ready` deltaP `4.4975` edge `0.0313` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2723` n `199` status `ready` deltaP `9.9323` edge `0.016` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6149` n `233` status `ready` deltaP `0.6046` edge `0.0079` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6385` n `233` status `ready` deltaP `-2.8096` edge `0.0001` maxDD `-0.3914`
- `market_context_high->equity_24h` score `-0.6849` n `199` status `ready` deltaP `9.2957` edge `0.3708` maxDD `-33.1875`
- `market_context_high->fx_4h` score `-1.0171` n `230` status `ready` deltaP `-5.922` edge `-0.0021` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.1411` n `233` status `ready` deltaP `3.7779` edge `0.0133` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.4903` n `233` status `ready` deltaP `0.4645` edge `-0.0321` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-1.6964` n `230` status `ready` deltaP `7.0076` edge `0.0811` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.9865` n `233` status `ready` deltaP `0.9033` edge `-0.0049` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
