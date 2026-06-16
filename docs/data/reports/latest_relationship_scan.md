# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T01:52:32.569019+00:00`
- Price records: `672`
- Market context records: `4047`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10528`

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

- `risk_on_high->unknown_4h` score `144.8831` n `40` status `ready` deltaP `-8.2012` edge `12.3099` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.8831` n `40` status `ready` deltaP `-8.2012` edge `12.3099` maxDD `-10.864`
- `market_context_high->unknown_24h` score `43.7357` n `137` status `ready` deltaP `-7.89` edge `4.1001` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `22.1691` n `156` status `ready` deltaP `1.6065` edge `2.379` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `4.1468` n `40` status `ready` deltaP `34.3154` edge `0.1168` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.1468` n `40` status `ready` deltaP `34.3154` edge `0.1168` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.5614` n `40` status `ready` deltaP `37.5915` edge `0.0509` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.5614` n `40` status `ready` deltaP `37.5915` edge `0.0509` maxDD `-0.0446`
- `market_context_high->index_24h` score `2.3228` n `137` status `ready` deltaP `21.2805` edge `0.0729` maxDD `-1.3629`
- `market_context_high->equity_4h` score `1.8416` n `156` status `ready` deltaP `16.3736` edge `0.1724` maxDD `-6.9137`
- `risk_on_high->crypto_major_4h` score `1.0669` n `40` status `ready` deltaP `19.2988` edge `0.0268` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.0669` n `40` status `ready` deltaP `19.2988` edge `0.0268` maxDD `-2.6576`
- `market_context_high->equity_1h` score `0.813` n `167` status `ready` deltaP `6.1377` edge `0.0828` maxDD `-2.144`
- `market_context_high->metal_24h` score `0.6978` n `137` status `ready` deltaP `8.978` edge `0.097` maxDD `-4.8962`
- `risk_on_high->equity_1h` score `0.4651` n `40` status `ready` deltaP `11.3623` edge `0.0021` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4651` n `40` status `ready` deltaP `11.3623` edge `0.0021` maxDD `-0.7937`
- `market_context_high->crypto_major_1h` score `0.2823` n `167` status `ready` deltaP `7.7844` edge `0.0438` maxDD `-3.7739`
- `risk_on_high->commodity_24h` score `0.1802` n `40` status `ready` deltaP `0.9099` edge `0.2371` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.1802` n `40` status `ready` deltaP `0.9099` edge `0.2371` maxDD `-12.9187`
- `risk_on_high->crypto_major_1h` score `0.1725` n `40` status `ready` deltaP `12.3054` edge `-0.0057` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
