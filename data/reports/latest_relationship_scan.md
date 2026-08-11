# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T00:22:32.835594+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->fx_24h` score `1.1169` n `145` status `ready` deltaP `20.4064` edge `0.0378` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.7785` n `172` status `ready` deltaP `10.7451` edge `0.0647` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.4998` n `180` status `ready` deltaP `7.2821` edge `0.0274` maxDD `-0.7439`
- `market_context_high->fx_1h` score `-0.027` n `180` status `ready` deltaP `6.151` edge `0.0007` maxDD `-0.613`
- `market_context_high->fx_4h` score `-0.0792` n `172` status `ready` deltaP `6.9413` edge `0.0071` maxDD `-0.4647`
- `market_context_high->index_4h` score `-1.2189` n `172` status `ready` deltaP `-7.2036` edge `-0.0178` maxDD `-1.5693`
- `market_context_high->metal_1h` score `-1.2972` n `180` status `ready` deltaP `-5.2195` edge `-0.0097` maxDD `-2.0884`
- `market_context_high->index_1h` score `-1.3422` n `180` status `ready` deltaP `-7.0758` edge `-0.0059` maxDD `-1.0359`
- `market_context_high->equity_1h` score `-1.4816` n `180` status `ready` deltaP `-6.0545` edge `-0.0219` maxDD `-6.8818`
- `market_context_high->metal_24h` score `-1.4922` n `145` status `ready` deltaP `2.5482` edge `-0.0089` maxDD `-2.9283`
- `market_context_high->index_24h` score `-1.5166` n `145` status `ready` deltaP `-6.0097` edge `0.0323` maxDD `-6.6003`
- `market_context_high->crypto_alt_1h` score `-2.9118` n `180` status `ready` deltaP `-11.5436` edge `-0.0467` maxDD `-6.5192`
- `market_context_high->metal_4h` score `-3.1885` n `172` status `ready` deltaP `-7.5334` edge `-0.0391` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.8577` n `180` status `ready` deltaP `-11.0479` edge `-0.0574` maxDD `-11.9002`
- `market_context_high->commodity_24h` score `-4.4599` n `145` status `ready` deltaP `3.6454` edge `-0.0035` maxDD `-35.4067`
- `market_context_high->equity_4h` score `-4.4611` n `172` status `ready` deltaP `-16.5343` edge `-0.1508` maxDD `-15.8728`
- `market_context_high->crypto_major_24h` score `-5.3712` n `145` status `ready` deltaP `-8.595` edge `-0.1486` maxDD `-28.6174`
- `market_context_high->equity_24h` score `-6.5578` n `145` status `ready` deltaP `-5.8543` edge `-0.0968` maxDD `-44.0594`
- `market_context_high->crypto_alt_4h` score `-7.1988` n `172` status `ready` deltaP `-15.7047` edge `-0.1604` maxDD `-20.1177`
- `market_context_high->crypto_alt_24h` score `-8.5006` n `145` status `ready` deltaP `-12.8226` edge `-0.2206` maxDD `-23.8506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
