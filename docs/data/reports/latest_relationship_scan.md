# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T18:37:26.592746+00:00`
- Price records: `672`
- Market context records: `5905`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11166`

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

- `news_risk_high->fx_4h` score `3.6047` n `30` status `ready` deltaP `37.4085` edge `0.0556` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `1.9878` n `30` status `ready` deltaP `24.0818` edge `0.019` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9361` n `30` status `ready` deltaP `11.3872` edge `0.0908` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.743` n `220` status `ready` deltaP `7.0732` edge `0.1242` maxDD `-4.0887`
- `news_risk_high->crypto_alt_1h` score `0.2271` n `30` status `ready` deltaP `5.1697` edge `0.0408` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.22` n `220` status `ready` deltaP `4.7714` edge `0.032` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3478` n `220` status `ready` deltaP `2.9096` edge `0.0031` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4718` n `30` status `ready` deltaP `0.7884` edge `-0.0291` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.4971` n `220` status `ready` deltaP `-1.5406` edge `-0.0019` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.5326` n `220` status `ready` deltaP `3.963` edge `0.0374` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.6257` n `220` status `ready` deltaP `3.0485` edge `0.0329` maxDD `-6.6758`
- `market_context_high->index_1h` score `-0.6414` n `220` status `ready` deltaP `-0.1279` edge `0.0034` maxDD `-0.7819`
- `market_context_high->fx_1h` score `-0.8317` n `220` status `ready` deltaP `-2.8879` edge `-0.0012` maxDD `-0.5751`
- `news_risk_high->index_1h` score `-1.2074` n `30` status `ready` deltaP `-11.9461` edge `-0.0237` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.5854` n `220` status `ready` deltaP `-2.2228` edge `-0.0171` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.7172` n `220` status `ready` deltaP `-3.5282` edge `-0.0334` maxDD `-5.725`
- `news_risk_high->commodity_4h` score `-1.9034` n `30` status `ready` deltaP `-15.1016` edge `-0.0558` maxDD `-2.3372`
- `market_context_high->crypto_major_4h` score `-2.0093` n `220` status `ready` deltaP `8.0155` edge `0.1262` maxDD `-25.6458`
- `market_context_high->index_4h` score `-2.0543` n `220` status `ready` deltaP `-1.7045` edge `0.0089` maxDD `-3.165`
- `market_context_high->fx_24h` score `-2.1312` n `213` status `ready` deltaP `0.8949` edge `0.0026` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
