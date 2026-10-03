# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T03:07:32.229334+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4818`

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

- `market_context_high->unknown_1h` score `365.0182` n `50` status `ready` deltaP `10.7246` edge `30.3516` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.1621` n `50` status `ready` deltaP `10.061` edge `24.3631` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.6824` n `70` status `ready` deltaP `26.6617` edge `0.9762` maxDD `-5.4326`
- `market_context_high->crypto_alt_24h` score `11.0932` n `50` status `ready` deltaP `22.0903` edge `0.9475` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.2794` n `70` status `ready` deltaP `33.7351` edge `0.6802` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `8.9086` n `50` status `ready` deltaP `31.3056` edge `0.6753` maxDD `-9.3299`
- `news_risk_high->crypto_alt_4h` score `7.9036` n `97` status `ready` deltaP `32.482` edge `0.5765` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.3099` n `50` status `ready` deltaP `17.0854` edge `0.5656` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.995` n `70` status `ready` deltaP `12.1627` edge `0.5946` maxDD `-4.4217`
- `news_risk_high->crypto_major_4h` score `6.9895` n `97` status `ready` deltaP `26.405` edge `0.4524` maxDD `-1.6783`
- `market_context_high->crypto_alt_4h` score `5.7802` n `50` status `ready` deltaP `15.8841` edge `0.5047` maxDD `-7.6465`
- `news_risk_high->equity_4h` score `3.3734` n `97` status `ready` deltaP `27.7926` edge `0.1571` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.1774` n `50` status `ready` deltaP `14.3533` edge `0.2354` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9881` n `50` status `ready` deltaP `13.4012` edge `0.2047` maxDD `-2.2692`
- `news_risk_high->index_24h` score `2.8088` n `70` status `ready` deltaP `25.511` edge `0.0882` maxDD `-0.2696`
- `market_context_high->fx_4h` score `2.7787` n `50` status `ready` deltaP `31.0122` edge `0.0383` maxDD `-0.0791`
- `news_risk_high->metal_24h` score `1.8246` n `70` status `ready` deltaP `9.6329` edge `0.1924` maxDD `-2.3658`
- `news_risk_high->crypto_alt_1h` score `1.6853` n `97` status `ready` deltaP `7.1162` edge `0.1449` maxDD `-2.4854`
- `news_risk_high->crypto_major_1h` score `1.5536` n `97` status `ready` deltaP `8.1641` edge `0.132` maxDD `-1.8902`
- `market_context_high->fx_1h` score `1.4352` n `50` status `ready` deltaP `20.1916` edge `0.0114` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
