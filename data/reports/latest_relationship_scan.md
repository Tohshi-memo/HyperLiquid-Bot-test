# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T09:07:35.159927+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13758`

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

- `market_context_high->index_1h` score `0.3466` n `105` status `ready` deltaP `10.7072` edge `0.0062` maxDD `-0.5622`
- `market_context_high->equity_1h` score `0.3053` n `105` status `ready` deltaP `8.4203` edge `0.0508` maxDD `-3.1861`
- `market_context_high->equity_4h` score `0.0931` n `105` status `ready` deltaP `4.7402` edge `0.1391` maxDD `-8.3685`
- `market_context_high->fx_4h` score `0.0803` n `105` status `ready` deltaP `7.9428` edge `0.0076` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.206` n `105` status `ready` deltaP `0.7756` edge `0.0043` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2531` n `105` status `ready` deltaP `6.5302` edge `-0.0184` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.3012` n `105` status `ready` deltaP `5.4283` edge `0.0176` maxDD `-1.7252`
- `market_context_high->metal_1h` score `-0.3252` n `105` status `ready` deltaP `2.1899` edge `-0.003` maxDD `-0.4291`
- `market_context_high->commodity_24h` score `-0.3304` n `103` status `ready` deltaP `5.2488` edge `0.1208` maxDD `-4.666`
- `market_context_high->unknown_1h` score `-0.4949` n `105` status `ready` deltaP `7.0317` edge `-0.0654` maxDD `-0.4843`
- `market_context_high->commodity_4h` score `-0.7293` n `105` status `ready` deltaP `-2.5` edge `0.0082` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7642` n `105` status `ready` deltaP `-6.0279` edge `-0.0012` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.946` n `105` status `ready` deltaP `-2.3424` edge `-0.0255` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.0638` n `105` status `ready` deltaP `-1.4571` edge `-0.0422` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-3.151` n `105` status `ready` deltaP `-0.7491` edge `-0.1306` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-3.2738` n `103` status `ready` deltaP `-15.1379` edge `-0.0128` maxDD `-2.0613`
- `market_context_high->crypto_major_4h` score `-3.449` n `105` status `ready` deltaP `1.3473` edge `-0.1943` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.0151` n `103` status `ready` deltaP `-3.0188` edge `-0.0444` maxDD `-18.6848`
- `market_context_high->unknown_24h` score `-4.3638` n `103` status `ready` deltaP `11.0673` edge `-0.3868` maxDD `-1.0505`
- `market_context_high->metal_24h` score `-4.4615` n `103` status `ready` deltaP `-17.6088` edge `-0.1238` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
