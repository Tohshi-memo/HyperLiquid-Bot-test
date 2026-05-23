# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T02:22:15.310700+00:00`
- Price records: `672`
- Market context records: `1586`
- Flow alert records: `6480`
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

- `market_context_high->metal_24h` score `13.6775` n `182` status `ready` deltaP `28.8518` edge `1.0475` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `12.1513` n `182` status `ready` deltaP `27.171` edge `1.0331` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.474` n `182` status `ready` deltaP `26.9135` edge `0.8066` maxDD `-8.0553`
- `market_context_high->equity_24h` score `4.5922` n `182` status `ready` deltaP `19.4502` edge `0.4857` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.1525` n `182` status `ready` deltaP `21.8216` edge `0.3092` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.0513` n `199` status `ready` deltaP `9.0544` edge `0.1367` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.2863` n `199` status `ready` deltaP `13.2545` edge `0.2803` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.1028` n `199` status `ready` deltaP `9.2796` edge `0.2222` maxDD `-13.3376`
- `market_context_high->fx_24h` score `0.0543` n `182` status `ready` deltaP `10.2793` edge `0.0409` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.323` n `199` status `ready` deltaP `0.8177` edge `0.0555` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5503` n `199` status `ready` deltaP `0.9133` edge `0.0289` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.586` n `199` status `ready` deltaP `-1.2457` edge `-0.0036` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.647` n `199` status `ready` deltaP `0.9238` edge `0.0031` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7134` n `199` status `ready` deltaP `5.4472` edge `0.0058` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.8271` n `199` status `ready` deltaP `-1.6948` edge `-0.0026` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.8443` n `199` status `ready` deltaP `-0.1444` edge `0.0284` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.1019` n `199` status `ready` deltaP `-1.8484` edge `0.0294` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.2886` n `199` status `ready` deltaP `10.516` edge `0.0917` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.387` n `199` status `ready` deltaP `-10.5497` edge `-0.0146` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.2596` n `199` status `ready` deltaP `-14.7001` edge `-0.1136` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
