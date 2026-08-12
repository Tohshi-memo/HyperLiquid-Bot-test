# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T18:37:30.741225+00:00`
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

- `news_risk_high->equity_4h` score `7.5597` n `34` status `ready` deltaP `40.0915` edge `0.3627` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `2.4787` n `32` status `ready` deltaP `17.1875` edge `0.3188` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.4787` n `32` status `ready` deltaP `17.1875` edge `0.3188` maxDD `-6.2481`
- `news_risk_high->index_4h` score `2.1607` n `34` status `ready` deltaP `23.4667` edge `0.0368` maxDD `-0.0546`
- `risk_on_high->commodity_4h` score `2.1442` n `32` status `ready` deltaP `14.253` edge `0.1019` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.1442` n `32` status `ready` deltaP `14.253` edge `0.1019` maxDD `-0.1258`
- `news_risk_high->equity_1h` score `1.7226` n `36` status `ready` deltaP `8.5829` edge `0.1182` maxDD `-0.5496`
- `risk_on_high->commodity_24h` score `1.7103` n `32` status `ready` deltaP `15.7986` edge `0.0372` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `1.7103` n `32` status `ready` deltaP `15.7986` edge `0.0372` maxDD `0.0`
- `risk_on_high->fx_24h` score `1.6506` n `32` status `ready` deltaP `18.4028` edge `0.0333` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.6506` n `32` status `ready` deltaP `18.4028` edge `0.0333` maxDD `-0.1418`
- `risk_on_high->commodity_1h` score `1.1173` n `32` status `ready` deltaP `12.1632` edge `0.0353` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1173` n `32` status `ready` deltaP `12.1632` edge `0.0353` maxDD `-0.1957`
- `risk_on_high->index_24h` score `0.9809` n `32` status `ready` deltaP `10.2431` edge `0.0439` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `0.9809` n `32` status `ready` deltaP `10.2431` edge `0.0439` maxDD `-0.4355`
- `risk_on_high->fx_4h` score `0.8987` n `32` status `ready` deltaP `10.2896` edge `0.0204` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8987` n `32` status `ready` deltaP `10.2896` edge `0.0204` maxDD `-0.1285`
- `risk_on_high->equity_24h` score `0.8759` n `32` status `ready` deltaP `3.125` edge `0.2694` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `0.8759` n `32` status `ready` deltaP `3.125` edge `0.2694` maxDD `-11.2348`
- `market_context_high->commodity_4h` score `0.6731` n `172` status `ready` deltaP `9.9652` edge `0.0535` maxDD `-2.1077`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
