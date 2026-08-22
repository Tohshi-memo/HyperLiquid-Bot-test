# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T09:52:22.823829+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14748`

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

- `market_context_high->unknown_1h` score `1.179` n `138` status `ready` deltaP `7.6608` edge `0.0699` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.4445` n `133` status `ready` deltaP `19.7185` edge `-0.0505` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0955` n `133` status `ready` deltaP `7.9051` edge `0.0098` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.0345` n `138` status `ready` deltaP `7.9233` edge `0.0047` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1101` n `138` status `ready` deltaP `2.5753` edge `0.0046` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2392` n `133` status `ready` deltaP `7.2334` edge `-0.0173` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.2418` n `138` status `ready` deltaP `5.9533` edge `0.0363` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.242` n `138` status `ready` deltaP `2.2998` edge `-0.0045` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.611` n `133` status `ready` deltaP `2.164` edge `0.0108` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.6933` n `133` status `ready` deltaP `-1.3135` edge `0.0049` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7191` n `138` status `ready` deltaP `-5.1441` edge `-0.0013` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-1.364` n `138` status `ready` deltaP `-1.0348` edge `-0.0099` maxDD `-3.7493`
- `market_context_high->commodity_24h` score `-1.5746` n `112` status `ready` deltaP `-3.869` edge `0.0779` maxDD `-4.666`
- `market_context_high->crypto_alt_4h` score `-1.6689` n `133` status `ready` deltaP `5.1176` edge `-0.0462` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.7119` n `133` status `ready` deltaP `-1.0579` edge `0.0681` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.2509` n `112` status `ready` deltaP `-4.5883` edge `0.004` maxDD `-2.2121`
- `market_context_high->crypto_major_1h` score `-2.5254` n `138` status `ready` deltaP `-3.4127` edge `-0.0852` maxDD `-4.1996`
- `market_context_high->index_24h` score `-4.286` n `112` status `ready` deltaP `-6.2004` edge `-0.0498` maxDD `-19.3346`
- `market_context_high->crypto_major_4h` score `-5.1741` n `133` status `ready` deltaP `-1.4968` edge `-0.3191` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-5.2273` n `112` status `ready` deltaP `-21.8502` edge `-0.1937` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
