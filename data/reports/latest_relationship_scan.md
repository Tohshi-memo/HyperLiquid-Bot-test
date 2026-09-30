# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T16:07:45.010240+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6916`

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

- `market_context_high->unknown_1h` score `308.1987` n `50` status `ready` deltaP `7.5808` edge `25.6376` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `281.8305` n `50` status `ready` deltaP `8.2317` edge `23.431` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.0379` n `135` status `ready` deltaP `26.9907` edge `1.1775` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.7001` n `50` status `ready` deltaP `17.8476` edge `0.5097` maxDD `-3.294`
- `news_risk_high->equity_24h` score `6.4157` n `135` status `ready` deltaP `24.5602` edge `0.6058` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.0859` n `135` status `ready` deltaP `23.6459` edge `0.6649` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.3981` n `50` status `ready` deltaP `13.1402` edge `0.3249` maxDD `-7.6792`
- `news_risk_high->index_24h` score `3.085` n `135` status `ready` deltaP `29.1898` edge `0.1103` maxDD `-0.4916`
- `market_context_high->fx_4h` score `3.0104` n `50` status `ready` deltaP `33.9085` edge `0.0383` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.001` n `50` status `ready` deltaP `15.6467` edge `0.1908` maxDD `-2.2692`
- `news_risk_high->metal_24h` score `2.7306` n `135` status `ready` deltaP `21.7129` edge `0.2102` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.6314` n `50` status `ready` deltaP `13.4551` edge `0.1959` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.2717` n `135` status `ready` deltaP `25.9699` edge `0.1763` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.398` n `50` status `ready` deltaP `19.7425` edge `0.0113` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.8012` n `135` status `ready` deltaP `9.1018` edge `0.0684` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5333` n `135` status `ready` deltaP `7.4551` edge `0.0858` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.3723` n `135` status `ready` deltaP `7.6203` edge `0.009` maxDD `-0.302`
- `market_context_high->equity_1h` score `0.0062` n `50` status `ready` deltaP `1.1018` edge `0.0585` maxDD `-1.2043`
- `market_context_high->commodity_1h` score `-0.0727` n `50` status `ready` deltaP `8.1497` edge `-0.009` maxDD `-2.3717`
- `market_context_high->metal_1h` score `-0.179` n `50` status `ready` deltaP `2.6946` edge `0.0094` maxDD `-0.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
