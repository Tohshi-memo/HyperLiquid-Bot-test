# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T23:37:26.110864+00:00`
- Price records: `672`
- Market context records: `7302`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13807`

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

- `market_context_high->fx_1h` score `-0.0984` n `126` status `ready` deltaP `5.148` edge `0.002` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.5216` n `126` status `ready` deltaP `0.1716` edge `-0.0108` maxDD `-1.5775`
- `market_context_high->crypto_alt_1h` score `-0.577` n `126` status `ready` deltaP `-0.4943` edge `0.0332` maxDD `-5.9775`
- `market_context_high->commodity_4h` score `-0.6991` n `121` status `ready` deltaP `2.7472` edge `-0.0111` maxDD `-2.4139`
- `market_context_high->fx_24h` score `-0.8562` n `116` status `ready` deltaP `1.6222` edge `0.0022` maxDD `-2.1564`
- `market_context_high->fx_4h` score `-0.9706` n `121` status `ready` deltaP `3.5914` edge `0.0116` maxDD `-1.4649`
- `market_context_high->crypto_major_1h` score `-1.0342` n `126` status `ready` deltaP `3.4146` edge `0.0321` maxDD `-7.6171`
- `market_context_high->index_1h` score `-1.2354` n `126` status `ready` deltaP `-4.5688` edge `-0.0083` maxDD `-2.1355`
- `market_context_high->unknown_4h` score `-1.3567` n `121` status `ready` deltaP `5.3871` edge `0.0869` maxDD `-6.2031`
- `market_context_high->unknown_1h` score `-1.7924` n `126` status `ready` deltaP `0.8079` edge `-0.0924` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-2.0146` n `121` status `ready` deltaP `2.0737` edge `0.0022` maxDD `-15.2776`
- `market_context_high->metal_1h` score `-2.1058` n `126` status `ready` deltaP `-9.4502` edge `-0.0021` maxDD `-1.4971`
- `market_context_high->metal_4h` score `-2.388` n `121` status `ready` deltaP `-8.558` edge `-0.0026` maxDD `-4.7198`
- `market_context_high->crypto_major_4h` score `-2.9577` n `121` status `ready` deltaP `2.6759` edge `-0.0076` maxDD `-23.4879`
- `market_context_high->unknown_24h` score `-3.1683` n `117` status `ready` deltaP `-7.9728` edge `-0.0387` maxDD `-13.1468`
- `market_context_high->commodity_24h` score `-3.3931` n `116` status `ready` deltaP `-6.8231` edge `-0.1575` maxDD `-2.3815`
- `market_context_high->equity_1h` score `-4.323` n `126` status `ready` deltaP `-8.5371` edge `-0.0657` maxDD `-14.3442`
- `market_context_high->index_4h` score `-4.6561` n `121` status `ready` deltaP `-13.8879` edge `-0.0513` maxDD `-9.1966`
- `market_context_high->metal_24h` score `-10.8363` n `117` status `ready` deltaP `-28.3788` edge `-0.125` maxDD `-20.4399`
- `market_context_high->index_24h` score `-12.618` n `116` status `ready` deltaP `-30.4573` edge `-0.1609` maxDD `-32.0038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
