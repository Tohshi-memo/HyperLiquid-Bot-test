# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T14:22:30.396551+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13344`

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

- `market_context_high->unknown_24h` score `17990.5481` n `56` status `ready` deltaP `8.596` edge `1499.1752` maxDD `-0.613`
- `news_risk_high->unknown_1h` score `416.6259` n `82` status `ready` deltaP `-4.8014` edge `34.793` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `18.2488` n `82` status `ready` deltaP `38.0236` edge `1.4143` maxDD `-9.098`
- `news_risk_high->crypto_alt_24h` score `18.2215` n `82` status `ready` deltaP `34.4785` edge `1.3374` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `8.3899` n `82` status `ready` deltaP `24.3398` edge `0.7149` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.7762` n `82` status `ready` deltaP `48.1118` edge `0.2616` maxDD `-0.0797`
- `market_context_high->crypto_alt_24h` score `5.87` n `56` status `ready` deltaP `21.1946` edge `0.7017` maxDD `-4.5683`
- `news_risk_high->metal_24h` score `4.5576` n `82` status `ready` deltaP `24.2431` edge `0.2636` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.1138` n `56` status `ready` deltaP `39.8276` edge `0.0773` maxDD `0.0`
- `market_context_high->equity_24h` score `2.2776` n `56` status `ready` deltaP `33.399` edge `0.3318` maxDD `-16.9971`
- `market_context_high->index_24h` score `2.0171` n `56` status `ready` deltaP `42.5369` edge `0.0585` maxDD `-2.6779`
- `market_context_high->metal_24h` score `1.6318` n `56` status `ready` deltaP `17.0567` edge `0.1317` maxDD `-0.5634`
- `risk_on_high->crypto_alt_4h` score `0.4328` n `65` status `ready` deltaP `10.7622` edge `0.1512` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.4328` n `65` status `ready` deltaP `10.7622` edge `0.1512` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.399` n `82` status `ready` deltaP `12.0427` edge `0.0337` maxDD `-0.6935`
- `risk_on_high->fx_1h` score `0.122` n `65` status `ready` deltaP `4.8526` edge `0.0034` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.122` n `65` status `ready` deltaP `4.8526` edge `0.0034` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.0484` n `65` status `ready` deltaP `4.0626` edge `0.0019` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0484` n `65` status `ready` deltaP `4.0626` edge `0.0019` maxDD `-0.3081`
- `market_context_high->fx_1h` score `-0.1034` n `143` status `ready` deltaP `2.8946` edge `-0.0009` maxDD `-0.5323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
