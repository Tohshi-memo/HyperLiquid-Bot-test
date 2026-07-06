# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T16:52:26.584279+00:00`
- Price records: `672`
- Market context records: `5897`
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

- `news_risk_high->fx_4h` score `3.6181` n `30` status `ready` deltaP `37.561` edge `0.0557` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.025` n `30` status `ready` deltaP `24.5309` edge `0.0191` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9291` n `30` status `ready` deltaP `11.3872` edge `0.0899` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.8683` n `226` status `ready` deltaP `7.3926` edge `0.1331` maxDD `-4.1352`
- `news_risk_high->crypto_alt_1h` score `0.224` n `30` status `ready` deltaP `5.02` edge `0.0414` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.2316` n `226` status `ready` deltaP `4.7613` edge `0.0312` maxDD `-4.4103`
- `market_context_high->metal_1h` score `-0.2949` n `226` status `ready` deltaP `3.5067` edge `0.0059` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4546` n `30` status `ready` deltaP `1.0878` edge `-0.0289` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5579` n `226` status `ready` deltaP `-1.7302` edge `-0.0029` maxDD `-1.9006`
- `market_context_high->crypto_major_1h` score `-0.5778` n `226` status `ready` deltaP `3.3636` edge `0.0356` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.6208` n `226` status `ready` deltaP `0.253` edge `0.0035` maxDD `-0.7819`
- `market_context_high->crypto_alt_1h` score `-0.6862` n `226` status `ready` deltaP `2.3356` edge `0.0299` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.86` n `226` status `ready` deltaP `-3.2272` edge `-0.0013` maxDD `-0.5751`
- `news_risk_high->index_1h` score `-1.2595` n `30` status `ready` deltaP `-12.8443` edge `-0.0244` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.6248` n `226` status `ready` deltaP `-2.8154` edge `-0.0182` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.6465` n `226` status `ready` deltaP `-2.725` edge `-0.0297` maxDD `-5.725`
- `market_context_high->crypto_major_4h` score `-1.8218` n `226` status `ready` deltaP `8.4854` edge `0.1471` maxDD `-25.6458`
- `news_risk_high->commodity_4h` score `-1.8718` n `30` status `ready` deltaP `-14.6443` edge `-0.0548` maxDD `-2.3372`
- `market_context_high->index_4h` score `-1.9922` n `226` status `ready` deltaP `-1.1076` edge `0.0101` maxDD `-3.165`
- `market_context_high->fx_24h` score `-2.0082` n `219` status `ready` deltaP `2.5542` edge `0.0073` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
