# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T18:52:29.600175+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14792`

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

- `news_risk_high->unknown_24h` score `47.9069` n `50` status `ready` deltaP `11.5717` edge `3.9151` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.4269` n `50` status `ready` deltaP `26.7769` edge `0.867` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `11.5462` n `50` status `ready` deltaP `35.2055` edge `0.7716` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `7.8829` n `50` status `ready` deltaP `34.2591` edge `0.5216` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.1418` n `50` status `ready` deltaP `41.1952` edge `0.0857` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.4896` n `50` status `ready` deltaP `41.1654` edge `0.0254` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.2871` n `137` status `ready` deltaP `25.4776` edge `0.1449` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.6288` n `50` status `ready` deltaP `15.1796` edge `0.1534` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `2.1211` n `50` status `ready` deltaP `32.0242` edge `-0.0325` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.4624` n `50` status `ready` deltaP `19.2473` edge `0.0706` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.3359` n `50` status `ready` deltaP `18.2575` edge `0.0066` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.2783` n `50` status `ready` deltaP `16.8144` edge `0.0225` maxDD `-0.2455`
- `market_context_high->unknown_1h` score `1.2598` n `137` status `ready` deltaP `12.5519` edge `0.0662` maxDD `-1.5916`
- `news_risk_high->commodity_1h` score `0.5113` n `50` status `ready` deltaP `14.1497` edge `0.0025` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1201` n `50` status `ready` deltaP `7.0599` edge `0.0023` maxDD `-0.0505`
- `news_risk_high->index_4h` score `0.0872` n `50` status `ready` deltaP `6.2549` edge `0.0053` maxDD `-0.1788`
- `news_risk_high->metal_1h` score `0.0571` n `50` status `ready` deltaP `4.8024` edge `-0.0021` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0619` n `50` status `ready` deltaP `8.0334` edge `-0.0056` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4107` n `137` status `ready` deltaP `3.1918` edge `-0.0007` maxDD `-0.8587`
- `market_context_high->unknown_24h` score `-0.5086` n `133` status `ready` deltaP `5.5567` edge `-0.0067` maxDD `-3.1513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
