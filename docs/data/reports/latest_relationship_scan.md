# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T22:22:27.058609+00:00`
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

- `news_risk_high->equity_4h` score `7.5571` n `36` status `ready` deltaP `39.939` edge `0.3635` maxDD `0.0`
- `news_risk_high->index_4h` score `2.2749` n `36` status `ready` deltaP `25.254` edge `0.0344` maxDD `-0.0546`
- `risk_on_high->crypto_major_24h` score `2.2431` n `32` status `ready` deltaP `15.9722` edge `0.2967` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.2431` n `32` status `ready` deltaP `15.9722` edge `0.2967` maxDD `-6.2481`
- `risk_on_high->commodity_4h` score `2.1979` n `32` status `ready` deltaP `15.0152` edge `0.1013` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.1979` n `32` status `ready` deltaP `15.0152` edge `0.1013` maxDD `-0.1258`
- `risk_on_high->commodity_24h` score `1.827` n `32` status `ready` deltaP `16.4931` edge `0.0423` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `1.827` n `32` status `ready` deltaP `16.4931` edge `0.0423` maxDD `0.0`
- `news_risk_high->equity_1h` score `1.8065` n `36` status `ready` deltaP `9.3314` edge `0.1202` maxDD `-0.5496`
- `risk_on_high->fx_24h` score `1.6367` n `32` status `ready` deltaP `18.2292` edge `0.0333` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.6367` n `32` status `ready` deltaP `18.2292` edge `0.0333` maxDD `-0.1418`
- `risk_on_high->commodity_1h` score `1.1341` n `32` status `ready` deltaP `12.4626` edge `0.0347` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1341` n `32` status `ready` deltaP `12.4626` edge `0.0347` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.8853` n `32` status `ready` deltaP `10.1372` edge `0.0203` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8853` n `32` status `ready` deltaP `10.1372` edge `0.0203` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.8651` n `165` status `ready` deltaP `11.4357` edge `0.0597` maxDD `-2.1077`
- `market_context_high->commodity_1h` score `0.7216` n `165` status `ready` deltaP `9.7732` edge `0.0257` maxDD `-0.4578`
- `risk_on_high->index_24h` score `0.5446` n `32` status `ready` deltaP `7.6389` edge `0.0249` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `0.5446` n `32` status `ready` deltaP `7.6389` edge `0.0249` maxDD `-0.4355`
- `risk_on_high->index_1h` score `0.2883` n `32` status `ready` deltaP `9.8054` edge `0.0091` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
