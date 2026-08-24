# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T20:22:28.249620+00:00`
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

- `news_risk_high->unknown_24h` score `45.3827` n `51` status `ready` deltaP `11.4583` edge `3.7055` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.8351` n `51` status `ready` deltaP `23.9538` edge `0.9145` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `12.8251` n `51` status `ready` deltaP `40.237` edge `0.8936` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.3572` n `51` status `ready` deltaP `48.9481` edge `0.1353` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.9478` n `51` status `ready` deltaP `27.0804` edge `0.2255` maxDD `-2.164`
- `market_context_high->unknown_24h` score `3.6449` n `99` status `ready` deltaP `6.4078` edge `0.2903` maxDD `-0.6752`
- `news_risk_high->unknown_1h` score `3.6053` n `51` status `ready` deltaP `16.784` edge `0.219` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.3796` n `51` status `ready` deltaP `39.7597` edge `0.03` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.6306` n `130` status `ready` deltaP `18.9915` edge `0.0501` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2829` n `51` status `ready` deltaP `17.4445` edge `0.0076` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9982` n `51` status `ready` deltaP `18.4924` edge `0.0411` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9725` n `51` status `ready` deltaP `14.0064` edge `0.0274` maxDD `-0.1788`
- `news_risk_high->metal_24h` score `0.3668` n `51` status `ready` deltaP `25.4698` edge `-0.135` maxDD `-0.0053`
- `news_risk_high->commodity_1h` score `0.3237` n `51` status `ready` deltaP `9.5867` edge `-0.0061` maxDD `-0.4666`
- `market_context_high->metal_4h` score `0.2445` n `130` status `ready` deltaP `11.9348` edge `-0.0133` maxDD `-1.3378`
- `news_risk_high->index_1h` score `0.1998` n `51` status `ready` deltaP `8.3744` edge `0.0051` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `0.0624` n `130` status `ready` deltaP `11.3542` edge `-0.0256` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1458` n `51` status `ready` deltaP `1.5939` edge `-0.007` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1815` n `51` status `ready` deltaP `7.063` edge `-0.0091` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4069` n `130` status `ready` deltaP `3.0101` edge `0.001` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
