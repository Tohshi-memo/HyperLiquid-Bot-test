# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T08:37:27.389450+00:00`
- Price records: `672`
- Market context records: `5862`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10104`

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

- `news_risk_high->fx_4h` score `3.7011` n `30` status `ready` deltaP `38.628` edge `0.0555` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `1.9627` n `30` status `ready` deltaP `23.7824` edge `0.0189` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.8683` n `30` status `ready` deltaP `11.5369` edge `0.0811` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.6155` n `246` status `ready` deltaP `6.9106` edge `0.151` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.2543` n `30` status `ready` deltaP `5.3194` edge `0.0433` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3349` n `246` status `ready` deltaP `0.8556` edge `-0.0001` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.4307` n `246` status `ready` deltaP `4.5604` edge `0.0344` maxDD `-5.0555`
- `news_risk_high->metal_1h` score `-0.4352` n `30` status `ready` deltaP `1.3872` edge `-0.0284` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.5008` n `246` status `ready` deltaP `3.3385` edge `0.0031` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.5548` n `246` status `ready` deltaP `-1.3704` edge `-0.0019` maxDD `-2.1412`
- `market_context_high->index_1h` score `-0.6167` n `246` status `ready` deltaP `0.3006` edge `0.0037` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.7648` n `246` status `ready` deltaP `3.8947` edge `0.0424` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.9124` n `246` status `ready` deltaP `2.7177` edge `0.0393` maxDD `-6.6758`
- `news_risk_high->index_1h` score `-1.2409` n `30` status `ready` deltaP `-12.5449` edge `-0.024` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.2455` n `246` status `ready` deltaP `-0.4574` edge `0.0121` maxDD `-3.165`
- `market_context_high->equity_24h` score `-1.615` n `228` status `ready` deltaP `14.9122` edge `0.2739` maxDD `-31.6316`
- `market_context_high->metal_4h` score `-1.7591` n `246` status `ready` deltaP `-3.4553` edge `-0.0333` maxDD `-6.2024`
- `news_risk_high->commodity_4h` score `-1.7763` n `30` status `ready` deltaP `-13.2723` edge `-0.0517` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.8241` n `228` status `ready` deltaP `4.8794` edge `0.0154` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.828` n `246` status `ready` deltaP `-5.437` edge `-0.0032` maxDD `-2.2593`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
