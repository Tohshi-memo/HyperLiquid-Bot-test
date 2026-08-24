# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T02:07:20.184400+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14856`

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

- `news_risk_high->unknown_24h` score `53.1634` n `46` status `ready` deltaP `17.1875` edge `4.3157` maxDD `0.0`
- `news_risk_high->equity_24h` score `17.3371` n `46` status `ready` deltaP `48.7621` edge `1.1512` maxDD `-1.522`
- `news_risk_high->unknown_4h` score `13.0649` n `51` status `ready` deltaP `23.4965` edge `0.9367` maxDD `-0.0348`
- `news_risk_high->index_24h` score `6.6589` n `46` status `ready` deltaP `56.3255` edge `0.1884` maxDD `-0.0528`
- `risk_on_high->unknown_1h` score `3.8281` n `37` status `ready` deltaP `-10.1594` edge `0.6034` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `3.8281` n `37` status `ready` deltaP `-10.1594` edge `0.6034` maxDD `-1.5916`
- `risk_on_high->equity_4h` score `3.1449` n `37` status `ready` deltaP `4.1653` edge `0.2773` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `3.1449` n `37` status `ready` deltaP `4.1653` edge `0.2773` maxDD `-0.773`
- `news_risk_high->fx_4h` score `3.1141` n `51` status `ready` deltaP `36.7109` edge `0.0282` maxDD `-0.0746`
- `news_risk_high->crypto_alt_24h` score `3.0459` n `46` status `ready` deltaP `27.6042` edge `0.0698` maxDD `0.0`
- `news_risk_high->unknown_1h` score `2.9047` n `51` status `ready` deltaP `15.4367` edge `0.1696` maxDD `-0.7693`
- `news_risk_high->equity_4h` score `2.8829` n `51` status `ready` deltaP `23.8791` edge `0.1581` maxDD `-2.164`
- `risk_on_high->metal_4h` score `2.3649` n `37` status `ready` deltaP `30.8051` edge `0.0005` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.3649` n `37` status `ready` deltaP `30.8051` edge `0.0005` maxDD `-0.0367`
- `news_risk_high->metal_24h` score `2.1141` n `46` status `ready` deltaP `37.7567` edge `-0.0713` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `1.8088` n `145` status `ready` deltaP `21.3194` edge `0.0223` maxDD `-0.0956`
- `market_context_high->unknown_1h` score `1.7105` n `157` status `ready` deltaP `10.7908` edge `0.1155` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.2542` n `51` status `ready` deltaP `17.1451` edge `0.0072` maxDD `-0.0257`
- `risk_on_high->index_4h` score `1.1467` n `37` status `ready` deltaP `14.6012` edge `0.0462` maxDD `-0.1719`
- `risk_on_and_context->index_4h` score `1.1467` n `37` status `ready` deltaP `14.6012` edge `0.0462` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
