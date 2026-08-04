# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T18:07:36.191925+00:00`
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

- `market_context_high->unknown_24h` score `26.0712` n `61` status `ready` deltaP `21.1038` edge `2.0362` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4169` n `89` status `ready` deltaP `1.0876` edge `0.5437` maxDD `-3.6303`
- `market_context_high->crypto_alt_24h` score `2.3559` n `61` status `ready` deltaP `16.4987` edge `0.1856` maxDD `-2.9416`
- `market_context_high->commodity_4h` score `1.2724` n `89` status `ready` deltaP `15.8348` edge `0.0851` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.2006` n `90` status `ready` deltaP `5.1929` edge `0.0237` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1746` n `90` status `ready` deltaP `7.9042` edge `-0.0033` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.1541` n `89` status `ready` deltaP `14.677` edge `0.0079` maxDD `-1.8797`
- `market_context_high->commodity_24h` score `0.0215` n `61` status `ready` deltaP `19.47` edge `0.138` maxDD `-16.2038`
- `market_context_high->fx_24h` score `-0.29` n `61` status `ready` deltaP `8.4614` edge `0.04` maxDD `-4.3126`
- `market_context_high->index_1h` score `-0.5472` n `90` status `ready` deltaP `0.2928` edge `-0.0187` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5776` n `90` status `ready` deltaP `-2.2056` edge `-0.0099` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7172` n `90` status `ready` deltaP `-2.159` edge `-0.0065` maxDD `-3.0178`
- `market_context_high->metal_24h` score `-0.7194` n `61` status `ready` deltaP `-12.1044` edge `0.1053` maxDD `-2.6802`
- `market_context_high->metal_4h` score `-0.7414` n `89` status `ready` deltaP `2.7474` edge `0.0101` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8517` n `89` status `ready` deltaP `4.3334` edge `0.0009` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7461` n `90` status `ready` deltaP `4.2016` edge `-0.0983` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0024` n `89` status `ready` deltaP `-11.6505` edge `-0.0536` maxDD `-4.7021`
- `market_context_high->index_24h` score `-3.3463` n `61` status `ready` deltaP `-16.1743` edge `-0.1017` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.4715` n `90` status `ready` deltaP `-12.159` edge `-0.0709` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.478` n `90` status `ready` deltaP `2.1989` edge `-0.2598` maxDD `-1.2421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
