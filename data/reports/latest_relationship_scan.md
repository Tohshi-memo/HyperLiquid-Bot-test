# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T23:22:29.526024+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7158`

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

- `market_context_high->unknown_4h` score `20.8441` n `99` status `ready` deltaP `1.5213` edge `1.7604` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.7764` n `61` status `ready` deltaP `23.7506` edge `0.0806` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.8081` n `99` status `ready` deltaP `10.8555` edge `0.0512` maxDD `-1.165`
- `market_context_high->commodity_1h` score `0.0389` n `107` status `ready` deltaP `6.2567` edge `0.0116` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.3155` n `107` status `ready` deltaP `0.957` edge `0.0028` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.5076` n `99` status `ready` deltaP `-1.4782` edge `0.0054` maxDD `-0.5168`
- `market_context_high->index_1h` score `-1.0224` n `107` status `ready` deltaP `-1.9965` edge `-0.0067` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-1.1188` n `107` status `ready` deltaP `-1.171` edge `-0.006` maxDD `-1.6873`
- `market_context_high->fx_24h` score `-2.187` n `61` status `ready` deltaP `-7.2575` edge `-0.0031` maxDD `-1.7949`
- `market_context_high->crypto_major_1h` score `-2.9363` n `107` status `ready` deltaP `-2.4498` edge `-0.0521` maxDD `-10.7675`
- `market_context_high->crypto_major_24h` score `-3.5342` n `61` status `ready` deltaP `-5.2368` edge `-0.1178` maxDD `-19.0308`
- `market_context_high->metal_4h` score `-3.5945` n `99` status `ready` deltaP `-12.229` edge `-0.0307` maxDD `-5.985`
- `market_context_high->metal_24h` score `-3.7343` n `61` status `ready` deltaP `-12.406` edge `0.0148` maxDD `-7.463`
- `market_context_high->crypto_alt_1h` score `-3.91` n `107` status `ready` deltaP `-3.4165` edge `-0.0747` maxDD `-14.9355`
- `market_context_high->equity_1h` score `-4.0411` n `107` status `ready` deltaP `-1.1347` edge `-0.0963` maxDD `-12.6316`
- `market_context_high->index_4h` score `-5.0666` n `99` status `ready` deltaP `-25.4727` edge `-0.0523` maxDD `-5.3413`
- `market_context_high->index_24h` score `-8.0063` n `61` status `ready` deltaP `-37.8302` edge `-0.1715` maxDD `-7.1458`
- `market_context_high->unknown_1h` score `-8.2805` n `107` status `ready` deltaP `-0.9821` edge `-0.6346` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `-10.8364` n `61` status `ready` deltaP `-2.3623` edge `-0.4542` maxDD `-64.213`
- `market_context_high->crypto_major_4h` score `-14.7307` n `99` status `ready` deltaP `-25.6252` edge `-0.3666` maxDD `-46.2099`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
