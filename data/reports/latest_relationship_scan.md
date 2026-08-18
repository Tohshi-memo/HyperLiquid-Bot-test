# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T17:37:35.978505+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11624`

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

- `market_context_high->crypto_major_24h` score `2.6088` n `91` status `ready` deltaP `9.9587` edge `0.2718` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.6967` n `91` status `ready` deltaP `19.3727` edge `0.2717` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.1669` n `96` status `ready` deltaP `9.7618` edge `0.0623` maxDD `-0.4112`
- `market_context_high->metal_4h` score `0.7595` n `96` status `ready` deltaP `14.126` edge `0.0267` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6443` n `96` status `ready` deltaP `12.6185` edge `0.0083` maxDD `-0.0982`
- `market_context_high->equity_4h` score `0.5565` n `96` status `ready` deltaP `4.2937` edge `0.1066` maxDD `-2.4411`
- `market_context_high->crypto_major_4h` score `0.4442` n `96` status `ready` deltaP `7.9522` edge `0.0861` maxDD `-3.1677`
- `market_context_high->unknown_1h` score `0.4111` n `96` status `ready` deltaP `8.9072` edge `-0.0024` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `-0.0216` n `96` status `ready` deltaP `8.3841` edge `0.0693` maxDD `-5.4926`
- `market_context_high->metal_1h` score `-0.0321` n `96` status `ready` deltaP `4.0232` edge `0.0092` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.1796` n `91` status `ready` deltaP `12.6917` edge `-0.0782` maxDD `-0.3771`
- `market_context_high->fx_4h` score `-0.2099` n `96` status `ready` deltaP `3.5315` edge `-0.0002` maxDD `-0.3539`
- `market_context_high->commodity_4h` score `-0.3837` n `96` status `ready` deltaP `3.7856` edge `0.0106` maxDD `-2.4692`
- `market_context_high->fx_1h` score `-0.4553` n `96` status `ready` deltaP `-3.5679` edge `0.0013` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.4829` n `96` status `ready` deltaP `1.3286` edge `0.0094` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.5481` n `96` status `ready` deltaP `0.736` edge `0.0093` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.5693` n `96` status `ready` deltaP `0.7876` edge `0.0128` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.8386` n `96` status `ready` deltaP `-6.8426` edge `-0.0053` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.2984` n `91` status `ready` deltaP `-6.8714` edge `0.0282` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.4512` n `91` status `ready` deltaP `-28.8571` edge `-0.0286` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
