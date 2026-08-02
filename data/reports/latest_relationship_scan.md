# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T08:52:23.784128+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5900`

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

- `news_risk_high->unknown_24h` score `5188.4807` n `60` status `ready` deltaP `30.9416` edge `432.2092` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.8584` n `45` status `ready` deltaP `59.9153` edge `1.1285` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `7.0929` n `45` status `ready` deltaP `40.5662` edge `0.4055` maxDD `-4.7891`
- `news_risk_high->equity_4h` score `4.5361` n `68` status `ready` deltaP `16.5261` edge `0.3442` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.589` n `68` status `ready` deltaP `15.6115` edge `0.0664` maxDD `-0.3783`
- `market_context_high->fx_4h` score `1.0326` n `45` status `ready` deltaP `21.128` edge `0.0248` maxDD `-1.3685`
- `market_context_high->commodity_4h` score `0.735` n `45` status `ready` deltaP `11.3483` edge `0.1032` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.6` n `68` status `ready` deltaP `9.4928` edge `0.069` maxDD `-2.916`
- `market_context_high->crypto_alt_4h` score `0.2293` n `45` status `ready` deltaP `3.7026` edge `0.0991` maxDD `-5.2176`
- `market_context_high->commodity_1h` score `0.1845` n `45` status `ready` deltaP `5.2794` edge `0.0259` maxDD `-1.3282`
- `news_risk_high->fx_4h` score `0.1564` n `68` status `ready` deltaP `12.5986` edge `0.0248` maxDD `-0.6604`
- `market_context_high->fx_1h` score `0.1253` n `45` status `ready` deltaP `9.5742` edge `0.0025` maxDD `-0.6874`
- `news_risk_high->metal_4h` score `0.1142` n `68` status `ready` deltaP `5.3174` edge `0.0268` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.0757` n `68` status `ready` deltaP `6.1818` edge `0.0367` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.0427` n `68` status `ready` deltaP `3.267` edge `0.005` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.1034` n `68` status `ready` deltaP `1.8669` edge `0.0066` maxDD `-0.5845`
- `news_risk_high->metal_1h` score `-0.1349` n `68` status `ready` deltaP `2.6154` edge `0.0056` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2358` n `68` status `ready` deltaP `2.0694` edge `0.028` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.2704` n `45` status `ready` deltaP `3.9631` edge `0.0369` maxDD `-2.506`
- `market_context_high->crypto_alt_1h` score `-0.5112` n `45` status `ready` deltaP `-0.8117` edge `0.0026` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
