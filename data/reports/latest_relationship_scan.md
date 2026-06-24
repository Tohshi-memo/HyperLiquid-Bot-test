# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T10:07:35.042276+00:00`
- Price records: `672`
- Market context records: `4611`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9851`

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

- `market_context_high->unknown_1h` score `69.3259` n `147` status `ready` deltaP `7.8079` edge `5.771` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.2892` n `147` status `ready` deltaP `9.0561` edge `0.4181` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.439` n `147` status `ready` deltaP `2.4777` edge `0.0265` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5622` n `147` status `ready` deltaP `-1.8769` edge `-0.0041` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7739` n `147` status `ready` deltaP `1.4892` edge `-0.0009` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.9191` n `147` status `ready` deltaP `-2.5856` edge `-0.0019` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.9363` n `147` status `ready` deltaP `1.0567` edge `-0.0148` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.1175` n `147` status `ready` deltaP `4.3492` edge `0.0385` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.6964` n `147` status `ready` deltaP `-4.0959` edge `-0.0132` maxDD `-2.7358`
- `market_context_high->equity_4h` score `-1.7898` n `147` status `ready` deltaP `-1.3709` edge `-0.0434` maxDD `-8.8203`
- `market_context_high->unknown_24h` score `-2.2491` n `145` status `ready` deltaP `2.9263` edge `-0.1146` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-3.0023` n `147` status `ready` deltaP `-4.598` edge `-0.0891` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.6365` n `145` status `ready` deltaP `11.6295` edge `0.061` maxDD `-29.3255`
- `market_context_high->fx_24h` score `-5.3267` n `145` status `ready` deltaP `-12.3252` edge `-0.0105` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.6528` n `147` status `ready` deltaP `-2.7353` edge `-0.1241` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.8949` n `147` status `ready` deltaP `-6.4493` edge `-0.1563` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.4015` n `145` status `ready` deltaP `-8.3166` edge `-0.1072` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.2717` n `147` status `ready` deltaP `-3.9986` edge `-0.2963` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.3946` n `147` status `ready` deltaP `-7.343` edge `-0.3623` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.4126` n `147` status `ready` deltaP `-6.0281` edge `-0.4568` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
