# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T17:22:34.103745+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11964`

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

- `news_risk_high->unknown_24h` score `737.6976` n `136` status `ready` deltaP `1.2153` edge `61.4667` maxDD `0.0`
- `market_context_high->unknown_1h` score `212.702` n `31` status `ready` deltaP `9.4988` edge `17.6665` maxDD `-0.0395`
- `market_context_high->equity_4h` score `4.675` n `31` status `ready` deltaP `26.2736` edge `0.2479` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `3.7033` n `31` status `ready` deltaP `20.4564` edge `0.2265` maxDD `-3.3417`
- `market_context_high->index_4h` score `3.6179` n `31` status `ready` deltaP `38.6949` edge `0.0506` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `2.8186` n `31` status `ready` deltaP `16.1142` edge `0.2179` maxDD `-5.2359`
- `market_context_high->equity_1h` score `2.1241` n `31` status `ready` deltaP `22.4793` edge `0.0591` maxDD `-1.5564`
- `market_context_high->index_1h` score `1.4393` n `31` status `ready` deltaP `19.4031` edge `0.0101` maxDD `-0.2275`
- `news_risk_high->index_24h` score `1.1104` n `136` status `ready` deltaP `17.5143` edge `0.0453` maxDD `-2.2287`
- `market_context_high->metal_4h` score `1.1071` n `31` status `ready` deltaP `19.3941` edge `0.0297` maxDD `-0.3647`
- `market_context_high->fx_1h` score `0.6602` n `31` status `ready` deltaP `16.6795` edge `0.0091` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.6314` n `31` status `ready` deltaP `12.1209` edge `0.0576` maxDD `-4.8632`
- `news_risk_high->metal_24h` score `0.5818` n `136` status `ready` deltaP `16.6463` edge `0.123` maxDD `-6.8392`
- `news_risk_high->crypto_alt_24h` score `-0.0639` n `136` status `ready` deltaP `14.1237` edge `0.2957` maxDD `-29.2814`
- `news_risk_high->index_1h` score `-0.0863` n `139` status `ready` deltaP `2.7636` edge `0.0034` maxDD `-0.3214`
- `news_risk_high->crypto_alt_1h` score `-0.0917` n `139` status `ready` deltaP `4.4727` edge `0.0536` maxDD `-4.2849`
- `market_context_high->fx_4h` score `-0.135` n `31` status `ready` deltaP `6.7221` edge `0.0047` maxDD `-0.6787`
- `news_risk_high->equity_4h` score `-0.2211` n `139` status `ready` deltaP `15.4358` edge `0.0396` maxDD `-9.2079`
- `news_risk_high->equity_1h` score `-0.3024` n `139` status `ready` deltaP `2.6139` edge `0.0235` maxDD `-1.957`
- `market_context_high->metal_1h` score `-0.3679` n `31` status `ready` deltaP `-2.825` edge `0.0117` maxDD `-0.215`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
