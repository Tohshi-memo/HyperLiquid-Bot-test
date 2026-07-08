# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T05:07:26.313853+00:00`
- Price records: `672`
- Market context records: `6054`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11127`

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

- `news_risk_high->fx_24h` score `8.0542` n `30` status `ready` deltaP `72.2222` edge `0.1897` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2527` n `30` status `ready` deltaP `43.9634` edge `0.0659` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2705` n `30` status `ready` deltaP `27.2255` edge `0.0216` maxDD `-0.1113`
- `news_risk_high->crypto_alt_24h` score `1.9433` n `30` status `ready` deltaP `27.0139` edge `-0.0034` maxDD `-0.5131`
- `news_risk_high->commodity_24h` score `1.9217` n `30` status `ready` deltaP `23.4723` edge `0.0242` maxDD `-0.3101`
- `market_context_high->equity_4h` score `1.2827` n `206` status `ready` deltaP `7.727` edge `0.1471` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.0149` n `30` status `ready` deltaP `11.3872` edge `0.1009` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.4024` n `30` status `ready` deltaP `6.517` edge `0.0543` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1054` n `30` status `ready` deltaP `9.2361` edge `0.0391` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4796` n `206` status `ready` deltaP `2.5318` edge `0.0015` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.5161` n `30` status `ready` deltaP `0.0399` edge `-0.0298` maxDD `-1.2643`
- `market_context_high->fx_1h` score `-0.5618` n `206` status `ready` deltaP `0.0087` edge `-0.0012` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.705` n `206` status `ready` deltaP `-1.9824` edge `-0.0009` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.8028` n `206` status `ready` deltaP `4.85` edge `0.0415` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.8041` n `206` status `ready` deltaP `4.7047` edge `0.0408` maxDD `-9.3536`
- `market_context_high->index_4h` score `-1.0303` n `206` status `ready` deltaP `0.891` edge `0.0153` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-1.0329` n `30` status `ready` deltaP `-9.2515` edge `-0.0193` maxDD `-1.1161`
- `market_context_high->equity_24h` score `-1.0584` n `193` status `ready` deltaP `24.633` edge `0.4936` maxDD `-47.1479`
- `market_context_high->equity_1h` score `-1.0697` n `206` status `ready` deltaP `0.6308` edge `0.0195` maxDD `-4.3608`
- `market_context_high->commodity_4h` score `-1.1677` n `206` status `ready` deltaP `-3.5786` edge `-0.0189` maxDD `-2.5555`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
