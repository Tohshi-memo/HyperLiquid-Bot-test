# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T18:07:31.577572+00:00`
- Price records: `672`
- Market context records: `5903`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11166`

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

- `news_risk_high->fx_4h` score `3.6047` n `30` status `ready` deltaP `37.4085` edge `0.0556` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `1.9878` n `30` status `ready` deltaP `24.0818` edge `0.019` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9322` n `30` status `ready` deltaP `11.3872` edge `0.0903` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.7216` n `221` status `ready` deltaP `6.9267` edge `0.1234` maxDD `-4.0887`
- `news_risk_high->crypto_alt_1h` score `0.231` n `30` status `ready` deltaP `5.1697` edge `0.0413` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.2302` n `221` status `ready` deltaP `4.6489` edge `0.0315` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3445` n `221` status `ready` deltaP `2.9581` edge `0.0032` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4515` n `30` status `ready` deltaP `1.0878` edge `-0.0285` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.4901` n `221` status `ready` deltaP `-1.451` edge `-0.0016` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.5536` n `221` status `ready` deltaP `3.71` edge `0.0364` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.637` n `221` status `ready` deltaP `-0.0596` edge `0.0035` maxDD `-0.7819`
- `market_context_high->crypto_alt_1h` score `-0.644` n `221` status `ready` deltaP `2.8016` edge `0.0322` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.8123` n `221` status `ready` deltaP `-2.6452` edge `-0.0012` maxDD `-0.5751`
- `news_risk_high->index_1h` score `-1.2152` n `30` status `ready` deltaP `-12.0958` edge `-0.0237` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.5947` n `221` status `ready` deltaP `-2.4018` edge `-0.0171` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.7093` n `221` status `ready` deltaP `-3.4661` edge `-0.0328` maxDD `-5.725`
- `news_risk_high->commodity_4h` score `-1.9034` n `30` status `ready` deltaP `-15.1016` edge `-0.0558` maxDD `-2.3372`
- `market_context_high->crypto_major_4h` score `-1.9782` n `221` status `ready` deltaP `7.8944` edge `0.131` maxDD `-25.6458`
- `market_context_high->index_4h` score `-2.0635` n `221` status `ready` deltaP `-1.8038` edge `0.0088` maxDD `-3.165`
- `market_context_high->fx_24h` score `-2.1094` n `214` status `ready` deltaP `1.1779` edge `0.0035` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
