# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T08:22:31.070493+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3728`

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

- `news_risk_high->unknown_1h` score `3359.3749` n `31` status `ready` deltaP `1.6322` edge `279.9546` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3235.8969` n `31` status `ready` deltaP `3.634` edge `269.6395` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `20.9335` n `31` status `ready` deltaP `32.409` edge `1.5284` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.8679` n `31` status `ready` deltaP `30.3293` edge `1.0368` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.8999` n `31` status `ready` deltaP `25.8232` edge `0.8195` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.0745` n `31` status `ready` deltaP `21.1201` edge `0.6191` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.2469` n `31` status `ready` deltaP `29.1454` edge `0.291` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.9752` n `31` status `ready` deltaP `15.1013` edge `0.6789` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.8768` n `31` status `ready` deltaP `39.8893` edge `0.1533` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.6076` n `31` status `ready` deltaP `14.2674` edge `0.233` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.3103` n `31` status `ready` deltaP `28.5356` edge `0.0283` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.2715` n `31` status `ready` deltaP `25.3033` edge `0.0206` maxDD `0.0`
- `news_risk_high->index_1h` score `2.2624` n `31` status `ready` deltaP `27.8009` edge `0.0117` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.0885` n `31` status `ready` deltaP `13.8497` edge `0.1004` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.7899` n `31` status `ready` deltaP `5.3699` edge `0.2398` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6408` n `31` status `ready` deltaP `8.3639` edge `0.1903` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.0974` n `31` status `ready` deltaP `24.0438` edge `0.0083` maxDD `-0.2315`
- `market_context_high->equity_1h` score `0.4958` n `38` status `ready` deltaP `11.8973` edge `0.0251` maxDD `-1.2685`
- `news_risk_high->commodity_4h` score `0.3247` n `31` status `ready` deltaP `8.3694` edge `0.0256` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3122` n `31` status `ready` deltaP `11.1379` edge `0.0215` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
