# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T09:07:26.279229+00:00`
- Price records: `672`
- Market context records: `5864`
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

- `news_risk_high->fx_4h` score `3.7023` n `30` status `ready` deltaP `38.628` edge `0.0556` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `1.9627` n `30` status `ready` deltaP `23.7824` edge `0.0189` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9002` n `30` status `ready` deltaP `11.8363` edge `0.0832` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.5976` n `244` status `ready` deltaP `6.6273` edge `0.1514` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.2855` n `30` status `ready` deltaP `5.6188` edge `0.0453` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3584` n `244` status `ready` deltaP `0.4491` edge `-0.0004` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.4203` n `244` status `ready` deltaP `4.6604` edge `0.0346` maxDD `-5.0555`
- `news_risk_high->metal_1h` score `-0.4375` n `30` status `ready` deltaP `1.3872` edge `-0.0287` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4406` n `244` status `ready` deltaP `3.7916` edge `0.0051` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.5857` n `244` status `ready` deltaP `-1.8136` edge `-0.0029` maxDD `-2.1412`
- `market_context_high->index_1h` score `-0.6062` n `244` status `ready` deltaP `0.4737` edge `0.0039` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.7603` n `244` status `ready` deltaP `3.8309` edge `0.0432` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.9161` n `244` status `ready` deltaP `2.6406` edge `0.0395` maxDD `-6.6758`
- `news_risk_high->index_1h` score `-1.2323` n `30` status `ready` deltaP `-12.3952` edge `-0.0239` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.2513` n `244` status `ready` deltaP `-0.5698` edge `0.0121` maxDD `-3.165`
- `market_context_high->metal_4h` score `-1.7366` n `244` status `ready` deltaP `-3.3237` edge `-0.0331` maxDD `-6.0573`
- `market_context_high->equity_24h` score `-1.7797` n `228` status `ready` deltaP `14.3824` edge `0.2637` maxDD `-31.6316`
- `news_risk_high->commodity_4h` score `-1.7976` n `30` status `ready` deltaP `-13.5772` edge `-0.0524` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.8273` n `228` status `ready` deltaP `4.8794` edge `0.015` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.8541` n `244` status `ready` deltaP `-5.8802` edge `-0.0036` maxDD `-2.2593`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
