# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T14:22:30.892264+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14776`

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

- `news_risk_high->unknown_24h` score `45.1734` n `53` status `ready` deltaP `11.6319` edge `3.6869` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.2306` n `53` status `ready` deltaP `25.1323` edge `0.8616` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `11.2551` n `53` status `ready` deltaP `32.5111` edge `0.7653` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `6.8578` n `53` status `ready` deltaP `29.2453` edge `0.4696` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0102` n `53` status `ready` deltaP `39.9404` edge `0.0831` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.9814` n `53` status `ready` deltaP `35.8779` edge `0.0227` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.8637` n `136` status `ready` deltaP `23.4398` edge `0.1232` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.7843` n `53` status `ready` deltaP `15.5632` edge `0.1638` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `1.8212` n `53` status `ready` deltaP `29.1896` edge `-0.0386` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.7441` n `53` status `ready` deltaP `19.889` edge `0.0898` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1165` n `53` status `ready` deltaP `15.6197` edge `0.0059` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.0967` n `137` status `ready` deltaP `11.8034` edge `0.0576` maxDD `-1.5916`
- `news_risk_high->equity_1h` score `0.4209` n `53` status `ready` deltaP `12.7754` edge `0.0052` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.4116` n `53` status `ready` deltaP `10.5271` edge `-0.0046` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.1743` n `53` status `ready` deltaP `7.1186` edge `0.0068` maxDD `-0.1788`
- `news_risk_high->metal_4h` score `-0.0689` n `53` status `ready` deltaP `7.4062` edge `-0.002` maxDD `-0.249`
- `news_risk_high->index_1h` score `-0.0713` n `53` status `ready` deltaP `3.8499` edge `0.0005` maxDD `-0.1583`
- `news_risk_high->metal_1h` score `-0.2401` n `53` status `ready` deltaP `1.3332` edge `-0.0063` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4348` n `137` status `ready` deltaP `2.7427` edge `-0.0008` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.898` n `136` status `ready` deltaP `4.9229` edge `-0.0282` maxDD `-2.6898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
