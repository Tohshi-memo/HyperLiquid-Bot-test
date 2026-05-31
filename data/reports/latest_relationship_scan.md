# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T14:52:21.899883+00:00`
- Price records: `672`
- Market context records: `2467`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9236`

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

- `news_risk_high->crypto_alt_24h` score `22.7952` n `30` status `ready` deltaP `45.625` edge `1.6543` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `22.6045` n `30` status `ready` deltaP `56.2153` edge `1.5529` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `20.9513` n `30` status `ready` deltaP `28.7848` edge `1.5855` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `14.7073` n `30` status `ready` deltaP `28.6458` edge `1.0927` maxDD `-3.3119`
- `news_risk_high->index_24h` score `9.987` n `30` status `ready` deltaP `27.5695` edge `0.6695` maxDD `-1.3507`
- `news_risk_high->unknown_24h` score `7.4711` n `30` status `ready` deltaP `23.9236` edge `0.4857` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.6485` n `116` status `ready` deltaP `22.0845` edge `0.3563` maxDD `-1.626`
- `news_risk_high->equity_4h` score `4.6342` n `30` status `ready` deltaP `-3.4553` edge `0.4658` maxDD `-2.1935`
- `market_context_high->crypto_alt_4h` score `3.9559` n `136` status `ready` deltaP `20.5882` edge `0.4603` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8803` n `136` status `ready` deltaP `18.0236` edge `0.3842` maxDD `-10.1468`
- `news_risk_high->metal_4h` score `3.8596` n `30` status `ready` deltaP `18.5162` edge `0.4335` maxDD `-2.6359`
- `news_risk_high->fx_24h` score `3.6071` n `30` status `ready` deltaP `35.0347` edge `0.0855` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `2.836` n `30` status `ready` deltaP `20.5894` edge `0.1662` maxDD `-3.0367`
- `news_risk_high->crypto_alt_4h` score `2.4308` n `30` status `ready` deltaP `10.0` edge `0.1901` maxDD `-2.3362`
- `market_context_high->crypto_major_24h` score `2.3746` n `116` status `ready` deltaP `12.5539` edge `0.61` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `1.6478` n `30` status `ready` deltaP `21.0467` edge `0.0154` maxDD `-0.1382`
- `market_context_high->unknown_4h` score `1.5915` n `136` status `ready` deltaP `10.1507` edge `0.167` maxDD `-3.4972`
- `news_risk_high->index_4h` score `1.4592` n `30` status `ready` deltaP `-2.3069` edge `0.272` maxDD `-2.2298`
- `news_risk_high->crypto_major_4h` score `1.3539` n `30` status `ready` deltaP `11.504` edge `0.1777` maxDD `-4.1319`
- `news_risk_high->unknown_1h` score `1.2498` n `30` status `ready` deltaP `16.2176` edge `0.0392` maxDD `-1.4536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
