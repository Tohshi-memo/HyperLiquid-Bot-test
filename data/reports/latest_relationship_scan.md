# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T23:07:25.983072+00:00`
- Price records: `672`
- Market context records: `6134`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `10.6941` n `30` status `ready` deltaP `39.5139` edge `0.6425` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.7541` n `30` status `ready` deltaP `68.5764` edge `0.189` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3335` n `32` status `ready` deltaP `45.1982` edge `0.0644` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3919` n `32` status `ready` deltaP `28.7425` edge `0.0216` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.4034` n `195` status `ready` deltaP `0.6549` edge `0.2134` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.2075` n `32` status `ready` deltaP `13.2298` edge `0.1133` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.605` n `32` status `ready` deltaP `8.3271` edge `0.0682` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.4285` n `195` status `ready` deltaP `4.0549` edge `0.1004` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.1406` n `30` status `ready` deltaP `8.1944` edge `0.0145` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2754` n `195` status `ready` deltaP `1.4348` edge `-0.0003` maxDD `-0.5659`
- `market_context_high->unknown_4h` score `-0.3847` n `195` status `ready` deltaP `-2.7643` edge `0.2396` maxDD `-11.925`
- `news_risk_high->commodity_24h` score `-0.5695` n `30` status `ready` deltaP `14.0973` edge `-0.1209` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `-0.6608` n `30` status `ready` deltaP `9.8611` edge `-0.0725` maxDD `-4.2368`
- `market_context_high->metal_4h` score `-0.6666` n `195` status `ready` deltaP `3.2372` edge `0.0117` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7727` n `195` status `ready` deltaP `-2.2885` edge `-0.0045` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.8127` n `32` status `ready` deltaP `-3.5928` edge `-0.0305` maxDD `-1.6464`
- `market_context_high->equity_1h` score `-0.8266` n `195` status `ready` deltaP `-0.8583` edge `0.0113` maxDD `-4.2573`
- `market_context_high->metal_1h` score `-0.8847` n `195` status `ready` deltaP `1.7918` edge `-0.0058` maxDD `-2.0564`
- `market_context_high->metal_24h` score `-0.9451` n `195` status `ready` deltaP `15.3419` edge `0.0334` maxDD `-11.8809`
- `market_context_high->crypto_alt_1h` score `-0.9709` n `195` status `ready` deltaP `3.3111` edge `0.0287` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
