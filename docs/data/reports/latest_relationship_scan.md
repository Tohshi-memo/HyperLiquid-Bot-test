# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T05:37:28.892873+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3680`

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

- `news_risk_high->unknown_1h` score `3340.6165` n `31` status `ready` deltaP `1.4825` edge `278.3924` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3203.3001` n `31` status `ready` deltaP `3.634` edge `266.9231` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `19.461` n `31` status `ready` deltaP `30.5026` edge `1.4184` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.5214` n `31` status `ready` deltaP `28.4229` edge `0.9373` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.5051` n `31` status `ready` deltaP `24.2634` edge `0.797` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.4849` n `31` status `ready` deltaP `19.9006` edge `0.5781` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.057` n `31` status `ready` deltaP `27.9259` edge `0.2833` maxDD `-2.178`
- `news_risk_high->fx_24h` score `4.745` n `31` status `ready` deltaP `38.6762` edge `0.1504` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `4.624` n `31` status `ready` deltaP `13.8818` edge `0.642` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `3.3934` n `31` status `ready` deltaP `12.5343` edge `0.2267` maxDD `-0.1986`
- `news_risk_high->index_1h` score `2.2445` n `31` status `ready` deltaP `27.6512` edge `0.0112` maxDD `-0.0136`
- `news_risk_high->index_24h` score `2.2047` n `31` status `ready` deltaP `24.7834` edge `0.0185` maxDD `0.0`
- `news_risk_high->index_4h` score `2.2007` n `31` status `ready` deltaP `27.3161` edge `0.0273` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.0512` n `31` status `ready` deltaP `13.9994` edge `0.0963` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.6527` n `31` status `ready` deltaP `5.0705` edge `0.2242` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.5581` n `31` status `ready` deltaP `8.3639` edge `0.1797` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.085` n `31` status `ready` deltaP `23.8941` edge `0.0077` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3096` n `31` status `ready` deltaP `8.0645` edge `0.0257` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.2355` n `31` status `ready` deltaP `9.9183` edge `0.0198` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3495` n `31` status `ready` deltaP `-2.2117` edge `0.0118` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
