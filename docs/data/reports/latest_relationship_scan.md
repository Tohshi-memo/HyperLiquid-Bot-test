# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T03:07:28.713574+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10991`

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

- `risk_on_high->unknown_4h` score `22.2227` n `145` status `ready` deltaP `-3.0078` edge `2.0725` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `22.2227` n `145` status `ready` deltaP `-3.0078` edge `2.0725` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.7305` n `241` status `ready` deltaP `1.0443` edge `0.9674` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `4.7212` n `37` status `ready` deltaP `22.5742` edge `0.2699` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.9439` n `37` status `ready` deltaP `20.1389` edge `0.1944` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.2695` n `37` status `ready` deltaP `16.2657` edge `0.2053` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.4515` n `37` status `ready` deltaP `25.0659` edge `0.0593` maxDD `-0.7692`
- `market_context_high->equity_24h` score `2.0877` n `161` status `ready` deltaP `13.9514` edge `0.4348` maxDD `-16.9737`
- `news_risk_high->equity_1h` score `1.5727` n `37` status `ready` deltaP `12.935` edge `0.0839` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.56` n `37` status `ready` deltaP `7.6179` edge `0.0993` maxDD `-0.2737`
- `news_risk_high->metal_1h` score `1.3688` n `37` status `ready` deltaP `16.3619` edge `0.0243` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1742` n `37` status `ready` deltaP `14.7233` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.1079` n `37` status `ready` deltaP `5.8667` edge `0.0715` maxDD `-0.4628`
- `news_risk_high->fx_24h` score `1.1018` n `37` status `ready` deltaP `21.8656` edge `0.0476` maxDD `-3.1244`
- `news_risk_high->crypto_alt_1h` score `0.8206` n `37` status `ready` deltaP `8.5775` edge `0.0377` maxDD `-0.7867`
- `risk_on_high->crypto_major_24h` score `0.6206` n `78` status `ready` deltaP `9.5353` edge `0.7486` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `0.6206` n `78` status `ready` deltaP `9.5353` edge `0.7486` maxDD `-47.9416`
- `news_risk_high->commodity_1h` score `-0.0371` n `37` status `ready` deltaP `5.5754` edge `0.0027` maxDD `-0.9036`
- `news_risk_high->crypto_alt_4h` score `-0.042` n `37` status `ready` deltaP `2.7398` edge `0.0111` maxDD `-1.296`
- `risk_on_high->index_1h` score `-0.1084` n `145` status `ready` deltaP `5.0867` edge `-0.0031` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
