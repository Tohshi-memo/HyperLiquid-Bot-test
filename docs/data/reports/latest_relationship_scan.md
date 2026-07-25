# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T14:22:31.765642+00:00`
- Price records: `672`
- Market context records: `7886`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14677`

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

- `market_context_high->equity_24h` score `14.0522` n `109` status `ready` deltaP `29.7298` edge `1.107` maxDD `-6.0681`
- `market_context_high->equity_4h` score `4.8626` n `109` status `ready` deltaP `15.0655` edge `0.4024` maxDD `-5.1426`
- `market_context_high->metal_24h` score `4.4118` n `109` status `ready` deltaP `22.1358` edge `0.3087` maxDD `-0.7564`
- `market_context_high->crypto_alt_4h` score `1.7095` n `109` status `ready` deltaP `14.4568` edge `0.1578` maxDD `-3.9374`
- `market_context_high->commodity_24h` score `1.6707` n `109` status `ready` deltaP `21.6559` edge `0.1532` maxDD `-7.0012`
- `market_context_high->crypto_major_4h` score `1.5902` n `109` status `ready` deltaP `16.1437` edge `0.1967` maxDD `-6.7444`
- `market_context_high->fx_24h` score `1.2012` n `109` status `ready` deltaP `32.1387` edge `0.0485` maxDD `-3.0343`
- `market_context_high->crypto_major_1h` score `1.1744` n `114` status `ready` deltaP `12.8585` edge `0.053` maxDD `-1.6021`
- `market_context_high->equity_1h` score `0.8397` n `114` status `ready` deltaP `11.6564` edge `0.1117` maxDD `-4.2072`
- `market_context_high->index_4h` score `0.7856` n `109` status `ready` deltaP `15.2181` edge `0.0599` maxDD `-1.0041`
- `market_context_high->commodity_4h` score `0.733` n `109` status `ready` deltaP `10.6408` edge `0.0495` maxDD `-1.0817`
- `market_context_high->metal_4h` score `0.5379` n `109` status `ready` deltaP `9.2442` edge `0.0996` maxDD `-0.979`
- `market_context_high->index_1h` score `0.4881` n `114` status `ready` deltaP `9.823` edge `0.0182` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.4568` n `114` status `ready` deltaP `5.5836` edge `0.0441` maxDD `-1.4603`
- `market_context_high->index_24h` score `-0.0812` n `109` status `ready` deltaP `0.7807` edge `0.1197` maxDD `-1.5339`
- `market_context_high->metal_1h` score `-0.2421` n `114` status `ready` deltaP `2.8443` edge `0.0237` maxDD `-0.6936`
- `market_context_high->commodity_1h` score `-0.2448` n `114` status `ready` deltaP `3.9908` edge `0.0053` maxDD `-1.1842`
- `market_context_high->fx_1h` score `-0.3541` n `114` status `ready` deltaP `1.3751` edge `-0.0002` maxDD `-0.4112`
- `market_context_high->fx_4h` score `-0.6761` n `109` status `ready` deltaP `1.594` edge `0.0006` maxDD `-1.4993`
- `market_context_high->crypto_alt_24h` score `-1.6485` n `109` status `ready` deltaP `12.3282` edge `0.236` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
