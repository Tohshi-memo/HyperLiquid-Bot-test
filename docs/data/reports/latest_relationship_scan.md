# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T10:30:20.116470+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11739`

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

- `market_context_high->commodity_4h` score `1.0424` n `120` status `ready` deltaP `12.4187` edge `0.0887` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.4811` n `120` status `ready` deltaP `7.9491` edge `0.0287` maxDD `-1.3282`
- `market_context_high->fx_24h` score `0.4636` n `112` status `ready` deltaP `19.6965` edge `0.0487` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.2896` n `112` status `ready` deltaP `0.7452` edge `0.136` maxDD `-2.6802`
- `market_context_high->fx_1h` score `0.1301` n `120` status `ready` deltaP `8.0988` edge `-0.0023` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1792` n `120` status `ready` deltaP `8.6585` edge `0.0053` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.6557` n `120` status `ready` deltaP `-3.5728` edge `-0.0108` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.8378` n `120` status `ready` deltaP `-3.5928` edge `-0.0124` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.9976` n `120` status `ready` deltaP `-2.6746` edge `-0.0119` maxDD `-1.6054`
- `market_context_high->equity_1h` score `-1.2688` n `120` status `ready` deltaP `4.0968` edge `-0.0335` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.5077` n `120` status `ready` deltaP `-5.8435` edge `-0.0289` maxDD `-4.7021`
- `market_context_high->index_24h` score `-1.8397` n `112` status `ready` deltaP `-1.1284` edge `0.0737` maxDD `-7.8922`
- `market_context_high->metal_4h` score `-1.8523` n `120` status `ready` deltaP `-2.7134` edge `-0.0128` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-2.0991` n `120` status `ready` deltaP `0.8943` edge `-0.0419` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.7053` n `120` status `ready` deltaP `-6.7515` edge `-0.0431` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.7262` n `112` status `ready` deltaP `-10.1717` edge `-0.0984` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.93` n `120` status `ready` deltaP `0.4979` edge `-0.2347` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.0503` n `112` status `ready` deltaP `11.2106` edge `0.0261` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.5642` n `120` status `ready` deltaP `-7.1037` edge `-0.1618` maxDD `-27.3622`
- `market_context_high->unknown_1h` score `-8.13` n `120` status `ready` deltaP `1.7715` edge `-0.6446` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
