# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T09:07:30.012132+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8612`

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

- `news_risk_high->crypto_major_4h` score `9.5064` n `62` status `ready` deltaP `34.0087` edge `0.5858` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.5595` n `62` status `ready` deltaP `20.1908` edge `0.4631` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.5494` n `62` status `ready` deltaP `10.7305` edge `0.2342` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.2508` n `62` status `ready` deltaP `22.6804` edge `0.1197` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.7616` n `117` status `ready` deltaP `13.8681` edge `0.2341` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.5537` n `62` status `ready` deltaP `28.8012` edge `0.047` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.0175` n `62` status `ready` deltaP `7.9293` edge `0.1508` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8091` n `62` status `ready` deltaP `23.0781` edge `0.0119` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.6874` n `62` status `ready` deltaP `16.8618` edge `0.088` maxDD `-2.7837`
- `market_context_high->fx_4h` score `1.2391` n `117` status `ready` deltaP `23.3141` edge `0.0235` maxDD `-0.3868`
- `news_risk_high->metal_4h` score `1.1852` n `62` status `ready` deltaP `17.2846` edge `0.0783` maxDD `-0.993`
- `market_context_high->crypto_major_24h` score `1.185` n `110` status `ready` deltaP `6.6761` edge `0.293` maxDD `-14.4342`
- `market_context_high->commodity_4h` score `1.1825` n `117` status `ready` deltaP `16.2967` edge `0.0599` maxDD `-1.6002`
- `market_context_high->fx_1h` score `0.8689` n `117` status `ready` deltaP `14.1896` edge `0.0062` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7334` n `117` status `ready` deltaP `11.9057` edge `0.0214` maxDD `-0.5059`
- `news_risk_high->commodity_24h` score `0.7187` n `62` status `ready` deltaP `27.0092` edge `0.0687` maxDD `-8.196`
- `news_risk_high->crypto_alt_1h` score `0.7184` n `62` status `ready` deltaP `2.4097` edge `0.0957` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `0.4347` n `117` status `ready` deltaP `-0.7218` edge `0.2134` maxDD `-7.1222`
- `market_context_high->metal_24h` score `-0.0796` n `110` status `ready` deltaP `12.9928` edge `0.049` maxDD `-5.6663`
- `market_context_high->crypto_major_1h` score `-0.0982` n `117` status `ready` deltaP `7.5158` edge `0.0306` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
