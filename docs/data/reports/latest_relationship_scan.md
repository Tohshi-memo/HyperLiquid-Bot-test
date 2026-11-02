# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T08:37:28.479099+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4873`

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

- `market_context_high->unknown_4h` score `769.4633` n `33` status `ready` deltaP `8.8415` edge `64.063` maxDD `0.0`
- `market_context_high->unknown_1h` score `210.3279` n `33` status `ready` deltaP `6.7774` edge `17.4932` maxDD `-0.2178`
- `news_risk_high->crypto_alt_24h` score `5.9634` n `104` status `ready` deltaP `27.1902` edge `0.8749` maxDD `-19.3308`
- `market_context_high->crypto_alt_4h` score `5.2797` n `33` status `ready` deltaP `23.9099` edge `0.31` maxDD `-1.6876`
- `market_context_high->equity_4h` score `5.1998` n `33` status `ready` deltaP `6.9476` edge `0.4572` maxDD `-2.283`
- `market_context_high->crypto_major_4h` score `4.0897` n `33` status `ready` deltaP `21.0505` edge `0.2341` maxDD `-1.6901`
- `market_context_high->equity_1h` score `3.2887` n `33` status `ready` deltaP `10.4564` edge `0.2444` maxDD `-1.2043`
- `news_risk_high->crypto_alt_4h` score `2.6172` n `127` status `ready` deltaP `10.4763` edge `0.2869` maxDD `-7.4246`
- `market_context_high->index_4h` score `2.5147` n `33` status `ready` deltaP `24.2147` edge `0.0708` maxDD `-0.1474`
- `market_context_high->crypto_major_1h` score `1.9246` n `33` status `ready` deltaP `10.4564` edge `0.1297` maxDD `-1.1219`
- `market_context_high->crypto_alt_1h` score `1.1688` n `33` status `ready` deltaP `8.3243` edge `0.1385` maxDD `-1.5324`
- `market_context_high->fx_1h` score `0.9968` n `33` status `ready` deltaP `13.1873` edge `0.0123` maxDD `-0.0388`
- `market_context_high->commodity_4h` score `0.9284` n `33` status `ready` deltaP `19.1057` edge `0.0329` maxDD `-1.633`
- `market_context_high->metal_4h` score `0.6942` n `33` status `ready` deltaP `13.0636` edge `0.0444` maxDD `-0.7323`
- `market_context_high->index_1h` score `0.3996` n `33` status `ready` deltaP `3.6473` edge `0.0331` maxDD `-0.2628`
- `market_context_high->metal_1h` score `0.2156` n `33` status `ready` deltaP `5.7068` edge `0.0153` maxDD `-0.3895`
- `news_risk_high->crypto_alt_1h` score `-0.3038` n `138` status `ready` deltaP `2.1978` edge `0.0537` maxDD `-4.584`
- `market_context_high->commodity_1h` score `-0.4735` n `33` status `ready` deltaP `-3.1982` edge `0.0145` maxDD `-0.6439`
- `market_context_high->fx_4h` score `-0.4985` n `33` status `ready` deltaP `-2.7347` edge `0.0158` maxDD `-0.1285`
- `news_risk_high->fx_1h` score `-0.5957` n `138` status `ready` deltaP `-0.4491` edge `-0.0033` maxDD `-0.6065`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
