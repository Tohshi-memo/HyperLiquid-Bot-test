# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T11:22:28.022260+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8390`

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

- `market_context_high->unknown_4h` score `39.7392` n `149` status `ready` deltaP `-0.311` edge `3.337` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.6179` n `52` status `ready` deltaP `-7.5516` edge `1.2077` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.6179` n `52` status `ready` deltaP `-7.5516` edge `1.2077` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.8871` n `52` status `ready` deltaP `50.1736` edge `0.4061` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8871` n `52` status `ready` deltaP `50.1736` edge `0.4061` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5879` n `149` status `ready` deltaP `43.4622` edge `0.3951` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `3.1082` n `89` status `ready` deltaP `20.0021` edge `0.4802` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.8195` n `52` status `ready` deltaP `32.5399` edge `0.053` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8195` n `52` status `ready` deltaP `32.5399` edge `0.053` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7192` n `149` status `ready` deltaP `29.0422` edge `0.0748` maxDD `-0.345`
- `news_risk_high->equity_4h` score `1.1329` n `89` status `ready` deltaP `15.1856` edge `0.1277` maxDD `-3.3619`
- `market_context_high->commodity_1h` score `1.1169` n `149` status `ready` deltaP `16.2109` edge `0.0227` maxDD `-0.3491`
- `risk_on_high->fx_24h` score `0.8747` n `52` status `ready` deltaP `17.8686` edge `-0.042` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.8747` n `52` status `ready` deltaP `17.8686` edge `-0.042` maxDD `-0.0054`
- `market_context_high->fx_24h` score `0.7398` n `149` status `ready` deltaP `15.0937` edge `-0.0174` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.4936` n `52` status `ready` deltaP `9.293` edge `0.0144` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4936` n `52` status `ready` deltaP `9.293` edge `0.0144` maxDD `-0.1507`
- `news_risk_high->fx_4h` score `0.3903` n `89` status `ready` deltaP `10.1552` edge `0.027` maxDD `-0.2398`
- `news_risk_high->equity_1h` score `0.2733` n `95` status `ready` deltaP `9.8408` edge `0.0216` maxDD `-1.8403`
- `news_risk_high->crypto_major_4h` score `0.1323` n `89` status `ready` deltaP `11.3575` edge `0.2659` maxDD `-19.972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
