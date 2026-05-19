# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T02:37:18.548718+00:00`
- Price records: `672`
- Market context records: `1178`
- Flow alert records: `5295`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `19.8381` n `144` status `ready` deltaP `44.9652` edge `1.4666` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `9.5138` n `144` status `ready` deltaP `22.2223` edge `0.8463` maxDD `-15.1306`
- `market_context_high->equity_24h` score `5.4664` n `144` status `ready` deltaP `18.4028` edge `0.4819` maxDD `-9.5911`
- `market_context_high->metal_24h` score `5.324` n `144` status `ready` deltaP `-2.7778` edge `0.6289` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.6953` n `144` status `ready` deltaP `18.0555` edge `0.3334` maxDD `-3.6664`
- `market_context_high->equity_4h` score `2.7513` n `150` status `ready` deltaP `14.0854` edge `0.2017` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.2491` n `150` status `ready` deltaP `10.124` edge `0.1049` maxDD `-2.1308`
- `market_context_high->unknown_4h` score `0.7057` n `150` status `ready` deltaP `6.1138` edge `0.1397` maxDD `-6.7322`
- `market_context_high->index_1h` score `0.6396` n `150` status `ready` deltaP `8.8942` edge `0.0257` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4551` n `150` status `ready` deltaP `3.9141` edge `0.0496` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.0844` n `150` status `ready` deltaP `7.8902` edge `0.0` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `0.0301` n `150` status `ready` deltaP `8.0955` edge `0.142` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `-0.105` n `150` status `ready` deltaP `5.6866` edge `0.0252` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.1976` n `150` status `ready` deltaP `7.4811` edge `-0.0053` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.3483` n `150` status `ready` deltaP `1.2775` edge `0.0311` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.8962` n `150` status `ready` deltaP `-4.2176` edge `-0.006` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-1.0808` n `150` status `ready` deltaP `-4.878` edge `-0.0064` maxDD `-1.6381`
- `market_context_high->unknown_24h` score `-1.3204` n `144` status `ready` deltaP `4.3403` edge `0.134` maxDD `-10.1706`
- `market_context_high->crypto_alt_4h` score `-1.3855` n `150` status `ready` deltaP `3.5204` edge `0.0954` maxDD `-16.7194`
- `market_context_high->fx_24h` score `-1.7874` n `144` status `ready` deltaP `2.7778` edge `-0.0014` maxDD `-12.368`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
