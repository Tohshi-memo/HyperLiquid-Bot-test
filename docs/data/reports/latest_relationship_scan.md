# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T16:07:29.677565+00:00`
- Price records: `672`
- Market context records: `5894`
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

- `news_risk_high->fx_4h` score `3.6583` n `30` status `ready` deltaP `38.0183` edge `0.056` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0621` n `30` status `ready` deltaP `24.98` edge `0.0192` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9065` n `30` status `ready` deltaP `11.3872` edge `0.087` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.8142` n `225` status `ready` deltaP `7.2412` edge `0.1296` maxDD `-4.1352`
- `news_risk_high->crypto_alt_1h` score `0.2232` n `30` status `ready` deltaP `5.02` edge `0.0413` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.2433` n `226` status `ready` deltaP `4.7613` edge `0.0297` maxDD `-4.4103`
- `market_context_high->metal_1h` score `-0.3058` n `226` status `ready` deltaP `3.357` edge `0.0055` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4655` n `30` status `ready` deltaP `0.9381` edge `-0.0293` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5781` n `226` status `ready` deltaP `-2.0296` edge `-0.0035` maxDD `-1.9006`
- `market_context_high->crypto_major_1h` score `-0.6004` n `226` status `ready` deltaP `3.3636` edge `0.0327` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.6216` n `226` status `ready` deltaP `0.253` edge `0.0034` maxDD `-0.7819`
- `market_context_high->crypto_alt_1h` score `-0.687` n `226` status `ready` deltaP `2.3356` edge `0.0298` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.8229` n `226` status `ready` deltaP `-2.7781` edge `-0.0012` maxDD `-0.5751`
- `news_risk_high->index_1h` score `-1.2603` n `30` status `ready` deltaP `-12.8443` edge `-0.0245` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.6129` n `225` status `ready` deltaP `-2.6315` edge `-0.0179` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.6523` n `225` status `ready` deltaP `-2.79` edge `-0.03` maxDD `-5.725`
- `news_risk_high->commodity_4h` score `-1.8418` n `30` status `ready` deltaP `-14.187` edge `-0.054` maxDD `-2.3372`
- `market_context_high->crypto_major_4h` score `-1.8762` n `225` status `ready` deltaP `8.3103` edge `0.1413` maxDD `-25.6458`
- `market_context_high->fx_24h` score `-2.0051` n `219` status `ready` deltaP `2.5542` edge `0.0077` maxDD `-5.5435`
- `market_context_high->index_4h` score `-2.0127` n `225` status `ready` deltaP `-1.3042` edge `0.0097` maxDD `-3.165`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
