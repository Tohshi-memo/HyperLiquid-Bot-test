# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T02:52:15.944747+00:00`
- Price records: `672`
- Market context records: `1588`
- Flow alert records: `6486`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8814`

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

- `market_context_high->metal_24h` score `13.7521` n `182` status `ready` deltaP `29.1991` edge `1.0514` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `12.2941` n `182` status `ready` deltaP `27.171` edge `1.045` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.5844` n `182` status `ready` deltaP `26.9135` edge `0.8158` maxDD `-8.0553`
- `market_context_high->equity_24h` score `4.7268` n `182` status `ready` deltaP `19.7974` edge `0.4946` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.1784` n `182` status `ready` deltaP `21.9952` edge `0.3102` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.0767` n `199` status `ready` deltaP `9.2069` edge `0.1378` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.2754` n `199` status `ready` deltaP `13.2545` edge `0.2789` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.1036` n `199` status `ready` deltaP `9.2796` edge `0.2223` maxDD `-13.3376`
- `market_context_high->fx_24h` score `0.0217` n `182` status `ready` deltaP `9.932` edge `0.0405` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.3113` n `199` status `ready` deltaP `0.9674` edge `0.056` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5503` n `199` status `ready` deltaP `0.9133` edge `0.0289` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.5782` n `199` status `ready` deltaP `-1.096` edge `-0.0036` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6721` n `199` status `ready` deltaP `0.6244` edge `0.003` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7134` n `199` status `ready` deltaP `5.4472` edge `0.0058` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.8232` n `199` status `ready` deltaP `-1.6948` edge `-0.0021` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.8342` n `199` status `ready` deltaP `0.0053` edge `0.0287` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.0971` n `199` status `ready` deltaP `-1.8484` edge `0.0298` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.2862` n `199` status `ready` deltaP `10.516` edge `0.0919` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.387` n `199` status `ready` deltaP `-10.5497` edge `-0.0146` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.2611` n `199` status `ready` deltaP `-14.7001` edge `-0.1138` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
