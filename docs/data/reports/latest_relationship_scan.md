# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T13:52:21.701501+00:00`
- Price records: `672`
- Market context records: `1944`
- Flow alert records: `7491`
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

- `market_context_high->crypto_alt_4h` score `7.0901` n `229` status `ready` deltaP `22.1267` edge `0.5578` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.4704` n `229` status `ready` deltaP `25.7254` edge `0.4923` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.5466` n `229` status `ready` deltaP `14.1763` edge `0.3201` maxDD `-9.8581`
- `market_context_high->equity_4h` score `1.9637` n `229` status `ready` deltaP `13.7233` edge `0.1816` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `0.7398` n `199` status `ready` deltaP `14.8792` edge `0.4945` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.6927` n `233` status `ready` deltaP `7.7305` edge `0.1048` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.5233` n `233` status `ready` deltaP `7.0321` edge `0.1081` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.2126` n `199` status `ready` deltaP `11.9871` edge `0.1804` maxDD `-12.7414`
- `market_context_high->index_24h` score `0.1453` n `199` status `ready` deltaP `4.1922` edge `0.107` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.1207` n `229` status `ready` deltaP `8.4081` edge `0.0629` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.204` n `233` status `ready` deltaP `4.6472` edge `0.0314` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2747` n `199` status `ready` deltaP `9.9323` edge `0.0158` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6077` n `233` status `ready` deltaP `0.6046` edge `0.0085` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6385` n `233` status `ready` deltaP `-2.8096` edge `0.0001` maxDD `-0.3914`
- `market_context_high->equity_24h` score `-0.7382` n `199` status `ready` deltaP `9.1244` edge `0.3675` maxDD `-33.1875`
- `market_context_high->fx_4h` score `-1.0048` n `229` status `ready` deltaP `-5.715` edge `-0.0019` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.1543` n `233` status `ready` deltaP `3.6282` edge `0.0132` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.4675` n `233` status `ready` deltaP `0.6142` edge `-0.0312` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-1.6819` n `229` status `ready` deltaP `6.9645` edge `0.0826` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.974` n `233` status `ready` deltaP `1.053` edge `-0.0043` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
