# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T03:22:29.773044+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11077`

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

- `risk_on_high->unknown_4h` score `22.2011` n `145` status `ready` deltaP `-3.0078` edge `2.0707` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `22.2011` n `145` status `ready` deltaP `-3.0078` edge `2.0707` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.5824` n `242` status `ready` deltaP `1.1729` edge `0.9542` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `4.6353` n `37` status `ready` deltaP `22.4005` edge `0.2639` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.9487` n `37` status `ready` deltaP `20.1389` edge `0.1948` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.2611` n `37` status `ready` deltaP `16.2657` edge `0.2046` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.4649` n `37` status `ready` deltaP `25.2184` edge `0.0594` maxDD `-0.7692`
- `market_context_high->equity_24h` score `2.029` n `162` status `ready` deltaP `13.9081` edge `0.4302` maxDD `-16.9737`
- `news_risk_high->equity_1h` score `1.5727` n `37` status `ready` deltaP `12.935` edge `0.0839` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.5466` n `37` status `ready` deltaP `7.4654` edge `0.0992` maxDD `-0.2737`
- `news_risk_high->metal_1h` score `1.3808` n `37` status `ready` deltaP `16.5116` edge `0.0243` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1742` n `37` status `ready` deltaP `14.7233` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->fx_24h` score `1.1018` n `37` status `ready` deltaP `21.8656` edge `0.0476` maxDD `-3.1244`
- `news_risk_high->crypto_major_1h` score `1.0911` n `37` status `ready` deltaP `5.717` edge `0.0711` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.8062` n `37` status `ready` deltaP `8.4278` edge `0.0375` maxDD `-0.7867`
- `risk_on_high->crypto_major_24h` score `0.7401` n `79` status `ready` deltaP `9.9134` edge `0.7614` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `0.7401` n `79` status `ready` deltaP `9.9134` edge `0.7614` maxDD `-47.9416`
- `news_risk_high->commodity_1h` score `-0.0371` n `37` status `ready` deltaP `5.5754` edge `0.0027` maxDD `-0.9036`
- `news_risk_high->crypto_alt_4h` score `-0.0528` n `37` status `ready` deltaP `2.7398` edge `0.0102` maxDD `-1.296`
- `risk_on_high->index_1h` score `-0.1084` n `145` status `ready` deltaP `5.0867` edge `-0.0031` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
