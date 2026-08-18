# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T18:37:34.137446+00:00`
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

- `market_context_high->crypto_major_24h` score `2.6769` n `91` status `ready` deltaP `10.0294` edge `0.277` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.6815` n `91` status `ready` deltaP `19.2899` edge `0.2703` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.1968` n `96` status `ready` deltaP `9.9115` edge `0.0638` maxDD `-0.4112`
- `market_context_high->metal_4h` score `0.7933` n `96` status `ready` deltaP `14.2784` edge `0.0285` maxDD `-1.273`
- `market_context_high->equity_4h` score `0.7337` n `96` status `ready` deltaP `4.9034` edge `0.1173` maxDD `-2.4411`
- `market_context_high->index_1h` score `0.6443` n `96` status `ready` deltaP `12.6185` edge `0.0083` maxDD `-0.0982`
- `market_context_high->crypto_major_4h` score `0.5032` n `96` status `ready` deltaP `8.1046` edge `0.09` maxDD `-3.1677`
- `market_context_high->unknown_1h` score `0.4543` n `96` status `ready` deltaP `9.3563` edge `-0.0018` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.0158` n `96` status `ready` deltaP `8.5366` edge `0.0714` maxDD `-5.4926`
- `market_context_high->metal_1h` score `-0.0189` n `96` status `ready` deltaP `4.1729` edge `0.0093` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.1077` n `91` status `ready` deltaP `13.2612` edge `-0.076` maxDD `-0.3771`
- `market_context_high->fx_4h` score `-0.202` n `96` status `ready` deltaP `3.6839` edge `-0.0002` maxDD `-0.3539`
- `market_context_high->commodity_4h` score `-0.4248` n `96` status `ready` deltaP `3.1758` edge `0.0094` maxDD `-2.4692`
- `market_context_high->fx_1h` score `-0.4475` n `96` status `ready` deltaP `-3.4182` edge `0.0013` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.4743` n `96` status `ready` deltaP `1.4783` edge `0.0095` maxDD `-2.413`
- `market_context_high->index_4h` score `-0.5073` n `96` status `ready` deltaP `1.3973` edge `0.0139` maxDD `-0.5728`
- `market_context_high->crypto_major_1h` score `-0.5668` n `96` status `ready` deltaP `0.4366` edge `0.0089` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8635` n `96` status `ready` deltaP `-7.2917` edge `-0.0055` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.2302` n `91` status `ready` deltaP `-6.2805` edge `0.033` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.397` n `91` status `ready` deltaP `-28.2548` edge `-0.0281` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
