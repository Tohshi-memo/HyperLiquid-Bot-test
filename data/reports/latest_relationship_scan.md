# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T11:22:20.066773+00:00`
- Price records: `672`
- Market context records: `2239`
- Flow alert records: `8340`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9203`

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

- `news_risk_high->crypto_alt_24h` score `25.7521` n `37` status `ready` deltaP `55.7057` edge `1.8335` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.6568` n `37` status `ready` deltaP `45.7348` edge `1.0438` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.5423` n `37` status `ready` deltaP `36.707` edge `0.9986` maxDD `-2.1831`
- `market_context_high->crypto_alt_4h` score `12.7505` n `131` status `ready` deltaP `35.3367` edge `0.9206` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.5185` n `131` status `ready` deltaP `40.9909` edge `0.7396` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `9.3991` n `37` status `ready` deltaP `36.6085` edge `0.5618` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `8.4634` n `37` status `ready` deltaP `22.1566` edge `0.9954` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `6.6912` n `123` status `ready` deltaP `27.3798` edge `0.5782` maxDD `-13.5842`
- `market_context_high->unknown_4h` score `6.3126` n `131` status `ready` deltaP `25.1152` edge `0.404` maxDD `-1.6306`
- `market_context_high->crypto_major_24h` score `4.5945` n `123` status `ready` deltaP `16.6413` edge `0.9516` maxDD `-31.8801`
- `market_context_high->equity_4h` score `4.435` n `131` status `ready` deltaP `24.3705` edge `0.2506` maxDD `-1.4791`
- `market_context_high->index_4h` score `4.0207` n `131` status `ready` deltaP `30.3191` edge `0.1703` maxDD `-0.3228`
- `news_risk_high->commodity_4h` score `3.9341` n `43` status `ready` deltaP `33.2246` edge `0.35` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.3415` n `37` status `ready` deltaP `34.009` edge `0.0702` maxDD `-0.1442`
- `market_context_high->index_24h` score `2.8917` n `123` status `ready` deltaP `11.7209` edge `0.2204` maxDD `-1.9385`
- `market_context_high->crypto_major_1h` score `2.7703` n `143` status `ready` deltaP `14.6351` edge `0.181` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `2.7567` n `143` status `ready` deltaP `15.7343` edge `0.2112` maxDD `-4.9097`
- `news_risk_high->index_24h` score `2.7239` n `37` status `ready` deltaP `11.7868` edge `0.1903` maxDD `-1.3507`
- `news_risk_high->commodity_24h` score `2.579` n `37` status `ready` deltaP `0.2111` edge `0.2952` maxDD `-3.202`
- `news_risk_high->fx_4h` score `2.1512` n `43` status `ready` deltaP `27.2794` edge `0.0158` maxDD `-0.1382`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
