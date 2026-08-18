# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T18:16:06.288442+00:00`
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

- `market_context_high->crypto_major_24h` score `2.6649` n `91` status `ready` deltaP `10.0294` edge `0.276` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.6854` n `91` status `ready` deltaP `19.2899` edge `0.2708` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.1992` n `96` status `ready` deltaP `9.9115` edge `0.064` maxDD `-0.4112`
- `market_context_high->metal_4h` score `0.7751` n `96` status `ready` deltaP `14.126` edge `0.028` maxDD `-1.273`
- `market_context_high->equity_4h` score `0.6951` n `96` status `ready` deltaP `4.751` edge `0.1151` maxDD `-2.4411`
- `market_context_high->index_1h` score `0.6456` n `96` status `ready` deltaP `12.6185` edge `0.0084` maxDD `-0.0982`
- `market_context_high->crypto_major_4h` score `0.4742` n `96` status `ready` deltaP `7.9522` edge `0.0886` maxDD `-3.1677`
- `market_context_high->unknown_1h` score `0.4531` n `96` status `ready` deltaP `9.3563` edge `-0.0019` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `-0.0072` n `96` status `ready` deltaP `8.3841` edge `0.0705` maxDD `-5.4926`
- `market_context_high->metal_1h` score `-0.0309` n `96` status `ready` deltaP `4.0232` edge `0.0093` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.1324` n `91` status `ready` deltaP `13.0876` edge `-0.0769` maxDD `-0.3771`
- `market_context_high->fx_4h` score `-0.202` n `96` status `ready` deltaP `3.6839` edge `-0.0002` maxDD `-0.3539`
- `market_context_high->commodity_4h` score `-0.4137` n `96` status `ready` deltaP `3.3283` edge `0.0098` maxDD `-2.4692`
- `market_context_high->fx_1h` score `-0.4475` n `96` status `ready` deltaP `-3.4182` edge `0.0013` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.4735` n `96` status `ready` deltaP `1.4783` edge `0.0096` maxDD `-2.413`
- `market_context_high->index_4h` score `-0.5219` n `96` status `ready` deltaP `1.2449` edge `0.0137` maxDD `-0.5728`
- `market_context_high->crypto_major_1h` score `-0.5535` n `96` status `ready` deltaP `0.5863` edge `0.0096` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8557` n `96` status `ready` deltaP `-7.142` edge `-0.0055` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.2502` n `91` status `ready` deltaP `-6.4541` edge `0.0316` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.4121` n `91` status `ready` deltaP `-28.4284` edge `-0.0282` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
