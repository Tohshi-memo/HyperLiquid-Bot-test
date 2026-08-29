# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T09:37:27.868895+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11772`

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

- `news_risk_high->unknown_24h` score `49.0586` n `56` status `ready` deltaP `13.0704` edge `4.0556` maxDD `-2.3617`
- `news_risk_high->crypto_alt_24h` score `24.136` n `56` status `ready` deltaP `36.2351` edge `1.9904` maxDD `-14.9839`
- `market_context_high->unknown_24h` score `8.2591` n `116` status `ready` deltaP `16.8881` edge `0.6489` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.2577` n `80` status `ready` deltaP `10.8232` edge `0.5083` maxDD `-1.7183`
- `market_context_high->metal_24h` score `3.7702` n `116` status `ready` deltaP `30.6753` edge `0.2116` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.6787` n `80` status `ready` deltaP `5.6737` edge `0.2211` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.6763` n `116` status `ready` deltaP `19.4439` edge `0.1341` maxDD `-0.5894`
- `news_risk_high->equity_24h` score `2.3994` n `56` status `ready` deltaP `22.0486` edge `0.3498` maxDD `-12.4677`
- `news_risk_high->fx_4h` score `2.3425` n `80` status `ready` deltaP `34.2073` edge `0.0221` maxDD `-0.3953`
- `news_risk_high->crypto_major_24h` score `1.9367` n `56` status `ready` deltaP `19.2708` edge `0.3597` maxDD `-16.524`
- `news_risk_high->metal_24h` score `1.5498` n `56` status `ready` deltaP `35.4167` edge `0.034` maxDD `-3.7137`
- `news_risk_high->index_24h` score `1.254` n `56` status `ready` deltaP `18.3283` edge `0.0243` maxDD `-1.0255`
- `market_context_high->unknown_1h` score `1.1019` n `119` status `ready` deltaP `8.7619` edge `0.0826` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6752` n `80` status `ready` deltaP `13.4431` edge `0.0055` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4657` n `80` status `ready` deltaP `12.9491` edge `0.0054` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.1974` n `116` status `ready` deltaP `8.5524` edge `0.0094` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.3988` n `80` status `ready` deltaP `0.1572` edge `-0.0085` maxDD `-0.8275`
- `news_risk_high->index_4h` score `-0.5531` n `80` status `ready` deltaP `1.4634` edge `-0.0165` maxDD `-1.7996`
- `news_risk_high->commodity_4h` score `-0.5799` n `80` status `ready` deltaP `7.3476` edge `0.0108` maxDD `-2.0635`
- `news_risk_high->equity_1h` score `-0.5976` n `80` status `ready` deltaP `8.4581` edge `-0.0396` maxDD `-5.1385`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
