# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T08:52:27.244194+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8658`

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

- `news_risk_high->unknown_4h` score `384.6228` n `83` status `ready` deltaP `-21.8153` edge `32.2868` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `14.1281` n `83` status `ready` deltaP `34.3583` edge `1.0862` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `13.1672` n `83` status `ready` deltaP `26.4244` edge `1.1206` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `9.6085` n `83` status `ready` deltaP `35.6573` edge `0.7404` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `8.7254` n `52` status `ready` deltaP `47.2222` edge `0.4123` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.7254` n `52` status `ready` deltaP `47.2222` edge `0.4123` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.4262` n `149` status `ready` deltaP `40.5108` edge `0.4013` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.9917` n `83` status `ready` deltaP `41.0873` edge `0.243` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.1482` n `83` status `ready` deltaP `31.4696` edge `0.1813` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.6169` n `52` status `ready` deltaP `33.8408` edge `-0.0033` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.6169` n `52` status `ready` deltaP `33.8408` edge `-0.0033` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.482` n `149` status `ready` deltaP `31.0659` edge `0.0213` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.3956` n `52` status `ready` deltaP `29.4911` edge `0.038` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.3956` n `52` status `ready` deltaP `29.4911` edge `0.038` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.2953` n `149` status `ready` deltaP `25.9934` edge `0.0598` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9671` n `149` status `ready` deltaP `14.8636` edge `0.0192` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.3439` n `52` status `ready` deltaP `7.9457` edge `0.0109` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3439` n `52` status `ready` deltaP `7.9457` edge `0.0109` maxDD `-0.1507`
- `news_risk_high->index_4h` score `0.324` n `83` status `ready` deltaP `11.1262` edge `0.0302` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.0758` n `52` status `ready` deltaP `5.2165` edge `0.0055` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
