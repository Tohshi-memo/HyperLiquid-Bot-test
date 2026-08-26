# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T10:22:29.923942+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `45.7482` n `52` status `ready` deltaP `11.6319` edge `3.7348` maxDD `0.0`
- `news_risk_high->unknown_4h` score `11.8116` n `53` status `ready` deltaP `23.1506` edge `0.8399` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `9.5047` n `52` status `ready` deltaP `31.5838` edge `0.604` maxDD `-1.4667`
- `news_risk_high->equity_24h` score `7.0825` n `52` status `ready` deltaP `29.7143` edge `0.4852` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.1491` n `52` status `ready` deltaP `41.226` edge `0.0861` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.7963` n `53` status `ready` deltaP `33.7437` edge `0.0215` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.7483` n `53` status `ready` deltaP `15.4135` edge `0.1618` maxDD `-0.8426`
- `market_context_high->unknown_4h` score `2.4447` n `136` status `ready` deltaP `21.4581` edge `0.1015` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.7973` n `53` status `ready` deltaP `20.1939` edge `0.0922` maxDD `-2.164`
- `news_risk_high->metal_24h` score `1.6623` n `52` status `ready` deltaP `29.1533` edge `-0.0516` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.0782` n `53` status `ready` deltaP `15.1706` edge `0.0057` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.0666` n `136` status `ready` deltaP `11.4873` edge `0.0572` maxDD `-1.5916`
- `news_risk_high->commodity_1h` score `0.5015` n `53` status `ready` deltaP `11.4253` edge `-0.0031` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4411` n `53` status `ready` deltaP `12.9251` edge `0.0068` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.1571` n `53` status `ready` deltaP `6.8138` edge `0.0074` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0636` n `53` status `ready` deltaP `3.9996` edge `0.0005` maxDD `-0.1583`
- `news_risk_high->metal_1h` score `-0.3935` n `53` status `ready` deltaP `0.1356` edge `-0.0111` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.438` n `136` status `ready` deltaP `2.7122` edge `-0.001` maxDD `-0.8587`
- `news_risk_high->metal_4h` score `-0.444` n `53` status `ready` deltaP `4.9672` edge `-0.017` maxDD `-0.249`
- `news_risk_high->commodity_4h` score `-0.9527` n `53` status `ready` deltaP `-0.7536` edge `0.0062` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
