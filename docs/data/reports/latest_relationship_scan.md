# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T23:12:51.305674+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6551`

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

- `market_context_high->unknown_4h` score `22.0402` n `45` status `ready` deltaP `-2.229` edge `1.8963` maxDD `-0.9139`
- `market_context_high->equity_24h` score `4.7016` n `37` status `ready` deltaP `11.2472` edge `0.7463` maxDD `-31.3588`
- `market_context_high->fx_4h` score `1.387` n `45` status `ready` deltaP `18.1741` edge `0.031` maxDD `-0.2597`
- `market_context_high->index_24h` score `1.1788` n `37` status `ready` deltaP `14.8649` edge `0.1151` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.8882` n `37` status `ready` deltaP `10.9422` edge `0.0099` maxDD `-0.0397`
- `market_context_high->index_4h` score `0.4567` n `45` status `ready` deltaP `14.9899` edge `0.0223` maxDD `-2.4279`
- `market_context_high->commodity_4h` score `0.3803` n `45` status `ready` deltaP `5.4912` edge `0.0405` maxDD `-1.633`
- `market_context_high->commodity_1h` score `0.3155` n `57` status `ready` deltaP `11.4692` edge `0.0186` maxDD `-1.7019`
- `market_context_high->equity_1h` score `0.1058` n `57` status `ready` deltaP `2.2245` edge `0.1139` maxDD `-5.2128`
- `market_context_high->metal_1h` score `-0.1423` n `57` status `ready` deltaP `1.3263` edge `0.0057` maxDD `-0.6226`
- `market_context_high->commodity_24h` score `-0.1475` n `37` status `ready` deltaP `2.2195` edge `0.0858` maxDD `-6.5601`
- `market_context_high->index_1h` score `-0.455` n `57` status `ready` deltaP `-2.889` edge `0.0191` maxDD `-0.6537`
- `market_context_high->fx_1h` score `-0.4565` n `57` status `ready` deltaP `-4.3623` edge `0.0063` maxDD `-0.1928`
- `market_context_high->metal_24h` score `-1.5403` n `37` status `ready` deltaP `8.0472` edge `-0.1267` maxDD `-1.4245`
- `market_context_high->metal_4h` score `-1.6143` n `45` status `ready` deltaP `-6.4939` edge `-0.0387` maxDD `-1.2025`
- `market_context_high->crypto_alt_1h` score `-1.879` n `57` status `ready` deltaP `1.3026` edge `-0.0603` maxDD `-10.1421`
- `market_context_high->crypto_major_1h` score `-2.5395` n `57` status `ready` deltaP `-1.0926` edge `-0.1084` maxDD `-11.7911`
- `market_context_high->equity_4h` score `-3.0737` n `45` status `ready` deltaP `14.0515` edge `-0.0135` maxDD `-24.9053`
- `market_context_high->crypto_alt_4h` score `-5.1682` n `45` status `ready` deltaP `9.1023` edge `-0.2182` maxDD `-18.5201`
- `market_context_high->crypto_major_24h` score `-8.3641` n `37` status `ready` deltaP `-9.0841` edge `-0.1604` maxDD `-32.0839`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
