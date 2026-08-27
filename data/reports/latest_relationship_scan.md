# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T04:22:25.717182+00:00`
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

- `news_risk_high->unknown_24h` score `49.7141` n `50` status `ready` deltaP `11.5717` edge `4.0657` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.1572` n `50` status `ready` deltaP `36.9326` edge `1.061` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.2717` n `50` status `ready` deltaP `25.5549` edge `0.8622` maxDD `-0.1276`
- `news_risk_high->equity_24h` score `5.8963` n `50` status `ready` deltaP `28.0415` edge `0.3977` maxDD `-4.7964`
- `news_risk_high->fx_4h` score `3.8945` n `50` status `ready` deltaP `45.5061` edge `0.0302` maxDD `-0.0559`
- `news_risk_high->index_24h` score `3.3882` n `50` status `ready` deltaP `34.8048` edge `0.0655` maxDD `-0.2147`
- `market_context_high->unknown_4h` score `3.1143` n `137` status `ready` deltaP `24.2556` edge `0.1385` maxDD `-0.5878`
- `news_risk_high->metal_24h` score `3.0674` n `50` status `ready` deltaP `38.5872` edge `0.0026` maxDD `-0.0053`
- `news_risk_high->unknown_1h` score `2.6832` n `50` status `ready` deltaP `15.6287` edge `0.155` maxDD `-0.8474`
- `news_risk_high->fx_1h` score `1.4557` n `50` status `ready` deltaP `19.6048` edge `0.0076` maxDD `-0.0257`
- `news_risk_high->equity_4h` score `1.3829` n `50` status `ready` deltaP `20.6646` edge `0.054` maxDD `-2.1218`
- `market_context_high->unknown_1h` score `1.3153` n `137` status `ready` deltaP `13.001` edge `0.0679` maxDD `-1.5974`
- `news_risk_high->equity_1h` score `1.2959` n `50` status `ready` deltaP `17.1138` edge `0.0218` maxDD `-0.2319`
- `market_context_high->unknown_24h` score `0.6948` n `136` status `ready` deltaP `5.6893` edge `0.0931` maxDD `-3.1835`
- `news_risk_high->commodity_1h` score `0.5175` n `50` status `ready` deltaP `14.2994` edge `0.0023` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.2342` n `50` status `ready` deltaP `8.1524` edge `0.0049` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.1435` n `50` status `ready` deltaP `7.509` edge `0.0023` maxDD `-0.0505`
- `news_risk_high->metal_1h` score `0.0524` n `50` status `ready` deltaP `4.8024` edge `-0.0027` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.3329` n `137` status `ready` deltaP `4.5391` edge `0.0003` maxDD `-0.8587`
- `news_risk_high->metal_4h` score `-0.3718` n `50` status `ready` deltaP `5.3293` edge `-0.0134` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
