# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T12:37:30.531148+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11633`

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

- `market_context_high->crypto_major_24h` score `2.3041` n `86` status `ready` deltaP `8.6394` edge `0.2552` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.5994` n `86` status `ready` deltaP `17.456` edge `0.272` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.0341` n `96` status `ready` deltaP `9.3127` edge `0.0545` maxDD `-0.4329`
- `market_context_high->metal_4h` score `0.7505` n `96` status `ready` deltaP `14.5833` edge `0.0229` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6599` n `96` status `ready` deltaP `12.9179` edge `0.0076` maxDD `-0.0982`
- `market_context_high->crypto_major_4h` score `0.6208` n `96` status `ready` deltaP `9.0193` edge `0.0937` maxDD `-3.1677`
- `market_context_high->unknown_1h` score `0.5292` n `96` status `ready` deltaP `9.2066` edge `0.0054` maxDD `-0.4807`
- `market_context_high->crypto_alt_4h` score `0.3924` n `96` status `ready` deltaP `10.2134` edge `0.0916` maxDD `-5.4926`
- `market_context_high->equity_4h` score `0.0479` n `96` status `ready` deltaP `2.6168` edge `0.077` maxDD `-2.5696`
- `market_context_high->metal_1h` score `-0.0717` n `96` status `ready` deltaP `3.7238` edge `0.0079` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.1989` n `96` status `ready` deltaP `3.6839` edge `0.0002` maxDD `-0.3539`
- `market_context_high->unknown_24h` score `-0.2249` n `86` status `ready` deltaP `12.3171` edge `-0.0825` maxDD `-0.1352`
- `market_context_high->commodity_4h` score `-0.3702` n `96` status `ready` deltaP `4.0905` edge `0.0103` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.3784` n `96` status `ready` deltaP `2.0771` edge `0.0178` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.4467` n `96` status `ready` deltaP `-3.4182` edge `0.0014` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.4787` n `96` status `ready` deltaP `1.3348` edge `0.0142` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.5933` n `96` status `ready` deltaP `0.7876` edge `0.0108` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.8635` n `96` status `ready` deltaP `-7.2917` edge `-0.0055` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.0702` n `86` status `ready` deltaP `-7.2709` edge `0.0191` maxDD `-7.2168`
- `market_context_high->fx_24h` score `-4.6068` n `86` status `ready` deltaP `-30.9177` edge `-0.0301` maxDD `-1.1479`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
