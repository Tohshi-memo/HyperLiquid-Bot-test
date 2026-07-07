# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T02:22:25.481921+00:00`
- Price records: `672`
- Market context records: `5937`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11219`

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

- `news_risk_high->fx_24h` score `6.7263` n `30` status `ready` deltaP `61.4583` edge `0.1508` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.51` n `30` status `ready` deltaP `39.2709` edge `0.2179` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.6131` n `30` status `ready` deltaP `37.4085` edge `0.0563` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1028` n `30` status `ready` deltaP `25.4291` edge `0.0196` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.3337` n `221` status `ready` deltaP `9.823` edge `0.1551` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8761` n `30` status `ready` deltaP `10.9381` edge `0.0861` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2021` n `30` status `ready` deltaP `5.3194` edge `0.0366` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.0793` n `221` status `ready` deltaP `6.2922` edge `0.0399` maxDD `-4.3608`
- `news_risk_high->index_24h` score `-0.2993` n `30` status `ready` deltaP `5.9375` edge `0.0092` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.307` n `221` status `ready` deltaP `3.8597` edge `0.002` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.443` n `30` status `ready` deltaP `1.5369` edge `-0.0304` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5584` n `221` status `ready` deltaP `-2.6452` edge `-0.0024` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.583` n `221` status `ready` deltaP `3.7134` edge `0.0326` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.6667` n `221` status `ready` deltaP `2.9513` edge `0.0283` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.6973` n `221` status `ready` deltaP `-1.2979` edge `-0.0006` maxDD `-0.5751`
- `market_context_high->index_1h` score `-0.8375` n `221` status `ready` deltaP `1.4374` edge `0.0054` maxDD `-0.7819`
- `news_risk_high->index_1h` score `-1.1225` n `30` status `ready` deltaP `-10.5988` edge `-0.0218` maxDD `-1.1161`
- `market_context_high->equity_24h` score `-1.1674` n `213` status `ready` deltaP `17.3171` edge `0.2425` maxDD `-31.2762`
- `market_context_high->commodity_4h` score `-1.7673` n `221` status `ready` deltaP `-5.1505` edge `-0.0209` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.7791` n `221` status `ready` deltaP `-3.6233` edge `-0.0407` maxDD `-5.725`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
