# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T09:37:13.727450+00:00`
- Price records: `634`
- Market context records: `741`
- Flow alert records: `2093`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1117`

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

- `market_context_high->crypto_major_24h` score `12.6974` n `146` status `ready` deltaP `30.2566` edge `0.8898` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5963` n `146` status `ready` deltaP `7.6794` edge `0.5033` maxDD `-0.0508`
- `market_context_high->index_24h` score `0.1491` n `146` status `ready` deltaP `1.5058` edge `0.2019` maxDD `-5.9609`
- `market_context_high->fx_4h` score `-0.2909` n `155` status `ready` deltaP `6.0975` edge `0.0092` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3585` n `160` status `ready` deltaP `3.7839` edge `0.0027` maxDD `-0.291`
- `market_context_high->equity_24h` score `-0.539` n `146` status `ready` deltaP `-0.1257` edge `0.2164` maxDD `-10.5047`
- `market_context_high->commodity_1h` score `-0.6175` n `160` status `ready` deltaP `1.3339` edge `0.0371` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.8356` n `160` status `ready` deltaP `1.6374` edge `0.0048` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-0.9732` n `160` status `ready` deltaP `-0.2796` edge `0.0018` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.0534` n `160` status `ready` deltaP `5.9028` edge `-0.0021` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.4156` n `160` status `ready` deltaP `4.3948` edge `-0.0158` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.5185` n `160` status `ready` deltaP `-4.256` edge `-0.021` maxDD `-3.5069`
- `market_context_high->crypto_major_4h` score `-1.5652` n `155` status `ready` deltaP `17.41` edge `0.1241` maxDD `-22.648`
- `market_context_high->index_4h` score `-1.775` n `155` status `ready` deltaP `1.6434` edge `-0.0066` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.1724` n `155` status `ready` deltaP `2.3614` edge `0.0602` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.5967` n `155` status `ready` deltaP `-1.2882` edge `0.0074` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.1068` n `160` status `ready` deltaP `-3.7004` edge `-0.0383` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7026` n `155` status `ready` deltaP `-5.7088` edge `0.0796` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.7783` n `155` status `ready` deltaP `4.9734` edge `-0.1602` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.3659` n `146` status `ready` deltaP `-15.4277` edge `-0.0679` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
