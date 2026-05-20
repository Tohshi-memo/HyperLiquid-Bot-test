# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T01:37:20.833854+00:00`
- Price records: `672`
- Market context records: `1275`
- Flow alert records: `5579`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8820`

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

- `market_context_high->crypto_major_24h` score `17.9821` n `128` status `ready` deltaP `41.5798` edge `1.3345` maxDD `-8.0553`
- `market_context_high->metal_24h` score `10.6597` n `128` status `ready` deltaP `6.4236` edge `1.0122` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `8.8517` n `128` status `ready` deltaP `25.7812` edge `0.7674` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `6.1541` n `133` status `ready` deltaP `5.2643` edge `0.5994` maxDD `-6.7322`
- `market_context_high->index_24h` score `5.2648` n `128` status `ready` deltaP `27.4306` edge `0.3645` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.9054` n `128` status `ready` deltaP `25.3472` edge `0.5644` maxDD `-14.2815`
- `market_context_high->equity_4h` score `3.3934` n `133` status `ready` deltaP `17.1167` edge `0.235` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.3778` n `128` status `ready` deltaP `1.5625` edge `0.4607` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.7081` n `128` status `ready` deltaP `-12.6736` edge `0.375` maxDD `-6.8535`
- `market_context_high->index_4h` score `1.6483` n `133` status `ready` deltaP `12.7889` edge `0.1204` maxDD `-2.1308`
- `market_context_high->metal_4h` score `0.888` n `133` status `ready` deltaP `18.0749` edge `0.0966` maxDD `-6.4478`
- `market_context_high->metal_1h` score `0.4939` n `145` status `ready` deltaP `12.165` edge `0.0211` maxDD `-2.2164`
- `market_context_high->index_1h` score `0.4811` n `145` status `ready` deltaP `8.0963` edge `0.0231` maxDD `-0.9584`
- `market_context_high->equity_1h` score `0.4307` n `145` status `ready` deltaP `4.9206` edge `0.0458` maxDD `-1.7505`
- `market_context_high->fx_24h` score `0.1373` n `128` status `ready` deltaP `4.0799` edge `0.0307` maxDD `-0.3831`
- `market_context_high->crypto_major_4h` score `-0.0759` n `133` status `ready` deltaP `7.5405` edge `0.166` maxDD `-11.0798`
- `market_context_high->crypto_alt_1h` score `-0.3458` n `145` status `ready` deltaP `0.8579` edge `0.037` maxDD `-3.6309`
- `market_context_high->fx_1h` score `-0.4482` n `145` status `ready` deltaP `1.6385` edge `-0.0027` maxDD `-0.3124`
- `market_context_high->crypto_alt_4h` score `-0.7179` n `133` status `ready` deltaP `8.1584` edge `0.1817` maxDD `-19.2499`
- `market_context_high->crypto_major_1h` score `-0.7323` n `145` status `ready` deltaP `0.5534` edge `0.0045` maxDD `-5.8323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
