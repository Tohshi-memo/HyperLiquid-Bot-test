# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T12:52:21.652230+00:00`
- Price records: `672`
- Market context records: `2562`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9198`

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

- `market_context_high->crypto_alt_4h` score `5.759` n `148` status `ready` deltaP `25.1277` edge `0.5803` maxDD `-15.4319`
- `market_context_high->crypto_major_24h` score `5.0031` n `117` status `ready` deltaP `12.7137` edge `0.5975` maxDD `-15.2264`
- `market_context_high->unknown_24h` score `4.942` n `117` status `ready` deltaP `19.0438` edge `0.3177` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `3.9166` n `148` status `ready` deltaP `17.2173` edge `0.3926` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.5823` n `148` status `ready` deltaP `9.7849` edge `0.1716` maxDD `-3.7312`
- `market_context_high->equity_24h` score `1.373` n `117` status `ready` deltaP `19.765` edge `0.041` maxDD `-2.0014`
- `market_context_high->crypto_alt_1h` score `1.329` n `148` status `ready` deltaP `10.738` edge `0.1579` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.7437` n `148` status `ready` deltaP `8.6381` edge `0.1238` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.6443` n `117` status `ready` deltaP `6.25` edge `0.1101` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.2319` n `117` status `ready` deltaP `-0.5609` edge `0.6713` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.0932` n `148` status `ready` deltaP `7.5024` edge `0.0419` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1439` n `148` status `ready` deltaP `3.9165` edge `0.0113` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.4493` n `148` status `ready` deltaP `0.971` edge `0.0107` maxDD `-2.9823`
- `market_context_high->commodity_1h` score `-0.4569` n `148` status `ready` deltaP `4.7338` edge `0.0182` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.4698` n `148` status `ready` deltaP `1.5092` edge `0.0198` maxDD `-2.8543`
- `market_context_high->fx_1h` score `-0.5685` n `148` status `ready` deltaP `0.2994` edge `0.0041` maxDD `-0.278`
- `market_context_high->fx_24h` score `-0.7098` n `117` status `ready` deltaP `1.1485` edge `0.0038` maxDD `-1.8634`
- `market_context_high->equity_1h` score `-0.7257` n `148` status `ready` deltaP `0.3278` edge `0.0212` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8596` n `148` status `ready` deltaP `0.2596` edge `0.0126` maxDD `-0.8774`
- `market_context_high->metal_4h` score `-0.911` n `148` status `ready` deltaP `3.3949` edge `0.0402` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
