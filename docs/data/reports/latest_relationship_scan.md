# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T20:07:19.204401+00:00`
- Price records: `580`
- Market context records: `679`
- Flow alert records: `1925`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `9.3619` n `146` status `ready` deltaP `23.3924` edge `0.6576` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.509` n `146` status `ready` deltaP `8.6126` edge `0.4898` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2174` n `147` status `ready` deltaP `7.0748` edge `0.0121` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.302` n `149` status `ready` deltaP `2.4733` edge `0.0026` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.461` n `149` status `ready` deltaP `2.315` edge `0.0436` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5928` n `149` status `ready` deltaP `0.7873` edge `0.0041` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.175` n `149` status `ready` deltaP `-1.6321` edge `-0.006` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.3093` n `149` status `ready` deltaP `-4.9765` edge `-0.0156` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.4334` n `149` status `ready` deltaP `4.233` edge `-0.0162` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.6216` n `147` status `ready` deltaP `2.8402` edge `-0.0018` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.7022` n `149` status `ready` deltaP `5.4379` edge `-0.0058` maxDD `-11.4508`
- `market_context_high->crypto_major_4h` score `-1.7388` n `147` status `ready` deltaP `16.1095` edge `0.1183` maxDD `-22.648`
- `market_context_high->crypto_alt_4h` score `-1.7805` n `147` status `ready` deltaP `5.2648` edge `0.0735` maxDD `-15.2248`
- `market_context_high->index_24h` score `-2.1058` n `146` status `ready` deltaP `-6.4155` edge `0.0668` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-2.6309` n `147` status `ready` deltaP `-1.4455` edge `0.0056` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3646` n `149` status `ready` deltaP `-5.0929` edge `-0.0505` maxDD `-9.0076`
- `market_context_high->equity_24h` score `-3.641` n `146` status `ready` deltaP `-8.6158` edge `0.0145` maxDD `-10.5047`
- `market_context_high->commodity_4h` score `-3.7026` n `147` status `ready` deltaP `-5.6632` edge `0.0793` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.5676` n `147` status `ready` deltaP `1.9178` edge `-0.2056` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.8101` n `146` status `ready` deltaP `-9.1496` edge `-0.0385` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
