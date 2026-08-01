# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T19:37:23.219026+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5932`

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

- `news_risk_high->unknown_24h` score `5189.5351` n `60` status `ready` deltaP `33.0213` edge `432.2832` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.3441` n `53` status `ready` deltaP `56.231` edge `1.1102` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `5.7205` n `64` status `ready` deltaP `20.2363` edge `0.4015` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.2894` n `64` status `ready` deltaP `19.779` edge `0.078` maxDD `-0.1926`
- `market_context_high->commodity_24h` score `1.8943` n `53` status `ready` deltaP `28.6976` edge `0.2374` maxDD `-10.2019`
- `market_context_high->crypto_alt_4h` score `0.6645` n `53` status `ready` deltaP `9.1953` edge `0.1196` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.6493` n `68` status `ready` deltaP `9.0437` edge `0.0761` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.2549` n `53` status `ready` deltaP `14.4731` edge `0.0158` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.2127` n `64` status `ready` deltaP `6.3262` edge `0.0327` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1653` n `68` status `ready` deltaP `7.08` edge `0.0422` maxDD `-3.1233`
- `news_risk_high->crypto_major_4h` score `0.0477` n `64` status `ready` deltaP `4.7637` edge `0.1164` maxDD `-8.6965`
- `news_risk_high->fx_4h` score `0.036` n `64` status `ready` deltaP `11.3186` edge `0.0233` maxDD `-0.6604`
- `market_context_high->fx_1h` score `-0.0029` n `53` status `ready` deltaP `7.3523` edge `0.001` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.0839` n `68` status `ready` deltaP `2.0166` edge `0.0081` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.1035` n `68` status `ready` deltaP `2.2191` edge `0.0042` maxDD `-0.2475`
- `market_context_high->commodity_1h` score `-0.1057` n `53` status `ready` deltaP `3.7284` edge `0.0157` maxDD `-1.3282`
- `news_risk_high->metal_1h` score `-0.1263` n `68` status `ready` deltaP `2.6154` edge `0.0067` maxDD `-0.5599`
- `market_context_high->fx_24h` score `-0.1413` n `53` status `ready` deltaP `5.8467` edge `0.0409` maxDD `-2.506`
- `news_risk_high->crypto_major_1h` score `-0.1422` n `68` status `ready` deltaP `2.6682` edge `0.036` maxDD `-3.762`
- `market_context_high->commodity_4h` score `-0.2628` n `53` status `ready` deltaP `3.5722` edge `0.03` maxDD `-3.0005`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
