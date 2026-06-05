# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T06:41:50.743338+00:00`
- Price records: `672`
- Market context records: `2945`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `16.6463` n `137` status `ready` deltaP `15.3703` edge `1.6764` maxDD `-22.6673`
- `market_context_high->equity_24h` score `7.9736` n `137` status `ready` deltaP `18.38` edge `0.7423` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `7.1875` n `137` status `ready` deltaP `16.5488` edge `0.5351` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.939` n `137` status `ready` deltaP `14.3832` edge `0.2471` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `2.7636` n `137` status `ready` deltaP `17.9225` edge `0.384` maxDD `-11.1879`
- `market_context_high->equity_4h` score `1.2625` n `138` status `ready` deltaP `9.6169` edge `0.1603` maxDD `-5.203`
- `market_context_high->index_4h` score `0.7869` n `138` status `ready` deltaP `15.4847` edge `0.0818` maxDD `-2.3986`
- `market_context_high->crypto_alt_4h` score `0.304` n `138` status `ready` deltaP `16.3551` edge `0.3766` maxDD `-30.8239`
- `market_context_high->unknown_4h` score `0.2706` n `138` status `ready` deltaP `3.853` edge `0.1022` maxDD `-3.7602`
- `market_context_high->index_1h` score `0.0712` n `138` status `ready` deltaP `5.7494` edge `0.0202` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.3722` n `138` status `ready` deltaP `0.6053` edge `0.0465` maxDD `-2.5241`
- `market_context_high->crypto_alt_1h` score `-0.3889` n `138` status `ready` deltaP `5.6474` edge `0.0885` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.5226` n `138` status `ready` deltaP `-0.9221` edge `0.0027` maxDD `-0.2081`
- `market_context_high->crypto_major_1h` score `-0.548` n `138` status `ready` deltaP `5.7429` edge `0.0784` maxDD `-9.622`
- `market_context_high->unknown_1h` score `-0.5869` n `138` status `ready` deltaP `2.1262` edge `0.01` maxDD `-3.1801`
- `market_context_high->metal_1h` score `-0.6672` n `138` status `ready` deltaP `-0.1801` edge `0.0044` maxDD `-3.4325`
- `market_context_high->commodity_1h` score `-0.6786` n `138` status `ready` deltaP `-1.1195` edge `-0.0042` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.8817` n `138` status `ready` deltaP `-0.4949` edge `0.0077` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2168` n `138` status `ready` deltaP `2.5229` edge `0.0192` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.4047` n `137` status `ready` deltaP `-2.5598` edge `-0.0128` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
