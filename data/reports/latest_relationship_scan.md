# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T08:22:30.390767+00:00`
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

- `news_risk_high->unknown_24h` score `5188.5229` n `60` status `ready` deltaP `31.2882` edge `432.2104` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.0411` n `47` status `ready` deltaP `60.2936` edge `1.1412` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `5.8504` n `47` status `ready` deltaP `36.8782` edge `0.3544` maxDD `-6.3509`
- `news_risk_high->equity_4h` score `4.5337` n `68` status `ready` deltaP `16.5261` edge `0.344` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.5902` n `68` status `ready` deltaP `15.6115` edge `0.0665` maxDD `-0.3783`
- `market_context_high->fx_4h` score `1.1359` n `47` status `ready` deltaP `22.5253` edge `0.0241` maxDD `-1.3685`
- `news_risk_high->equity_1h` score `0.6168` n `68` status `ready` deltaP `9.6425` edge `0.0694` maxDD `-2.916`
- `market_context_high->commodity_4h` score `0.4983` n `47` status `ready` deltaP `9.1366` edge `0.0876` maxDD `-2.7703`
- `market_context_high->crypto_alt_4h` score `0.2159` n `47` status `ready` deltaP `3.8077` edge `0.098` maxDD `-5.323`
- `news_risk_high->fx_4h` score `0.1284` n `68` status `ready` deltaP `12.2938` edge `0.0245` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1119` n `68` status `ready` deltaP `5.3174` edge `0.0265` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.0749` n `68` status `ready` deltaP `6.1818` edge `0.0366` maxDD `-3.1233`
- `market_context_high->fx_1h` score `0.0029` n `47` status `ready` deltaP `7.2652` edge `0.0022` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.0133` n `47` status `ready` deltaP `3.1596` edge `0.023` maxDD `-1.3282`
- `news_risk_high->fx_1h` score `-0.0357` n `68` status `ready` deltaP `3.4167` edge `0.0049` maxDD `-0.2475`
- `market_context_high->fx_24h` score `-0.0802` n `47` status `ready` deltaP `6.7369` edge `0.0428` maxDD `-2.506`
- `news_risk_high->index_1h` score `-0.1026` n `68` status `ready` deltaP `1.8669` edge `0.0067` maxDD `-0.5845`
- `news_risk_high->metal_1h` score `-0.1513` n `68` status `ready` deltaP `2.316` edge `0.0055` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2592` n `68` status `ready` deltaP `1.77` edge `0.027` maxDD `-3.762`
- `news_risk_high->commodity_1h` score `-0.6194` n `68` status `ready` deltaP `3.5664` edge `-0.0252` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
