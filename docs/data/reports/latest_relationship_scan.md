# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T17:07:25.925629+00:00`
- Price records: `672`
- Market context records: `2263`
- Flow alert records: `8410`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9257`

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

- `news_risk_high->crypto_alt_24h` score `21.9506` n `43` status `ready` deltaP `52.4669` edge `1.5383` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.7288` n `43` status `ready` deltaP `42.1188` edge `1.0739` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.7102` n `43` status `ready` deltaP `33.0911` edge `1.0367` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.7289` n `43` status `ready` deltaP `23.066` edge `0.8817` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `9.1157` n `115` status `ready` deltaP `29.3251` edge `0.6053` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `8.6792` n `43` status `ready` deltaP `33.3696` edge `0.5234` maxDD `-1.4744`
- `market_context_high->crypto_alt_4h` score `8.5333` n `146` status `ready` deltaP `27.556` edge `0.7953` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `8.1933` n `146` status `ready` deltaP `32.8016` edge `0.6451` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `5.9022` n `115` status `ready` deltaP `16.7769` edge `1.0341` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.332` n `146` status `ready` deltaP `21.7654` edge `0.3602` maxDD `-1.8773`
- `news_risk_high->commodity_4h` score `3.7468` n `43` status `ready` deltaP `32.1575` edge `0.3331` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.7295` n `43` status `ready` deltaP `12.0559` edge `0.2723` maxDD `-1.3507`
- `news_risk_high->fx_24h` score `3.6363` n `43` status `ready` deltaP `37.2295` edge `0.0733` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.3398` n `115` status `ready` deltaP `13.8557` edge `0.2377` maxDD `-1.4737`
- `news_risk_high->commodity_24h` score `3.2008` n `43` status `ready` deltaP `2.8989` edge `0.3291` maxDD `-3.202`
- `market_context_high->index_4h` score `2.8614` n `146` status `ready` deltaP `25.5596` edge `0.1445` maxDD `-2.1155`
- `market_context_high->equity_4h` score `2.366` n `146` status `ready` deltaP `19.0068` edge `0.2109` maxDD `-5.9024`
- `market_context_high->equity_24h` score `2.3491` n `115` status `ready` deltaP `20.6341` edge `0.2109` maxDD `-6.8828`
- `market_context_high->crypto_alt_1h` score `2.2736` n `158` status `ready` deltaP `13.7402` edge `0.2166` maxDD `-6.1656`
- `news_risk_high->fx_4h` score `2.0589` n `43` status `ready` deltaP `26.3648` edge `0.0142` maxDD `-0.1382`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
