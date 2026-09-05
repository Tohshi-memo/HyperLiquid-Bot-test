# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T17:22:25.656929+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10585`

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

- `risk_on_high->unknown_4h` score `22.0918` n `138` status `ready` deltaP `0.7379` edge `1.9653` maxDD `-4.0053`
- `risk_on_and_context->unknown_4h` score `22.0918` n `138` status `ready` deltaP `0.7379` edge `1.9653` maxDD `-4.0053`
- `market_context_high->unknown_4h` score `9.2402` n `228` status `ready` deltaP `3.236` edge `0.9141` maxDD `-5.2527`
- `news_risk_high->crypto_alt_24h` score `7.0811` n `37` status `ready` deltaP `25.1783` edge `0.4492` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.7709` n `37` status `ready` deltaP `19.7917` edge `0.1823` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.5116` n `37` status `ready` deltaP `17.0279` edge `0.2204` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3807` n `37` status `ready` deltaP `24.1513` edge `0.0595` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.8047` n `37` status `ready` deltaP `10.3618` edge `0.1014` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.5332` n `37` status `ready` deltaP `12.4859` edge `0.0836` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.2598` n `37` status `ready` deltaP `15.0146` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1251` n `37` status `ready` deltaP `14.1245` edge `0.013` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.1211` n `37` status `ready` deltaP `5.8667` edge `0.0726` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.9297` n `37` status `ready` deltaP `9.0266` edge `0.0438` maxDD `-0.7867`
- `news_risk_high->crypto_major_24h` score `0.8626` n `37` status `ready` deltaP `16.5776` edge `0.2777` maxDD `-18.2098`
- `news_risk_high->fx_24h` score `0.6172` n `37` status `ready` deltaP `16.4836` edge `0.0431` maxDD `-3.1244`
- `news_risk_high->crypto_alt_4h` score `0.5583` n `37` status `ready` deltaP `5.7886` edge `0.0408` maxDD `-1.296`
- `market_context_high->equity_24h` score `0.5318` n `177` status `ready` deltaP `13.8124` edge `0.3868` maxDD `-20.7654`
- `risk_on_high->index_1h` score `0.083` n `148` status `ready` deltaP `8.0434` edge `-0.002` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.083` n `148` status `ready` deltaP `8.0434` edge `-0.002` maxDD `-0.5764`
- `news_risk_high->commodity_1h` score `-0.0169` n `37` status `ready` deltaP `5.8748` edge `0.0033` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
