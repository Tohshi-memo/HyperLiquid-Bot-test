# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T22:07:31.444211+00:00`
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

- `market_context_high->unknown_24h` score `48.051` n `109` status `ready` deltaP `3.7571` edge `3.9835` maxDD `-0.0104`
- `market_context_high->commodity_4h` score `1.1628` n `119` status `ready` deltaP `13.1749` edge `0.0937` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9328` n `109` status `ready` deltaP `3.7004` edge `0.1699` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5356` n `109` status `ready` deltaP `21.4854` edge `0.046` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.5037` n `120` status `ready` deltaP `8.097` edge `0.0296` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.009` n `120` status `ready` deltaP `5.709` edge `-0.0042` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3883` n `119` status `ready` deltaP `5.6119` edge `-0.0012` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5601` n `120` status `ready` deltaP `-2.3632` edge `-0.0066` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.803` n `120` status `ready` deltaP `-3.2836` edge `-0.01` maxDD `-3.0178`
- `market_context_high->index_1h` score `-1.072` n `120` status `ready` deltaP `-3.1094` edge `-0.0152` maxDD `-1.6054`
- `market_context_high->crypto_alt_4h` score `-1.2367` n `119` status `ready` deltaP `1.8354` edge `-0.0318` maxDD `-5.7857`
- `market_context_high->metal_4h` score `-1.3159` n `119` status `ready` deltaP `1.2467` edge `0.0055` maxDD `-3.211`
- `market_context_high->equity_1h` score `-1.3837` n `120` status `ready` deltaP `3.3706` edge `-0.0434` maxDD `-10.5179`
- `market_context_high->index_24h` score `-1.4075` n `109` status `ready` deltaP `-4.7189` edge `0.0705` maxDD `-7.8922`
- `market_context_high->index_4h` score `-1.7433` n `119` status `ready` deltaP `-8.6637` edge `-0.0403` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-2.6694` n `120` status `ready` deltaP `-7.0522` edge `-0.0381` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-2.8994` n `109` status `ready` deltaP `-5.3116` edge `-0.0619` maxDD `-4.5445`
- `market_context_high->commodity_24h` score `-6.2424` n `109` status `ready` deltaP `9.8099` edge `0.0108` maxDD `-52.7876`
- `market_context_high->equity_4h` score `-6.246` n `119` status `ready` deltaP `-0.8252` edge `-0.2664` maxDD `-34.9766`
- `market_context_high->crypto_major_4h` score `-7.3027` n `119` status `ready` deltaP `-6.5202` edge `-0.1439` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
