# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T01:07:27.651354+00:00`
- Price records: `672`
- Market context records: `6870`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11786`

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

- `market_context_high->unknown_24h` score `1.1443` n `176` status `ready` deltaP `-2.6666` edge `0.5397` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2324` n `224` status `ready` deltaP `2.5369` edge `0.0018` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.5956` n `224` status `ready` deltaP `-0.5988` edge `-0.0039` maxDD `-2.1443`
- `market_context_high->crypto_alt_1h` score `-0.6249` n `224` status `ready` deltaP `1.612` edge `0.0136` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.6461` n `224` status `ready` deltaP `3.3977` edge `0.0139` maxDD `-4.2314`
- `market_context_high->index_1h` score `-0.8406` n `224` status `ready` deltaP `-2.0771` edge `-0.0028` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.9406` n `224` status `ready` deltaP `-5.3411` edge `-0.0082` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9976` n `224` status `ready` deltaP `10.872` edge `0.006` maxDD `-2.1765`
- `market_context_high->commodity_24h` score `-1.0178` n `176` status `ready` deltaP `4.6055` edge `0.0713` maxDD `-5.2791`
- `market_context_high->commodity_4h` score `-1.349` n `224` status `ready` deltaP `-2.4102` edge `-0.0079` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6973` n `224` status `ready` deltaP `-3.7104` edge `-0.0266` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.8814` n `224` status `ready` deltaP `0.7378` edge `-0.0281` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.018` n `224` status `ready` deltaP `3.4138` edge `-0.0235` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.4328` n `224` status `ready` deltaP `-0.2073` edge `-0.0122` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.1279` n `224` status `ready` deltaP `-1.6797` edge `-0.0571` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1635` n `224` status `ready` deltaP `-0.6041` edge `-0.0432` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.1985` n `224` status `ready` deltaP `-9.5823` edge `0.0339` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.551` n `176` status `ready` deltaP `-9.7083` edge `-0.0109` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.4515` n `224` status `ready` deltaP `0.6544` edge `-0.1652` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.9359` n `176` status `ready` deltaP `-18.5866` edge `-0.1732` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
