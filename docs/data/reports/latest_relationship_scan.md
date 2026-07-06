# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T16:37:32.952043+00:00`
- Price records: `672`
- Market context records: `5896`
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

- `news_risk_high->fx_4h` score `3.6315` n `30` status `ready` deltaP `37.7134` edge `0.0558` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.037` n `30` status `ready` deltaP `24.6806` edge `0.0191` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9182` n `30` status `ready` deltaP `11.3872` edge `0.0885` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.8683` n `226` status `ready` deltaP `7.3926` edge `0.1331` maxDD `-4.1352`
- `news_risk_high->crypto_alt_1h` score `0.2177` n `30` status `ready` deltaP `5.02` edge `0.0406` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.237` n `226` status `ready` deltaP `4.7613` edge `0.0305` maxDD `-4.4103`
- `market_context_high->metal_1h` score `-0.2973` n `226` status `ready` deltaP `3.5067` edge `0.0056` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.457` n `30` status `ready` deltaP `1.0878` edge `-0.0292` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5672` n `226` status `ready` deltaP `-1.8799` edge `-0.0031` maxDD `-1.9006`
- `market_context_high->crypto_major_1h` score `-0.5887` n `226` status `ready` deltaP `3.3636` edge `0.0342` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.6216` n `226` status `ready` deltaP `0.253` edge `0.0034` maxDD `-0.7819`
- `market_context_high->crypto_alt_1h` score `-0.6925` n `226` status `ready` deltaP `2.3356` edge `0.0291` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.8481` n `226` status `ready` deltaP `-3.0775` edge `-0.0013` maxDD `-0.5751`
- `news_risk_high->index_1h` score `-1.2603` n `30` status `ready` deltaP `-12.8443` edge `-0.0245` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.6145` n `226` status `ready` deltaP `-2.6629` edge `-0.0179` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.6473` n `226` status `ready` deltaP `-2.725` edge `-0.0298` maxDD `-5.725`
- `market_context_high->crypto_major_4h` score `-1.8109` n `226` status `ready` deltaP `8.4854` edge `0.1485` maxDD `-25.6458`
- `news_risk_high->commodity_4h` score `-1.8616` n `30` status `ready` deltaP `-14.4918` edge `-0.0545` maxDD `-2.3372`
- `market_context_high->index_4h` score `-1.9922` n `226` status `ready` deltaP `-1.1076` edge `0.0101` maxDD `-3.165`
- `market_context_high->fx_24h` score `-2.0075` n `219` status `ready` deltaP `2.5542` edge `0.0074` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
