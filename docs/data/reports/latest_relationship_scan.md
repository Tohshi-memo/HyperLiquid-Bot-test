# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T16:37:29.895713+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8456`

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

- `market_context_high->unknown_4h` score `39.9502` n `149` status `ready` deltaP `-0.4634` edge `3.3556` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `18.6531` n `36` status `ready` deltaP `30.0347` edge `1.4921` maxDD `-9.3661`
- `risk_on_high->unknown_4h` score `13.8289` n `52` status `ready` deltaP `-7.704` edge `1.2263` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.8289` n `52` status `ready` deltaP `-7.704` edge `1.2263` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.5937` n `52` status `ready` deltaP `47.9167` edge `0.3967` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5937` n `52` status `ready` deltaP `47.9167` edge `0.3967` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `7.8556` n `36` status `ready` deltaP `-4.1667` edge `1.1942` maxDD `-10.0773`
- `market_context_high->commodity_24h` score `7.2946` n `149` status `ready` deltaP `41.2053` edge `0.3857` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.1135` n `93` status `ready` deltaP `22.1004` edge `0.514` maxDD `-8.4837`
- `risk_on_high->commodity_4h` score `2.7449` n `52` status `ready` deltaP `32.3874` edge `0.0478` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7449` n `52` status `ready` deltaP `32.3874` edge `0.0478` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.6446` n `149` status `ready` deltaP `28.8897` edge `0.0696` maxDD `-0.345`
- `news_risk_high->equity_4h` score `1.3253` n `93` status `ready` deltaP `13.6097` edge `0.1097` maxDD `-4.1995`
- `market_context_high->commodity_1h` score `1.1217` n `149` status `ready` deltaP `16.3606` edge `0.0221` maxDD `-0.3491`
- `news_risk_high->crypto_major_4h` score `0.9532` n `93` status `ready` deltaP `13.9392` edge `0.2937` maxDD `-15.8202`
- `news_risk_high->equity_1h` score `0.7477` n `93` status `ready` deltaP `11.8344` edge `0.0327` maxDD `-1.6096`
- `risk_on_high->fx_24h` score `0.5607` n `52` status `ready` deltaP `15.2644` edge `-0.0508` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.5607` n `52` status `ready` deltaP `15.2644` edge `-0.0508` maxDD `-0.0054`
- `risk_on_high->commodity_1h` score `0.4984` n `52` status `ready` deltaP `9.4427` edge `0.0138` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4984` n `52` status `ready` deltaP `9.4427` edge `0.0138` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
