# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T08:03:38.430510+00:00`
- Price records: `672`
- Market context records: `8176`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5904`

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

- `news_risk_high->unknown_24h` score `8757.0963` n `42` status `ready` deltaP `36.9792` edge `729.5115` maxDD `0.0`
- `market_context_high->equity_24h` score `19.0321` n `54` status `ready` deltaP `43.8658` edge `1.3846` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.3714` n `55` status `ready` deltaP `38.0128` edge `0.551` maxDD `-0.5442`
- `news_risk_high->equity_4h` score `8.4261` n `46` status `ready` deltaP `31.8863` edge `0.5186` maxDD `-1.3202`
- `market_context_high->metal_24h` score `8.245` n `54` status `ready` deltaP `42.8819` edge `0.4012` maxDD `0.0`
- `market_context_high->index_4h` score `4.0818` n `55` status `ready` deltaP `36.9346` edge `0.0982` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.4047` n `50` status `ready` deltaP `25.4551` edge `0.1449` maxDD `-1.1366`
- `news_risk_high->crypto_major_4h` score `3.3788` n `46` status `ready` deltaP `18.7235` edge `0.3689` maxDD `-2.1767`
- `market_context_high->equity_1h` score `3.3433` n `55` status `ready` deltaP `18.3642` edge `0.1765` maxDD `-0.6254`
- `news_risk_high->index_4h` score `2.716` n `46` status `ready` deltaP `22.4682` edge `0.0956` maxDD `-0.191`
- `market_context_high->index_1h` score `2.0061` n `55` status `ready` deltaP `23.1764` edge `0.0265` maxDD `-0.1069`
- `news_risk_high->crypto_major_1h` score `1.8607` n `50` status `ready` deltaP `11.7425` edge `0.1165` maxDD `-1.1783`
- `market_context_high->metal_4h` score `1.8518` n `55` status `ready` deltaP `21.8016` edge `0.0608` maxDD `-0.813`
- `news_risk_high->metal_4h` score `1.7994` n `46` status `ready` deltaP `16.8213` edge `0.0846` maxDD `-0.7433`
- `market_context_high->crypto_alt_24h` score `1.7963` n `54` status `ready` deltaP `4.8032` edge `0.5754` maxDD `-19.5034`
- `market_context_high->index_24h` score `1.7912` n `54` status `ready` deltaP `15.22` edge `0.1952` maxDD `-1.3621`
- `news_risk_high->crypto_alt_1h` score `1.6209` n `50` status `ready` deltaP `12.1916` edge `0.0972` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.349` n `46` status `ready` deltaP `15.2903` edge `0.2102` maxDD `-5.8012`
- `market_context_high->fx_24h` score `0.8016` n `54` status `ready` deltaP `17.8241` edge `0.0543` maxDD `-0.6283`
- `news_risk_high->index_1h` score `0.6092` n `50` status `ready` deltaP `8.4491` edge `0.0233` maxDD `-0.3089`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
