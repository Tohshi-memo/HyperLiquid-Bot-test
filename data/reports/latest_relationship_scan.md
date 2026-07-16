# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T20:52:31.419705+00:00`
- Price records: `672`
- Market context records: `6957`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11735`

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

- `market_context_high->fx_1h` score `-0.26` n `237` status `ready` deltaP `2.0345` edge `0.0016` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3794` n `237` status `ready` deltaP `2.43` edge `0.0216` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.734` n `237` status `ready` deltaP `-0.3885` edge `-0.0004` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7349` n `237` status `ready` deltaP `-2.2398` edge `-0.0025` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9536` n `236` status `ready` deltaP `11.4019` edge `0.0081` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.1958` n `237` status `ready` deltaP `3.1785` edge `0.0144` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.3041` n `237` status `ready` deltaP `-3.1235` edge `-0.0157` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.5889` n `237` status `ready` deltaP `-1.9809` edge `-0.0291` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6614` n `236` status `ready` deltaP `-4.4879` edge `-0.0341` maxDD `-5.5853`
- `market_context_high->unknown_24h` score `-1.6719` n `224` status `ready` deltaP `-9.1096` edge `0.3014` maxDD `-18.7342`
- `market_context_high->index_4h` score `-1.8161` n `236` status `ready` deltaP `7.591` edge `-0.0145` maxDD `-12.1818`
- `market_context_high->equity_1h` score `-2.0443` n `237` status `ready` deltaP `1.7894` edge `-0.0186` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-2.1096` n `236` status `ready` deltaP `3.6688` edge `0.0034` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-3.1202` n `236` status `ready` deltaP `-0.1861` edge `-0.0237` maxDD `-22.0069`
- `market_context_high->unknown_4h` score `-3.3119` n `236` status `ready` deltaP `-8.7356` edge `0.0188` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.7411` n `224` status `ready` deltaP `-6.3359` edge `-0.0827` maxDD `-5.2791`
- `market_context_high->crypto_major_4h` score `-3.7935` n `236` status `ready` deltaP `-1.5915` edge `-0.0518` maxDD `-24.2483`
- `market_context_high->fx_24h` score `-4.4178` n `224` status `ready` deltaP `-7.2822` edge `-0.0149` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.6839` n `236` status `ready` deltaP `3.9117` edge `-0.0956` maxDD `-66.2476`
- `market_context_high->index_24h` score `-12.3964` n `224` status `ready` deltaP `-7.3772` edge `-0.1331` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
