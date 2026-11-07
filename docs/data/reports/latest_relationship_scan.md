# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T11:07:25.874954+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4001`

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

- `market_context_high->equity_1h` score `3.4975` n `32` status `ready` deltaP `8.9259` edge `0.2779` maxDD `-2.3425`
- `news_risk_high->equity_4h` score `1.247` n `62` status `ready` deltaP `11.5312` edge `0.1569` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.6263` n `62` status `ready` deltaP `11.8607` edge `0.0209` maxDD `-0.4888`
- `market_context_high->fx_1h` score `0.589` n `32` status `ready` deltaP `8.9072` edge `0.0168` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.5363` n `32` status `ready` deltaP `4.0232` edge `0.0449` maxDD `-0.1621`
- `market_context_high->crypto_major_1h` score `0.4414` n `32` status `ready` deltaP `8.4955` edge `0.0585` maxDD `-3.0172`
- `market_context_high->metal_1h` score `0.3536` n `32` status `ready` deltaP `8.6265` edge `0.0206` maxDD `-0.6226`
- `market_context_high->crypto_alt_1h` score `0.3518` n `32` status `ready` deltaP `9.5434` edge `0.063` maxDD `-3.1881`
- `news_risk_high->index_24h` score `0.3345` n `62` status `ready` deltaP `9.9294` edge `0.1435` maxDD `-6.6786`
- `news_risk_high->index_1h` score `0.0551` n `62` status `ready` deltaP `7.3498` edge `0.0034` maxDD `-0.2931`
- `news_risk_high->fx_24h` score `0.053` n `62` status `ready` deltaP `-2.7442` edge `0.0669` maxDD `-0.2016`
- `market_context_high->commodity_1h` score `0.0189` n `32` status `ready` deltaP `7.4289` edge `0.0075` maxDD `-1.7019`
- `news_risk_high->equity_1h` score `-0.0854` n `62` status `ready` deltaP `-0.4491` edge `0.047` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.1316` n `62` status `ready` deltaP `2.8588` edge `0.0026` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.1866` n `62` status `ready` deltaP `2.4243` edge `0.0045` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.54` n `62` status `ready` deltaP `-3.9743` edge `-0.007` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-0.9475` n `62` status `ready` deltaP `1.4211` edge `-0.0404` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.147` n `62` status `ready` deltaP `-1.5453` edge `-0.0212` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.2344` n `62` status `ready` deltaP `-2.7046` edge `0.0202` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.635` n `62` status `ready` deltaP `-11.6235` edge `-0.0028` maxDD `-1.1434`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
