# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T11:37:23.551057+00:00`
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

- `market_context_high->unknown_1h` score `366.4905` n `50` status `ready` deltaP `11.4731` edge `30.4693` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `294.3284` n `50` status `ready` deltaP `12.0244` edge `24.4472` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.4143` n `50` status `ready` deltaP `27.8995` edge `1.1022` maxDD `-11.6271`
- `news_risk_high->crypto_major_4h` score `11.0105` n `64` status `ready` deltaP `39.5952` edge `0.6739` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `10.8623` n `50` status `ready` deltaP `35.5529` edge `0.8098` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.226` n `64` status `ready` deltaP `28.0573` edge `0.7136` maxDD `-2.8784`
- `news_risk_high->crypto_alt_4h` score `7.8496` n `64` status `ready` deltaP `27.9371` edge `0.6023` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.4785` n `50` status `ready` deltaP `18.5327` edge `0.57` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.321` n `50` status `ready` deltaP `18.2496` edge `0.534` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.4363` n `64` status `ready` deltaP `32.5742` edge `0.1684` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `4.0089` n `64` status `ready` deltaP `27.5614` edge `0.2116` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.3381` n `50` status `ready` deltaP `15.2515` edge `0.2428` maxDD `-3.6376`
- `market_context_high->fx_4h` score `3.0638` n `50` status `ready` deltaP `34.4262` edge `0.0393` maxDD `-0.0791`
- `news_risk_high->index_4h` score `3.0606` n `64` status `ready` deltaP `33.2025` edge `0.0599` maxDD `-0.4296`
- `market_context_high->crypto_major_1h` score `3.0288` n `50` status `ready` deltaP `13.8503` edge `0.2051` maxDD `-2.2692`
- `news_risk_high->crypto_major_1h` score `2.9544` n `64` status `ready` deltaP `12.3503` edge `0.1994` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.1739` n `64` status `ready` deltaP `17.0305` edge `0.1092` maxDD `-0.993`
- `news_risk_high->index_1h` score `1.7266` n `64` status `ready` deltaP `21.192` edge `0.0176` maxDD `-0.1997`
- `market_context_high->fx_1h` score `1.5226` n `50` status `ready` deltaP `21.2395` edge `0.0117` maxDD `-0.113`
- `news_risk_high->crypto_alt_1h` score `1.5105` n `64` status `ready` deltaP `5.5015` edge `0.1411` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
