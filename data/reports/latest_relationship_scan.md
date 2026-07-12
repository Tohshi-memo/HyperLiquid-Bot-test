# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T01:22:30.567263+00:00`
- Price records: `672`
- Market context records: `6449`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5875`

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

- `news_risk_high->crypto_alt_24h` score `11.6432` n `32` status `ready` deltaP `29.6875` edge `0.7871` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `8.479` n `145` status `ready` deltaP `19.6217` edge `0.9058` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.307` n `32` status `ready` deltaP `52.2569` edge `0.1772` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1096` n `32` status `ready` deltaP `42.7591` edge `0.062` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.8922` n `32` status `ready` deltaP `33.8542` edge `0.1192` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.2942` n `32` status `ready` deltaP `11.4583` edge `0.4239` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4697` n `32` status `ready` deltaP `29.7904` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5326` n `32` status `ready` deltaP `13.8286` edge `0.151` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.223` n `180` status `ready` deltaP `-5.9215` edge `0.2315` maxDD `-3.2083`
- `news_risk_high->crypto_alt_1h` score `0.8965` n `32` status `ready` deltaP `9.8241` edge `0.0956` maxDD `-1.6923`
- `market_context_high->index_4h` score `0.0628` n `180` status `ready` deltaP `7.2256` edge `0.0247` maxDD `-0.4108`
- `market_context_high->metal_4h` score `-0.1659` n `180` status `ready` deltaP `8.0387` edge `0.0414` maxDD `-2.7056`
- `news_risk_high->unknown_1h` score `-0.1828` n `32` status `ready` deltaP `6.2313` edge `-0.0223` maxDD `-0.7581`
- `market_context_high->unknown_4h` score `-0.3251` n `180` status `ready` deltaP `-15.3929` edge `0.3161` maxDD `-10.5788`
- `market_context_high->commodity_24h` score `-0.3841` n `145` status `ready` deltaP `2.5826` edge `0.1415` maxDD `-5.5913`
- `news_risk_high->metal_1h` score `-0.5137` n `32` status `ready` deltaP `1.1976` edge `-0.0241` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.5615` n `180` status `ready` deltaP `0.642` edge `0.0015` maxDD `-1.8877`
- `market_context_high->crypto_alt_1h` score `-0.5761` n `180` status `ready` deltaP `6.0047` edge `0.0174` maxDD `-5.8368`
- `market_context_high->equity_4h` score `-0.5787` n `180` status `ready` deltaP `6.8529` edge `0.05` maxDD `-8.2573`
- `news_risk_high->index_24h` score `-0.6166` n `32` status `ready` deltaP `2.4306` edge `-0.0081` maxDD `-2.3058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
