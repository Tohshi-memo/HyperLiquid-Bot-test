# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T08:22:24.747399+00:00`
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

- `market_context_high->equity_1h` score `0.3209` n `105` status `ready` deltaP `8.57` edge `0.0511` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3083` n `105` status `ready` deltaP `10.2581` edge `0.006` maxDD `-0.5622`
- `market_context_high->equity_4h` score `0.1135` n `105` status `ready` deltaP `4.7402` edge `0.1408` maxDD `-8.3685`
- `market_context_high->fx_4h` score `0.0557` n `105` status `ready` deltaP `7.4854` edge `0.0075` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.2146` n `105` status `ready` deltaP `0.6259` edge `0.0042` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2476` n `105` status `ready` deltaP `6.5302` edge `-0.0177` maxDD `-1.273`
- `market_context_high->commodity_24h` score `-0.2707` n `103` status `ready` deltaP `5.7696` edge `0.1223` maxDD `-4.666`
- `market_context_high->index_4h` score `-0.3004` n `105` status `ready` deltaP `5.4283` edge `0.0177` maxDD `-1.7252`
- `market_context_high->metal_1h` score `-0.318` n `105` status `ready` deltaP `2.1899` edge `-0.0024` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.4553` n `105` status `ready` deltaP `7.1814` edge `-0.0631` maxDD `-0.4843`
- `market_context_high->commodity_4h` score `-0.6985` n `105` status `ready` deltaP `-2.0427` edge `0.0091` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7635` n `105` status `ready` deltaP `-6.0279` edge `-0.0011` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.9117` n `105` status `ready` deltaP `-2.3424` edge `-0.0211` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.0054` n `105` status `ready` deltaP `-1.3074` edge `-0.0357` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-2.9404` n `105` status `ready` deltaP `-0.2918` edge `-0.1161` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-3.2528` n `105` status `ready` deltaP `1.8046` edge `-0.181` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.3323` n `103` status `ready` deltaP `-15.6588` edge `-0.0142` maxDD `-2.0613`
- `market_context_high->index_24h` score `-3.9817` n `103` status `ready` deltaP `-2.498` edge `-0.0436` maxDD `-18.6848`
- `market_context_high->unknown_24h` score `-4.1776` n `103` status `ready` deltaP `11.4145` edge `-0.3736` maxDD `-1.0505`
- `market_context_high->metal_24h` score `-4.4334` n `103` status `ready` deltaP `-17.6088` edge `-0.1202` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
