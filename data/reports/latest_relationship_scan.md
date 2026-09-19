# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T14:22:25.954775+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8594`

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

- `news_risk_high->crypto_major_24h` score `52.62` n `72` status `ready` deltaP `31.4236` edge `4.2647` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `46.1697` n `72` status `ready` deltaP `35.9375` edge `3.7458` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `38.6608` n `141` status `ready` deltaP `-2.4066` edge `3.2611` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `10.1882` n `72` status `ready` deltaP `40.9722` edge `0.5801` maxDD `-0.0053`
- `risk_on_high->unknown_4h` score `9.534` n `51` status `ready` deltaP `-9.4154` edge `0.8798` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.534` n `51` status `ready` deltaP `-9.4154` edge `0.8798` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.4074` n `51` status `ready` deltaP `46.0069` edge `0.3939` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.4074` n `51` status `ready` deltaP `46.0069` edge `0.3939` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.1785` n `141` status `ready` deltaP `38.9147` edge `0.3913` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.6311` n `90` status `ready` deltaP `24.9492` edge `0.5072` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.5616` n `90` status `ready` deltaP `21.5718` edge `0.3621` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.2819` n `98` status `ready` deltaP `19.0731` edge `0.1929` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.618` n `51` status `ready` deltaP `30.9809` edge `0.0466` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.618` n `51` status `ready` deltaP `30.9809` edge `0.0466` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5228` n `141` status `ready` deltaP `27.3514` edge `0.0697` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.4773` n `98` status `ready` deltaP `20.8695` edge `0.1196` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.8473` n `72` status `ready` deltaP `23.7847` edge `0.0798` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.1228` n `141` status `ready` deltaP `15.6899` edge `0.0225` maxDD `-0.3491`
- `news_risk_high->metal_1h` score `0.7195` n `98` status `ready` deltaP `15.6055` edge `0.0161` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.6807` n `90` status `ready` deltaP `16.7751` edge `0.0503` maxDD `-2.0994`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
