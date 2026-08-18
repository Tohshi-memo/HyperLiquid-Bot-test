# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T19:08:18.798292+00:00`
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

- `market_context_high->crypto_major_24h` score `2.7009` n `91` status `ready` deltaP `10.0294` edge `0.279` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.6745` n `91` status `ready` deltaP `19.2899` edge `0.2694` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.2184` n `96` status `ready` deltaP `10.0612` edge `0.0646` maxDD `-0.4112`
- `market_context_high->metal_4h` score `0.8261` n `96` status `ready` deltaP `14.5833` edge `0.0292` maxDD `-1.273`
- `market_context_high->equity_4h` score `0.7965` n `96` status `ready` deltaP `5.2083` edge `0.1205` maxDD `-2.4411`
- `market_context_high->index_1h` score `0.6575` n `96` status `ready` deltaP `12.7682` edge `0.0084` maxDD `-0.0982`
- `market_context_high->crypto_major_4h` score `0.5356` n `96` status `ready` deltaP `8.1046` edge `0.0927` maxDD `-3.1677`
- `market_context_high->unknown_1h` score `0.4423` n `96` status `ready` deltaP `9.2066` edge `-0.0018` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.0362` n `96` status `ready` deltaP `8.5366` edge `0.0731` maxDD `-5.4926`
- `market_context_high->metal_1h` score `-0.0058` n `96` status `ready` deltaP `4.3226` edge `0.0094` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.0655` n `91` status `ready` deltaP `13.6085` edge `-0.0748` maxDD `-0.3771`
- `market_context_high->fx_4h` score `-0.1861` n `96` status `ready` deltaP `3.9888` edge `-0.0002` maxDD `-0.3539`
- `market_context_high->commodity_4h` score `-0.4271` n `96` status `ready` deltaP `3.1758` edge `0.0091` maxDD `-2.4692`
- `market_context_high->fx_1h` score `-0.4475` n `96` status `ready` deltaP `-3.4182` edge `0.0013` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.4727` n `96` status `ready` deltaP `1.4783` edge `0.0097` maxDD `-2.413`
- `market_context_high->index_4h` score `-0.4781` n `96` status `ready` deltaP `1.7022` edge `0.0143` maxDD `-0.5728`
- `market_context_high->crypto_major_1h` score `-0.5769` n `96` status `ready` deltaP `0.2869` edge `0.0086` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8635` n `96` status `ready` deltaP `-7.2917` edge `-0.0055` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.1872` n `91` status `ready` deltaP `-5.9333` edge `0.0362` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.3656` n `91` status `ready` deltaP `-27.9075` edge `-0.0278` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
