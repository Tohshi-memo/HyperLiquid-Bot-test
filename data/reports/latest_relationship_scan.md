# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T08:52:26.683702+00:00`
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

- `market_context_high->index_1h` score `0.3335` n `105` status `ready` deltaP `10.5575` edge `0.0061` maxDD `-0.5622`
- `market_context_high->equity_1h` score `0.3185` n `105` status `ready` deltaP `8.57` edge `0.0509` maxDD `-3.1861`
- `market_context_high->equity_4h` score `0.0955` n `105` status `ready` deltaP `4.7402` edge `0.1393` maxDD `-8.3685`
- `market_context_high->fx_4h` score `0.0716` n `105` status `ready` deltaP `7.7903` edge `0.0075` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.2146` n `105` status `ready` deltaP `0.6259` edge `0.0042` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2507` n `105` status `ready` deltaP `6.5302` edge `-0.0181` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.3012` n `105` status `ready` deltaP `5.4283` edge `0.0176` maxDD `-1.7252`
- `market_context_high->commodity_24h` score `-0.3129` n `103` status `ready` deltaP `5.4224` edge `0.1211` maxDD `-4.666`
- `market_context_high->metal_1h` score `-0.3228` n `105` status `ready` deltaP `2.1899` edge `-0.0028` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.4637` n `105` status `ready` deltaP `7.1814` edge `-0.0638` maxDD `-0.4843`
- `market_context_high->commodity_4h` score `-0.719` n `105` status `ready` deltaP `-2.3476` edge `0.0085` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.765` n `105` status `ready` deltaP `-6.0279` edge `-0.0013` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.9444` n `105` status `ready` deltaP `-2.3424` edge `-0.0253` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.0506` n `105` status `ready` deltaP `-1.3074` edge `-0.0415` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-3.0932` n `105` status `ready` deltaP `-0.5967` edge `-0.1268` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-3.2937` n `103` status `ready` deltaP `-15.3115` edge `-0.0133` maxDD `-2.0613`
- `market_context_high->crypto_major_4h` score `-3.3984` n `105` status `ready` deltaP `1.4997` edge `-0.1911` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.0037` n `103` status `ready` deltaP `-2.8452` edge `-0.0441` maxDD `-18.6848`
- `market_context_high->unknown_24h` score `-4.2767` n `103` status `ready` deltaP `11.2409` edge `-0.3807` maxDD `-1.0505`
- `market_context_high->metal_24h` score `-4.4513` n `103` status `ready` deltaP `-17.6088` edge `-0.1225` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
