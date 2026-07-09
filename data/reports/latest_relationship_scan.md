# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T10:42:57.330048+00:00`
- Price records: `672`
- Market context records: `6174`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11132`

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

- `news_risk_high->crypto_alt_24h` score `12.5774` n `32` status `ready` deltaP `42.3848` edge `0.7803` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.2104` n `32` status `ready` deltaP `63.3106` edge `0.1788` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0187` n `32` status `ready` deltaP `41.8335` edge `0.0606` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.34` n `32` status `ready` deltaP `28.2138` edge `0.0208` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.7308` n `194` status `ready` deltaP `0.9824` edge `0.2385` maxDD `-3.7317`
- `news_risk_high->crypto_major_24h` score `1.6602` n `32` status `ready` deltaP `15.7956` edge `0.1855` maxDD `-4.2368`
- `news_risk_high->crypto_major_1h` score `1.2022` n `32` status `ready` deltaP `12.8597` edge `0.1151` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6222` n `32` status `ready` deltaP `8.2539` edge `0.0709` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.3562` n `194` status `ready` deltaP `-1.2879` edge `0.2915` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.131` n `194` status `ready` deltaP `20.3916` edge `0.1377` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.0853` n `32` status `ready` deltaP `9.663` edge `0.0118` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.1617` n `194` status `ready` deltaP `2.392` edge `0.0623` maxDD `-2.671`
- `market_context_high->fx_1h` score `-0.2956` n `194` status `ready` deltaP `1.1519` edge `-0.001` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.4856` n `32` status `ready` deltaP `13.5559` edge `-0.1103` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6861` n `194` status `ready` deltaP `3.3872` edge `0.0082` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7253` n `194` status `ready` deltaP `-1.8014` edge `-0.0038` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7852` n `32` status `ready` deltaP `-3.2138` edge `-0.0295` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8716` n `194` status `ready` deltaP `1.9408` edge `-0.0057` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.9815` n `194` status `ready` deltaP `3.0026` edge `0.0294` maxDD `-9.3536`
- `market_context_high->equity_1h` score `-1.0038` n `194` status `ready` deltaP `-2.8115` edge `0.0016` maxDD `-4.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
