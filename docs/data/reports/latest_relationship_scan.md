# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T17:52:36.127132+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10041`

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

- `market_context_high->unknown_1h` score `86.9179` n `47` status `ready` deltaP `10.116` edge `7.1828` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `44.0297` n `47` status `ready` deltaP `30.4226` edge `3.5056` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.446` n `47` status `ready` deltaP `24.782` edge `2.3266` maxDD `-2.7051`
- `market_context_high->equity_24h` score `24.5523` n `47` status `ready` deltaP `29.7281` edge `1.8834` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8274` n `47` status `ready` deltaP `34.7628` edge `0.4335` maxDD `-0.3705`
- `news_risk_high->crypto_major_24h` score `5.0525` n `91` status `ready` deltaP `0.5419` edge `1.5484` maxDD `-63.6743`
- `market_context_high->metal_24h` score `3.7791` n `47` status `ready` deltaP `32.4542` edge `0.1224` maxDD `-0.2401`
- `news_risk_high->crypto_alt_1h` score `3.0577` n `115` status `ready` deltaP `14.931` edge `0.2043` maxDD `-1.5895`
- `market_context_high->index_4h` score `3.0336` n `47` status `ready` deltaP `34.6361` edge `0.0373` maxDD `-0.2323`
- `news_risk_high->crypto_alt_24h` score `2.951` n `91` status `ready` deltaP `-1.6617` edge `1.0907` maxDD `-49.7699`
- `news_risk_high->crypto_major_1h` score `2.6688` n `115` status `ready` deltaP `17.8964` edge `0.1466` maxDD `-1.8141`
- `market_context_high->equity_4h` score `2.5289` n `47` status `ready` deltaP `17.6018` edge `0.1352` maxDD `-1.3444`
- `news_risk_high->crypto_major_4h` score `2.3889` n `112` status `ready` deltaP `16.79` edge `0.3003` maxDD `-13.719`
- `news_risk_high->crypto_alt_4h` score `2.2174` n `112` status `ready` deltaP `8.5366` edge `0.373` maxDD `-15.9436`
- `news_risk_high->fx_4h` score `1.6317` n `112` status `ready` deltaP `23.8458` edge `0.0406` maxDD `-0.421`
- `news_risk_high->metal_24h` score `1.1424` n `91` status `ready` deltaP `25.0191` edge `0.1245` maxDD `-7.2536`
- `news_risk_high->fx_24h` score `1.0921` n `91` status `ready` deltaP `27.3943` edge `0.1205` maxDD `-1.7159`
- `market_context_high->index_1h` score `1.0098` n `47` status `ready` deltaP `15.2089` edge `0.0106` maxDD `-0.2275`
- `news_risk_high->commodity_24h` score `0.9791` n `91` status `ready` deltaP `15.5811` edge `0.0818` maxDD `-1.9933`
- `news_risk_high->metal_1h` score `0.9764` n `115` status `ready` deltaP `16.2015` edge `0.0227` maxDD `-0.6142`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
