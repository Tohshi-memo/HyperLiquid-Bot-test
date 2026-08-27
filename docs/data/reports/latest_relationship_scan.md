# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T01:52:26.851136+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14779`

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

- `news_risk_high->unknown_24h` score `49.2737` n `50` status `ready` deltaP `11.5717` edge `4.029` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.0927` n `50` status `ready` deltaP `36.5872` edge `0.9746` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.2763` n `50` status `ready` deltaP `25.4024` edge `0.8636` maxDD `-0.1276`
- `news_risk_high->equity_24h` score `6.4076` n `50` status `ready` deltaP `29.7686` edge `0.4288` maxDD `-4.7964`
- `news_risk_high->fx_4h` score `3.7849` n `50` status `ready` deltaP `44.2866` edge `0.0292` maxDD `-0.0559`
- `news_risk_high->index_24h` score `3.59` n `50` status `ready` deltaP `36.532` edge `0.0708` maxDD `-0.2147`
- `market_context_high->unknown_4h` score `3.1189` n `137` status `ready` deltaP `24.1031` edge `0.1399` maxDD `-0.5878`
- `news_risk_high->metal_24h` score `2.778` n `50` status `ready` deltaP `36.8601` edge `-0.01` maxDD `-0.0053`
- `news_risk_high->unknown_1h` score `2.658` n `50` status `ready` deltaP `15.3293` edge `0.1549` maxDD `-0.8474`
- `news_risk_high->fx_1h` score `1.4569` n `50` status `ready` deltaP `19.6048` edge `0.0077` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.3486` n `50` status `ready` deltaP `17.5629` edge `0.0232` maxDD `-0.2319`
- `market_context_high->unknown_1h` score `1.2901` n `137` status `ready` deltaP `12.7016` edge `0.0678` maxDD `-1.5974`
- `news_risk_high->equity_4h` score `1.2447` n `50` status `ready` deltaP `19.5976` edge `0.0496` maxDD `-2.1218`
- `market_context_high->unknown_24h` score `0.599` n `134` status `ready` deltaP `5.6016` edge `0.0857` maxDD `-3.1835`
- `news_risk_high->commodity_1h` score `0.5331` n `50` status `ready` deltaP `14.5988` edge `0.0023` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.145` n `50` status `ready` deltaP `7.509` edge `0.0025` maxDD `-0.0505`
- `news_risk_high->index_4h` score `0.1186` n `50` status `ready` deltaP `6.9329` edge `0.0034` maxDD `-0.1788`
- `news_risk_high->metal_1h` score `0.0103` n `50` status `ready` deltaP `4.0539` edge `-0.0031` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.2478` n `50` status `ready` deltaP `6.5488` edge `-0.0112` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3321` n `137` status `ready` deltaP `4.5391` edge `0.0004` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
