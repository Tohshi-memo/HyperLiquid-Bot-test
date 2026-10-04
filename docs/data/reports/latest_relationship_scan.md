# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T18:22:25.126591+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5058`

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

- `market_context_high->unknown_1h` score `96.7304` n `97` status `ready` deltaP `-0.4599` edge `8.1054` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `78.4692` n `97` status `ready` deltaP `2.604` edge `6.5529` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.5951` n `65` status `ready` deltaP `37.5821` edge `0.6527` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `9.2914` n `46` status `ready` deltaP `30.7971` edge `0.6342` maxDD `-4.5519`
- `market_context_high->crypto_alt_24h` score `9.1199` n `46` status `ready` deltaP `24.3584` edge `0.7249` maxDD `-8.1838`
- `news_risk_high->crypto_alt_4h` score `7.5378` n `65` status `ready` deltaP `24.9695` edge `0.5961` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `7.2936` n `65` status `ready` deltaP `21.7976` edge `0.4725` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.9285` n `97` status `ready` deltaP `21.5631` edge `0.3373` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.8453` n `65` status `ready` deltaP `26.7361` edge `0.1422` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8368` n `65` status `ready` deltaP `25.9123` edge `0.208` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.2841` n `65` status `ready` deltaP `35.8771` edge `0.0607` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8945` n `65` status `ready` deltaP `12.4113` edge `0.194` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.6744` n `65` status `ready` deltaP `23.3467` edge `0.1088` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.2076` n `65` status `ready` deltaP `27.1142` edge `0.0182` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `2.156` n `97` status `ready` deltaP `15.3297` edge `0.1225` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.6781` n `65` status `ready` deltaP `6.0663` edge `0.1513` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `1.651` n `97` status `ready` deltaP `6.8252` edge `0.271` maxDD `-7.6465`
- `market_context_high->fx_4h` score `1.4068` n `97` status `ready` deltaP `25.1257` edge `0.0254` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3646` n `46` status `ready` deltaP `25.536` edge `0.1065` maxDD `-1.8102`
- `market_context_high->fx_1h` score `0.9504` n `97` status `ready` deltaP `14.8666` edge `0.0065` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
