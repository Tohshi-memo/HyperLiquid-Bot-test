# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T15:52:59.911438+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `46.8207` n `51` status `ready` deltaP `14.5833` edge `3.8045` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.5523` n `51` status `ready` deltaP `40.237` edge `0.9542` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.8833` n `51` status `ready` deltaP `24.1063` edge `0.9175` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.5072` n `51` status `ready` deltaP `48.9481` edge `0.1478` maxDD `-0.2147`
- `market_context_high->unknown_24h` score `4.8612` n `82` status `ready` deltaP `8.4857` edge `0.3778` maxDD `-0.6752`
- `news_risk_high->equity_4h` score `4.1158` n `51` status `ready` deltaP `27.995` edge `0.2334` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5814` n `51` status `ready` deltaP `16.3349` edge `0.22` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.3138` n `51` status `ready` deltaP `38.9975` edge `0.0296` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.6788` n `130` status `ready` deltaP `19.144` edge `0.0531` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2566` n `51` status `ready` deltaP `17.1451` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->index_4h` score `1.0795` n `51` status `ready` deltaP `15.0735` edge `0.0292` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `1.0535` n `51` status `ready` deltaP `19.0912` edge `0.0442` maxDD `-0.9128`
- `news_risk_high->metal_24h` score `0.8993` n `51` status `ready` deltaP `28.4211` edge `-0.1103` maxDD `-0.0053`
- `news_risk_high->index_1h` score `0.2691` n `51` status `ready` deltaP `9.572` edge `0.006` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.2039` n `51` status `ready` deltaP `8.5388` edge `-0.0091` maxDD `-0.4666`
- `market_context_high->metal_4h` score `0.1621` n `130` status `ready` deltaP `11.3251` edge `-0.0161` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.0385` n `130` status `ready` deltaP `10.9051` edge `-0.0246` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1177` n `51` status `ready` deltaP `2.1927` edge `-0.0074` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.2639` n `51` status `ready` deltaP `6.4533` edge `-0.0119` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.424` n `130` status `ready` deltaP `2.7107` edge `0.0008` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
