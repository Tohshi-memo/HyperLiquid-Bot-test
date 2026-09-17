# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T22:22:31.300168+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9108`

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

- `news_risk_high->unknown_4h` score `467.8799` n `71` status `ready` deltaP `-12.3218` edge `39.1491` maxDD `-4.1571`
- `risk_on_high->commodity_24h` score `9.2152` n `52` status `ready` deltaP `50.0` edge `0.4346` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.2152` n `52` status `ready` deltaP `50.0` edge `0.4346` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `7.9996` n `57` status `ready` deltaP `26.1513` edge `0.6302` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.9161` n `149` status `ready` deltaP `43.2886` edge `0.4236` maxDD `-0.8682`
- `news_risk_high->index_24h` score `4.6859` n `57` status `ready` deltaP `32.2643` edge `0.193` maxDD `-0.075`
- `news_risk_high->equity_24h` score `3.8854` n `57` status `ready` deltaP `19.3713` edge `0.5464` maxDD `-6.5262`
- `news_risk_high->crypto_major_24h` score `3.6579` n `57` status `ready` deltaP `12.3081` edge `0.5864` maxDD `-13.2931`
- `risk_on_high->commodity_4h` score `3.0861` n `52` status `ready` deltaP `33.6069` edge `0.0681` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0861` n `52` status `ready` deltaP `33.6069` edge `0.0681` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.9858` n `149` status `ready` deltaP `30.1092` edge `0.0899` maxDD `-0.345`
- `news_risk_high->metal_24h` score `2.5728` n `57` status `ready` deltaP `18.8871` edge `0.1339` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `1.8432` n `52` status `ready` deltaP `26.3755` edge `-0.018` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.8432` n `52` status `ready` deltaP `26.3755` edge `-0.018` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.7084` n `149` status `ready` deltaP `23.6006` edge `0.0066` maxDD `-0.0593`
- `news_risk_high->index_4h` score `1.5362` n `71` status `ready` deltaP `21.5561` edge `0.0309` maxDD `-0.3938`
- `market_context_high->commodity_1h` score `1.2979` n `149` status `ready` deltaP `17.7079` edge `0.0278` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.6746` n `52` status `ready` deltaP `10.79` edge `0.0195` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6746` n `52` status `ready` deltaP `10.79` edge `0.0195` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2309` n `149` status `ready` deltaP `10.8006` edge `0.0052` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
