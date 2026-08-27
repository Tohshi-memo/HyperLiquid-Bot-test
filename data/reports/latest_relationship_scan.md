# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T18:52:24.382965+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14777`

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

- `news_risk_high->unknown_24h` score `52.149` n `50` status `ready` deltaP `11.6319` edge `4.2682` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.579` n `50` status `ready` deltaP `37.8403` edge `1.5901` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.9932` n `50` status `ready` deltaP `26.7744` edge `0.9142` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `4.8004` n `50` status `ready` deltaP `46.0903` edge `0.097` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `4.5187` n `50` status `ready` deltaP `25.8403` edge `0.2971` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `4.0113` n `50` status `ready` deltaP `46.7256` edge `0.0318` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `3.0714` n `50` status `ready` deltaP `17.1257` edge `0.1774` maxDD `-0.8495`
- `market_context_high->unknown_24h` score `2.7246` n `128` status `ready` deltaP `5.3819` edge `0.2644` maxDD `-3.1917`
- `news_risk_high->index_24h` score `2.6275` n `50` status `ready` deltaP `29.8403` edge `0.0351` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.5501` n `148` status `ready` deltaP `19.9366` edge `0.1203` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.5815` n `50` status `ready` deltaP `21.1018` edge `0.0081` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1415` n `50` status `ready` deltaP `16.6647` edge `0.0119` maxDD `-0.2301`
- `market_context_high->unknown_1h` score `0.948` n `148` status `ready` deltaP `9.423` edge `0.0612` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.8205` n `50` status `ready` deltaP `18.9878` edge `0.0181` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.5354` n `50` status `ready` deltaP `14.7485` edge `0.0016` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1382` n `50` status `ready` deltaP `7.6587` edge `0.0006` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0617` n `50` status `ready` deltaP `4.8024` edge `-0.0015` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.1027` n `50` status `ready` deltaP `7.4634` edge `-0.0052` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.1573` n `50` status `ready` deltaP `4.3415` edge `-0.0024` maxDD `-0.1719`
- `market_context_high->metal_4h` score `-0.448` n `148` status `ready` deltaP `6.3283` edge `-0.0079` maxDD `-3.3377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
