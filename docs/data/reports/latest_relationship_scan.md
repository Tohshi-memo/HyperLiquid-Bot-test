# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T05:07:31.405423+00:00`
- Price records: `672`
- Market context records: `5847`
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
- `news_risk_high->crypto_major_1h` score `0.8207` n `30` status `ready` deltaP `11.2375` edge `0.077` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.7524` n `257` status `ready` deltaP `7.9322` edge `0.1556` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.1928` n `30` status `ready` deltaP `4.8703` edge `0.0384` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3039` n `257` status `ready` deltaP `1.4219` edge `0.0001` maxDD `-0.5499`
- `news_risk_high->metal_1h` score `-0.411` n `30` status `ready` deltaP `1.6866` edge `-0.0273` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4125` n `257` status `ready` deltaP `4.3227` edge `0.0375` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.4638` n `257` status `ready` deltaP `3.6062` edge `0.0044` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.5022` n `257` status `ready` deltaP `-0.5231` edge `-0.0008` maxDD `-2.1412`
- `market_context_high->index_1h` score `-0.5764` n `257` status `ready` deltaP `0.9122` edge `0.0048` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.8071` n `257` status `ready` deltaP `3.5462` edge `0.0412` maxDD `-6.2348`
- `market_context_high->equity_24h` score `-0.8128` n `229` status `ready` deltaP `16.929` edge `0.3273` maxDD `-31.6316`
- `market_context_high->crypto_alt_1h` score `-0.9754` n `257` status `ready` deltaP `2.2892` edge `0.0369` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.183` n `257` status `ready` deltaP `0.4591` edge `0.014` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.2331` n `30` status `ready` deltaP `-12.3952` edge `-0.024` maxDD `-1.1161`
- `market_context_high->fx_4h` score `-1.7446` n `257` status `ready` deltaP `-3.9694` edge `-0.0023` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.798` n `229` status `ready` deltaP `5.1264` edge `0.0171` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-2.0955` n `257` status `ready` deltaP `-4.3466` edge `-0.0393` maxDD `-8.6964`
- `market_context_high->commodity_4h` score `-2.3044` n `257` status `ready` deltaP `-0.0297` edge `-0.0126` maxDD `-7.0053`
- `market_context_high->crypto_major_4h` score `-2.8175` n `257` status `ready` deltaP `7.3265` edge `0.1536` maxDD `-25.6458`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
