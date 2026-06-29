# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T14:07:31.437975+00:00`
- Price records: `672`
- Market context records: `5150`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5596`

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

- `market_context_high->unknown_24h` score `29.253` n `64` status `ready` deltaP `33.5069` edge `2.2403` maxDD `-1.0743`
- `market_context_high->unknown_4h` score `6.4327` n `129` status `ready` deltaP `19.0312` edge `0.5114` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `5.6275` n `140` status `ready` deltaP `10.231` edge `0.4649` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `5.3831` n `129` status `ready` deltaP `16.7411` edge `0.4969` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.3841` n `129` status `ready` deltaP `15.3431` edge `0.4923` maxDD `-14.0065`
- `market_context_high->crypto_alt_24h` score `4.1274` n `64` status `ready` deltaP `19.0972` edge `0.7958` maxDD `-27.5167`
- `market_context_high->crypto_major_24h` score `3.9192` n `64` status `ready` deltaP `17.3611` edge `0.8103` maxDD `-27.2194`
- `market_context_high->commodity_24h` score `1.8203` n `64` status `ready` deltaP `19.2708` edge `0.1465` maxDD `-5.1955`
- `market_context_high->equity_4h` score `1.2392` n `129` status `ready` deltaP `11.2403` edge `0.1922` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `0.9355` n `140` status `ready` deltaP `8.2806` edge `0.1473` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.8922` n `140` status `ready` deltaP `5.8511` edge `0.1315` maxDD `-5.0257`
- `market_context_high->metal_24h` score `0.8352` n `64` status `ready` deltaP `0.3472` edge `0.2356` maxDD `-5.4668`
- `market_context_high->equity_1h` score `0.6047` n `140` status `ready` deltaP `7.0958` edge `0.0624` maxDD `-2.745`
- `market_context_high->metal_1h` score `-0.0079` n `140` status `ready` deltaP `5.7699` edge `0.0171` maxDD `-1.8592`
- `market_context_high->index_1h` score `-0.1501` n `140` status `ready` deltaP `3.7896` edge `0.0126` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.2804` n `140` status `ready` deltaP `1.4286` edge `0.0001` maxDD `-0.646`
- `market_context_high->index_4h` score `-0.4206` n `129` status `ready` deltaP `6.1933` edge `0.0354` maxDD `-2.9391`
- `market_context_high->fx_24h` score `-0.4355` n `64` status `ready` deltaP `6.7708` edge `0.0081` maxDD `-0.8294`
- `market_context_high->commodity_1h` score `-0.6583` n `140` status `ready` deltaP `-0.3807` edge `-0.001` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.6593` n `129` status `ready` deltaP `2.1425` edge `0.005` maxDD `-1.638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
