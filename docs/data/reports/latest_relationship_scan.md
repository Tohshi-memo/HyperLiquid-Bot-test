# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T06:52:28.686993+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4826`

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

- `market_context_high->unknown_1h` score `366.139` n `50` status `ready` deltaP `11.024` edge `30.443` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.631` n `50` status `ready` deltaP `11.7378` edge `24.391` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.9099` n `50` status `ready` deltaP `24.6944` edge `0.9982` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.8398` n `70` status `ready` deltaP `33.7351` edge `0.7269` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.4527` n `50` status `ready` deltaP `32.3472` edge `0.7137` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `9.1294` n `82` status `ready` deltaP `35.6708` edge `0.5433` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.6063` n `82` status `ready` deltaP `30.6402` edge `0.564` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.3231` n `50` status `ready` deltaP `17.0854` edge `0.5667` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.9585` n `50` status `ready` deltaP `16.4939` edge `0.5155` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.074` n `70` status `ready` deltaP `33.0407` edge `0.1351` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8698` n `82` status `ready` deltaP `30.4878` edge `0.1805` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.2614` n `50` status `ready` deltaP `14.8024` edge `0.2394` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9689` n `50` status `ready` deltaP `13.2515` edge `0.2041` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8555` n `50` status `ready` deltaP `31.9268` edge `0.0386` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.5356` n `82` status `ready` deltaP `12.6661` edge `0.1624` maxDD `-1.5096`
- `news_risk_high->crypto_alt_24h` score `2.2661` n `70` status `ready` deltaP `7.8373` edge `0.6098` maxDD `-22.7223`
- `news_risk_high->metal_4h` score `1.9793` n `82` status `ready` deltaP `17.0731` edge `0.0927` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.5228` n `82` status `ready` deltaP `6.1195` edge `0.138` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.4484` n `50` status `ready` deltaP `20.3413` edge `0.0115` maxDD `-0.113`
- `news_risk_high->index_4h` score `1.3671` n `82` status `ready` deltaP `19.3598` edge `0.0444` maxDD `-0.4296`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
