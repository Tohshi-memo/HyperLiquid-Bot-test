# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T14:22:27.787263+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4117`

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

- `market_context_high->unknown_4h` score `204.5569` n `33` status `ready` deltaP `-0.0785` edge `17.0689` maxDD `-0.4239`
- `market_context_high->fx_4h` score `3.428` n `33` status `ready` deltaP `36.6223` edge `0.0505` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.0771` n `37` status `ready` deltaP `8.5613` edge `0.2453` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.8554` n `33` status `ready` deltaP `24.2147` edge `0.0402` maxDD `-2.4279`
- `news_risk_high->equity_4h` score `1.0432` n `57` status `ready` deltaP `8.8869` edge `0.1484` maxDD `-4.2454`
- `news_risk_high->fx_24h` score `0.8534` n `57` status `ready` deltaP `1.9828` edge `0.08` maxDD `-0.1014`
- `market_context_high->crypto_major_1h` score `0.6836` n `37` status `ready` deltaP `9.152` edge `0.0545` maxDD `-3.0172`
- `news_risk_high->index_4h` score `0.5159` n `57` status `ready` deltaP `13.8479` edge `0.0216` maxDD `-0.4888`
- `market_context_high->fx_1h` score `0.4948` n `37` status `ready` deltaP `7.9706` edge `0.0152` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.3688` n `37` status `ready` deltaP `10.3496` edge `0.0598` maxDD `-3.1881`
- `news_risk_high->index_24h` score `0.2865` n `57` status `ready` deltaP `8.6623` edge `0.1458` maxDD `-6.6786`
- `market_context_high->index_1h` score `0.2733` n `37` status `ready` deltaP `1.6508` edge `0.0388` maxDD `-0.1621`
- `news_risk_high->index_1h` score `0.1934` n `57` status `ready` deltaP `9.9485` edge `0.0038` maxDD `-0.2931`
- `market_context_high->commodity_1h` score `0.1607` n `37` status `ready` deltaP `9.767` edge `0.0101` maxDD `-1.7019`
- `news_risk_high->fx_4h` score `0.001` n `57` status `ready` deltaP `5.8408` edge `0.0054` maxDD `-0.2038`
- `news_risk_high->equity_1h` score `-0.0498` n `57` status `ready` deltaP `-0.021` edge `0.0487` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.0854` n `57` status `ready` deltaP `3.7031` edge `0.0029` maxDD `-0.0826`
- `market_context_high->metal_1h` score `-0.0988` n `37` status `ready` deltaP `0.6029` edge `0.0161` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.1227` n `33` status `ready` deltaP `1.3628` edge `0.0206` maxDD `-1.633`
- `news_risk_high->metal_1h` score `-0.6923` n `57` status `ready` deltaP `-6.8889` edge `-0.0071` maxDD `-0.5256`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
