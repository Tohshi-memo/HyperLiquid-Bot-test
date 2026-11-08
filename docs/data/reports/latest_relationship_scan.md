# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T23:07:49.078521+00:00`
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

- `market_context_high->unknown_4h` score `22.0606` n `45` status `ready` deltaP `-2.229` edge `1.898` maxDD `-0.9139`
- `market_context_high->equity_24h` score `4.7016` n `37` status `ready` deltaP `11.2472` edge `0.7463` maxDD `-31.3588`
- `market_context_high->fx_4h` score `1.3911` n `45` status `ready` deltaP `18.1741` edge `0.0312` maxDD `-0.2479`
- `market_context_high->index_24h` score `1.1796` n `37` status `ready` deltaP `14.8649` edge `0.1152` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.8882` n `37` status `ready` deltaP `10.9422` edge `0.0099` maxDD `-0.0397`
- `market_context_high->index_4h` score `0.4559` n `45` status `ready` deltaP `14.9899` edge `0.0222` maxDD `-2.4279`
- `market_context_high->commodity_4h` score `0.3935` n `45` status `ready` deltaP `5.4912` edge `0.0416` maxDD `-1.633`
- `market_context_high->commodity_1h` score `0.321` n `57` status `ready` deltaP `11.4692` edge `0.0193` maxDD `-1.7019`
- `market_context_high->equity_1h` score `0.1019` n `57` status `ready` deltaP `2.2245` edge `0.1134` maxDD `-5.2128`
- `market_context_high->metal_1h` score `-0.1454` n `57` status `ready` deltaP `1.3263` edge `0.0053` maxDD `-0.6226`
- `market_context_high->commodity_24h` score `-0.1482` n `37` status `ready` deltaP `2.2195` edge `0.0857` maxDD `-6.5601`
- `market_context_high->fx_1h` score `-0.4549` n `57` status `ready` deltaP `-4.3623` edge `0.0065` maxDD `-0.1928`
- `market_context_high->index_1h` score `-0.4558` n `57` status `ready` deltaP `-2.889` edge `0.019` maxDD `-0.6537`
- `market_context_high->metal_24h` score `-1.5403` n `37` status `ready` deltaP `8.0472` edge `-0.1267` maxDD `-1.4245`
- `market_context_high->metal_4h` score `-1.6203` n `45` status `ready` deltaP `-6.4939` edge `-0.0392` maxDD `-1.2025`
- `market_context_high->crypto_alt_1h` score `-1.9281` n `57` status `ready` deltaP `1.3026` edge `-0.0666` maxDD `-10.1421`
- `market_context_high->crypto_major_1h` score `-2.5925` n `57` status `ready` deltaP `-1.0926` edge `-0.1152` maxDD `-11.7911`
- `market_context_high->equity_4h` score `-3.0809` n `45` status `ready` deltaP `14.0515` edge `-0.0141` maxDD `-24.9053`
- `market_context_high->crypto_alt_4h` score `-5.3179` n `45` status `ready` deltaP `9.1023` edge `-0.226` maxDD `-18.8942`
- `market_context_high->crypto_major_24h` score `-8.3557` n `37` status `ready` deltaP `-9.0841` edge `-0.1597` maxDD `-32.0839`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
