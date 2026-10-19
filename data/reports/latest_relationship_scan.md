# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T13:37:30.394191+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8542`

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

- `market_context_high->commodity_24h` score `1.8652` n `76` status `ready` deltaP `17.5629` edge `0.1235` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.5243` n `43` status `ready` deltaP `14.0723` edge `0.0077` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.5243` n `43` status `ready` deltaP `14.0723` edge `0.0077` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.4458` n `43` status `ready` deltaP `10.1684` edge `-0.0003` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.4458` n `43` status `ready` deltaP `10.1684` edge `-0.0003` maxDD `-0.4273`
- `market_context_high->crypto_major_1h` score `0.2567` n `79` status `ready` deltaP `3.968` edge `0.0946` maxDD `-3.7178`
- `market_context_high->crypto_major_4h` score `0.1492` n `77` status `ready` deltaP `3.3873` edge `0.337` maxDD `-15.2359`
- `market_context_high->crypto_major_24h` score `0.0249` n `76` status `ready` deltaP `-0.5117` edge `0.6163` maxDD `-35.1086`
- `risk_on_high->commodity_24h` score `0.0145` n `43` status `ready` deltaP `12.9424` edge `-0.0053` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.0145` n `43` status `ready` deltaP `12.9424` edge `-0.0053` maxDD `-1.7154`
- `risk_on_high->fx_4h` score `-0.0385` n `43` status `ready` deltaP `2.4605` edge `0.0068` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0385` n `43` status `ready` deltaP `2.4605` edge `0.0068` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.2388` n `43` status `ready` deltaP `0.7123` edge `-0.0007` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2388` n `43` status `ready` deltaP `0.7123` edge `-0.0007` maxDD `-0.1065`
- `market_context_high->metal_1h` score `-0.312` n `79` status `ready` deltaP `-1.5861` edge `0.0056` maxDD `-0.4687`
- `market_context_high->fx_4h` score `-0.4957` n `77` status `ready` deltaP `-0.6504` edge `0.0045` maxDD `-0.7635`
- `risk_on_high->index_4h` score `-0.5675` n `43` status `ready` deltaP `5.3257` edge `0.0039` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.5675` n `43` status `ready` deltaP `5.3257` edge `0.0039` maxDD `-0.9359`
- `market_context_high->metal_4h` score `-0.5983` n `77` status `ready` deltaP `-0.5029` edge `0.0489` maxDD `-0.7797`
- `market_context_high->index_1h` score `-0.6622` n `79` status `ready` deltaP `2.4557` edge `-0.0048` maxDD `-1.0073`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
