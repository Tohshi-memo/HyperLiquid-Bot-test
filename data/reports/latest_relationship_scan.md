# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T13:22:26.382551+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3916`

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

- `news_risk_high->equity_24h` score `0.2742` n `117` status `ready` deltaP `23.7291` edge `1.0356` maxDD `-86.0244`
- `news_risk_high->index_4h` score `-0.0811` n `117` status `ready` deltaP `9.2193` edge `0.0124` maxDD `-2.0743`
- `news_risk_high->index_1h` score `-0.2297` n `117` status `ready` deltaP `6.3911` edge `0.0021` maxDD `-0.9325`
- `news_risk_high->fx_1h` score `-0.4127` n `117` status `ready` deltaP `-1.6492` edge `-0.0011` maxDD `-0.2651`
- `news_risk_high->crypto_alt_4h` score `-0.5793` n `117` status `ready` deltaP `4.0312` edge `0.1625` maxDD `-14.0916`
- `news_risk_high->index_24h` score `-0.5865` n `117` status `ready` deltaP `-2.6558` edge `0.126` maxDD `-6.6786`
- `news_risk_high->crypto_alt_1h` score `-0.6892` n `117` status `ready` deltaP `1.1131` edge `0.027` maxDD `-5.8225`
- `news_risk_high->metal_1h` score `-1.0255` n `117` status `ready` deltaP `-3.1412` edge `-0.0114` maxDD `-1.2495`
- `news_risk_high->crypto_major_4h` score `-1.1296` n `117` status `ready` deltaP `-3.3615` edge `0.0587` maxDD `-9.1553`
- `news_risk_high->fx_4h` score `-1.1691` n `117` status `ready` deltaP `-2.2188` edge `-0.0017` maxDD `-0.4745`
- `news_risk_high->fx_24h` score `-1.3308` n `117` status `ready` deltaP `-15.4304` edge `-0.0043` maxDD `-0.4086`
- `news_risk_high->equity_1h` score `-1.3675` n `117` status `ready` deltaP `-0.5771` edge `0.0188` maxDD `-10.2217`
- `news_risk_high->crypto_major_1h` score `-1.547` n `117` status `ready` deltaP `-3.4163` edge `-0.0056` maxDD `-4.7103`
- `news_risk_high->equity_4h` score `-2.143` n `117` status `ready` deltaP `9.6767` edge `0.1078` maxDD `-23.0714`
- `news_risk_high->metal_4h` score `-2.4666` n `117` status `ready` deltaP `-6.3126` edge `-0.0455` maxDD `-2.7708`
- `news_risk_high->commodity_1h` score `-2.744` n `117` status `ready` deltaP `-13.1417` edge `-0.0044` maxDD `-3.2657`
- `news_risk_high->metal_24h` score `-3.3896` n `117` status `ready` deltaP `-4.0738` edge `-0.2178` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.8259` n `117` status `ready` deltaP `-22.7747` edge `-0.0149` maxDD `-9.5011`
- `news_risk_high->crypto_major_24h` score `-6.3431` n `117` status `ready` deltaP `-17.1443` edge `0.1514` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-10.2731` n `117` status `ready` deltaP `-23.6019` edge `0.0077` maxDD `-39.1824`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
