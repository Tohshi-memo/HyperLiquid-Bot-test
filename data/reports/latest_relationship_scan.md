# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T06:37:30.366625+00:00`
- Price records: `672`
- Market context records: `8276`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5892`

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

- `news_risk_high->unknown_24h` score `6577.6329` n `50` status `ready` deltaP `39.2361` edge `547.8745` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.2549` n `54` status `ready` deltaP `26.2308` edge `0.4894` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.0378` n `54` status `ready` deltaP `21.5292` edge `0.1405` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7485` n `54` status `ready` deltaP `22.7247` edge `0.0966` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0648` n `54` status `ready` deltaP `9.8691` edge `0.2683` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7956` n `54` status `ready` deltaP `14.1051` edge `0.099` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.4987` n `54` status `ready` deltaP `10.0078` edge `0.0979` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4839` n `54` status `ready` deltaP `16.774` edge `0.2176` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.0428` n `54` status `ready` deltaP `9.4343` edge `0.0708` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.4423` n `54` status `ready` deltaP `6.6035` edge `0.0217` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1938` n `54` status `ready` deltaP `7.4462` edge `0.0033` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0964` n `54` status `ready` deltaP `3.1049` edge `0.0116` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4089` n `54` status `ready` deltaP `5.3748` edge `0.0075` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1755` n `54` status `ready` deltaP `-9.1096` edge `-0.042` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.7392` n `50` status `ready` deltaP `-19.9514` edge `-0.0492` maxDD `-5.0181`
- `news_risk_high->metal_24h` score `-5.4254` n `50` status `ready` deltaP `-17.4861` edge `-0.0609` maxDD `-10.6379`
- `news_risk_high->commodity_4h` score `-8.855` n `54` status `ready` deltaP `-31.4194` edge `-0.1977` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-12.1992` n `50` status `ready` deltaP `-25.2431` edge `-0.3239` maxDD `-27.2864`
- `news_risk_high->commodity_24h` score `-12.3733` n `50` status `ready` deltaP `-13.4444` edge `-0.3475` maxDD `-33.8515`
- `news_risk_high->crypto_major_24h` score `-34.6037` n `50` status `ready` deltaP `-16.9722` edge `-1.318` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
