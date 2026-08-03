# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T06:37:40.533598+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5903`

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

- `news_risk_high->unknown_24h` score `859.0763` n `36` status `ready` deltaP `19.2708` edge `71.5033` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `13.1487` n `40` status `ready` deltaP `51.4583` edge `0.7924` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.025` n `40` status `ready` deltaP `51.3194` edge `0.5894` maxDD `-0.6889`
- `news_risk_high->commodity_1h` score `1.0461` n `36` status `ready` deltaP `21.3905` edge `0.0127` maxDD `-0.6947`
- `news_risk_high->equity_4h` score `0.6893` n `36` status `ready` deltaP `-7.6897` edge `0.216` maxDD `-3.4427`
- `market_context_high->commodity_1h` score `0.337` n `47` status `ready` deltaP `7.2652` edge `0.0322` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.3013` n `47` status `ready` deltaP `5.0338` edge `0.0897` maxDD `-2.7703`
- `news_risk_high->index_4h` score `0.2669` n `36` status `ready` deltaP `0.7961` edge `0.055` maxDD `-0.3783`
- `market_context_high->fx_4h` score `0.0329` n `47` status `ready` deltaP `13.8752` edge `-0.0041` maxDD `-1.8531`
- `market_context_high->fx_1h` score `0.0243` n `47` status `ready` deltaP `7.5646` edge `-0.0084` maxDD `-0.7804`
- `news_risk_high->fx_24h` score `-0.007` n `36` status `ready` deltaP `8.1597` edge `0.0405` maxDD `-2.3054`
- `news_risk_high->commodity_4h` score `-0.078` n `36` status `ready` deltaP `8.8754` edge `-0.0143` maxDD `-1.7762`
- `news_risk_high->crypto_alt_1h` score `-0.2154` n `36` status `ready` deltaP `6.7532` edge `-0.0086` maxDD `-3.1233`
- `market_context_high->crypto_alt_4h` score `-0.233` n `47` status `ready` deltaP `2.1439` edge `0.0464` maxDD `-4.9116`
- `news_risk_high->fx_4h` score `-0.2964` n `36` status `ready` deltaP `1.0501` edge `0.0289` maxDD `-0.5789`
- `news_risk_high->metal_1h` score `-0.3392` n `36` status `ready` deltaP `-1.1976` edge `-0.0035` maxDD `-0.5599`
- `news_risk_high->fx_1h` score `-0.4201` n `36` status `ready` deltaP `-3.3101` edge `0.0003` maxDD `-0.2341`
- `news_risk_high->index_1h` score `-0.4542` n `36` status `ready` deltaP `-1.6467` edge `-0.0029` maxDD `-0.5845`
- `market_context_high->fx_24h` score `-0.6803` n `40` status `ready` deltaP `0.6597` edge `0.0369` maxDD `-2.506`
- `news_risk_high->metal_4h` score `-0.9083` n `36` status `ready` deltaP `-3.3876` edge `-0.018` maxDD `-0.8085`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
