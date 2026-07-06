# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T04:52:25.533870+00:00`
- Price records: `672`
- Market context records: `5846`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10128`

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

- `news_risk_high->fx_1h` score `1.9627` n `30` status `ready` deltaP `23.7824` edge `0.0189` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.7981` n `30` status `ready` deltaP `11.0878` edge `0.0751` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.7553` n `258` status `ready` deltaP `7.908` edge `0.156` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.1717` n `30` status `ready` deltaP `4.7206` edge `0.0367` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3157` n `258` status `ready` deltaP `1.2243` edge `-0.0001` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.3804` n `258` status `ready` deltaP `4.469` edge `0.0392` maxDD `-5.0555`
- `news_risk_high->metal_1h` score `-0.4211` n `30` status `ready` deltaP `1.5369` edge `-0.0276` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4583` n `258` status `ready` deltaP `3.63` edge `0.0047` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.5039` n `258` status `ready` deltaP `-0.5559` edge `-0.0008` maxDD `-2.1412`
- `market_context_high->index_1h` score `-0.5638` n `258` status `ready` deltaP `1.0932` edge `0.0052` maxDD `-0.7819`
- `market_context_high->equity_24h` score `-0.7654` n `230` status `ready` deltaP `16.8162` edge `0.332` maxDD `-31.6316`
- `market_context_high->crypto_major_1h` score `-0.7801` n `258` status `ready` deltaP `3.5685` edge `0.0433` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.9588` n `258` status `ready` deltaP `2.3175` edge `0.0381` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1797` n `258` status `ready` deltaP `0.4786` edge `0.0143` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.2339` n `30` status `ready` deltaP `-12.3952` edge `-0.0241` maxDD `-1.1161`
- `market_context_high->fx_4h` score `-1.7326` n `258` status `ready` deltaP `-3.7673` edge `-0.0021` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.7822` n `230` status `ready` deltaP `5.3713` edge `0.0175` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-2.0983` n `258` status `ready` deltaP `-4.312` edge `-0.0399` maxDD `-8.6964`
- `market_context_high->commodity_4h` score `-2.3032` n `258` status `ready` deltaP `-0.0295` edge `-0.0125` maxDD `-7.0053`
- `market_context_high->crypto_major_4h` score `-2.834` n `258` status `ready` deltaP `7.3159` edge `0.1523` maxDD `-25.6458`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
