# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T10:52:27.236922+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7492`

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

- `market_context_high->unknown_1h` score `419.0898` n `49` status `ready` deltaP `7.8394` edge `34.8768` maxDD `-0.0597`
- `news_risk_high->unknown_24h` score `390.2296` n `135` status `ready` deltaP `1.9097` edge `32.5064` maxDD `0.0`
- `market_context_high->unknown_4h` score `358.2705` n `37` status `ready` deltaP `8.2317` edge `29.801` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.7159` n `135` status `ready` deltaP `26.9907` edge `1.234` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `7.1627` n `135` status `ready` deltaP `25.6019` edge `0.6611` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.8193` n `135` status `ready` deltaP `23.9931` edge `0.7237` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.465` n `135` status `ready` deltaP `31.794` edge `0.1246` maxDD `-0.4916`
- `market_context_high->crypto_major_4h` score `3.1394` n `37` status `ready` deltaP `8.7385` edge `0.2737` maxDD `-3.294`
- `news_risk_high->metal_24h` score `3.054` n `135` status `ready` deltaP `23.9699` edge `0.2221` maxDD `-2.192`
- `market_context_high->fx_4h` score `3.0059` n `37` status `ready` deltaP `34.2535` edge `0.0352` maxDD `-0.0449`
- `news_risk_high->equity_4h` score `2.6101` n `135` status `ready` deltaP `27.7992` edge `0.1923` maxDD `-9.143`
- `market_context_high->crypto_alt_1h` score `2.4582` n `49` status `ready` deltaP `15.5505` edge `0.1675` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `2.3304` n `49` status `ready` deltaP `14.0688` edge `0.1614` maxDD `-3.546`
- `market_context_high->fx_1h` score `1.3809` n `49` status `ready` deltaP `19.4977` edge `0.0115` maxDD `-0.113`
- `news_risk_high->crypto_alt_4h` score `1.2015` n `135` status `ready` deltaP `9.283` edge `0.3042` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.8872` n `135` status `ready` deltaP `8.2036` edge `0.1103` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.8852` n `135` status `ready` deltaP `9.4012` edge `0.0734` maxDD `-1.6514`
- `news_risk_high->index_1h` score `0.4802` n `135` status `ready` deltaP `8.6682` edge `0.011` maxDD `-0.302`
- `market_context_high->crypto_alt_4h` score `0.318` n `37` status `ready` deltaP `5.0388` edge `0.1365` maxDD `-7.6792`
- `market_context_high->metal_1h` score `-0.0486` n `49` status `ready` deltaP `3.715` edge `0.0099` maxDD `-0.6053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
