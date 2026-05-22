# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T07:07:15.734423+00:00`
- Price records: `672`
- Market context records: `1504`
- Flow alert records: `6239`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8791`

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

- `market_context_high->metal_24h` score `13.5177` n `165` status `ready` deltaP `23.5386` edge `1.0696` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.1733` n `165` status `ready` deltaP `28.911` edge `0.94` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.4313` n `165` status `ready` deltaP `27.3548` edge `0.8001` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.7706` n `165` status `ready` deltaP `19.9874` edge `0.2896` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7498` n `165` status `ready` deltaP `13.2197` edge `0.3737` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.0372` n `191` status `ready` deltaP `6.0793` edge `0.1289` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.9942` n `165` status `ready` deltaP `19.2235` edge `0.0596` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.2487` n `192` status `ready` deltaP `2.757` edge `0.0074` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.2903` n `192` status `ready` deltaP `1.0385` edge `0.0289` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.509` n `192` status `ready` deltaP `0.131` edge `-0.0029` maxDD `-0.3914`
- `market_context_high->crypto_alt_4h` score `-0.5857` n `191` status `ready` deltaP `9.5199` edge `0.1934` maxDD `-19.5565`
- `market_context_high->crypto_alt_1h` score `-0.6296` n `192` status `ready` deltaP `1.2444` edge `0.0416` maxDD `-4.1892`
- `market_context_high->metal_1h` score `-0.6707` n `192` status `ready` deltaP `6.3748` edge `0.0051` maxDD `-6.3532`
- `market_context_high->crypto_major_1h` score `-1.0406` n `192` status `ready` deltaP `-1.3535` edge `0.0113` maxDD `-6.1883`
- `market_context_high->crypto_major_4h` score `-1.0496` n `191` status `ready` deltaP `5.4176` edge `0.1473` maxDD `-13.3376`
- `market_context_high->metal_4h` score `-1.169` n `191` status `ready` deltaP `11.1703` edge `0.0973` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.17` n `191` status `ready` deltaP `-3.285` edge `0.0333` maxDD `-3.7119`
- `market_context_high->commodity_1h` score `-1.3158` n `192` status `ready` deltaP `-1.7122` edge `-0.0061` maxDD `-4.7041`
- `market_context_high->fx_4h` score `-1.5394` n `191` status `ready` deltaP `-3.8541` edge `-0.0097` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-3.6273` n `165` status `ready` deltaP `-1.1269` edge `-0.0218` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
