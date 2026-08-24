# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T11:51:03.057631+00:00`
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

- `news_risk_high->unknown_24h` score `48.3231` n `51` status `ready` deltaP `17.0139` edge `3.9135` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.8583` n `51` status `ready` deltaP `40.237` edge `0.9797` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `13.1475` n `51` status `ready` deltaP `24.2587` edge `0.9385` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.614` n `51` status `ready` deltaP `48.9481` edge `0.1567` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.7205` n `51` status `ready` deltaP `17.0834` edge `0.2266` maxDD `-0.7693`
- `news_risk_high->equity_4h` score `3.7096` n `51` status `ready` deltaP `26.623` edge `0.2087` maxDD `-2.164`
- `news_risk_high->fx_4h` score `3.2358` n `51` status `ready` deltaP `38.0829` edge `0.0292` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.7193` n `137` status `ready` deltaP `19.6502` edge `0.0531` maxDD `-0.5994`
- `market_context_high->unknown_24h` score `1.5363` n `81` status `ready` deltaP `3.4337` edge `0.1558` maxDD `-1.0533`
- `news_risk_high->metal_24h` score `1.3339` n `51` status `ready` deltaP `31.1989` edge `-0.0926` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.2194` n `51` status `ready` deltaP `16.696` edge `0.0073` maxDD `-0.0257`
- `news_risk_high->index_4h` score `0.9751` n `51` status `ready` deltaP `14.1589` edge `0.0266` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `0.9475` n `51` status `ready` deltaP `18.3427` edge `0.0356` maxDD `-0.9128`
- `market_context_high->metal_4h` score `0.3189` n `137` status `ready` deltaP `12.234` edge `-0.0091` maxDD `-1.3378`
- `news_risk_high->index_1h` score `0.2348` n `51` status `ready` deltaP `9.1229` edge `0.0046` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1476` n `51` status `ready` deltaP `8.0897` edge `-0.0108` maxDD `-0.4666`
- `market_context_high->unknown_1h` score `0.0315` n `137` status `ready` deltaP `11.3728` edge `-0.0283` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1185` n `51` status `ready` deltaP `2.1927` edge `-0.0075` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1571` n `51` status `ready` deltaP `7.3679` edge `-0.0091` maxDD `-0.249`
- `market_context_high->metal_1h` score `-0.3894` n `137` status `ready` deltaP `-1.1135` edge `-0.0048` maxDD `-0.6822`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
