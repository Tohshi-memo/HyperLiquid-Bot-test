# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T09:22:27.437466+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3905`

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

- `news_risk_high->equity_4h` score `1.3055` n `62` status `ready` deltaP `12.4459` edge `0.1583` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.7031` n `62` status `ready` deltaP `12.7753` edge `0.0212` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.2952` n `62` status `ready` deltaP `9.235` edge `0.1431` maxDD `-6.6786`
- `news_risk_high->fx_24h` score `0.1424` n `62` status `ready` deltaP `-1.7025` edge `0.0674` maxDD `-0.2016`
- `news_risk_high->index_1h` score `0.0544` n `62` status `ready` deltaP `7.3498` edge `0.0033` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.108` n `62` status `ready` deltaP `-0.7485` edge `0.0461` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.116` n `62` status `ready` deltaP `3.1582` edge `0.0026` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.2032` n `62` status `ready` deltaP `2.1194` edge `0.0044` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5641` n `62` status `ready` deltaP `-4.4234` edge `-0.0071` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-0.9816` n `62` status `ready` deltaP `0.8114` edge `-0.0407` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.2203` n `62` status `ready` deltaP `-2.4435` edge `-0.0246` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.3312` n `62` status `ready` deltaP `-3.7716` edge `0.0149` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.5955` n `62` status `ready` deltaP `-11.1744` edge `-0.0025` maxDD `-1.1434`
- `news_risk_high->crypto_major_1h` score `-2.0266` n `62` status `ready` deltaP `-8.3301` edge `-0.0316` maxDD `-3.2066`
- `news_risk_high->crypto_alt_4h` score `-2.2426` n `62` status `ready` deltaP `-3.1619` edge `-0.0044` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.8032` n `62` status `ready` deltaP `-5.4268` edge `-0.2618` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.5299` n `62` status `ready` deltaP `-31.2795` edge `-0.0118` maxDD `-3.9061`
- `news_risk_high->equity_24h` score `-4.9185` n `62` status `ready` deltaP `20.6933` edge `0.3901` maxDD `-86.0244`
- `news_risk_high->commodity_24h` score `-10.5913` n `62` status `ready` deltaP `-28.6178` edge `-0.1258` maxDD `-27.9483`
- `news_risk_high->crypto_major_24h` score `-14.5285` n `62` status `ready` deltaP `-31.3172` edge `-0.1516` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
