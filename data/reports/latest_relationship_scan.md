# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T15:07:31.685747+00:00`
- Price records: `672`
- Market context records: `8208`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5920`

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

- `news_risk_high->unknown_24h` score `8136.4527` n `43` status `ready` deltaP `36.9792` edge `677.7912` maxDD `0.0`
- `market_context_high->equity_24h` score `20.9705` n `35` status `ready` deltaP `40.511` edge `1.5685` maxDD `-4.9489`
- `market_context_high->crypto_alt_24h` score `14.2193` n `35` status `ready` deltaP `26.9196` edge `1.1084` maxDD `-4.2337`
- `market_context_high->equity_4h` score `8.881` n `35` status `ready` deltaP `46.9905` edge `0.4311` maxDD `-0.0094`
- `market_context_high->crypto_major_24h` score `8.6878` n `35` status `ready` deltaP `26.3988` edge `1.1091` maxDD `-9.7014`
- `market_context_high->metal_24h` score `8.2177` n `35` status `ready` deltaP `44.886` edge `0.3957` maxDD `-0.4771`
- `news_risk_high->equity_4h` score `7.2159` n `54` status `ready` deltaP `25.7735` edge `0.4892` maxDD `-3.4427`
- `market_context_high->crypto_major_4h` score `4.4743` n `35` status `ready` deltaP `19.9826` edge `0.3043` maxDD `-2.5062`
- `market_context_high->crypto_alt_4h` score `4.1283` n `35` status `ready` deltaP `17.4303` edge `0.2564` maxDD `-0.6195`
- `market_context_high->index_4h` score `3.8248` n `35` status `ready` deltaP `37.9225` edge `0.0702` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.6997` n `35` status `ready` deltaP `36.5897` edge `0.0822` maxDD `-0.0926`
- `news_risk_high->equity_1h` score `3.2249` n `54` status `ready` deltaP `22.7268` edge `0.1481` maxDD `-1.1366`
- `market_context_high->index_24h` score `2.936` n `35` status `ready` deltaP `27.2668` edge `0.2566` maxDD `-0.9576`
- `news_risk_high->crypto_major_4h` score `2.6825` n `54` status `ready` deltaP `13.5276` edge `0.3231` maxDD `-2.8833`
- `news_risk_high->index_4h` score `2.6809` n `54` status `ready` deltaP `22.4198` edge `0.093` maxDD `-0.191`
- `market_context_high->equity_1h` score `2.6296` n `35` status `ready` deltaP `14.367` edge `0.138` maxDD `-0.1718`
- `news_risk_high->crypto_major_1h` score `1.9769` n `54` status `ready` deltaP `13.4509` edge `0.1148` maxDD `-1.1783`
- `market_context_high->fx_24h` score `1.9326` n `35` status `ready` deltaP `34.9057` edge `0.0709` maxDD `-0.4666`
- `news_risk_high->crypto_alt_1h` score `1.8698` n `54` status `ready` deltaP `15.0033` edge `0.0992` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.4533` n `54` status `ready` deltaP `17.5362` edge `0.2086` maxDD `-5.8012`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
