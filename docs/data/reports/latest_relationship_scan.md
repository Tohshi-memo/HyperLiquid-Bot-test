# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T19:07:56.352705+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9856`

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

- `market_context_high->unknown_24h` score `24.0497` n `65` status `ready` deltaP `20.5101` edge `1.8717` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4992` n `89` status `ready` deltaP `1.6973` edge `0.5465` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.3728` n `89` status `ready` deltaP `16.4445` edge `0.0894` maxDD `-2.7703`
- `market_context_high->crypto_alt_24h` score `1.3391` n `65` status `ready` deltaP `12.1607` edge `0.1555` maxDD `-3.6649`
- `market_context_high->commodity_1h` score `0.173` n `90` status `ready` deltaP `4.8935` edge `0.0234` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1614` n `90` status `ready` deltaP `7.7545` edge `-0.0034` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.1438` n `89` status `ready` deltaP `14.5246` edge `0.0076` maxDD `-1.8797`
- `market_context_high->fx_24h` score `0.0964` n `65` status `ready` deltaP `11.7014` edge `0.0506` maxDD `-4.3126`
- `market_context_high->metal_24h` score `-0.1988` n `65` status `ready` deltaP `-8.977` edge `0.1512` maxDD `-2.6802`
- `market_context_high->metal_1h` score `-0.5426` n `90` status `ready` deltaP `-1.6068` edge `-0.0094` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5565` n `90` status `ready` deltaP `0.1431` edge `-0.0189` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.7273` n `90` status `ready` deltaP `-2.3087` edge `-0.0068` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.7809` n `89` status `ready` deltaP `2.1376` edge `0.0091` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8807` n `89` status `ready` deltaP `4.181` edge `-0.0018` maxDD `-5.7857`
- `market_context_high->commodity_24h` score `-1.2436` n `65` status `ready` deltaP `16.0283` edge `0.0754` maxDD `-21.0021`
- `market_context_high->equity_1h` score `-1.7251` n `90` status `ready` deltaP `4.3513` edge `-0.0966` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0251` n `89` status `ready` deltaP `-11.8029` edge `-0.0555` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.8873` n `65` status `ready` deltaP `-13.4669` edge `-0.0609` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.4547` n `90` status `ready` deltaP `-12.0093` edge `-0.0705` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4912` n `90` status `ready` deltaP `2.0492` edge `-0.2599` maxDD `-1.2421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
