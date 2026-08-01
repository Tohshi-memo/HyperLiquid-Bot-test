# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T19:52:24.567324+00:00`
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

- `news_risk_high->unknown_24h` score `5189.4289` n `60` status `ready` deltaP `32.848` edge `432.2755` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.3892` n `53` status `ready` deltaP `56.4043` edge `1.1128` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `5.4759` n `65` status `ready` deltaP `19.2589` edge `0.3918` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.1292` n `65` status `ready` deltaP `18.8016` edge `0.0761` maxDD `-0.2539`
- `market_context_high->commodity_24h` score `1.8752` n `53` status `ready` deltaP `28.5242` edge `0.2361` maxDD `-10.2019`
- `market_context_high->crypto_alt_4h` score `0.6739` n `53` status `ready` deltaP `9.1953` edge `0.1208` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.6625` n `68` status `ready` deltaP `9.1934` edge `0.0762` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.2549` n `53` status `ready` deltaP `14.4731` edge `0.0158` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.2334` n `65` status `ready` deltaP `6.7988` edge `0.0322` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1521` n `68` status `ready` deltaP `6.9303` edge `0.0415` maxDD `-3.1233`
- `news_risk_high->fx_4h` score `0.0956` n `65` status `ready` deltaP `12.0638` edge `0.0233` maxDD `-0.6604`
- `market_context_high->fx_1h` score `0.0091` n `53` status `ready` deltaP `7.502` edge `0.001` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.0754` n `68` status `ready` deltaP `2.1663` edge `0.0082` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.0957` n `68` status `ready` deltaP `2.3688` edge `0.0042` maxDD `-0.2475`
- `market_context_high->commodity_1h` score `-0.1057` n `53` status `ready` deltaP `3.7284` edge `0.0157` maxDD `-1.3282`
- `market_context_high->fx_24h` score `-0.1292` n `53` status `ready` deltaP `6.02` edge `0.0413` maxDD `-2.506`
- `news_risk_high->metal_1h` score `-0.1349` n `68` status `ready` deltaP `2.4657` edge `0.0066` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1563` n `68` status `ready` deltaP `2.5185` edge `0.0352` maxDD `-3.762`
- `news_risk_high->crypto_major_4h` score `-0.2603` n `65` status `ready` deltaP `3.9704` edge `0.1001` maxDD `-9.7953`
- `market_context_high->commodity_4h` score `-0.2731` n `53` status `ready` deltaP `3.4198` edge `0.0297` maxDD `-3.0005`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
