# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T14:07:35.614882+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13342`

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

- `market_context_high->unknown_24h` score `18024.5933` n `56` status `ready` deltaP `8.596` edge `1502.0123` maxDD `-0.613`
- `news_risk_high->unknown_1h` score `413.9859` n `82` status `ready` deltaP `-4.8014` edge `34.573` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `18.2026` n `82` status `ready` deltaP `37.8512` edge `1.4116` maxDD `-9.098`
- `news_risk_high->crypto_alt_24h` score `18.1963` n `82` status `ready` deltaP `34.4785` edge `1.3353` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `8.3365` n `82` status `ready` deltaP `24.1674` edge `0.7116` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.7576` n `82` status `ready` deltaP `47.9394` edge `0.2612` maxDD `-0.0797`
- `market_context_high->crypto_alt_24h` score `6.0291` n `56` status `ready` deltaP `21.1946` edge `0.7221` maxDD `-4.5683`
- `news_risk_high->metal_24h` score `4.5588` n `82` status `ready` deltaP `24.2431` edge `0.2637` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.1054` n `56` status `ready` deltaP `39.8276` edge `0.0766` maxDD `0.0`
- `market_context_high->equity_24h` score `2.7976` n `56` status `ready` deltaP `35.0123` edge `0.3635` maxDD `-15.3934`
- `market_context_high->index_24h` score `2.1906` n `56` status `ready` deltaP `44.1502` edge `0.0628` maxDD `-2.4366`
- `market_context_high->metal_24h` score `1.6633` n `56` status `ready` deltaP `17.0567` edge `0.1307` maxDD `-0.4935`
- `risk_on_high->crypto_alt_4h` score `0.4524` n `65` status `ready` deltaP `10.9146` edge `0.1527` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.4524` n `65` status `ready` deltaP `10.9146` edge `0.1527` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.4077` n `82` status `ready` deltaP `12.1951` edge `0.0338` maxDD `-0.6935`
- `risk_on_high->fx_1h` score `0.122` n `65` status `ready` deltaP `4.8526` edge `0.0034` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.122` n `65` status `ready` deltaP `4.8526` edge `0.0034` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.0364` n `65` status `ready` deltaP `4.2123` edge `0.0019` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0364` n `65` status `ready` deltaP `4.2123` edge `0.0019` maxDD `-0.3081`
- `market_context_high->fx_1h` score `-0.1034` n `143` status `ready` deltaP `2.8946` edge `-0.0009` maxDD `-0.5323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
