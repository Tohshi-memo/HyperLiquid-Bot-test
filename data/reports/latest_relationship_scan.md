# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T09:37:27.949265+00:00`
- Price records: `672`
- Market context records: `3165`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8854`

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

- `market_context_high->commodity_24h` score `13.7575` n `101` status `ready` deltaP `47.2171` edge `0.8745` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.0021` n `101` status `ready` deltaP `15.8004` edge `2.431` maxDD `-71.142`
- `market_context_high->unknown_24h` score `11.7348` n `101` status `ready` deltaP `20.2643` edge `0.8916` maxDD `-1.9039`
- `market_context_high->index_24h` score `6.2054` n `101` status `ready` deltaP `29.2216` edge `0.8562` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.7755` n `101` status `ready` deltaP `14.3651` edge `1.3581` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.979` n `134` status `ready` deltaP `18.593` edge `0.1701` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.8254` n `101` status `ready` deltaP `13.2219` edge `0.0034` maxDD `-0.4876`
- `market_context_high->commodity_1h` score `0.2087` n `134` status `ready` deltaP `4.3279` edge `0.0308` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.3318` n `134` status `ready` deltaP `11.0506` edge `0.1209` maxDD `-14.7778`
- `market_context_high->crypto_alt_1h` score `-0.3966` n `134` status `ready` deltaP `6.1221` edge `0.1213` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.4161` n `134` status `ready` deltaP `5.3758` edge `0.0171` maxDD `-4.5023`
- `market_context_high->index_4h` score `-0.9656` n `134` status `ready` deltaP `15.1665` edge `0.066` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0443` n `134` status `ready` deltaP `3.1504` edge `0.0714` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.0693` n `134` status `ready` deltaP `-9.5451` edge `-0.0052` maxDD `-0.7941`
- `market_context_high->equity_1h` score `-1.3333` n `134` status `ready` deltaP `3.881` edge `0.0116` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.356` n `134` status `ready` deltaP `-11.7401` edge `-0.0071` maxDD `-1.4115`
- `market_context_high->metal_1h` score `-2.0787` n `134` status `ready` deltaP `-3.7291` edge `-0.009` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.0878` n `134` status `ready` deltaP `18.4224` edge `0.414` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-2.9295` n `134` status `ready` deltaP `2.9717` edge `-0.0613` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.5499` n `134` status `ready` deltaP `11.5126` edge `0.2605` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
