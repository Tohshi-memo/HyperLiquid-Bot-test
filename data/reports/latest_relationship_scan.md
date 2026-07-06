# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T15:52:34.085360+00:00`
- Price records: `672`
- Market context records: `5893`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10264`

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

- `news_risk_high->fx_4h` score `3.6705` n `30` status `ready` deltaP `38.1707` edge `0.056` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0741` n `30` status `ready` deltaP `25.1297` edge `0.0192` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9135` n `30` status `ready` deltaP `11.3872` edge `0.0879` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.8106` n `225` status `ready` deltaP `7.2412` edge `0.1293` maxDD `-4.1352`
- `news_risk_high->crypto_alt_1h` score `0.2325` n `30` status `ready` deltaP `5.02` edge `0.0425` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.2472` n `226` status `ready` deltaP `4.7613` edge `0.0292` maxDD `-4.4103`
- `market_context_high->metal_1h` score `-0.3051` n `226` status `ready` deltaP `3.357` edge `0.0056` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4647` n `30` status `ready` deltaP `0.9381` edge `-0.0292` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5688` n `226` status `ready` deltaP `-1.8799` edge `-0.0033` maxDD `-1.9006`
- `market_context_high->crypto_major_1h` score `-0.5934` n `226` status `ready` deltaP `3.3636` edge `0.0336` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.6216` n `226` status `ready` deltaP `0.253` edge `0.0034` maxDD `-0.7819`
- `market_context_high->crypto_alt_1h` score `-0.6776` n `226` status `ready` deltaP `2.3356` edge `0.031` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.8109` n `226` status `ready` deltaP `-2.6284` edge `-0.0012` maxDD `-0.5751`
- `news_risk_high->index_1h` score `-1.2603` n `30` status `ready` deltaP `-12.8443` edge `-0.0245` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.6034` n `225` status `ready` deltaP `-2.479` edge `-0.0177` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.6546` n `225` status `ready` deltaP `-2.79` edge `-0.0303` maxDD `-5.725`
- `news_risk_high->commodity_4h` score `-1.8323` n `30` status `ready` deltaP `-14.0345` edge `-0.0538` maxDD `-2.3372`
- `market_context_high->crypto_major_4h` score `-1.8746` n `225` status `ready` deltaP `8.3103` edge `0.1415` maxDD `-25.6458`
- `market_context_high->fx_24h` score `-2.0036` n `219` status `ready` deltaP `2.5542` edge `0.0079` maxDD `-5.5435`
- `market_context_high->index_4h` score `-2.0127` n `225` status `ready` deltaP `-1.3042` edge `0.0097` maxDD `-3.165`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
