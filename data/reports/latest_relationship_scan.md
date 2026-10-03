# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T11:22:25.010311+00:00`
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

- `market_context_high->unknown_1h` score `366.4233` n `50` status `ready` deltaP `11.3234` edge `30.4647` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `294.3104` n `50` status `ready` deltaP `12.0244` edge `24.4457` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.3536` n `50` status `ready` deltaP `27.7262` edge `1.0983` maxDD `-11.6271`
- `news_risk_high->crypto_major_4h` score `10.9268` n `65` status `ready` deltaP `39.7635` edge `0.6658` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `10.7837` n `50` status `ready` deltaP `35.3795` edge `0.8044` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.1963` n `65` status `ready` deltaP `28.2256` edge `0.71` maxDD `-2.8784`
- `news_risk_high->crypto_alt_4h` score `7.8902` n `65` status `ready` deltaP `28.2496` edge `0.6036` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.4773` n `50` status `ready` deltaP `18.5327` edge `0.5699` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.3222` n `50` status `ready` deltaP `18.2496` edge `0.5341` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.4109` n `65` status `ready` deltaP `32.6463` edge `0.1658` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `4.0097` n `65` status `ready` deltaP `27.8258` edge `0.2099` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.3537` n `50` status `ready` deltaP `15.4012` edge `0.2431` maxDD `-3.6376`
- `market_context_high->fx_4h` score `3.0517` n `50` status `ready` deltaP `34.274` edge `0.0393` maxDD `-0.0791`
- `news_risk_high->index_4h` score `3.0498` n `65` status `ready` deltaP `33.2186` edge `0.0589` maxDD `-0.4296`
- `market_context_high->crypto_major_1h` score `3.0288` n `50` status `ready` deltaP `13.8503` edge `0.2051` maxDD `-2.2692`
- `news_risk_high->crypto_major_1h` score `2.9681` n `65` status `ready` deltaP `12.9272` edge `0.1967` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.1939` n `65` status `ready` deltaP `17.4312` edge `0.1082` maxDD `-0.993`
- `news_risk_high->index_1h` score `1.5826` n `65` status `ready` deltaP `20.0622` edge `0.0173` maxDD `-0.1997`
- `market_context_high->fx_1h` score `1.5106` n `50` status `ready` deltaP `21.0898` edge `0.0117` maxDD `-0.113`
- `news_risk_high->crypto_alt_1h` score `1.4293` n `65` status `ready` deltaP `4.7858` edge `0.1391` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
