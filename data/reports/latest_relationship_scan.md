# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T11:27:54.789903+00:00`
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

- `market_context_high->commodity_4h` score `1.1089` n `120` status `ready` deltaP `12.876` edge `0.0912` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.5111` n `120` status `ready` deltaP `8.2485` edge `0.0292` maxDD `-1.3282`
- `market_context_high->fx_24h` score `0.4279` n `113` status `ready` deltaP `19.175` edge `0.0476` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.2231` n `113` status `ready` deltaP `0.5289` edge `0.1319` maxDD `-2.6802`
- `market_context_high->fx_1h` score `0.1215` n `120` status `ready` deltaP `7.9491` edge `-0.0024` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1831` n `120` status `ready` deltaP `8.6585` edge `0.0048` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.6471` n `120` status `ready` deltaP `-3.4231` edge `-0.0107` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.8245` n `120` status `ready` deltaP `-3.4431` edge `-0.0117` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.9832` n `120` status `ready` deltaP `-2.5249` edge `-0.0117` maxDD `-1.6054`
- `market_context_high->equity_1h` score `-1.2586` n `120` status `ready` deltaP `4.2465` edge `-0.0332` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.518` n `120` status `ready` deltaP `-5.996` edge `-0.0292` maxDD `-4.7021`
- `market_context_high->index_24h` score `-1.8847` n `113` status `ready` deltaP `-1.2262` edge `0.0706` maxDD `-7.8922`
- `market_context_high->metal_4h` score `-1.9057` n `120` status `ready` deltaP `-3.1707` edge `-0.0142` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-2.1355` n `120` status `ready` deltaP `0.5894` edge `-0.0429` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.7065` n `120` status `ready` deltaP `-6.7515` edge `-0.0432` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.6697` n `113` status `ready` deltaP `-9.8556` edge `-0.0958` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.9574` n `120` status `ready` deltaP `0.3455` edge `-0.2372` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-5.9722` n `113` status `ready` deltaP `11.661` edge `0.0331` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.674` n `120` status `ready` deltaP `-7.561` edge `-0.1679` maxDD `-27.3622`
- `market_context_high->unknown_1h` score `-8.0497` n `120` status `ready` deltaP `1.9212` edge `-0.6389` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
