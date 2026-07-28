# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T15:03:13.506694+00:00`
- Price records: `672`
- Market context records: `8207`
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
- `market_context_high->equity_24h` score `21.0269` n `35` status `ready` deltaP `40.511` edge `1.5732` maxDD `-4.9489`
- `market_context_high->crypto_alt_24h` score `14.2493` n `35` status `ready` deltaP `26.9196` edge `1.1109` maxDD `-4.2337`
- `market_context_high->equity_4h` score `8.8786` n `35` status `ready` deltaP `46.9905` edge `0.4309` maxDD `-0.0094`
- `market_context_high->crypto_major_24h` score `8.7105` n `35` status `ready` deltaP `26.3988` edge `1.112` maxDD `-9.7014`
- `market_context_high->metal_24h` score `8.2277` n `35` status `ready` deltaP `44.886` edge `0.3963` maxDD `-0.4583`
- `news_risk_high->equity_4h` score `7.2135` n `54` status `ready` deltaP `25.7735` edge `0.489` maxDD `-3.4427`
- `market_context_high->crypto_major_4h` score `4.4719` n `35` status `ready` deltaP `19.9826` edge `0.3041` maxDD `-2.5062`
- `market_context_high->crypto_alt_4h` score `4.1149` n `35` status `ready` deltaP `17.2778` edge `0.2563` maxDD `-0.6195`
- `market_context_high->index_4h` score `3.8248` n `35` status `ready` deltaP `37.9225` edge `0.0702` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.6997` n `35` status `ready` deltaP `36.5897` edge `0.0822` maxDD `-0.0926`
- `news_risk_high->equity_1h` score `3.2213` n `54` status `ready` deltaP `22.7268` edge `0.1478` maxDD `-1.1366`
- `market_context_high->index_24h` score `2.9399` n `35` status `ready` deltaP `27.2668` edge `0.2571` maxDD `-0.9576`
- `news_risk_high->crypto_major_4h` score `2.6809` n `54` status `ready` deltaP `13.5276` edge `0.3229` maxDD `-2.8833`
- `news_risk_high->index_4h` score `2.6809` n `54` status `ready` deltaP `22.4198` edge `0.093` maxDD `-0.191`
- `market_context_high->equity_1h` score `2.626` n `35` status `ready` deltaP `14.367` edge `0.1377` maxDD `-0.1718`
- `news_risk_high->crypto_major_1h` score `1.9745` n `54` status `ready` deltaP `13.4509` edge `0.1146` maxDD `-1.1783`
- `market_context_high->fx_24h` score `1.9318` n `35` status `ready` deltaP `34.9057` edge `0.0708` maxDD `-0.4666`
- `news_risk_high->crypto_alt_1h` score `1.8686` n `54` status `ready` deltaP `15.0033` edge `0.0991` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.4446` n `54` status `ready` deltaP `17.3837` edge `0.2085` maxDD `-5.8012`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
