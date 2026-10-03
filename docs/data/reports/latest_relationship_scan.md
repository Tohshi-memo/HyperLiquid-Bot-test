# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T04:37:32.414443+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4818`

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

- `market_context_high->unknown_1h` score `366.2241` n `50` status `ready` deltaP `11.3234` edge `30.4481` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.4704` n `50` status `ready` deltaP `10.9756` edge `24.3827` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.3481` n `50` status `ready` deltaP `23.1319` edge `0.9618` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.5506` n `70` status `ready` deltaP `33.7351` edge `0.7028` maxDD `-2.8784`
- `news_risk_high->crypto_alt_24h` score `9.9841` n `70` status `ready` deltaP `19.1319` edge `0.8734` maxDD `-9.5149`
- `market_context_high->crypto_major_24h` score `9.0166` n `50` status `ready` deltaP `31.3056` edge `0.6843` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `7.7977` n `91` status `ready` deltaP `29.9467` edge `0.487` maxDD `-0.9466`
- `news_risk_high->crypto_alt_4h` score `7.7469` n `91` status `ready` deltaP `31.9033` edge `0.5673` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.2637` n `50` status `ready` deltaP `16.628` edge `0.5648` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.8501` n `50` status `ready` deltaP `16.189` edge `0.5085` maxDD `-7.6465`
- `news_risk_high->crypto_major_24h` score `4.9641` n `70` status `ready` deltaP `12.1627` edge `0.5294` maxDD `-11.7448`
- `news_risk_high->index_24h` score `3.6496` n `70` status `ready` deltaP `31.7857` edge `0.1081` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.4483` n `91` status `ready` deltaP `27.6032` edge `0.1646` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.169` n `50` status `ready` deltaP `14.2036` edge `0.2357` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9713` n `50` status `ready` deltaP `13.2515` edge `0.2043` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7665` n `50` status `ready` deltaP `30.8598` edge `0.0383` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.1508` n `91` status `ready` deltaP `10.79` edge `0.147` maxDD `-1.5096`
- `news_risk_high->crypto_alt_1h` score `1.7747` n `91` status `ready` deltaP `7.5443` edge `0.1495` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.4232` n `50` status `ready` deltaP `20.0419` edge `0.0114` maxDD `-0.113`
- `market_context_high->fx_24h` score `1.2184` n `50` status `ready` deltaP `23.8056` edge `0.0993` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
