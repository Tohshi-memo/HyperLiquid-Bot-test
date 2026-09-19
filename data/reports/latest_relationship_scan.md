# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T19:07:29.457118+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8502`

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

- `news_risk_high->crypto_major_24h` score `51.2929` n `72` status `ready` deltaP `28.125` edge `4.1761` maxDD `-5.8019`
- `market_context_high->unknown_4h` score `48.0172` n `122` status `ready` deltaP `-3.3961` edge `4.0474` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `44.8263` n `72` status `ready` deltaP `33.6806` edge `3.6489` maxDD `-9.3661`
- `risk_on_high->unknown_4h` score `30.0031` n `32` status `ready` deltaP `-16.9207` edge `2.6356` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `30.0031` n `32` status `ready` deltaP `-16.9207` edge `2.6356` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `9.8812` n `32` status `ready` deltaP `48.7847` edge `0.4982` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.8812` n `32` status `ready` deltaP `48.7847` edge `0.4982` maxDD `0.0`
- `news_risk_high->equity_24h` score `9.0507` n `72` status `ready` deltaP `37.6736` edge `0.5073` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.748` n `122` status `ready` deltaP `40.588` edge `0.4276` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.6188` n `98` status `ready` deltaP `21.161` edge `0.4481` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.2385` n `98` status `ready` deltaP `21.3134` edge `0.3369` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.2915` n `98` status `ready` deltaP `19.0731` edge `0.1937` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.5804` n `122` status `ready` deltaP `26.7818` edge `0.0783` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.3803` n `98` status `ready` deltaP `19.8216` edge `0.1185` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.0869` n `32` status `ready` deltaP `23.247` edge `0.0539` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0869` n `32` status `ready` deltaP `23.247` edge `0.0539` maxDD `-0.1313`
- `news_risk_high->metal_24h` score `1.7297` n `72` status `ready` deltaP `22.5694` edge `0.0781` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.399` n `122` status `ready` deltaP `17.4266` edge `0.0256` maxDD `-0.3491`
- `news_risk_high->metal_4h` score `0.8502` n `98` status `ready` deltaP `19.4344` edge `0.0467` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.7446` n `98` status `ready` deltaP `15.9049` edge `0.0162` maxDD `-0.8144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
