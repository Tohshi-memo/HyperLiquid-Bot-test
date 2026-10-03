# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T11:07:31.178930+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4806`

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

- `market_context_high->unknown_1h` score `366.3537` n `50` status `ready` deltaP `11.1737` edge `30.4599` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `294.2996` n `50` status `ready` deltaP `12.0244` edge `24.4448` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.2882` n `50` status `ready` deltaP `27.5529` edge `1.094` maxDD `-11.6271`
- `news_risk_high->crypto_major_4h` score `10.8403` n `66` status `ready` deltaP `39.9266` edge `0.6575` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `10.7026` n `50` status `ready` deltaP `35.2062` edge `0.7988` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.1661` n `66` status `ready` deltaP `28.3887` edge `0.7064` maxDD `-2.8784`
- `news_risk_high->crypto_alt_4h` score `7.8989` n `66` status `ready` deltaP `28.5526` edge `0.6023` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.4761` n `50` status `ready` deltaP `18.5327` edge `0.5698` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.3174` n `50` status `ready` deltaP `18.2496` edge `0.5337` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.3853` n `66` status `ready` deltaP `32.7162` edge `0.1632` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.9976` n `66` status `ready` deltaP `27.93` edge `0.2082` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.3525` n `50` status `ready` deltaP `15.4012` edge `0.243` maxDD `-3.6376`
- `news_risk_high->index_4h` score `3.0399` n `66` status `ready` deltaP `33.2295` edge `0.058` maxDD `-0.4296`
- `market_context_high->fx_4h` score `3.0383` n `50` status `ready` deltaP `34.1218` edge `0.0392` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0145` n `50` status `ready` deltaP `13.7006` edge `0.2049` maxDD `-2.2692`
- `news_risk_high->crypto_major_1h` score `2.9793` n `66` status `ready` deltaP `13.337` edge `0.1949` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.2115` n `66` status `ready` deltaP `17.8151` edge `0.1071` maxDD `-0.993`
- `market_context_high->fx_1h` score `1.4987` n `50` status `ready` deltaP `20.9401` edge `0.0117` maxDD `-0.113`
- `news_risk_high->index_1h` score `1.4402` n `66` status `ready` deltaP `18.9666` edge `0.0169` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.3285` n `66` status `ready` deltaP `3.9467` edge `0.1363` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
