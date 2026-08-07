# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T00:07:31.019341+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11765`

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

- `market_context_high->unknown_24h` score `30.021` n `109` status `ready` deltaP `3.7571` edge `2.481` maxDD `-0.0104`
- `market_context_high->commodity_4h` score `1.1526` n `120` status `ready` deltaP `13.0312` edge `0.0938` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9004` n `109` status `ready` deltaP `3.7004` edge `0.1672` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5488` n `109` status `ready` deltaP `21.4854` edge `0.0477` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4763` n `120` status `ready` deltaP `7.7994` edge `0.0293` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0194` n `120` status `ready` deltaP `5.5539` edge `-0.0045` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.4036` n `120` status `ready` deltaP `5.3021` edge `-0.0011` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5544` n `120` status `ready` deltaP `-2.2255` edge `-0.0068` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.777` n `120` status `ready` deltaP `-2.994` edge `-0.0086` maxDD `-3.0178`
- `market_context_high->index_1h` score `-1.0719` n `120` status `ready` deltaP `-3.1237` edge `-0.0151` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.2889` n `109` status `ready` deltaP `-3.3833` edge `0.0768` maxDD `-7.8922`
- `market_context_high->metal_4h` score `-1.3039` n `120` status `ready` deltaP `1.3066` edge `0.0061` maxDD `-3.211`
- `market_context_high->equity_1h` score `-1.4028` n `120` status `ready` deltaP `3.0489` edge `-0.0437` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.6855` n `120` status `ready` deltaP `-7.7921` edge `-0.0387` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.8892` n `120` status `ready` deltaP `1.9738` edge `-0.0316` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.6165` n `120` status `ready` deltaP `-6.6018` edge `-0.0367` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.0419` n `109` status `ready` deltaP `-6.3132` edge `-0.0671` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-6.0969` n `120` status `ready` deltaP `-0.0579` edge `-0.2524` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.3009` n `109` status `ready` deltaP `9.8099` edge `0.0033` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.2948` n `120` status `ready` deltaP `-6.5257` edge `-0.1432` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
