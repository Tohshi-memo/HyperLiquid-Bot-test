# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T14:07:37.861081+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9930`

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

- `market_context_high->unknown_4h` score `46.7686` n `46` status `ready` deltaP `7.3171` edge `3.8486` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `30.9651` n `46` status `ready` deltaP `15.9647` edge `2.4896` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2272` n `46` status `ready` deltaP `12.3189` edge `1.2802` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `16.1747` n `46` status `ready` deltaP `15.1042` edge `1.2472` maxDD `0.0`
- `market_context_high->index_24h` score `5.538` n `46` status `ready` deltaP `20.1314` edge `0.336` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `3.2701` n `101` status `ready` deltaP `39.169` edge `0.2887` maxDD `-3.4467`
- `news_risk_high->crypto_major_24h` score `3.248` n `101` status `ready` deltaP `-9.3905` edge `1.0191` maxDD `-46.1999`
- `news_risk_high->crypto_alt_4h` score `2.2563` n `101` status `ready` deltaP `11.7544` edge `0.2306` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.0423` n `101` status `ready` deltaP `12.938` edge `0.1305` maxDD `-2.058`
- `market_context_high->index_4h` score `1.936` n `46` status `ready` deltaP `22.8592` edge `0.0223` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `1.5715` n `101` status `ready` deltaP `14.3458` edge `0.1611` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.3482` n `101` status `ready` deltaP `14.435` edge `0.0684` maxDD `-2.8494`
- `news_risk_high->fx_4h` score `1.0538` n `101` status `ready` deltaP `17.1773` edge `0.0369` maxDD `-0.421`
- `market_context_high->equity_4h` score `0.9928` n `46` status `ready` deltaP `7.5292` edge `0.0632` maxDD `-0.4529`
- `market_context_high->metal_24h` score `0.9654` n `46` status `ready` deltaP `21.9203` edge `-0.0423` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.852` n `46` status `ready` deltaP `7.3614` edge `0.0462` maxDD `-0.2751`
- `market_context_high->crypto_alt_4h` score `0.7008` n `46` status `ready` deltaP `7.4496` edge `0.0682` maxDD `-2.7574`
- `market_context_high->index_1h` score `0.6591` n `46` status `ready` deltaP `10.5051` edge `0.0102` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5562` n `101` status `ready` deltaP `14.1489` edge `0.0122` maxDD `-0.8144`
- `news_risk_high->metal_24h` score `0.4283` n `101` status `ready` deltaP `18.1105` edge `0.0186` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
