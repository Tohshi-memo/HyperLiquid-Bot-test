# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T19:22:24.271220+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3144`

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

- `news_risk_high->unknown_1h` score `3218.676` n `31` status `ready` deltaP `2.231` edge `268.2257` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3212.2062` n `31` status `ready` deltaP `4.3962` edge `267.6602` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `30.0969` n `31` status `ready` deltaP `39.2361` edge `2.2465` maxDD `0.0`
- `news_risk_high->equity_24h` score `27.5698` n `31` status `ready` deltaP `38.3681` edge `2.0417` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `23.9417` n `31` status `ready` deltaP `38.5417` edge `1.7382` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.1917` n `31` status `ready` deltaP `25.236` edge `0.7681` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.1455` n `31` status `ready` deltaP `37.3771` edge `0.561` maxDD `-2.178`
- `news_risk_high->metal_24h` score `6.9111` n `31` status `ready` deltaP `24.916` edge `0.4373` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.5972` n `31` status `ready` deltaP `18.3025` edge `0.8655` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.8885` n `31` status `ready` deltaP `41.1907` edge `0.1456` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.839` n `31` status `ready` deltaP `39.7569` edge `0.1382` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.4459` n `31` status `ready` deltaP `19.8377` edge `0.1736` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.1978` n `31` status `ready` deltaP `35.7003` edge `0.0545` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6554` n `31` status `ready` deltaP `31.6931` edge `0.0185` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3395` n `31` status `ready` deltaP `8.6633` edge `0.2883` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1061` n `31` status `ready` deltaP `11.6573` edge `0.228` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4285` n `31` status `ready` deltaP `28.3851` edge `0.0218` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.8602` n `31` status `ready` deltaP `14.4915` edge `0.0694` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.2826` n `31` status `ready` deltaP `10.3511` edge `0.007` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4826` n `31` status `ready` deltaP `-3.1099` edge `0.0067` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
