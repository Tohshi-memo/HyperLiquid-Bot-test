# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T05:22:26.758591+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4858`

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

- `market_context_high->unknown_1h` score `366.2313` n `50` status `ready` deltaP `11.1737` edge `30.4497` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.4836` n `50` status `ready` deltaP `10.9756` edge `24.3838` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.523` n `50` status `ready` deltaP `23.6528` edge `0.9729` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.6394` n `70` status `ready` deltaP `33.7351` edge `0.7102` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.1234` n `50` status `ready` deltaP `31.3056` edge `0.6932` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `8.4672` n `88` status `ready` deltaP `32.7189` edge `0.5078` maxDD `-0.6258`
- `news_risk_high->crypto_alt_24h` score `7.8465` n `70` status `ready` deltaP `15.3671` edge `0.7928` maxDD `-14.3096`
- `news_risk_high->crypto_alt_4h` score `7.7382` n `88` status `ready` deltaP `31.5688` edge `0.5688` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.2709` n `50` status `ready` deltaP `16.628` edge `0.5654` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.8911` n `50` status `ready` deltaP `16.3415` edge `0.5109` maxDD `-7.6465`
- `news_risk_high->index_24h` score `3.8544` n `70` status `ready` deltaP `33.0407` edge `0.1168` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.5828` n `88` status `ready` deltaP `28.52` edge `0.1697` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.1702` n `50` status `ready` deltaP `14.2036` edge `0.2358` maxDD `-3.6376`
- `news_risk_high->crypto_major_24h` score `3.0637` n `70` status `ready` deltaP `12.1627` edge `0.4648` maxDD `-18.2464`
- `market_context_high->crypto_major_1h` score `2.9558` n `50` status `ready` deltaP `13.1018` edge `0.204` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7787` n `50` status `ready` deltaP `31.0122` edge `0.0383` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.4814` n `88` status `ready` deltaP `12.7382` edge `0.1574` maxDD `-1.5096`
- `news_risk_high->crypto_alt_1h` score `1.8973` n `88` status `ready` deltaP `8.4309` edge `0.1538` maxDD `-2.4854`
- `news_risk_high->metal_4h` score `1.4703` n `88` status `ready` deltaP `13.2761` edge `0.0881` maxDD `-0.993`
- `market_context_high->fx_1h` score `1.4112` n `50` status `ready` deltaP `19.8922` edge `0.0114` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
