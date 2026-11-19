# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T15:52:41.027695+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2592`

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

- `market_context_high->unknown_1h` score `12131.6775` n `107` status `ready` deltaP `0.7248` edge `1010.9881` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `8046.3562` n `102` status `ready` deltaP `-0.3736` edge `670.5606` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `25.1059` n `88` status `ready` deltaP `45.6281` edge `1.8473` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.6923` n `88` status `ready` deltaP `23.5322` edge `1.4814` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.9517` n `102` status `ready` deltaP `3.7243` edge `0.4197` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.3266` n `102` status `ready` deltaP `4.6389` edge `0.2872` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.5181` n `102` status `ready` deltaP `18.5348` edge `0.0486` maxDD `-5.9858`
- `market_context_high->metal_24h` score `0.3763` n `88` status `ready` deltaP `18.7184` edge `0.2154` maxDD `-14.7068`
- `market_context_high->metal_1h` score `-0.2372` n `107` status `ready` deltaP `3.611` edge `0.012` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.3292` n `107` status `ready` deltaP `3.9831` edge `0.0709` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.3506` n `107` status `ready` deltaP `2.0776` edge `0.0024` maxDD `-1.2295`
- `market_context_high->index_4h` score `-1.2131` n `102` status `ready` deltaP `-3.0727` edge `-0.0007` maxDD `-4.7471`
- `market_context_high->crypto_alt_1h` score `-1.3651` n `107` status `ready` deltaP `-2.8583` edge `0.0275` maxDD `-5.4428`
- `market_context_high->fx_1h` score `-1.6387` n `107` status `ready` deltaP `-11.8278` edge `-0.002` maxDD `-0.4566`
- `market_context_high->equity_1h` score `-1.6791` n `107` status `ready` deltaP `4.8813` edge `0.0054` maxDD `-10.8962`
- `market_context_high->fx_4h` score `-2.3764` n `102` status `ready` deltaP `-14.9061` edge `-0.0037` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4991` n `107` status `ready` deltaP `-10.3713` edge `-0.0313` maxDD `-3.9584`
- `market_context_high->fx_24h` score `-7.1063` n `88` status `ready` deltaP `-23.2481` edge `-0.0099` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.3674` n `102` status `ready` deltaP `-31.0049` edge `-0.1287` maxDD `-14.9509`
- `market_context_high->equity_4h` score `-9.235` n `102` status `ready` deltaP `-8.0853` edge `-0.048` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
