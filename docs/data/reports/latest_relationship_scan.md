# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T12:37:29.256113+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11792`

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

- `risk_on_high->crypto_major_24h` score `3.0509` n `32` status `ready` deltaP `21.0069` edge `0.3667` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.0509` n `32` status `ready` deltaP `21.0069` edge `0.3667` maxDD `-6.2481`
- `risk_on_high->equity_24h` score `2.7345` n `32` status `ready` deltaP `7.2917` edge `0.4799` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `2.7345` n `32` status `ready` deltaP `7.2917` edge `0.4799` maxDD `-11.2348`
- `risk_on_high->commodity_4h` score `2.3007` n `32` status `ready` deltaP `15.625` edge `0.1058` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.3007` n `32` status `ready` deltaP `15.625` edge `0.1058` maxDD `-0.1258`
- `risk_on_high->commodity_24h` score `2.1472` n `32` status `ready` deltaP `19.4444` edge `0.0493` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.1472` n `32` status `ready` deltaP `19.4444` edge `0.0493` maxDD `0.0`
- `risk_on_high->fx_24h` score `1.8062` n `32` status `ready` deltaP `20.1389` edge `0.0347` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.8062` n `32` status `ready` deltaP `20.1389` edge `0.0347` maxDD `-0.1418`
- `risk_on_high->index_24h` score `1.6707` n `32` status `ready` deltaP `14.4097` edge `0.0736` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `1.6707` n `32` status `ready` deltaP `14.4097` edge `0.0736` maxDD `-0.4355`
- `risk_on_high->commodity_1h` score `1.0909` n `32` status `ready` deltaP `12.0135` edge `0.0341` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.0909` n `32` status `ready` deltaP `12.0135` edge `0.0341` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9877` n `32` status `ready` deltaP `11.3567` edge `0.0207` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9877` n `32` status `ready` deltaP `11.3567` edge `0.0207` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.6554` n `178` status `ready` deltaP `9.5556` edge `0.0231` maxDD `-0.5752`
- `market_context_high->commodity_4h` score `0.5213` n `178` status `ready` deltaP `8.8483` edge `0.0483` maxDD `-2.1077`
- `risk_on_high->index_1h` score `0.3303` n `32` status `ready` deltaP `10.4042` edge `0.0105` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.3303` n `32` status `ready` deltaP `10.4042` edge `0.0105` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
