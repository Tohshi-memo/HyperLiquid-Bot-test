# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T17:37:35.100809+00:00`
- Price records: `672`
- Market context records: `5901`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11176`

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
- `news_risk_high->crypto_major_1h` score `0.9338` n `30` status `ready` deltaP `11.3872` edge `0.0905` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.7393` n `223` status `ready` deltaP `6.9343` edge `0.1254` maxDD `-4.1352`
- `news_risk_high->crypto_alt_1h` score `0.2333` n `30` status `ready` deltaP `5.1697` edge `0.0416` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.2387` n `223` status `ready` deltaP `4.6985` edge `0.0307` maxDD `-4.4103`
- `market_context_high->metal_1h` score `-0.3477` n `223` status `ready` deltaP `2.9115` edge `0.0031` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4499` n `30` status `ready` deltaP `1.0878` edge `-0.0283` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5192` n `223` status `ready` deltaP `-1.5655` edge `-0.002` maxDD `-1.6639`
- `market_context_high->crypto_major_1h` score `-0.6076` n `223` status `ready` deltaP `3.2109` edge `0.0328` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.6302` n `223` status `ready` deltaP `0.0712` edge `0.0035` maxDD `-0.7819`
- `market_context_high->crypto_alt_1h` score `-0.692` n `223` status `ready` deltaP `2.3147` edge `0.0293` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.8469` n `223` status `ready` deltaP `-3.0632` edge `-0.0013` maxDD `-0.5751`
- `news_risk_high->index_1h` score `-1.2331` n `30` status `ready` deltaP `-12.3952` edge `-0.024` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.6098` n `223` status `ready` deltaP `-2.6024` edge `-0.0177` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.6998` n `223` status `ready` deltaP `-3.3441` edge `-0.0324` maxDD `-5.725`
- `news_risk_high->commodity_4h` score `-1.8931` n `30` status `ready` deltaP `-14.9492` edge `-0.0555` maxDD `-2.3372`
- `market_context_high->crypto_major_4h` score `-1.9268` n `223` status `ready` deltaP `8.2515` edge `0.1352` maxDD `-25.6458`
- `market_context_high->index_4h` score `-2.053` n `223` status `ready` deltaP `-1.7028` edge `0.009` maxDD `-3.165`
- `market_context_high->fx_24h` score `-2.0679` n `216` status `ready` deltaP `1.7361` edge `0.0051` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
