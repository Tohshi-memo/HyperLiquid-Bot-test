# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T13:37:41.815233+00:00`
- Price records: `672`
- Market context records: `4096`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10376`

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

- `risk_on_high->unknown_4h` score `144.6615` n `40` status `ready` deltaP `-8.811` edge `12.2955` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.6615` n `40` status `ready` deltaP `-8.811` edge `12.2955` maxDD `-10.864`
- `market_context_high->unknown_1h` score `47.6849` n `179` status `ready` deltaP `2.1603` edge `4.1171` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.0505` n `144` status `ready` deltaP `-9.2396` edge `3.552` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `15.8265` n `176` status `ready` deltaP `-2.1065` edge `1.8752` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `2.7309` n `40` status `ready` deltaP `36.5244` edge `-0.0112` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `2.7309` n `40` status `ready` deltaP `36.5244` edge `-0.0112` maxDD `-0.0446`
- `market_context_high->equity_1h` score `0.6101` n `179` status `ready` deltaP `5.1651` edge `0.0731` maxDD `-2.2022`
- `risk_on_high->equity_1h` score `0.4808` n `40` status `ready` deltaP `11.2126` edge `0.0044` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4808` n `40` status `ready` deltaP `11.2126` edge `0.0044` maxDD `-0.7937`
- `risk_on_high->fx_4h` score `0.1547` n `40` status `ready` deltaP `11.311` edge `0.0035` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.1547` n `40` status `ready` deltaP `11.311` edge `0.0035` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0747` n `40` status `ready` deltaP `4.7006` edge `0.0012` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0747` n `40` status `ready` deltaP `4.7006` edge `0.0012` maxDD `-0.1704`
- `market_context_high->equity_4h` score `-0.0029` n `176` status `ready` deltaP `11.7517` edge `0.0745` maxDD `-6.9137`
- `risk_on_high->crypto_major_1h` score `-0.0121` n `40` status `ready` deltaP `10.509` edge `-0.0174` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `-0.0121` n `40` status `ready` deltaP `10.509` edge `-0.0174` maxDD `-2.3372`
- `market_context_high->index_24h` score `-0.1208` n `144` status `ready` deltaP `13.8648` edge `-0.1025` maxDD `0.0`
- `market_context_high->metal_1h` score `-0.1632` n `179` status `ready` deltaP `7.4725` edge `0.0322` maxDD `-4.9015`
- `risk_on_high->crypto_major_4h` score `-0.1686` n `40` status `ready` deltaP `15.9451` edge `-0.0538` maxDD `-2.6576`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
