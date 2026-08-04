# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T14:37:35.998512+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9839`

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

- `market_context_high->unknown_24h` score `35.5528` n `47` status `ready` deltaP `22.6987` edge `2.8157` maxDD `-0.0103`
- `market_context_high->commodity_24h` score `7.7696` n `47` status `ready` deltaP `37.0604` edge `0.429` maxDD `-1.2884`
- `market_context_high->crypto_alt_24h` score `6.9086` n `47` status `ready` deltaP `37.4963` edge `0.3431` maxDD `-0.3889`
- `market_context_high->unknown_4h` score `5.1909` n `89` status `ready` deltaP `-0.1319` edge `0.533` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.0355` n `89` status `ready` deltaP `14.4628` edge `0.0745` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.2723` n `89` status `ready` deltaP `5.8047` edge `0.0256` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.2134` n `89` status `ready` deltaP `15.7441` edge `0.0084` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.1877` n `89` status `ready` deltaP `8.0536` edge `-0.0032` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.5041` n `89` status `ready` deltaP `1.016` edge `-0.018` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5644` n `89` status `ready` deltaP `-1.8317` edge `-0.0107` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6021` n `89` status `ready` deltaP `4.2718` edge `0.0178` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8572` n `89` status `ready` deltaP `4.3334` edge `0.0002` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.129` n `89` status `ready` deltaP `-2.1345` edge `-0.0088` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.7169` n `89` status `ready` deltaP `4.5381` edge `-0.0968` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.8576` n `89` status `ready` deltaP `-10.1261` edge `-0.0452` maxDD `-4.7021`
- `market_context_high->fx_24h` score `-2.0523` n `47` status `ready` deltaP `-8.1523` edge `0.0039` maxDD `-4.3126`
- `market_context_high->metal_24h` score `-3.2511` n `47` status `ready` deltaP `-24.9852` edge `-0.1334` maxDD `-2.6802`
- `market_context_high->unknown_1h` score `-3.3859` n `89` status `ready` deltaP `2.9604` edge `-0.2572` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5385` n `89` status `ready` deltaP `-12.5463` edge `-0.0739` maxDD `-7.6533`
- `market_context_high->index_24h` score `-5.4396` n `47` status `ready` deltaP `-29.3698` edge `-0.2821` maxDD `-7.8922`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
