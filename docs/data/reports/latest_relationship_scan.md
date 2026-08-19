# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T10:43:06.992752+00:00`
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

- `market_context_high->crypto_major_24h` score `2.1169` n `96` status `ready` deltaP `6.9444` edge `0.2509` maxDD `-4.9964`
- `market_context_high->equity_4h` score `1.7665` n `96` status `ready` deltaP `10.2388` edge `0.1678` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.7097` n `96` status `ready` deltaP `14.4025` edge `0.0766` maxDD `-0.4112`
- `market_context_high->metal_4h` score `1.3406` n `96` status `ready` deltaP `19.004` edge `0.0426` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `1.0835` n `96` status `ready` deltaP `11.4583` edge `0.116` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.9414` n `96` status `ready` deltaP `16.0616` edge `0.0101` maxDD `-0.0982`
- `market_context_high->commodity_24h` score `0.9266` n `96` status `ready` deltaP `12.1528` edge `0.2211` maxDD `-4.666`
- `market_context_high->unknown_1h` score `0.2324` n `96` status `ready` deltaP `8.4581` edge `-0.0143` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.1914` n `96` status `ready` deltaP `9.7561` edge `0.0779` maxDD `-5.4926`
- `market_context_high->metal_1h` score `0.1859` n `96` status `ready` deltaP `6.2687` edge `0.0124` maxDD `-0.4291`
- `market_context_high->fx_4h` score `0.0961` n `96` status `ready` deltaP `8.562` edge `0.0055` maxDD `-0.3539`
- `market_context_high->index_4h` score `0.0851` n `96` status `ready` deltaP `7.6473` edge `0.0216` maxDD `-0.5728`
- `market_context_high->unknown_24h` score `0.085` n `96` status `ready` deltaP `16.6666` edge `-0.0534` maxDD `-1.0505`
- `market_context_high->fx_1h` score `-0.3261` n `96` status `ready` deltaP `-1.3224` edge `0.0029` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.3386` n `96` status `ready` deltaP `3.4306` edge `0.0182` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.4377` n `96` status `ready` deltaP `1.7777` edge `0.0122` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.5489` n `96` status `ready` deltaP `1.1941` edge `0.0067` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.9024` n `96` status `ready` deltaP `-7.8905` edge `-0.0065` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.209` n `96` status `ready` deltaP `-3.6458` edge `0.0719` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-4.0459` n `96` status `ready` deltaP `-23.4375` edge `-0.0226` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
