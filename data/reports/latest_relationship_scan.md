# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T01:37:14.418899+00:00`
- Price records: `672`
- Market context records: `1377`
- Flow alert records: `5876`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.3805` n `149` status `ready` deltaP `30.5451` edge `1.0246` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.0821` n `149` status `ready` deltaP `13.4193` edge `1.0841` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.1445` n `149` status `ready` deltaP `28.7158` edge `0.9389` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.2048` n `149` status `ready` deltaP `21.6804` edge `0.3145` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7428` n `149` status `ready` deltaP `14.7825` edge `0.3627` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5823` n `174` status `ready` deltaP `8.9185` edge `0.1554` maxDD `-3.6396`
- `market_context_high->metal_4h` score `-0.0236` n `174` status `ready` deltaP `11.3891` edge `0.0652` maxDD `-6.4478`
- `market_context_high->fx_24h` score `-0.0674` n `149` status `ready` deltaP `8.444` edge `0.043` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0791` n `186` status `ready` deltaP `3.7377` edge `0.015` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.0819` n `186` status `ready` deltaP `2.6287` edge `0.0315` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.3608` n `174` status `ready` deltaP `0.5905` edge `0.0587` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.3776` n `186` status `ready` deltaP `2.6544` edge `-0.0026` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.5655` n `186` status `ready` deltaP `6.5611` edge `0.008` maxDD `-3.5762`
- `market_context_high->crypto_alt_1h` score `-0.6546` n `186` status `ready` deltaP `0.5859` edge `0.0286` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.7282` n `186` status `ready` deltaP `-0.5103` edge `0.0042` maxDD `-2.252`
- `market_context_high->crypto_major_1h` score `-1.3683` n `186` status `ready` deltaP `-1.5308` edge `0.0027` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.465` n `174` status `ready` deltaP `7.6605` edge `0.1588` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.5878` n `174` status `ready` deltaP `3.8355` edge `0.113` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.966` n `174` status `ready` deltaP `-7.9163` edge `-0.014` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.2588` n `174` status `ready` deltaP `2.884` edge `-0.2099` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
