# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T21:22:27.673359+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11824`

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

- `news_risk_high->equity_4h` score `7.5559` n `36` status `ready` deltaP `39.939` edge `0.3634` maxDD `0.0`
- `news_risk_high->index_4h` score `2.3151` n `36` status `ready` deltaP `25.7113` edge `0.0347` maxDD `-0.0546`
- `risk_on_high->crypto_major_24h` score `2.2603` n `32` status `ready` deltaP `15.9722` edge `0.2989` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.2603` n `32` status `ready` deltaP `15.9722` edge `0.2989` maxDD `-6.2481`
- `risk_on_high->commodity_4h` score `2.1712` n `32` status `ready` deltaP `14.7104` edge `0.1011` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.1712` n `32` status `ready` deltaP `14.7104` edge `0.1011` maxDD `-0.1258`
- `news_risk_high->equity_1h` score `1.7909` n `36` status `ready` deltaP `9.1817` edge `0.1199` maxDD `-0.5496`
- `risk_on_high->commodity_24h` score `1.7609` n `32` status `ready` deltaP `16.1458` edge `0.0391` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `1.7609` n `32` status `ready` deltaP `16.1458` edge `0.0391` maxDD `0.0`
- `risk_on_high->fx_24h` score `1.6355` n `32` status `ready` deltaP `18.2292` edge `0.0332` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.6355` n `32` status `ready` deltaP `18.2292` edge `0.0332` maxDD `-0.1418`
- `risk_on_high->commodity_1h` score `1.1317` n `32` status `ready` deltaP `12.4626` edge `0.0345` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1317` n `32` status `ready` deltaP `12.4626` edge `0.0345` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.8597` n `32` status `ready` deltaP `9.8323` edge `0.0202` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8597` n `32` status `ready` deltaP `9.8323` edge `0.0202` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.8019` n `168` status `ready` deltaP `10.9902` edge `0.0574` maxDD `-2.1077`
- `market_context_high->commodity_1h` score `0.7108` n `168` status `ready` deltaP `9.784` edge `0.0262` maxDD `-0.5752`
- `risk_on_high->index_24h` score `0.6541` n `32` status `ready` deltaP `8.3333` edge `0.0294` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `0.6541` n `32` status `ready` deltaP `8.3333` edge `0.0294` maxDD `-0.4355`
- `risk_on_high->index_1h` score `0.2968` n `32` status `ready` deltaP `9.9551` edge `0.0092` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
