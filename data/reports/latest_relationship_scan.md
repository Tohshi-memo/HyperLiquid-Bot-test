# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T03:22:34.242343+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4662`

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

- `market_context_high->unknown_4h` score `322.6694` n `50` status `ready` deltaP `13.2622` edge `26.8007` maxDD `0.0`
- `market_context_high->unknown_1h` score `298.101` n `59` status `ready` deltaP `7.244` edge `24.8115` maxDD `-0.4433`
- `market_context_high->crypto_alt_24h` score `12.9128` n `50` status `ready` deltaP `28.2461` edge `1.0581` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `11.9943` n `59` status `ready` deltaP `31.5219` edge `0.7994` maxDD `-0.1353`
- `news_risk_high->crypto_major_4h` score `10.938` n `65` status `ready` deltaP `40.1736` edge `0.664` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `10.776` n `50` status `ready` deltaP `33.9931` edge `0.813` maxDD `-9.3299`
- `news_risk_high->crypto_alt_4h` score `7.3583` n `65` status `ready` deltaP `24.3598` edge `0.5852` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.0228` n `50` status `ready` deltaP `15.8659` edge `0.5498` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.4674` n `50` status `ready` deltaP `14.3598` edge `0.4888` maxDD `-7.6465`
- `news_risk_high->index_24h` score `5.0598` n `59` status `ready` deltaP `35.182` edge `0.1871` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8999` n `65` status `ready` deltaP `26.9793` edge `0.2064` maxDD `-2.9013`
- `news_risk_high->index_4h` score `3.0648` n `65` status `ready` deltaP `33.2857` edge `0.0597` maxDD `-0.4296`
- `market_context_high->fx_4h` score `3.0334` n `50` status `ready` deltaP `34.061` edge `0.0392` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `3.0262` n `65` status `ready` deltaP `13.7586` edge `0.196` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.5658` n `65` status `ready` deltaP `21.9747` edge `0.1089` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `2.3022` n `59` status `ready` deltaP `10.3167` edge `0.1681` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.0962` n `65` status `ready` deltaP `25.7669` edge `0.0179` maxDD `-0.1997`
- `market_context_high->crypto_alt_1h` score `2.0238` n `59` status `ready` deltaP `7.7235` edge `0.1918` maxDD `-3.6376`
- `news_risk_high->crypto_alt_1h` score `1.5486` n `65` status `ready` deltaP `5.1681` edge `0.1465` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.2316` n `50` status `ready` deltaP `23.6984` edge `0.1017` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
