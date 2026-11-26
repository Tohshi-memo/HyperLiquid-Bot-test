# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T13:37:29.641967+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3479`

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

- `news_risk_high->unknown_1h` score `3233.9088` n `31` status `ready` deltaP `1.9316` edge `269.4971` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3219.0451` n `31` status `ready` deltaP `3.4815` edge `268.2362` maxDD `-0.1191`
- `market_context_high->unknown_1h` score `152.8058` n `30` status `ready` deltaP `1.7165` edge `12.7318` maxDD `-0.4209`
- `news_risk_high->crypto_major_24h` score `34.7423` n `31` status `ready` deltaP `43.2292` edge `2.607` maxDD `0.0`
- `news_risk_high->equity_24h` score `34.0177` n `31` status `ready` deltaP `42.3611` edge `2.5524` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `28.802` n `31` status `ready` deltaP `42.5347` edge `2.1166` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.5989` n `31` status `ready` deltaP `26.4555` edge `0.7939` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.3602` n `31` status `ready` deltaP `38.5966` edge `0.6541` maxDD `-2.178`
- `news_risk_high->metal_24h` score `8.2853` n `31` status `ready` deltaP `28.9091` edge `0.5252` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.9071` n `31` status `ready` deltaP `19.522` edge `0.8971` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.7128` n `31` status `ready` deltaP `43.75` edge `0.1844` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.9355` n `31` status `ready` deltaP `41.5379` edge `0.1472` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7482` n `31` status `ready` deltaP `20.2868` edge `0.1958` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.423` n `31` status `ready` deltaP `37.2247` edge `0.0631` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7465` n `31` status `ready` deltaP `32.4416` edge `0.0211` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5039` n `31` status `ready` deltaP `10.0106` edge `0.3004` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2806` n `31` status `ready` deltaP `13.1543` edge `0.2404` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.208` n `30` status `ready` deltaP `27.2561` edge `0.0261` maxDD `-0.2381`
- `news_risk_high->metal_1h` score `1.4604` n `31` status `ready` deltaP `28.6845` edge `0.0239` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.9921` n `31` status `ready` deltaP `15.5586` edge `0.0792` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
