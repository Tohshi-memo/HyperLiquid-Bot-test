# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T03:37:21.077310+00:00`
- Price records: `672`
- Market context records: `3140`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7126`

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

- `market_context_high->commodity_24h` score `14.4682` n `106` status `ready` deltaP `48.1066` edge `0.9278` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `12.0059` n `106` status `ready` deltaP `21.4786` edge `0.9061` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `10.7285` n `106` status `ready` deltaP `10.0727` edge `2.3059` maxDD `-71.142`
- `market_context_high->index_24h` score `6.4161` n `106` status `ready` deltaP `30.5293` edge `0.8745` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.2475` n `106` status `ready` deltaP `10.8556` edge `1.3138` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.8722` n `143` status `ready` deltaP `18.8172` edge `0.1597` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.1498` n `146` status `ready` deltaP `4.1322` edge `0.0272` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.3954` n `146` status `ready` deltaP `6.0557` edge `0.1219` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.4645` n `106` status `ready` deltaP `5.3328` edge `-0.0015` maxDD `-0.4876`
- `market_context_high->index_1h` score `-0.5039` n `146` status `ready` deltaP `3.7015` edge `0.017` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.8145` n `146` status `ready` deltaP `3.4882` edge `0.0209` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-0.9585` n `146` status `ready` deltaP `3.3754` edge `0.0809` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.1197` n `146` status `ready` deltaP `-10.4688` edge `-0.0055` maxDD `-0.7941`
- `market_context_high->index_4h` score `-1.1783` n `143` status `ready` deltaP `11.6909` edge `0.0619` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.51` n `143` status `ready` deltaP `-14.4785` edge `-0.0086` maxDD `-1.411`
- `market_context_high->unknown_4h` score `-1.8658` n `143` status `ready` deltaP `5.2256` edge `0.0319` maxDD `-14.7778`
- `market_context_high->metal_1h` score `-2.054` n `146` status `ready` deltaP `-4.1547` edge `-0.0041` maxDD `-7.4828`
- `market_context_high->equity_4h` score `-2.8983` n `143` status `ready` deltaP `13.1524` edge `0.0713` maxDD `-36.7784`
- `market_context_high->crypto_alt_4h` score `-3.0089` n `143` status `ready` deltaP `19.2958` edge `0.4251` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.1189` n `146` status `ready` deltaP `1.9092` edge `-0.07` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
