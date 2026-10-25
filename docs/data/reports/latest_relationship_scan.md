# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T09:22:27.573110+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7928`

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

- `market_context_high->unknown_4h` score `38.0291` n `109` status `ready` deltaP `-0.821` edge `3.2081` maxDD `-1.016`
- `market_context_high->unknown_1h` score `4.11` n `114` status `ready` deltaP `4.3334` edge `0.3625` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `1.6243` n `44` status `ready` deltaP `15.3725` edge `0.3139` maxDD `-13.6514`
- `market_context_high->commodity_24h` score `0.9292` n `44` status `ready` deltaP `18.5448` edge `0.0864` maxDD `-3.6055`
- `market_context_high->crypto_major_24h` score `0.6053` n `44` status `ready` deltaP `7.1969` edge `0.1084` maxDD `-5.8084`
- `market_context_high->fx_4h` score `0.033` n `109` status `ready` deltaP `8.2471` edge `0.0091` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0814` n `114` status `ready` deltaP `3.2514` edge `0.0028` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.4847` n `114` status `ready` deltaP `0.0867` edge `0.0091` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.57` n `114` status `ready` deltaP `5.3682` edge `-0.0041` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6285` n `114` status `ready` deltaP `-1.5417` edge `-0.0051` maxDD `-1.2155`
- `market_context_high->fx_24h` score `-0.7491` n `44` status `ready` deltaP `1.6099` edge `0.0068` maxDD `-1.0858`
- `market_context_high->commodity_4h` score `-0.8304` n `109` status `ready` deltaP `-2.274` edge `0.0316` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.3413` n `114` status `ready` deltaP `2.0118` edge `-0.0273` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.8647` n `109` status `ready` deltaP `5.162` edge `-0.0188` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1158` n `109` status `ready` deltaP `-7.0388` edge `-0.0369` maxDD `-4.3282`
- `market_context_high->metal_24h` score `-2.9898` n `44` status `ready` deltaP `-7.339` edge `-0.0154` maxDD `-6.7857`
- `market_context_high->crypto_alt_1h` score `-3.0003` n `114` status `ready` deltaP `-1.6704` edge `-0.0515` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.7288` n `114` status `ready` deltaP `0.2547` edge `-0.0851` maxDD `-12.1865`
- `market_context_high->index_24h` score `-5.2847` n `44` status `ready` deltaP `-20.423` edge `-0.1741` maxDD `-5.078`
- `market_context_high->crypto_major_4h` score `-9.6877` n `109` status `ready` deltaP `-11.4763` edge `-0.2311` maxDD `-33.3092`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
