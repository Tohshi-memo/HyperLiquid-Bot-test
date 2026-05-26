# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T07:07:16.013213+00:00`
- Price records: `672`
- Market context records: `1923`
- Flow alert records: `7434`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6020`

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

- `market_context_high->crypto_alt_4h` score `7.6539` n `202` status `ready` deltaP `23.7594` edge `0.5939` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.169` n `202` status `ready` deltaP `29.0133` edge `0.5286` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.8147` n `202` status `ready` deltaP `17.2482` edge `0.4053` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.58` n `202` status `ready` deltaP `15.8326` edge `0.2189` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `0.827` n `214` status `ready` deltaP `8.9149` edge `0.1081` maxDD `-3.2225`
- `market_context_high->unknown_24h` score `0.7167` n `195` status `ready` deltaP `13.75` edge `0.5001` maxDD `-35.8966`
- `market_context_high->crypto_alt_1h` score `0.6542` n `214` status `ready` deltaP `8.0531` edge `0.1122` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.5138` n `195` status `ready` deltaP `12.6629` edge `0.201` maxDD `-12.7414`
- `market_context_high->index_4h` score `0.4711` n `202` status `ready` deltaP `10.3885` edge `0.0789` maxDD `-3.7119`
- `market_context_high->index_24h` score `0.2997` n `195` status `ready` deltaP `4.6367` edge `0.1169` maxDD `-4.1604`
- `market_context_high->equity_1h` score `-0.0769` n `214` status `ready` deltaP `5.3361` edge `0.0374` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.1941` n `195` status `ready` deltaP `10.5796` edge `0.0182` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.5899` n `214` status `ready` deltaP `0.7219` edge `0.0092` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.6113` n `214` status `ready` deltaP `5.476` edge `0.0187` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6932` n `214` status `ready` deltaP `-3.9062` edge `0.0004` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-0.789` n `202` status `ready` deltaP `11.045` edge `0.1298` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-0.8331` n `202` status `ready` deltaP `-2.7439` edge `0.0003` maxDD `-1.1056`
- `market_context_high->unknown_1h` score `-1.2069` n `214` status `ready` deltaP `1.6971` edge `-0.0167` maxDD `-3.6151`
- `market_context_high->equity_24h` score `-1.3263` n `195` status `ready` deltaP `6.4984` edge `0.336` maxDD `-33.1875`
- `market_context_high->commodity_1h` score `-2.0621` n `214` status `ready` deltaP `0.7849` edge `-0.0138` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
