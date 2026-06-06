# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T03:52:25.595227+00:00`
- Price records: `672`
- Market context records: `3035`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6988`

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

- `market_context_high->crypto_alt_24h` score `23.2833` n `99` status `ready` deltaP `11.332` edge `2.2564` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `13.1085` n `99` status `ready` deltaP `23.1061` edge `0.9848` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `12.8297` n `99` status `ready` deltaP `42.3769` edge `0.8107` maxDD `-1.2589`
- `market_context_high->equity_24h` score `8.2941` n `99` status `ready` deltaP `22.5063` edge `1.1885` maxDD `-18.3486`
- `market_context_high->index_24h` score `8.0275` n `99` status `ready` deltaP `22.096` edge `0.6472` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.873` n `125` status `ready` deltaP `19.4451` edge `0.1745` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `0.0253` n `129` status `ready` deltaP `2.2908` edge `0.0291` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.3459` n `125` status `ready` deltaP `1.8463` edge `0.0642` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.3788` n `129` status `ready` deltaP `4.2369` edge `0.0246` maxDD `-4.1126`
- `market_context_high->index_4h` score `-0.466` n `125` status `ready` deltaP `13.5061` edge `0.0757` maxDD `-13.705`
- `market_context_high->equity_1h` score `-0.4754` n `129` status `ready` deltaP `3.5685` edge `0.0368` maxDD `-6.7232`
- `market_context_high->fx_1h` score `-0.5252` n `129` status `ready` deltaP `-4.5897` edge `0.0001` maxDD `-0.2801`
- `market_context_high->crypto_alt_1h` score `-0.5568` n `129` status `ready` deltaP `6.3861` edge `0.099` maxDD `-14.7034`
- `market_context_high->unknown_1h` score `-0.8021` n `129` status `ready` deltaP `3.9212` edge `-0.0199` maxDD `-3.1801`
- `market_context_high->crypto_alt_4h` score `-0.9325` n `125` status `ready` deltaP `19.0707` edge `0.3495` maxDD `-42.0284`
- `market_context_high->crypto_major_1h` score `-0.9942` n `129` status `ready` deltaP `4.2798` edge `0.0703` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.1153` n `125` status `ready` deltaP `-8.5902` edge `-0.0033` maxDD `-0.9269`
- `market_context_high->metal_1h` score `-1.1443` n `129` status `ready` deltaP `-1.9484` edge `-0.0019` maxDD `-6.8783`
- `market_context_high->fx_24h` score `-1.4786` n `99` status `ready` deltaP `-2.4937` edge `-0.0194` maxDD `-0.6418`
- `market_context_high->equity_4h` score `-1.8189` n `125` status `ready` deltaP `10.3805` edge `0.0829` maxDD `-27.1574`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
