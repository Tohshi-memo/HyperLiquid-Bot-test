# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T05:52:13.801024+00:00`
- Price records: `672`
- Market context records: `1089`
- Flow alert records: `5039`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8786`

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

- `market_context_high->crypto_major_24h` score `16.5647` n `154` status `ready` deltaP `35.7065` edge `1.1887` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.7699` n `154` status `ready` deltaP `12.2594` edge `0.5225` maxDD `-9.5387`
- `market_context_high->equity_24h` score `5.6873` n `154` status `ready` deltaP `14.8803` edge `0.4244` maxDD `-3.6396`
- `market_context_high->metal_24h` score `4.8215` n `154` status `ready` deltaP `-2.879` edge `0.5877` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.6534` n `154` status `ready` deltaP `15.0133` edge `0.3185` maxDD `-2.1308`
- `market_context_high->equity_4h` score `2.038` n `163` status `ready` deltaP `11.0495` edge `0.1625` maxDD `-3.6396`
- `market_context_high->crypto_major_4h` score `1.0639` n `163` status `ready` deltaP `11.3647` edge `0.1815` maxDD `-6.4882`
- `market_context_high->index_4h` score `1.0244` n `163` status `ready` deltaP `8.7405` edge `0.0954` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.6435` n `172` status `ready` deltaP `8.5677` edge `0.0282` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.508` n `172` status `ready` deltaP `3.45` edge `0.0571` maxDD `-1.3546`
- `market_context_high->crypto_major_1h` score `0.1902` n `172` status `ready` deltaP `7.4885` edge `0.0425` maxDD `-4.1256`
- `market_context_high->fx_1h` score `0.0437` n `172` status `ready` deltaP `7.1717` edge `0.0014` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.1191` n `172` status `ready` deltaP `7.217` edge `0.003` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2553` n `172` status `ready` deltaP `2.8652` edge `0.0439` maxDD `-3.4088`
- `market_context_high->crypto_alt_4h` score `-0.3883` n `163` status `ready` deltaP `7.751` edge `0.1664` maxDD `-13.0347`
- `market_context_high->fx_4h` score `-0.5962` n `163` status `ready` deltaP `3.0918` edge `0.0026` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.6607` n `172` status `ready` deltaP `-0.6789` edge `0.0006` maxDD `-3.7959`
- `market_context_high->metal_4h` score `-1.7072` n `163` status `ready` deltaP `5.7357` edge `-0.0617` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-2.2118` n `163` status `ready` deltaP `9.2156` edge `-0.1241` maxDD `-6.7322`
- `market_context_high->fx_24h` score `-3.1403` n `154` status `ready` deltaP `4.2794` edge `-0.0235` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
