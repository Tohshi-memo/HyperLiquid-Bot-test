# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T07:22:25.154471+00:00`
- Price records: `672`
- Market context records: `6475`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5863`

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

- `news_risk_high->crypto_alt_24h` score `12.4353` n `32` status `ready` deltaP `33.3333` edge `0.8288` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `7.1062` n `153` status `ready` deltaP `16.8914` edge `0.8096` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.4143` n `32` status `ready` deltaP `53.2986` edge `0.1792` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1497` n `33` status `ready` deltaP `43.5006` edge `0.0604` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.1021` n `32` status `ready` deltaP `15.625` edge `0.4997` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `3.2301` n `32` status `ready` deltaP `29.6875` edge `0.0918` maxDD `-0.3101`
- `market_context_high->unknown_1h` score `1.9093` n `173` status `ready` deltaP `-4.8882` edge `0.2818` maxDD `-3.2083`
- `news_risk_high->fx_1h` score `1.8191` n `38` status `ready` deltaP `22.7624` edge `0.0179` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.594` n `38` status `ready` deltaP `5.2001` edge `0.0952` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.4465` n `172` status `ready` deltaP `11.4968` edge `0.0282` maxDD `-0.4108`
- `market_context_high->unknown_4h` score `0.3053` n `172` status `ready` deltaP `-15.0879` edge `0.3666` maxDD `-10.5788`
- `market_context_high->commodity_24h` score `0.2199` n `153` status `ready` deltaP `6.0968` edge `0.1645` maxDD `-5.2791`
- `market_context_high->crypto_alt_4h` score `0.1884` n `172` status `ready` deltaP `8.2459` edge `0.1161` maxDD `-6.7632`
- `market_context_high->metal_4h` score `0.1079` n `172` status `ready` deltaP `11.1316` edge `0.0436` maxDD `-2.7056`
- `news_risk_high->crypto_alt_1h` score `0.1038` n `38` status `ready` deltaP `1.8831` edge `0.0517` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.4618` n `32` status `ready` deltaP `4.6875` edge `-0.0033` maxDD `-2.3058`
- `news_risk_high->unknown_1h` score `-0.4688` n `38` status `ready` deltaP `4.4516` edge `-0.0316` maxDD `-0.9718`
- `market_context_high->metal_1h` score `-0.4965` n `173` status `ready` deltaP `1.9357` edge `0.0012` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.506` n `172` status `ready` deltaP `7.6822` edge `0.0538` maxDD `-8.2573`
- `market_context_high->commodity_1h` score `-0.5901` n `173` status `ready` deltaP `-0.501` edge `-0.004` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
