# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T02:52:24.282642+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13819`

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

- `market_context_high->equity_1h` score `0.3365` n `105` status `ready` deltaP `8.7197` edge `0.0514` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3323` n `105` status `ready` deltaP `10.5575` edge `0.006` maxDD `-0.5622`
- `market_context_high->equity_4h` score `0.1823` n `105` status `ready` deltaP `5.045` edge `0.1445` maxDD `-8.3685`
- `market_context_high->fx_4h` score `0.0162` n `105` status `ready` deltaP `6.8757` edge `0.0065` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.148` n `96` status `ready` deltaP `4.6875` edge `0.1331` maxDD `-4.666`
- `market_context_high->fx_1h` score `-0.2068` n `105` status `ready` deltaP `0.7756` edge `0.0042` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2398` n `105` status `ready` deltaP `6.5302` edge `-0.0167` maxDD `-1.273`
- `market_context_high->unknown_1h` score `-0.2527` n `105` status `ready` deltaP `8.5287` edge `-0.0552` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.2772` n `105` status `ready` deltaP `2.639` edge `-0.002` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.2878` n `105` status `ready` deltaP `5.5807` edge `0.0183` maxDD `-1.7252`
- `market_context_high->crypto_alt_1h` score `-0.6366` n `105` status `ready` deltaP `0.2025` edge `-0.0028` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.7307` n `105` status `ready` deltaP `-2.3476` edge `0.007` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.8113` n `105` status `ready` deltaP `0.6387` edge `-0.0238` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8211` n `105` status `ready` deltaP `-6.9261` edge `-0.0025` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-2.0279` n `105` status `ready` deltaP `2.9094` edge `-0.0614` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.4363` n `105` status `ready` deltaP `5.0058` edge `-0.1343` maxDD `-3.1677`
- `market_context_high->index_24h` score `-3.5952` n `96` status `ready` deltaP `1.0416` edge `-0.0511` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.7712` n `96` status `ready` deltaP `-20.1389` edge `-0.0217` maxDD `-1.9981`
- `market_context_high->unknown_24h` score `-4.7225` n `96` status `ready` deltaP `12.6736` edge `-0.4274` maxDD `-1.0505`
- `market_context_high->metal_24h` score `-4.9424` n `96` status `ready` deltaP `-21.0069` edge `-0.1628` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
