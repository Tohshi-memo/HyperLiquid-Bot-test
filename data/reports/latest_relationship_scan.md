# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T12:52:27.749395+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11781`

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

- `market_context_high->metal_24h` score `1.445` n `98` status `ready` deltaP `4.4784` edge `0.2074` maxDD `-2.6802`
- `market_context_high->commodity_4h` score `1.0394` n `109` status `ready` deltaP `12.5322` edge `0.0877` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.4656` n `98` status `ready` deltaP `20.1849` edge `0.0457` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.2932` n `113` status `ready` deltaP `6.5007` edge `0.0227` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0966` n `113` status `ready` deltaP `6.9101` edge `-0.003` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3315` n `109` status `ready` deltaP `6.5703` edge `-0.0003` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5954` n `113` status `ready` deltaP `-2.7277` edge `-0.0087` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.717` n `109` status `ready` deltaP `3.5467` edge `0.0079` maxDD `-3.211`
- `market_context_high->index_1h` score `-1.1373` n `113` status `ready` deltaP `-3.4762` edge `-0.0182` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.1673` n `98` status `ready` deltaP `-3.4899` edge `0.0931` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.37` n `113` status `ready` deltaP `-4.022` edge `-0.0163` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.706` n `113` status `ready` deltaP `2.2429` edge `-0.0772` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.839` n `109` status `ready` deltaP `-9.6191` edge `-0.0462` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.8983` n `109` status `ready` deltaP `2.9089` edge `-0.0386` maxDD `-5.7857`
- `market_context_high->crypto_alt_24h` score `-2.5239` n `98` status `ready` deltaP `-3.2278` edge `-0.0445` maxDD `-4.5445`
- `market_context_high->crypto_major_1h` score `-3.0393` n `113` status `ready` deltaP `-9.4417` edge `-0.053` maxDD `-7.6533`
- `market_context_high->unknown_24h` score `-3.1979` n `98` status `ready` deltaP `3.8407` edge `-0.2878` maxDD `-0.0104`
- `market_context_high->commodity_24h` score `-6.6721` n `98` status `ready` deltaP `6.7673` edge `-0.024` maxDD `-52.7876`
- `market_context_high->equity_4h` score `-6.7558` n `109` status `ready` deltaP `-1.509` edge `-0.3272` maxDD `-34.9766`
- `market_context_high->crypto_major_24h` score `-7.5979` n `98` status `ready` deltaP `-7.4653` edge `-0.2512` maxDD `-40.8499`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
